from fastapi import FastAPI
from app.config import db

def init_app():
    db.init()

    app = FastAPI(title="Eikon Therapeutics Takehome",
                  description="Takehome Project",
                  version=1)
    
    @app.on_event("startup")
    async def startup():
        await db.create_all()

    @app.on_event("shutdown")
    async def shutdown():
        await db.close()
    
    from app.controller import etl
    app.include_router(etl.router)

    return app

app = init_app()

