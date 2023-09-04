from typing import List
from sqlmodel import Field, Relationship, SQLModel
from app.models.experiment_compound import ExperimentCompound
from app.models.mixins import TimeMixin

class Compound(SQLModel, TimeMixin, table=True):

    compound_id: int = Field(default=None, primary_key=True)
    compound_name: str = Field(unique=True)
    compound_structure: str = Field(unique=True)
    experiments: List["Experiment"] = Relationship(back_populates="compounds", link_model=ExperimentCompound)