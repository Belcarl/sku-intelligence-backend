from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.sku import SKU

router = APIRouter()

@router.get("/")
def list_skus(search: str | None = None, db: Session = Depends(get_db)):
    query = db.query(SKU)

    if search:
        query = query.filter(SKU.sku_code.ilike(f"%{search}%"))

    return query.all()
