from fastapi import FastAPI
from .database import Base, engine
from .routes import users, finance

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users.router)
app.include_router(finance.router)
