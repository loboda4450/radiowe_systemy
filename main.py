from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from api import endpoints, endpoints_models, aux
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return endpoints.root()


@app.get("/api/v0.1/dsa/params")
async def params():
    return endpoints.get_params()


@app.post("/api/v0.1/dsa/alu/")
async def alu():
    return endpoints.alu()


@app.post("/api/v0.1/dsa/register/")
async def register(data: endpoints_models.Register = Depends(aux.check_data)):
    return endpoints.register(data=data)


@app.get("/api/v0.1/dsa/users/")
async def users(current_user: endpoints_models.User = Depends(aux.get_current_active_user)):
    return endpoints.users()


@app.delete("/api/v0.1/dsa/delete/")
async def delete_user(data: endpoints_models.Delete = None,
                      current_user: endpoints_models.User = Depends(aux.get_current_active_user)):
    return endpoints.delete_user(data=data)


@app.put("/api/v0.1/dsa/patch_user/")
async def from_alu(data: endpoints_models.Patch):
    return endpoints.patch_user(data=data)


@app.get("/api/v0.1/dsa/get_last_alu")
async def getalu():
    return endpoints.get_last_alu()


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return endpoints.login(form_data=form_data)


@app.get("/users/me")
async def read_users_me(current_user: endpoints_models.User = Depends(aux.get_current_active_user)):
    return current_user


if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=20232, reload=True, debug=True, workers=1)
