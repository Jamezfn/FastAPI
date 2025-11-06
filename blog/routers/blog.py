from fastapi import APIRouter
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException, Response

import schemas, models, dB



router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBlog)
def create(request: schemas.Blog, db: Session = Depends(dB.get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlogWithUser)
def get(id: int, db: Session = Depends(dB.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    return blog

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlogWithUser])
def get_all(db: Session = Depends(dB.get_db)):
    return db.query(models.Blog).all()

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowBlog)
def update(id: int, request: schemas.Blog, db: Session = Depends(dB.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    
    blog.update(request.dict())
    db.commit()
    return blog.first()

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(dB.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')

    db.delete(blog.first())
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)