from fastapi import FastAPI
from api import endpoints

app = FastAPI()


@app.get("/")
async def root():
    return endpoints.root()


@app.get("/api/v0.1/dsa/params")
async def params():
    return endpoints.get_params()


@app.post("/api/v0.1/dsa/calc/}")
async def calc(lat_min: float, lat_max: float, long_min: float, long_max: float):
    return endpoints.post_calc(lat_min, lat_max, long_min, long_max)


@app.post("/api/v0.1/dsa/register/")
async def register(long: float, lat: float, nf: float, prx: float, gt: float, gr: float, channel: int, aclr1: float,
                   aclr2: float):
    return endpoints.post_register(long, lat, nf, prx, gt, gr, channel, aclr1, aclr2)
