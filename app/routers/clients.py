from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/clients", tags=["clients"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Client])
def read_clients(db: Session = Depends(get_db)):
    return crud.get_clients(db)

@router.post("/", response_model=schemas.Client)
def create_new_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    return crud.create_client(db, client)
