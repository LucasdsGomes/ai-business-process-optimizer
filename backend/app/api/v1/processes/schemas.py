from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProcessCreate(BaseModel):
    name: str
    description: Optional[str] = None

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProcessResponse(BaseModel):
    id: int
    name: str
    description: str
    status: str
    analysis_result: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
