from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database.deps import get_db
from backend.app.models.process import Process
from backend.app.schemas.process import ProcessCreate, ProcessResponse

router = APIRouter(prefix="/processes", tags=["Processes"])

@router.post("/", response_model=ProcessResponse)
def create_process(
    payload: ProcessCreate,
    db: Session = Depends(get_db),
): 
    process = Process(name=payload.name, description=payload.description, type=payload.type) #**payload.dict()
    db.add(process)
    db.commit()
    db.refresh(process)
    return process