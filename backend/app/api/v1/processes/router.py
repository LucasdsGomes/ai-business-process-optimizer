from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from backend.app.api.v1.processes.schemas import ProcessCreate, ProcessResponse
from backend.app.api.v1.processes.service import ProcessService
from backend.app.database.deps import get_db

router = APIRouter(prefix="/processes", tags=["Processes"])

@router.post(
    "/",
    response_model=ProcessResponse,
    status_code=201
)
def create_process(
    data: ProcessCreate,
    db: Session = Depends(get_db)
):
    return ProcessService.create_process(db, data)


@router.get(
    "/",
    response_model=List[ProcessResponse]
)
def list_processes(
    db: Session = Depends(get_db)
):
    return ProcessService.list_processes(db)

@router.post("/{process_id}/analyze")
def analyze_process(
    process_id: int,
    db: Session = Depends(get_db)
):
    result = ProcessService.analyze_process(db, process_id)

    if not result:
        raise HTTPException(status_code=404, detail="Process not found")

    return {"analysis": result}