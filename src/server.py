from typing import Any
from mcp.server.fastmcp import FastMCP

from infra.docker_client import McpDockerClient


mcp = FastMCP("Docker Container Management", "1.0.0")
client = McpDockerClient.default()


@mcp.tool()
def start_container(
    container_name: str, image: str, config: dict[str, Any] | None = None
) -> str:
    """
    Start a container with the given name and image.
    Args:
        container_name (str): The name of the container to start.
        image (str): The Docker image to use.
        **kwargs (dict[str, str]): Additional keyword arguments for container configuration
        defined here https://docker-py.readthedocs.io/en/stable/containers.html#
    Returns:
        str: The container ID of the started container.
    """
    container_id = client.run_container(image, name=container_name, **(config or {}))
    if container_id is None:
        raise ValueError("Container could not be started")
    return container_id


@mcp.tool()
def stop_container(container_name: str) -> None:
    """
    Stop a container with the given name.
    Args:
        container_name (str): The name of the container to stop.
    """
    client.stop_container_by_name(container_name)


@mcp.tool()
def remove_container(container_name: str) -> None:
    """
    Remove a container with the given name.
    Args:
        container_name (str): The name of the container to remove.
    """
    client.remove_container_by_name(container_name)


@mcp.tool()
def list_containers() -> list[str]:
    """
    List all running containers.
    Returns:
        list[str]: A list of container names.
    """
    return [container.name for container in client.client.containers.list()]


if __name__ == "__main__":
    mcp.run()
