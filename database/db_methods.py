import random

from pony.orm import *
from database import db_models
from api import endpoints_models
from logme import logme
from fastapi import HTTPException
from typing import Optional

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

    db.flush()


@logme
@db_session
def register_user(data: endpoints_models.Register):
    db_models.User(long=data.long, lat=data.lat, nf=data.nf, prx=data.prx, gt=data.gt, gr=data.gr, channel=data.channel,
                   aclr1=data.aclr1, aclr2=data.aclr2,
                   carrier=data.carrier, bandwidth=data.bandwidth)
    db.flush()


@logme
@db_session
def patch_user(data: endpoints_models.Patch) -> dict:
    try:
        user = db_models.User.get(id=data.id)
        user.from_alu = data.from_alu
        db.flush()
        return {'message': f'successfully patched user[id={data.id}] with value from_alu={data.from_alu}'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Cannot patch user in database, possible cause is: {e}')


@logme
@db_session
def get_users():
    return [u.to_dict() for u in select(user for user in db_models.User)]


@logme
@db_session
def delete_user(data: endpoints_models.Delete):
    try:
        user = db_models.User.get(id=data.id)
        user.delete()
        db.flush()
        return {'message': f'Succesfuly removed user[id={data.id}] from database!'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Cannot delete user from database, possible cause is: {e}')