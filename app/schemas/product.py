from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from app.schemas.attribute import AttributeSchema
from app.schemas.category import CategorySchema
from app.schemas.color import ColorSchema
from app.schemas.gender import GenderSchema
from app.schemas.image import ImageSchema
from app.schemas.material import MaterialSchema
from app.schemas.size import SizeSchema


class ProductSchema(BaseModel):
    id: int
    name: str
    price: float
    quantity: Optional[int]
    user_id: int
    brand_id: int
    description: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]

    categories: List[CategorySchema] = []
    colors: List[ColorSchema] = []
    genders: List[GenderSchema] = []
    materials: List[MaterialSchema] = []
    sizes: List[SizeSchema] = []
    attributes: List[AttributeSchema] = []
    images: List[ImageSchema] = []

    class Config:
        from_attributes = True
