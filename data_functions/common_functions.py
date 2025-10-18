"""
BV-BRC Common Functions

This module provides common utility functions for the BV-BRC Solr API.
"""

import json
from typing import Any, Dict, List
from bvbrc_solr_api import create_client, query


def create_bvbrc_client(base_url: str = None, headers: Dict[str, str] = None) -> Any:
    """
    Create a BV-BRC client with optional configuration overrides.
    
    Args:
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        BV-BRC client instance
    """
    context_overrides = {}
    if base_url:
        context_overrides["base_url"] = base_url
    if headers:
        context_overrides["headers"] = headers
    
    return create_client(context_overrides)


def query_direct(core: str, filter_str: str = "", options: Dict[str, Any] = None,
                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query BV-BRC data directly using core name and filter string.
    
    Args:
        core: The core/collection name (e.g., "genome", "genome_feature")
        filter_str: RQL filter string (e.g., "eq(genome_id,123.45)")
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of records from the specified core
    """
    context_overrides = {}
    if base_url:
        context_overrides["base_url"] = base_url
    if headers:
        context_overrides["headers"] = headers
    
    return query(core, filter_str, options or {}, context_overrides)


def format_query_result(result: List[Dict[str, Any]], max_items: int = 10) -> str:
    """
    Format query result for display.
    
    Args:
        result: List of query results
        max_items: Maximum number of items to display
        
    Returns:
        Formatted string representation of results
    """
    if not result:
        return "No results found."
    
    total_count = len(result)
    display_count = min(total_count, max_items)
    
    formatted = f"Found {total_count} result(s). Showing first {display_count}:\n\n"
    
    for i, item in enumerate(result[:display_count]):
        formatted += f"Result {i+1}:\n"
        for key, value in item.items():
            if isinstance(value, (list, dict)):
                value = json.dumps(value, indent=2)
            formatted += f"  {key}: {value}\n"
        formatted += "\n"
    
    if total_count > max_items:
        formatted += f"... and {total_count - max_items} more results.\n"
    
    return formatted
