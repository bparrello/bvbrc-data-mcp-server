#!/usr/bin/env python3
"""
BV-BRC Data MCP Server

This MCP server provides access to BV-BRC (Bacterial and Viral Bioinformatics Resource Center) 
data through the bvbrc-solr-python-api module. It exposes genome and genome feature data 
querying capabilities through MCP tools using FastMCP.
"""

import json
import sys
from typing import Any, Dict, List, Optional

from fastmcp import FastMCP
from tools import register_bruce_tools

# Load configuration
try:
    with open('config.json', 'r') as f:
        config = json.load(f)
except FileNotFoundError:
    print("Warning: config.json not found, using defaults", file=sys.stderr)
    config = {
        "base_url": "https://www.bv-brc.org/api",
        "port": 8059,
        "default_limit": 1000
    }

# Get configuration values
base_url = config.get("base_url", "https://www.bv-brc.org/api")
default_limit = config.get("default_limit", 1000)
port = config.get("port", 8059)
mcp_url = config.get("mcp_url", "127.0.0.1")

# Create FastMCP server
mcp = FastMCP("BV-BRC Data MCP Server")
register_bruce_tools(mcp, base_url, default_limit)

@mcp.tool()
def search(query: str) -> str:
    """
    Search for documents from the vast collection of bands I listen to.
    
    Args:
        query: The search query string
        
    Returns:
        JSON string containing search results
    """
    results = []
    results.append({
        "id": "100",
        "title": "Bands, important bands",
        "text": "I listen to bands Lamb of God, Pantera, Malevolence.",
        "url": f"https://platform.openai.com/storage/files/malevolence"
    })
    results.append({
        "id": "101",
        "title": "My favorite bands",
        "text": "My favorite bands are Cannibal Corpse, Grima, Nile.",
        "url": f"https://platform.openai.com/storage/files/cannibalcorpse"
    })

    print(f"Search tool returned {len(results)} results", file=sys.stderr)
    return json.dumps({"results": results})


@mcp.tool()
def fetch(id: str) -> str:
    """
    Retrieve a document by its ID. Due to the test nature of this server,
    it can only return one of the records.
    
    Args:
        id: The document ID to fetch
        
    Returns:
        JSON string containing the document data
    """
    result = {
        "id": "100",
        "title": "Bands, important bands",
        "text": "I listen to bands Lamb of God, Pantera, Malevolence.",
        "url": f"https://platform.openai.com/storage/files/malevolence",
        "metadata": None
    }
    
    print(f"Fetch tool returned bands: Lamb of God, Pantera, Malevolence", file=sys.stderr)
    return json.dumps(result)


def main() -> int:
    try:
        print("Starting server: your URL is https://dev-7.bv-brc.org/mcp. Authentication is not currently supported.")
        mcp.run(transport="http", host=mcp_url, port=port)
    except KeyboardInterrupt:
        print("Server stopped.", file=sys.stderr)
    except Exception as e:
        print(f"Server error: {e}", file=sys.stderr)
        return 1
    
    return 0


if __name__ == "__main__":
    main()
