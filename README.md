# MCP Project with Docker Server

This project uses a custom server managed through the `"mcp"` configuration for integration with [MCP](https://marketplace.visualstudio.com/items?itemName=Microsoft.mcp) in Visual Studio Code.


> [!TIP]
> Example: "*launches an http-echo container mapping port 5678*"


## Configuration

Add the following to your MCP configuration (for example, in `.vscode/settings.json` or `.mcp/config.json`):

```json
"mcp": {
    "servers": {
        "docker-manager": {
            "env": {
                "DOCKER_SOCKET_PATH": "/path/to/your/docker.sock"
            },
            "type": "stdio",
            "command": "uv",
            "args": [
                "run",
                "--directory",
                "/path/to/mcp-docker-manager/src/",
                "-m",
                "server"
            ]
        }
    }
}
```

### Key Parameters

- **DOCKER_SOCKET_PATH**: Path to your Docker socket (e.g. `/var/run/docker.sock`).
- **command**: Set to `uv` to run your Python module.
- **args**:
  - `run --directory /path/to/the/project -m src.server`: Runs the `src.server` module from the specified directory.


