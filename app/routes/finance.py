from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, schemas, crud, auth

router = APIRouter()

@router.post("/transactions", response_model=schemas.TransactionOut)
def create(tx: schemas.TransactionCreate, db: Session = Depends(database.SessionLocal), user=Depends(auth.get_current_user)):
    return crud.create_transaction(db, user.id, tx)

@router.get("/transactions", response_model=list[schemas.TransactionOut])
def read_all(db: Session = Depends(database.SessionLocal), user=Depends(auth.get_current_user)):
    return crud.get_transactions(db, user.id)
