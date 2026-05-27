from fastapi import FastAPI
from app.api.v1 import auth, skus, health
from app.core.config import settings

app = FastAPI(title="SKU Intelligence API")

app.include_router(health.router, prefix="/api/v1/health", tags=["Health"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(skus.router, prefix="/api/v1/skus", tags=["SKUs"])

@app.get("/")
def root():
    return {"message": "SKU Intelligence API is running", "env": settings.ENV}
