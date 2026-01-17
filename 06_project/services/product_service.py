from sqlalchemy.orm import Session

from models.product import Product
from repositories.product_repository import ProductRepository
from repositories.manufacturer_repository import ManufacturerRepository
from schemas.product import ProductCreate


class ProductService:
    def __init__(self):
        self.product_repo = ProductRepository()
        self.manufacturer_repo = ManufacturerRepository()

    def create_product(
        self, db: Session, payload: ProductCreate
    ) -> Product:

        # Business rule: SKU must be unique
        if self.product_repo.get_by_sku(db, payload.sku):
            raise ValueError("Product with this SKU already exists")

        # Business rule: manufacturer must exist
        manufacturer = self.manufacturer_repo.get_by_id(
            db, payload.manufacturer_id
        )
        if not manufacturer:
            raise ValueError("Manufacturer does not exist")

        product = Product(
            name=payload.name,
            sku=payload.sku,
            price=payload.price,
            is_active=payload.is_active,
            manufacturer_id=payload.manufacturer_id
        )

        return self.product_repo.create(db, product)

    def get_all_products(self, db: Session):
        return self.product_repo.get_all(db)
