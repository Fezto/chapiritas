from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db  # Asegúrate de que la ruta es correcta según tu estructura
from app.db.models import User, Product  # Importa tus modelos SQLAlchemy

router = APIRouter()  # Crea una instancia de APIRouter


# Rutas para Usuarios
@router.get("/users", response_model=list)
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return user

@router.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user_data: dict, db: Session = Depends(get_db)):
    user = User(**user_data)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Rutas para Productos

