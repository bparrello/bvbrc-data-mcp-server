"""
BV-BRC Common Functions

This module provides common utility functions for the BV-BRC Solr API.
"""

import json
from typing import Any, Dict, List, Tuple
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
                base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query BV-BRC data directly using core name and filter string with cursor-based streaming.
    
    Args:
        core: The core/collection name (e.g., "genome", "genome_feature")
        filter_str: RQL filter string (e.g., "eq(genome_id,123.45)")
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of records from the specified core, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    # Use stream_all_solr for cursor-based streaming
    pager = getattr(client, core).stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=filter_str if filter_str else "*:*",
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


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
