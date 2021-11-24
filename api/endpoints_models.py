from pydantic import BaseModel


class Alu(BaseModel):
    lat_min: float
    lat_max: float
    long_min: float
    long_max: float


class Register(BaseModel):
    long: float
    lat: float
    nf: float
    prx: float
    gt: float
    gr: float
    channel: int
    aclr1: float
    aclr2: float
    carrier: int
    bandwidth: int


class Delete(BaseModel):
    id: int


class Patch(BaseModel):
    id: int
    from_alu: float
