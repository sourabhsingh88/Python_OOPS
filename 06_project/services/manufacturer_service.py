from sqlalchemy.orm import Session

from models.manufacturer import Manufacturer
from repositories.manufacturer_repository import ManufacturerRepository
from schemas.manufacturer import ManufacturerCreate


class ManufacturerService:
    def __init__(self):
        self.repo = ManufacturerRepository()

    def create_manufacturer(
        self, db: Session, payload: ManufacturerCreate
    ) -> Manufacturer:

        # Business rule: manufacturer name must be unique
        existing = self.repo.get_by_name(db, payload.name)
        if existing:
            raise ValueError("Manufacturer already exists")

        manufacturer = Manufacturer(
            name=payload.name,
            country=payload.country
        )

        return self.repo.create(db, manufacturer)

    def get_all_manufacturers(self, db: Session):
        return self.repo.get_all(db)
