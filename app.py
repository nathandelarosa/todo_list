from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from database import *

app = FastAPI()
templates = Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"), name="static")


# renders home template with table populated with all the data #
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    data = select_all()
    return templates.TemplateResponse("home.html", {"request": request, "todo_data": data})

# renders new template on "/new" #
@app.get("/new", response_class=HTMLResponse)
def new(request: Request):
    return templates.TemplateResponse("new.html", {"request": request})

# same thing as first route #
@app.get("/home", response_class=HTMLResponse)
def home(request: Request):
    data = select_all()
    return templates.TemplateResponse("home.html", {"request": request, "todo_data": data})

# inserts new task to database then redirect back to home page #
@app.post("/save", response_class=HTMLResponse)
async def save(
    request: Request,
    priority_input: str = Form(""),
    task_input: str = Form(""),
    date_input: str = Form("")
):
    
    add_task(priority_input, task_input, date_input)

    return RedirectResponse(url="/home", status_code=301)

# delete task row then redirect to home page # 
@app.post("/delete", response_class=HTMLResponse)
async def delete(request: Request, id_input: str = Form(...)):
    id_num = id_input

    del_task(id_num)

    return RedirectResponse(url="/home", status_code=301)

# get data from row and populate it into new.html template #
@app.post("/edit", response_class=HTMLResponse)
async def edit(request: Request, id_input: str = Form(...)):
    id_num = id_input

    data = edit_task(id_num)

    priority = (data[0])
    task = (data[1])
    date = (data[3])

    return templates.TemplateResponse(
        "new.html",
        {
            "request": request,
            "priority": priority,
            "task": task,
            "date": date,
        }
    )