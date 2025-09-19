from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from app.services.calc_limon import calc_limon

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/api/calc/limon")
def api_calc_limon(rise: float = Form(...), run: float = Form(...), steps: int = Form(...)):
    result = calc_limon(rise, run, steps)  # appelle ton module
    return {"ok": True, "result": result}
