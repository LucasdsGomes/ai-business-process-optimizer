from sqlalchemy.orm import Session
from backend.app.api.v1.processes.schemas import ProcessCreate
from backend.app.database.repositories.process_repository import ProcessRepository


class ProcessService:

    @staticmethod
    def create_process(db: Session, data: ProcessCreate):
        return ProcessRepository.create(db, data)

    @staticmethod
    def list_processes(db: Session):
        return ProcessRepository.get_all(db)
