from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from app.db.session import get_db  # Asegúrate de que la ruta es correcta según tu estructura
from app.db.models import Product  # Importa el modelo SQLAlchemy para Product
from app.schemas.product import ProductSchema  # Modelo Pydantic para Product

router = APIRouter()


@router.get("/products", response_model=List[ProductSchema])
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).options(
        joinedload(Product.categories),
        joinedload(Product.colors),
        joinedload(Product.genders),
        joinedload(Product.materials),
        joinedload(Product.sizes),
        joinedload(Product.attributes),
        joinedload(Product.images)
    ).all()
    return products


@router.get("/products/{product_id}", response_model=ProductSchema)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).options(
        joinedload(Product.categories),
        joinedload(Product.colors),
        joinedload(Product.genders),
        joinedload(Product.materials),
        joinedload(Product.sizes),
        joinedload(Product.attributes),
        joinedload(Product.images)
    ).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    return product

@router.post("/products", status_code=status.HTTP_201_CREATED, response_model=ProductSchema)
def create_product(product_data: ProductSchema, db: Session = Depends(get_db)):
    # Convertimos el modelo Pydantic a un dict y lo pasamos al constructor del modelo SQLAlchemy
    product = Product(**product_data.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
