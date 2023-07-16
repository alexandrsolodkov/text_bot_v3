from dataclasses import dataclass

from environs import Env


@dataclass()
class Bot:
    token: str
    admin: int
    root: int


@dataclass()
class Config:
    tg_bot: Bot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path=path)

    return Config(tg_bot=Bot(
        token=env.str("TOKEN"),
        admin=env.int("ADMIN"),
        root=env.int("ROOT")
    ))
