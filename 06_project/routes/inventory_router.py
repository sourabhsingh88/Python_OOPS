from fastapi import APIRouter , HTTPException , status , Depends
from core.config import get_db
from sqlalchemy.orm import Session
from schemas.manufacturer import ManufacturerCreate, ManufacturerResponse
from schemas.product import ProductCreate, ProductResponse

from services.manufacturer_service import ManufacturerService
from services.product_service import ProductService

router =  APIRouter(prefix="/product" , tags=["|| Product ||"])

@router.get("/")
def get_inventory() :
    return "All Inventory"


@router.post(
    "/products",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED
)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    service = ProductService()
    try:
        return service.create_product(db, product)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get(
    "/products",
    response_model=list[ProductResponse]
)
def list_products(db: Session = Depends(get_db)):
    service = ProductService()
    return service.get_all_products(db)
