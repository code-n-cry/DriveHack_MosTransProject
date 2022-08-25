from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from backend.api_router import router

app = FastAPI()
app.include_router(router)


@app.get('/')
async def index_page(request: Request):
    return {'MosTransProekt'}
