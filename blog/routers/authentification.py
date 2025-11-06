from fastapi import APIRouter
from fastapi import Depends, HTTPException, status 
from sqlalchemy.orm import Session

from dB import get_db
from hashing import Hash
import models, schemas

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@router.post('/login')
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    user_in = db.query(models.User).filter(models.User.email == user.email).first()
    if not user_in:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if not Hash.verify(user.password, user_in.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")
    return user_in