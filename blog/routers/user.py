from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from hashing import Hash

import schemas, models
from dB import get_db
from repository import user

router = APIRouter(
    prefix='/user',
    tags=['users']
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get(id, db)

@router.get('/', status_code=status.HTTP_200_OK, response_model=list[schemas.ShowUser])
def get_users(db: Session = Depends(get_db)):
    return user.all(db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowUser)
def update_user(id: int, request: schemas.User, db: Session = Depends(get_db)):
    return user.update(id, request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db)):
    user.delete(id, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)