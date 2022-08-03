from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items():
    return [{"name": "Foo"}]

@app.get("/dash-path/")
async def read_items():
    return [{"name": "dash"}]

@app.get("/test")
def routes():
    return "hello1"
