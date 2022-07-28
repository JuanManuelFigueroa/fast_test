#import coverage
from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy.orm import Session
from typing import Optional

import crud as crud
import schemas
from database import SessionLocal, engine
from models import Base, ItemOld, ModelName, items_db


app = FastAPI()
#scov = coverage.Coverage()
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/pipeline/")
def github_pipeline(pipeline: schemas.PipelineCreate, request: Request):
    print(pipeline)
    print(request.headers)
    return {'Response': 'ok'}


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@app.get("/")
async def root():
    a = 'coverage test'
    b = 'coverage test v2'
    return {"msg": "Hello World"}

@app.get("/route")
async def route():
    m = 'more lines'
    t = 'to coverage'
    a = 'at all'
    return {"msg": "route"}


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    items = items_db()
    return items[skip : skip + limit]

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    item = ItemOld(id=item_id)
    if q:
        item.q= q
    #Testing excpetion
    if item.id == "-1":
        raise HTTPException(status_code=404, detail="Invalid item")
    return item.dict()

@app.post("/items/", response_model=ItemOld)
async def create_item(item: ItemOld):
    return item
    
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.on_event("startup")
async def startup_event():
    print('startup')

@app.on_event("shutdown")
async def shutdown_event():
    print('shutdown')
