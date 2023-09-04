
from app.models.experiment import Experiment
from app.repository.BaseRepo import BaseRepo


class ExperimentRepository(BaseRepo[Experiment]):
    model = Experiment