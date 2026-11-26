
from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)
 
@app.get("/")
def home(req: Request):
    return templates.TemplateResponse(
        request=req,
        name="index.html"
    )

