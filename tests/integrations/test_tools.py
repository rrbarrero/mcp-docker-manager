import pytest
from fastmcp import Client
from server import mcp


@pytest.fixture
async def mcp_client():
    async with Client(mcp) as client:  # type: ignore
        yield client
        await client.call_tool("stop_container", {"container_name": "hello-world"})
        await client.call_tool("remove_container", {"container_name": "hello-world"})


@pytest.mark.anyio
async def test_start_container(mcp_client):
    result = await mcp_client.call_tool(
        "start_container",
        {"container_name": "hello-world", "image": "hello-world"},
    )
    assert isinstance(result[0].text, str)
    assert len(result[0].text) > 30
