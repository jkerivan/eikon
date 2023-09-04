

from app.models.compound import Compound
from app.repository.BaseRepo import BaseRepo


class CompoundRepository(BaseRepo[Compound]):
    model = Compound