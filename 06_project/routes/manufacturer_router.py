from fastapi import APIRouter , HTTPException , status , Depends
from core.config import get_db
from sqlalchemy.orm import Session
from schemas.manufacturer import ManufacturerCreate, ManufacturerResponse
from schemas.product import ProductCreate, ProductResponse
from services.manufacturer_service import ManufacturerService
from services.product_service import ProductService

router =  APIRouter(prefix="/manufacturer" , tags=["|| Manufacturer ||"])

@router.get("/")
def get_inventory() :
    return "All Inventory"


@router.post(
    "/manufacturers",
    response_model=ManufacturerResponse,
    status_code=status.HTTP_201_CREATED
)
def create_manufacturer(
    payload: ManufacturerCreate,
    db: Session = Depends(get_db)
):
    service = ManufacturerService()
    try:
        return service.create_manufacturer(db, payload)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get(
    "/manufacturers",
    response_model=list[ManufacturerResponse]
)
def list_manufacturers(db: Session = Depends(get_db)):
    service = ManufacturerService()
    return service.get_all_manufacturers(db)
