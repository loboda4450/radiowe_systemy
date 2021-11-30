import random

from pony.orm import *
from database import db_models
from api import endpoints_models
from logme import logme

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
                       aclr2=round(random.uniform(0, 40), 2))

    db.flush()


@logme
@db_session
def register_user(data: endpoints_models.Register):
    if not select(u for u in db_models.User if u.channel == data.channel).exists():
        db_models.User(long=data.long, lat=data.lat, nf=data.nf, prx=data.prx, gt=data.gt, gr=data.gr,
                       channel=data.channel,
                       aclr1=data.aclr1, aclr2=data.aclr2)
        db.flush()
    else:
        raise Exception('User already exist')


@logme
@db_session
def patch_user(data: endpoints_models.Patch) -> dict:
    if user := db_models.User.get(id=data.id):
        user.from_alu = data.from_alu
        db.flush()
        return {'message': f'successfully patched user[id={data.id}] with value from_alu={data.from_alu}'}
    else:
        raise Exception(f"There's no user with specified id={data.id}")


@logme
@db_session
def get_users():
    return [u.to_dict() for u in select(user for user in db_models.User)]


@logme
@db_session
def delete_user(data: endpoints_models.Delete):
    if user := db_models.User.get(id=data.id):
        user.delete()
        db.flush()
        return {'message': f'Succesfuly removed user[id={data.id}] from database!'}
    else:
        raise Exception(f"There's no user with specified id={data.id}")


@logme
@db_session
def get_last_alu():
    user = list(db_models.User.select())
    return user[-1].to_dict()


@logme
@db_session
def get_lat_min():
    return min(u.lat for u in db_models.User)


@logme
@db_session
def get_lat_max():
    return max(u.lat for u in db_models.User)


@logme
@db_session
def get_long_min():
    return min(u.long for u in db_models.User)


@logme
@db_session
def get_long_max():
    return max(u.long for u in db_models.User)
