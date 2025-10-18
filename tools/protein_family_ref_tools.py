#!/usr/bin/env python3
"""
BV-BRC Protein Family Reference Tools

This module contains MCP tools for querying protein family reference data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None
_default_limit = None

from data_functions import (
    query_protein_family_ref_by_id,
    query_protein_family_ref_by_filters,
    query_protein_family_ref_by_family_product,
    query_protein_family_ref_by_family_type,
    query_protein_family_ref_by_date_inserted_range,
    query_protein_family_ref_by_date_modified_range,
    query_protein_family_ref_by_keyword,
    query_protein_family_ref_all,
    format_query_result
)


def register_protein_family_ref_tools(mcp: FastMCP, base_url: str, default_limit: int):
    """Register all protein family reference-related MCP tools with the Flask app."""
    global _base_url, _default_limit
    _base_url = base_url
    _default_limit = default_limit
    

    
    @mcp.tool()
    def bvbrc_protein_family_ref_get_by_id(family_id: str, limit: int = _default_limit,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein family reference data by family ID.
        
        Args:
            family_id: The family ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein family reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_family_ref_by_id(family_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein family reference by family ID: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_family_ref_query_by_filters(filters_json: str, limit: int = _default_limit,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query protein family reference data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein family reference data
        """
        try:
            filters = json.loads(filters_json)
        except json.JSONDecodeError as e:
            return f"Error parsing filters JSON: {str(e)}"
        
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_family_ref_by_filters(filters, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein family reference by filters: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_family_ref_get_by_family_product(family_product: str, limit: int = _default_limit,
                                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein family reference data by family product.
        
        Args:
            family_product: The family product to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein family reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_family_ref_by_family_product(family_product, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein family reference by family product: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_family_ref_get_by_family_type(family_type: str, limit: int = _default_limit,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein family reference data by family type.
        
        Args:
            family_type: The family type to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein family reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_family_ref_by_family_type(family_type, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein family reference by family type: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_family_ref_get_by_date_inserted_range(start_date: str, end_date: str, limit: int = _default_limit,
                                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein family reference data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein family reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_family_ref_by_date_inserted_range(start_date, end_date, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein family reference by date inserted range: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_family_ref_get_by_date_modified_range(start_date: str, end_date: str, limit: int = _default_limit,
                                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein family reference data by date modified range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein family reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_family_ref_by_date_modified_range(start_date, end_date, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein family reference by date modified range: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_family_ref_search_by_keyword(keyword: str, limit: int = _default_limit,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search protein family reference data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein family reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_family_ref_by_keyword(keyword, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching protein family reference by keyword: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_family_ref_get_all(limit: int = _default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all protein family reference data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein family reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_family_ref_all(options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all protein family reference data: {str(e)}"
