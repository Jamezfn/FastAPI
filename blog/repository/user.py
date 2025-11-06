from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response

from hashing import Hash
import models, schemas

def create(request: schemas.User, db: Session):
    if db.query(models.User).filter(models.User.email == request.email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Email already exists')

    new_user = models.User(name=request.name, email=request.email, password=Hash.argon2(request.password))

    db.add(new_user)
    db.commit()
    db.refresh(new_user)    
    return new_user

def get(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found')
    return user

def all(db: Session):
    users = db.query(models.User).all()
    return users

def update(id: int, request: schemas.User, db: Session):
    user_to_update = db.query(models.User).filter(models.User.id == id)
    if not user_to_update.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found')
    
    user_to_update.update({
        'name': request.name,
        'email': request.email,
        'password': Hash.argon2(request.password)
    })
    db.commit()
    return user_to_update.first()

def delete(id: int, db: Session):
    user_to_delete = db.query(models.User).filter(models.User.id == id)
    if not user_to_delete.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found')

    db.delete(user_to_delete.first())
    db.commit()