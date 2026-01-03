from fastapi import FastAPI
from routes.inventory_router import  router as inventory_router
from core.database import Base , engine

app =  FastAPI(title="Inventory Management")


app.include_router(inventory_router)

@app.on_event("startup")
def start_up() :
    Base.metadata.create_all(bind=engine)

@app.get("/")
def home() :
    return {"Status" : "WelCome to Inventory Management"}
