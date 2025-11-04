#!/usr/bin/env python3
"""
BV-BRC Common Tools

This module contains shared MCP tools for BV-BRC data access.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None
_default_limit = None

from data_functions import (
    query_direct,
    format_query_result
)


def register_common_tools(mcp: FastMCP, base_url: str):
    """Register common MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    
    @mcp.tool()
    def bvbrc_query_direct(core: str, filter_str: str = "",
                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query BV-BRC data directly using core name and filter string.
        
        Args:
            core: The core/collection name (e.g., "genome", "genome_feature")
            filter_str: RQL filter string (e.g., "eq(genome_id,123.45)")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted query results
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_direct(core, filter_str, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying {core}: {str(e)}"
            }, indent=2)
