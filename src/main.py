from typing import Union
from fastapi import FastAPI
from routes import users, orders

app = FastAPI()
app.include_router(users.router)
app.include_router(orders.router)


@app.get("/")
def status():
    return {"status": "running"}
