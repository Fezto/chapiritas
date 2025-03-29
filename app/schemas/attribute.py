from pydantic import BaseModel


class AttributeSchema(BaseModel):
    id: int
    name: str
    value: float