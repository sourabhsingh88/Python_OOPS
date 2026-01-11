from fastapi import FastAPI
from core.database import Base, engine
from models.product import Product
from models.manufacturer import Manufacturer

from routes.inventory_router import router as product_router
from routes.manufacturer_router import router as manufacturer_router

app = FastAPI(title="Inventory Management")

print(">>> MAIN FILE LOADED")

app.include_router(product_router)
app.include_router(manufacturer_router)

@app.on_event("startup")
def start_up():
    print(">>> TABLES SEEN:", Base.metadata.tables.keys())
    Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"Status": "Welcome to Inventory Management"}
