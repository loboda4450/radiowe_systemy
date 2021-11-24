from pony.orm import *

db = Database("sqlite", "radio_users.sqlite", create_db=True)


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    long = Required(float)
    lat = Required(float)
    nf = Required(float)
    prx = Required(float)
    gt = Required(float)
    gr = Required(float)
    channel = Required(int)
    aclr1 = Required(float)
    aclr2 = Required(float)

    carrier = Required(int)
    bandwidth = Required(int)

    from_alu = Optional(float)


db.generate_mapping(create_tables=True)
