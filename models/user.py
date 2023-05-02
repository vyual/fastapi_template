from datetime import datetime
from typing import Optional
from pydantic import BaseModel, constr


class User(BaseModel):
    id: Optional[int] = None
    name: str
    job_title: str
    created_at: datetime
    updated_at: datetime


class UserIn(BaseModel):
    name: constr(min_length=8, max_length=32)
    job_title: constr(min_length=1, max_length=32)
