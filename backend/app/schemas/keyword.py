from pydantic import BaseModel

class KeywordCreate(BaseModel):
    name: str

class KeywordResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
