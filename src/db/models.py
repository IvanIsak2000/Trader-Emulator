from sqlalchemy import create_engine
from sqlalchemy import MetaData, BigInteger, String, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from sqlalchemy.orm.session import sessionmaker

meta = MetaData()
Base = declarative_base(metadata=meta)

engine = create_engine(
    'sqlite:///db.db',
    pool_size=10,
    max_overflow=20,
    connect_args={"timeout": 30},
    pool_pre_ping=True
)

session = sessionmaker(
    engine,
    expire_on_commit=False,
)


class UserModel(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, default=0)
    uid: Mapped[int] = mapped_column(BigInteger, default=0)
    username: Mapped[str] = mapped_column(String, nullable=False)
    balance: Mapped[int] = mapped_column(Float, default=0)


meta.create_all(engine)
