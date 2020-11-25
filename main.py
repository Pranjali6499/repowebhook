import models

from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from database import SessionLocal,engine
from sqlalchemy.orm import Session
app=FastAPI()
models.Base.metadata.create_all(bind=engine)
templates=Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    """
    displays the stock dashboard/homepage
    """
    return templates.TemplateResponse("home.html",{
        "request":request
    })

@app.post("/stock")

def create_stock():
    """
     creates the stock and stores it in the database
    """
    return{ 
        "code":"success",
        "message":"stock created"
    }

