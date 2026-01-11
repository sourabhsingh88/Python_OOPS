from sqlalchemy.orm import Session
from models.product import Product


class ProductRepository:

    def create(self, db: Session, product: Product) -> Product:
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    def get_by_id(self, db: Session, product_id: int):
        return (
            db.query(Product)
            .filter(Product.id == product_id)
            .first()
        )

    def get_by_sku(self, db: Session, sku: str):
        return (
            db.query(Product)
            .filter(Product.sku == sku)
            .first()
        )

    def get_all(self, db: Session):
        return db.query(Product).all()
