from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from backend.api_router import router

app = FastAPI()
app.include_router(router)
templates = Jinja2Templates(directory='frontend/templates/')
app.mount('/static', StaticFiles(directory='frontend/static'), name='static')


@app.get('/')
async def index_page(request: Request):
    return templates.TemplateResponse('main.html', {'request': request})
