from services.db_api.database import Session
from services.db_api.db_model import User


def add_user(tg_id: int, full_name: str, user_name: str):
    user = User(
        tg_id=tg_id,
        full_name=full_name,
        user_name=user_name
    )
    with Session() as session:
        session.add(user)
        session.commit()


def edit_user():
    pass


def get_user(tg_id: int):
    with Session() as session:
        return session.query(User.user_name).distinct(User.user_name).filter(User.tg_id == tg_id).all()


def exists_user(tg_id: int):
    with Session() as session:
        return session.query(User.user_name).filter(User.tg_id == tg_id).count() > 0


def delete_user(self):
    pass
