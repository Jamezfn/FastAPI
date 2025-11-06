from fastapi import APIRouter
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException, Response

import schemas, models, dB
from repository import blog



router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBlog)
def create(request: schemas.Blog, db: Session = Depends(dB.get_db)):
    return blog.create(request, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlogWithUser)
def get(id: int, db: Session = Depends(dB.get_db)):
    return blog.get(id, db)

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlogWithUser])
def get_all(db: Session = Depends(dB.get_db)):
    return blog.all(db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowBlog)
def update(id: int, request: schemas.Blog, db: Session = Depends(dB.get_db)):
    return blog.update(id, request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(dB.get_db)):
    blog.delete(id, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)