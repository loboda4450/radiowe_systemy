from pony.orm import *

db = Database("sqlite", "radio_users.sqlite", create_db=True)


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    lng = Required(float)
    lat = Required(float)
    nf = Required(float)
    ptx = Required(float)
    gt = Required(float)
    gr = Required(float)
    channel = Required(int)
    aclr1 = Required(float)
    aclr2 = Required(float)

    sinr = Optional(float)


db.generate_mapping(create_tables=True)
