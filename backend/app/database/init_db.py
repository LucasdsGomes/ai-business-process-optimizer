from backend.app.database.session import engine
from backend.app.database.base import Base
from backend.app.models import process, analysis, insight, automation

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db() #cmd - py -m backend.app.database.init_db
