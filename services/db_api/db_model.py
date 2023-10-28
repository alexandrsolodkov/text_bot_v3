from sqlalchemy import Column, Integer, String

from services.db_api.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer, nullable=False)
    full_name = Column(String)
    user_name = Column(String, nullable=False)

    def __init__(self, tg_id: int, full_name: str, user_name: str):
        self.tg_id = tg_id
        self.user_name = user_name
        self.full_name = full_name
