from fastapi.security import OAuth2PasswordRequestForm

from database import db_methods
from api import endpoints_models, aux
from logme import logme
from fastapi import HTTPException, Depends


@logme
def root():
    return {
        'message': "Hello, that's a root node of API, please send request to a proper node. Go to /docs to see all "
                   "possible nodes :)",
    }


@logme
def get_params():
    return {
        'carrier': 1811,  # MHz
        'channels': 12,  # just 12 channels XD
        'bandwidth': 10,  # Mhz per channel
        'lat_min': 52.361,
        'lat_max': 52.436,
        'long_min': 16.844,
        'long_max': 17.008
    }


@logme
def alu():
    try:
        return {
            'min_SNR': 6,  # dB
            'min_SINR': 0,  # dB
            'grid': 100,  # m
            'lat_min': db_methods.get_lat_min(),
            'lat_max': db_methods.get_lat_max(),
            'long_min': db_methods.get_long_min(),
            'long_max': db_methods.get_long_max(),
            'users': db_methods.get_users()  # contains all users in system
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Cannot get data from database, possible cause is: {e}')


@logme
def register(data: endpoints_models.Register):
    try:
        db_methods.register_user(data=data)

        return {
            'message': 'Registered user',
            'params':
                {
                    'long': data.long,
                    'lat': data.lat,
                    'nf': data.nf,
                    'ptx': data.ptx,
                    'gt': data.gt,
                    'gr': data.gr,
                    'channel': data.channel,
                    'aclr1': data.aclr1,
                    'aclr2': data.aclr2
                }
        }

    except Exception as e:
        raise HTTPException(status_code=422, detail=f'Cannot register user in database, possible cause is: {e}')


@logme
def users():
    try:
        return {'users': db_methods.get_users()}
    except Exception as e:
        raise HTTPException(status_code=422, detail=f'Cannot receive users from database, possible cause is: {e}')


@logme
def delete_user(data: endpoints_models.Delete):
    try:
        return db_methods.delete_user(data)
    except Exception as e:
        raise HTTPException(status_code=422, detail=f'Cannot delete user in database, possible cause is: {e}')


@logme
def patch_user(data: endpoints_models.Patch):
    try:
        return db_methods.patch_user(data=data)
    except Exception as e:
        raise HTTPException(status_code=422, detail=f'Cannot patch user in database, possible cause is: {e}')


@logme
def get_last_alu():
    try:
        return db_methods.get_last_alu()
    except Exception as e:
        raise HTTPException(status_code=422, detail=f'Cannot receive last user from database, possible cause is: {e}')


@logme
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = aux.prosthesis_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = endpoints_models.UserInDB(**user_dict)
    hashed_password = aux.fake_hash_password(form_data.password)
    if not hashed_password == user.hashed:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer", 'db': aux.prosthesis_users_db}
