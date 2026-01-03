from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    sku = Column(String(50), unique=True, nullable=False, index=True)
    price = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True)

    manufacturer_id = Column(
        Integer,
        ForeignKey("manufacturers.id"),
        nullable=False
    )

    manufacturer = relationship(
        "Manufacturer",
        back_populates="products"
    )

    def __str__(self):
        return f"Product(id={self.id}, name={self.name}, sku={self.sku})"
