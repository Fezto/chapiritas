from pydantic import BaseModel


class MaterialSchema(BaseModel):
    id: int
    name: str