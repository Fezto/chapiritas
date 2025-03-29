from pydantic import BaseModel


class SizeSchema(BaseModel):
    id: int
    name: str