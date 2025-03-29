from typing import Optional

from pydantic import BaseModel


class ImageSchema(BaseModel):
    id: int
    url: str
    description: Optional[str]
    order: int