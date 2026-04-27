from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/") 
def home():
    return FileResponse('static/home.html')
@app.get("/imc")
def IMC(a: float, b: float):
    risultato =a /(b*b)
    return {"risultato": risultato}
     
@app.post("/imc2")
def Controlla(peso: float = Form(...), altezza: float = Form(...)):
    risultato =a /(b*b)
    return {"risultato": risultato}

