from database import db_methods
from api import endpoints_models
from logme import logme
from fastapi import HTTPException


@logme
def root():
    return {
        'message': "Hello, that's a root node of API, please send request to a proper node :)",
        'avail_nodes':
            {
                'params': "/api/v0.1/dsa/params",
                'calc': "/api/v0.1/dsa/alu/{lat_min}{lat_max}{long_min}{long_max}",
                'register': "/api/v0.1/dsa/register/{long}{lat}{nf}{prx}{gt}{gr}{channel}{aclr1}{aclr2}",
                'response from alu': "/api/v0.1/dsa/from_alu/"
            }
    }


@logme
def get_params():
    return {
        'carrier': 1811,  # MHz
        'channels': 12,  # just 12 channels XD
        'bandwidth': 100,  # Mhz per channel
    }


@logme
def alu(data: endpoints_models.Alu):
    return {
        'min_SNR': 6,  # dB
        'min_SINR': 0,  # dB
        'grid': 100,  # m
        'lat_min': data.lat_min,
        'lat_max': data.lat_max,
        'long_min': data.long_min,
        'long_max': data.long_max,
        'users': db_methods.get_users()  # contains all users in system
    }


@logme
def register(data: endpoints_models.Register):
    try:
        db_methods.register_user(data=data)

        return {'message': 'Registered user',
                'params':
                    {'long': data.long,
                     'lat': data.lat,
                     'nf': data.nf,
                     'prx': data.prx,
                     'gt': data.gt,
                     'gr': data.gr,
                     'channel': data.channel,
                     'aclr1': data.aclr1,
                     'aclr2': data.aclr2,
                     'carrier': data.carrier,
                     'bandwidth': data.bandwidth}
                }

    except Exception as e:
        raise HTTPException(status_code=422, detail=f'Cannot register user in database, possible cause is: {e}')


@logme
def users():
    return {'users': db_methods.get_users()}


@logme
def delete_user(data: endpoints_models.Delete):
    return db_methods.delete_user(data)


@logme
def patch_user(data: endpoints_models.Patch):
    return db_methods.patch_user(data=data)
