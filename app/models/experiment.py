from typing import List
from sqlmodel import SQLModel, Field, Relationship
from app.models.experiment_compound import ExperimentCompound
from app.models.mixins import TimeMixin


class Experiment(SQLModel, TimeMixin, table=True):

    experiment_id: int = Field(None, primary_key=True, nullable=False)
    experiment_run_time: int = Field()
    user_id: int = Field(default=None, foreign_key="users.user_id")
    users: "Users" = Relationship(back_populates="experiments")
    compounds: List["Compound"] = Relationship(back_populates="experiments", link_model=ExperimentCompound)
    
    





