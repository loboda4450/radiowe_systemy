from fastapi import FastAPI
from api import endpoints, endpoints_models
from database import db_methods

app = FastAPI()


@app.get("/")
async def root():
    db_methods.fill_db()
    return endpoints.root()


@app.get("/api/v0.1/dsa/params")
async def params():
    return endpoints.get_params()


@app.post("/api/v0.1/dsa/alu/")
async def alu(data: endpoints_models.Alu):
    return endpoints.alu(data.lat_min, data.lat_max, data.long_min, data.long_max)


@app.post("/api/v0.1/dsa/register/")
async def register(data: endpoints_models.Register):
    return endpoints.register(data.long, data.lat, data.nf, data.prx, data.gt, data.gr, data.channel, data.aclr1,
                              data.aclr2)


@app.delete("/api/v0.1/dsa/delete/")
async def delete_user(data: endpoints_models.Delete = None):
    return endpoints.delete_user(data=data)


@app.patch("/api/v0.1/dsa/from_alu/")
async def from_alu():
    return endpoints.patch_user()
