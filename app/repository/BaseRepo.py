from typing import Generic, TypeVar, List, Type
from app.config import db, commit_rollback
from sqlalchemy.future import select

T = TypeVar('T')


class BaseRepo(Generic[T]):
    model: Type[T]

    @classmethod
    async def create(cls, model_instance: T):
        if not isinstance(model_instance, cls.model):
            raise ValueError(f"model_instance must be an instance of {cls.model}")
        db.add(model_instance)
        await commit_rollback()
        return model_instance
    
    @classmethod
    async def get_all(cls):
        query = select(cls.model)
        return (await db.execute(query)).scalars().all()
    
    @classmethod 
    async def create_all(cls, models: List[T]):
        db.add_all(models)
        await commit_rollback()