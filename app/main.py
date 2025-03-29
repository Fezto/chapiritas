from fastapi import FastAPI
from app.api.routers.user import router as users_router
from app.api.routers.product import router as products_router

app = FastAPI(title="API de ejemplo para chacharitas")

# Incluye el router de usuarios
app.include_router(users_router, prefix="", tags=["users"])
app.include_router(products_router, prefix="", tags=["users"])

