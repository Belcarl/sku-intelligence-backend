from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_skus():
    return {"skus": []}

@router.post("/")
def create_sku():
    return {"message": "SKU created"}