from sqlalchemy import Column, Integer, String
from backend.app.database import Base

class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    type = Column(String(255), nullable=True)

    def __repr__(self):
        return f"<Topic(name='{self.name}', type='{self.type}')>"
