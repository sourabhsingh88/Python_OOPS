from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base


class Manufacturer(Base):
    __tablename__ = "manufacturers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    country = Column(String(50), nullable=True)

    products = relationship(
        "Product",
        back_populates="manufacturer",
        cascade="all, delete-orphan"
    )

    def __str__(self):
        return f"Manufacturer(id={self.id}, name={self.name})"
