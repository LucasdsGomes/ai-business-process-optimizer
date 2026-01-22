from sqlalchemy.orm import Session
from backend.app.api.v1.processes.schemas import ProcessCreate
from backend.app.database.repositories.process_repository import ProcessRepository
from backend.app.clients.llm_client import LLMClient
from backend.app.models.process import Process


class ProcessService:

    @staticmethod
    def create_process(db: Session, data: ProcessCreate):
        return ProcessRepository.create(db, data)

    @staticmethod
    def list_processes(db: Session):
        return ProcessRepository.get_all(db)

    @staticmethod
    def analyze_process(db, process_id: int):
        process = db.query(Process).filter(Process.id == process_id).first()

        if not process:
            return None

        if process.status == "ANALYZED":
            return process.analysis_result

        process.status = "ANALYZING"
        db.commit()

        llm = LLMClient()
        analysis = llm.analyze_process(
            name=process.name,
            description=process.description
        )

        process.analysis_result = analysis
        process.status = "ANALYZED"

        db.commit()
        db.refresh(process)

        return analysis