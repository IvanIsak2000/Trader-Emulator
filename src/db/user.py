from sqlalchemy import select
from db.models import session, UserModel

from pydantic import BaseModel


class User(BaseModel):
    id: int
    uid: int
    username: str
    balance: float


class UserORM:
    def __init__(self):
        self.session = session

    def get(self, id: int) -> User | None:
        with self.session() as s:
            query = select(UserModel).where(UserModel.id == id)
            result = s.execute(query)
            user = result.scalar_one_or_none()
            if user:
                return User(
                    id=user.id,
                    uid=user.uid,
                    username=user.username,
                    balance=user.balance
                )
            return None

    def add(self, username: str) -> bool:
        with self.session() as s:
            with s.begin():
                s.add(
                    UserModel(
                        username=username
                    )
                )

                s.commit()
