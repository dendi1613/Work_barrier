from fastapi import FastAPI

from starlabs.lightning.database import Model, engine
from starlabs.lightning.routers import speedsters


Model.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(speedsters.router)
