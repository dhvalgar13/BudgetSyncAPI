from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    type = Column(String)  # income, expense, saving
    category = Column(String)
    amount = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="transactions")

User.transactions = relationship("Transaction", back_populates="user")
