from pydantic import BaseModel
from typing import List, Optional

class UserSchema(BaseModel):
    user_id: int
    name: str
    email: str
    signup_date: str
    total_experiments: Optional[int]
    avg_experiments: Optional[int]
    common_compound: Optional[str]

    class Config:
        orm_mode = True

class CompoundSchema(BaseModel):
    compound_id: int
    compound_name: str
    compound_structure: str

    class Config:
        orm_mode = True

class ExperimentSchema(BaseModel):
    experiment_id: int
    experiment_run_time: int
    user_id: int
    compounds: Optional[List[CompoundSchema]]

    class Config:
        orm_mode = True


class ExperimentCompoundSchema(BaseModel):
    experiment_id: int
    compound_id: int

    class Config:
        orm_mode = True