from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.models.keywords import Keyword
from backend.app.schemas.keyword import KeywordCreate, KeywordResponse

router = APIRouter(prefix="/keywords", tags=["Keywords"])

@router.post("/", response_model=KeywordResponse)
def create_keyword(data: KeywordCreate, db: Session = Depends(get_db)):
    exists = db.query(Keyword).filter(Keyword.name == data.name).first()
    if exists:
        raise HTTPException(status_code=409, detail="Keyword already exists")
    new_kw = Keyword(name=data.name)
    db.add(new_kw)
    db.commit()
    db.refresh(new_kw)
    return new_kw

@router.get("/", response_model=list[KeywordResponse])
def list_keywords(db: Session = Depends(get_db)):
    return db.query(Keyword).all()

@router.delete("/{keyword_id}")
def delete_keyword(keyword_id: int, db: Session = Depends(get_db)):
    kw = db.query(Keyword).filter(Keyword.id == keyword_id).first()
    if not kw:
        raise HTTPException(status_code=404, detail="Keyword not found")
    db.delete(kw)
    db.commit()
    return {"message": "deleted"}
