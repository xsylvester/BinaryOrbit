#! /usr/bin/python3

import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# to access my templates files
templates = Jinja2Templates(directory="../templates")

# static files directory (.js and .css)
app.mount("/static", StaticFiles(directory="../static"), name="static" )

# landing page of the sit
@app.get("/binaryorbit")
async def binaryOrbit(request:Request):
    return templates.TemplateResponse("binaryorbit.html",
                                       {"request":request}
                                      )
# signup page for new users
@app.get("/signup", response_class=HTMLResponse)
async def signup(request:Request):
    return templates.TemplateResponse("signup.html",
                                      {"request":request}
    )
    # returns a webpage with forms for users to fill

# login page for already registered users
@app.get("/signin", response_class=HTMLResponse)
async def signin(request:Request):
    return templates.TemplatesResponse("login.html", {"request":request})
    # returns a webpage for users to input their login data

# does the same stuff as /signin but from different paths
@app.get("/login", response_class=HTMLResponse)
async def login(request:Request):
    return templates.TemplatesResponse("login.html", {"request":request})
    # still returns a webpage for users login data to be entered
    
# used to submit data for processing   
@app.post("/submit", response_class=HTMLResponse)
async def signup(request:Request, username:str=Form(...),
                 email:str=Form(...), password:str=Form(...)
                 ):
    data = {"username":username, "email":email, "password":password}
    # do validation
    # handle database
    # then handle conditions    
    return templates.TemplateResponse("welcome.html",
                                       {"request":request, "username":username})
    
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=0)
