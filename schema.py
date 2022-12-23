from pydantic import BaseModel

class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True

class Book(OurBaseModel):
    title: str
    rating: int
    author_id: int


class Author(OurBaseModel):
    name: str
    age: int


