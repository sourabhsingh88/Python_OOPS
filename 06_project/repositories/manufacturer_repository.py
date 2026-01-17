from sqlalchemy.orm import Session
from models.manufacturer import Manufacturer


class ManufacturerRepository:

    def create(self, db: Session, manufacturer: Manufacturer) -> Manufacturer:
        db.add(manufacturer)
        db.commit()
        db.refresh(manufacturer)
        return manufacturer

    def get_by_id(self, db: Session, manufacturer_id: int):
        return db.query(Manufacturer).filter(
            Manufacturer.id == manufacturer_id
        ).first()

    def get_by_name(self, db: Session, name: str):
        return db.query(Manufacturer).filter(
            Manufacturer.name == name
        ).first()

    def get_all(self, db: Session):
        return db.query(Manufacturer).all()
