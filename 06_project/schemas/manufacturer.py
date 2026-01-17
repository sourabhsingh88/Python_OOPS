from pydantic import BaseModel, Field


class ManufacturerBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    country: str | None = None


class ManufacturerCreate(ManufacturerBase):
    pass


class ManufacturerResponse(ManufacturerBase):
    id: int

    class Config:
        from_attributes = True
