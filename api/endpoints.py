import database.db_methods as dbmethods
from logme import logme


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
def post_alu(lat_min, lat_max, long_min, long_max):
    return {
        'min_SNR': 6,  # dB
        'min_SINR': 0,  # dB
        'grid': 100,  # m
        'lat_min': lat_min,
        'lat_max': lat_max,
        'long_min': long_min,
        'long_max': long_max,
        'users': dbmethods.get_users()  # contains all users in system
    }


@logme
def post_register(long, lat, nf, prx, gt, gr, channel, aclr1, aclr2):
    return {
        'long': long,
        'lat': lat,
        'nf': nf,
        'prx': prx,
        'gt': gt,
        'gr': gr,
        'channel': channel,
        'aclr1': aclr1,
        'aclr2': aclr2
    }


@logme
def update_from_alu():
    return {'message': 'To be implemented'}
