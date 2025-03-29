from pydantic import BaseModel


class GenderSchema(BaseModel):
    id: int
    name: str