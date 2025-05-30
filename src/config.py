from pydantic import Field, field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    docker_socket_path: str = Field(
        default="/var/run/docker.sock",
        alias="DOCKER_SOCKET_PATH",
    )

    @field_validator("docker_socket_path", mode="after")
    def add_unix_prefix(cls, v: str) -> str:
        return v if v.startswith("unix://") else "unix://" + v.lstrip("/")


settings = Settings()
