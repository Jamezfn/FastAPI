from fastapi import FastAPI

import models
from dB import engine
from routers import blog, user, authentification

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(authentification.router)
app.include_router(user.router)
app.include_router(blog.router)