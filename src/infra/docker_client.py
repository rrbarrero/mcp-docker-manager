from docker import DockerClient
from docker.models.containers import Container
from config import settings


class McpDockerClient:
    def __init__(self, client: DockerClient):
        self.client = client

    def run_container(self, image: str, name: str | None = None, **kwargs):
        container: Container = self.client.containers.run(
            image, detach=True, name=name, **kwargs
        )
        return container.id

    def stop_container_by_name(self, container_name: str):
        container = self.client.containers.get(container_name)
        container.stop()

    def remove_container_by_name(self, container_name: str):
        container = self.client.containers.get(container_name)
        container.remove(force=True)

    def list_containers(self) -> list[str]:
        return [container.name for container in self.client.containers.list()]

    @classmethod
    def default(cls):
        return cls(DockerClient(base_url=settings.docker_socket_path))
