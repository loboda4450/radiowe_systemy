from api.endpoints_models import UserInDB, User, Register
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

prosthesis_users_db = {
    'admin': {
        'username': 'admin',
        'hashed': 'hashedsecret',
        'disabled': False},
    'admin2': {
        'username': 'admin2',
        'hashed': 'hashedsecret',
        'disabled': False}
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def fake_hash_password(password: str):
    # wow, that much security
    return "hashed" + password


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    user = get_user(prosthesis_users_db, token)
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


async def check_data(data: Register):
    if not 52.361 <= data.long <= 52.436:
        raise HTTPException(status_code=406, detail=f'Data validation error: longitude {data.long} exceeds limit ['
                                                    f'-180; 180]')
    if not 16.844 <= data.lng <= 17.008:
        raise HTTPException(status_code=406, detail=f'Data validation error: latitude {data.lat} exceeds limit [-90; 90]')
    if not 0 <= data.nf <= 40:
        raise HTTPException(status_code=406, detail=f'Data validation error: noise factor {data.nf} exceeds limit [0; '
                                                    f'40]')
    if not 0 <= data.ptx <= 40:
        raise HTTPException(status_code=406, detail=f'Data validation error: ptx {data.ptx} exceeds limit [0; 40]')
    if not 0 <= data.gt <= 40:
        raise HTTPException(status_code=406, detail=f'Data validation error: gain transmitter {data.gt} exceeds limit '
                                                    f'[0; 40]')
    if not 0 <= data.gr <= 40:
        raise HTTPException(status_code=406, detail=f'Data validation error: gain receiver {data.gr} exceeds limit ['
                                                    f'0; 40]')
    if not 0 <= data.channel <= 12:
        raise HTTPException(status_code=406, detail=f'Data validation error: channel {data.channel} exceeds limit [0; '
                                                    f'12]')
    if not 0 <= data.aclr1 <= 40:
        raise HTTPException(status_code=406, detail=f'Data validation error: aclr1 {data.aclr1} exceeds limit [0; 40]')
    if not 0 <= data.aclr2 <= 40:
        raise HTTPException(status_code=406, detail=f'Data validation error: aclr2 {data.aclr2} exceeds limit [0; 40]')

    return data
