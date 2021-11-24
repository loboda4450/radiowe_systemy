import random

from pony.orm import *
from database import db_models
from api import endpoints_models
from logme import logme
from fastapi import HTTPException

db = Database("sqlite", "radio_users.sqlite", create_db=True)


@logme
@db_session
def fill_db():
    for _ in range(50):
        db_models.User(long=round(random.uniform(-180, 180), 2),
                       lat=round(random.uniform(-90, 90), 2),
                       nf=round(random.uniform(0, 40), 2),
                       prx=round(random.uniform(0, 40), 2),
                       gt=round(random.uniform(0, 40), 2),
                       gr=round(random.uniform(0, 40), 2),
                       channel=random.randint(0, 12),
                       aclr1=round(random.uniform(0, 40), 2),
                       aclr2=round(random.uniform(0, 40), 2),
                       carrier=random.randint(0, 240),
                       bandwidth=random.randint(0, 240))


@logme
@db_session
def register_user(_long: float, _lat: float, _nf: float, _prx: float, _gt: float, _gr: float, _channel: int,
                  _aclr1: float, _aclr2: float, _carrier: int, _bandwidth: int):
    db_models.User(long=_long, lat=_lat, nf=_nf, prx=_prx, gt=_gt, gr=_gr, channel=_channel, aclr1=_aclr1, aclr2=_aclr2,
                   carrier=_carrier, bandwidth=_bandwidth)


@logme
@db_session
def update_user(_id: int, _from_alu: float):
    user = db_models.User.get(id=_id)
    user.from_alu = _from_alu
    db.flush()


@logme
@db_session
def get_users():
    return [u.to_dict() for u in select(user for user in db_models.User)]


@logme
@db_session
def delete_user(data: endpoints_models.Delete = None):
    # TODO: remove user from database
    raise HTTPException(status_code=400, detail=f'Not implemented error!, passed data: {data}')
