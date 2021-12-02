from typing import Optional
from pydantic import BaseModel


class Register(BaseModel):
    lng: float
    lat: float
    nf: float
    ptx: float
    gt: float
    gr: float
    channel: int
    aclr1: float
    aclr2: float


class Delete(BaseModel):
    id: int


class Patch(BaseModel):
    id: int
    from_alu: float


class User(BaseModel):
    username: str
    disabled: Optional[bool] = None


class UserInDB(User):
    hashed: str
