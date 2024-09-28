from fastapi import FastAPI
from routers import routerCultivos

app = FastAPI()

app.include_router(routerCultivos.router)