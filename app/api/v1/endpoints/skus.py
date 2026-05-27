from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.sku import SKU
from app.services.scraper import scrape_google

router = APIRouter()

# -----------------------------
# 1. DATABASE LIST + SEARCH
# -----------------------------
@router.get("/")
def list_skus(search: str | None = None, db: Session = Depends(get_db)):
    query = db.query(SKU)

    if search:
        query = query.filter(SKU.sku_code.ilike(f"%{search}%"))

    return query.all()


# -----------------------------
# 2. WEB SCRAPING SEARCH
# -----------------------------
@router.get("/search-web")
def search_web_sku(sku: str):
    results = scrape_google(sku)
    return {"sku": sku, "results": results}


# -----------------------------
# 3. CREATE SKU
# -----------------------------
@router.post("/")
def create_sku(payload: dict, db: Session = Depends(get_db)):
    sku = SKU(sku_code=payload["sku_code"], user_id=payload["user_id"])
    db.add(sku)
    db.commit()
    db.refresh(sku)
    return sku
