from pony.orm import *
from database import db_models
from api import endpoints_models
from logme import logme

db = Database("sqlite", "radio_users.sqlite", create_db=True)


@logme
@db_session
def register_user(data: endpoints_models.Register):
    db_models.User(lng=data.lng, lat=data.lat, nf=data.nf, ptx=data.ptx, gt=data.gt, gr=data.gr,
                   channel=data.channel,
                   aclr1=data.aclr1, aclr2=data.aclr2)
    db.flush()

    return db_models.User[-1].id


@logme
@db_session
def patch_user(data: endpoints_models.Patch) -> dict:
    if user := db_models.User.get(id=data.id):
        user.sinr = data.sinr
        db.flush()
        return {'message': f'successfully patched user[id={data.id}] with value sinr={data.sinr}'}
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
def is_user_updated(id: int):
    return db_models.User.get(id=id).sinr


@logme
@db_session
def get_last_alu():
    if select(u.sinr for u in db_models.User if u.sinr is None).exists():
        return db_models.User.get(id=min(u.id for u in db_models.User if u.sinr is None)).to_dict()
    else:
        raise Exception(f"There aint not served users")
