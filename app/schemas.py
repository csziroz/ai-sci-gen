# Pydantic схемы для валидации

from pydantic import BaseModel

class ScientistInput(BaseModel):
    gender: str
    age: int
    field: str
    personality: str
    appearance: str

class ScientistOutput(BaseModel):
    id: int
    biography: str
    image_url: str
