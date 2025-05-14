# 🧠 Smart File Agent with Claude + MCP

This is a lightweight AI-powered agent built using [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) and Claude Desktop. The agent exposes local file-handling tools (like listing files, reading files, and checking file sizes) which Claude can interact with using natural language.


---

## 🚀 Features

- 📂 List all files in a directory
- 📖 Read contents of any file
- 📏 Get the size of a file
- 💬 Fully driven by Claude through chat — no prompts or hardcoding needed

---

## 📁 Files in this Repo

| File               | Description                              |
|--------------------|------------------------------------------|
| `smart_file_agent.py` | Main MCP server with all tools in one file |

---

## ⚙️ Setup Instructions

### 1. 🔧 Install MCP SDK with CLI support

```bash
pip install "mcp[cli]"
```
### 2. Add it to Agent Server
```
uv run mcp install 'file path'
```

### 3. Access from Claude
