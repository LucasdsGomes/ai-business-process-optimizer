from pydantic import BaseModel
from datetime import datetime

class ProcessCreate(BaseModel):
    name: str
    description: str | None = None
    type: str = "generic"


class ProcessResponse(BaseModel):
    id: int
    name: str
    description: str | None
    type: str
    created_at: datetime

    class Config:
        from_attributes = True
