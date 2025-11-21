from fastapi import FastAPI
from app.core.database import engine, Base
from app.routers import auth

app = FastAPI(title="Elevé Backend - Sprint 1")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/")
def root():
    return {"message": "Elevé backend is running!"}