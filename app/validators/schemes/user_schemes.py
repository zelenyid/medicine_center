from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class UserScheme(BaseModel):
    email: str
    password: str


class DiseaseHistoryScheme(BaseModel):
    id: int
    author_id: int
    patient_id: int
    title: str
    date_updated: datetime
    date_created: datetime
    diagnosis: str
    status: bool
    content: Optional[str]
    file_name: Optional[str]
