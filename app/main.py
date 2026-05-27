from app.api.v1.endpoints import auth, skus, health

app.include_router(auth.router, prefix="/api/v1/auth")
app.include_router(skus.router, prefix="/api/v1/skus")
app.include_router(health.router, prefix="/api/v1/health")
