from sqlmodel import SQLModel, Field
from app.models.mixins import TimeMixin


class ExperimentCompound(SQLModel, TimeMixin, table=True):

    experiment_id: int = Field(
        default=None, foreign_key='experiment.experiment_id', primary_key=True)
    compound_id: int = Field(
        default=None, foreign_key='compound.compound_id', primary_key=True)
