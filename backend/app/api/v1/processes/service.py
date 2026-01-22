from sqlalchemy.orm import Session
from backend.app.api.v1.processes.schemas import ProcessCreate
from backend.app.database.repositories.process_repository import ProcessRepository
from backend.app.clients.llm_client import LLMClient


class ProcessService:

    @staticmethod
    def create_process(db: Session, data: ProcessCreate):
        return ProcessRepository.create(db, data)

    @staticmethod
    def list_processes(db: Session):
        return ProcessRepository.get_all(db)

    @staticmethod
    def analyze_process(db: Session, process_id: int):
        process = ProcessRepository.get_by_id(db, process_id)

        if not process:
            return None

        llm = LLMClient()
        return llm.analyze_process(
            name=process.name,
            description=process.description or ""
        )