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
    return endpoints.alu(data=data)


@app.post("/api/v0.1/dsa/register/")
async def register(data: endpoints_models.Register):
    return endpoints.register(data=data)


@app.get("/api/v0.1/dsa/users/")
async def users():
    return endpoints.users()


@app.delete("/api/v0.1/dsa/delete/")
async def delete_user(data: endpoints_models.Delete = None):
    return endpoints.delete_user(data=data)


@app.patch("/api/v0.1/dsa/from_alu/")
async def from_alu(data: endpoints_models.Patch):
    return endpoints.patch_user(data=data)
