from api.endpoints_models import UserInDB, User
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
