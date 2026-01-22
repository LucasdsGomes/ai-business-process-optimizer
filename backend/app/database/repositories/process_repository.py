from sqlalchemy.orm import Session
from app.models.process import Process
from app.api.v1.processes.schemas import ProcessCreate


class ProcessRepository:

    @staticmethod
    def create(db: Session, data: ProcessCreate) -> Process:
        process = Process(
            name=data.name,
            description=data.description
        )
        db.add(process)
        db.commit()
        db.refresh(process)
        return process

    @staticmethod
    def get_all(db: Session):
        return db.query(Process).all()
