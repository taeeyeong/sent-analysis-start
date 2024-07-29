from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates

from database import engine, SessionLocal

import schemas

app = FastAPI()

templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index2.html", {"request": request})

@app.post("/generate/")
async def generate_content(payload: schemas.GeneratePayload, db: Session = Depends(get_db)):
    