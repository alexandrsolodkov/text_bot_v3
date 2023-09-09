from dataclasses import dataclass

from environs import Env


@dataclass
class DatabaseConfig:
    database: str
    dh_host: str
    db_user: str
    db_password: str


@dataclass()
class Bot:
    token: str
    admin: int
    root: int


@dataclass()
class Config:
    tg_bot: Bot
    db: DatabaseConfig


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path=path)

    return Config(
        tg_bot=Bot(
            token=env.str("TOKEN"),
            admin=env.int("ADMIN"),
            root=env.int("ROOT")
        ),
        db=DatabaseConfig(
            database=env.str('DATABASE'),
            dh_host=env('DB_HOST'),
            db_user=env('DB_USER'),
            db_password=env('DB_PASSWORD')
        )
    )
