from fastapi import FastAPI
from app.api.routers.user import router as users_router
from app.api.routers.product import router as products_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API de ejemplo para chacharitas")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://chacharitas.org", "https://www.chacharitas.org"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Incluye el router de usuarios
app.include_router(users_router, prefix="", tags=["users"])
app.include_router(products_router, prefix="", tags=["users"])

