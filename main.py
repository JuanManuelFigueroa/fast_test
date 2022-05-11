#import coverage
from fastapi import FastAPI

app = FastAPI()
#scov = coverage.Coverage()


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

@app.get("/path")
async def path():
    m = 'more lines'
    t = 'to coverage'
    a = 'at all'
    return {"msg": "path"}

@app.get("/route2")
async def route2():
    m = 'more lines'
    t = 'to coverage'
    a = 'at all'
    return {"msg": "route2"}

@app.get("/path2")
async def path2():
    m = 'more lines'
    t = 'to coverage'
    a = 'at all'
    return {"msg": "path2"}

@app.get("/route3")
async def route3():
    m = 'more lines'
    t = 'to coverage'
    a = 'at all'
    return {"msg": "route3"}

@app.get("/path3")
async def path3():
    m = 'more lines'
    t = 'to coverage'
    a = 'at all'
    return {"msg": "path3"}

@app.on_event("startup")
async def startup_event():
    print('startup')

@app.on_event("shutdown")
async def shutdown_event():
    print('shutdown')
