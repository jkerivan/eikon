from typing import List
from sqlmodel import SQLModel, Field, Relationship
import datetime
from app.models.experiment import Experiment
from app.models.mixins import TimeMixin

class Users(SQLModel, TimeMixin, table=True):

    user_id: int = Field(None, primary_key=True, nullable=False)
    name: str = Field(unique=True)
    email: str = Field(unique=True)
    signup_date: datetime.date = Field(None, nullable=True)
    total_experiments: int = Field(None, nullable=True)
    avg_experiments: int = Field(None, nullable=True)
    common_compound: str = Field(None, nullable=True)
    experiments: List[Experiment] = Relationship(back_populates="users")




