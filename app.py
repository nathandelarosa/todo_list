from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from database import *

app = FastAPI()
templates = Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    data = select_all()
    return templates.TemplateResponse("home.html", {"request": request, "todo_data": data})

@app.get("/new", response_class=HTMLResponse)
def new(request: Request):
    return templates.TemplateResponse("new.html", {"request": request})

@app.get("/home", response_class=HTMLResponse)
def home(request: Request):
    data = select_all()
    return templates.TemplateResponse("home.html", {"request": request, "todo_data": data})

@app.post("/save", response_class=HTMLResponse)
async def save(
    request: Request,
    priority_input: str = Form(""),
    task_input: str = Form("")
):
    
    add_task(priority_input, task_input)

    return RedirectResponse(url="/home", status_code=301)

@app.post("/delete", response_class=HTMLResponse)
async def delete(request: Request, id_input: str = Form(...)):
    id_num = id_input

    del_task(id_num)

    return RedirectResponse(url="/home", status_code=301)
