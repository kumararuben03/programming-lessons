from databases import Base
from sqlalchemy import Column, Integer, String

class Todos(Base):
    __tablename__ = 'todo'

    task_id = Column(Integer, primary_key=True, index=True)
    date = Column(String)
    user = Column(String)
    task = Column(String)
    priority = Column(Integer)
