

from app.models.experiment_compound import ExperimentCompound
from app.repository.BaseRepo import BaseRepo


class ExperimentCompoundRepository(BaseRepo[ExperimentCompound]):

    model = ExperimentCompound