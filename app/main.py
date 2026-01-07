from fastapi import FastAPI
from .routers import user

app = FastAPI(title="FastAPI CRUD")

app.include_router(user.router)


@app.get("/health")
def health():
    return {"status": "ok"}
