#!/usr/bin/env python3
"""
BV-BRC Pathway Reference Tools

This module contains MCP tools for querying pathway reference data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None
_default_limit = None

from data_functions import (
    query_pathway_ref_by_id,
    query_pathway_ref_by_filters,
    query_pathway_ref_by_ec_number,
    query_pathway_ref_by_ec_description,
    query_pathway_ref_by_map_location,
    query_pathway_ref_by_map_name,
    query_pathway_ref_by_map_type,
    query_pathway_ref_by_occurrence,
    query_pathway_ref_by_pathway_class,
    query_pathway_ref_by_pathway_id,
    query_pathway_ref_by_pathway_name,
    query_pathway_ref_by_occurrence_range,
    query_pathway_ref_by_date_inserted_range,
    query_pathway_ref_by_date_modified_range,
    query_pathway_ref_by_keyword,
    query_pathway_ref_all,
    format_query_result
)


def register_pathway_ref_tools(mcp: FastMCP, base_url: str, default_limit: int):
    """Register all pathway reference-related MCP tools with the Flask app."""
    global _base_url, _default_limit
    _base_url = base_url
    _default_limit = default_limit
    

    
    @mcp.tool()
    def bvbrc_pathway_ref_get_by_id(id: str, limit: int = _default_limit,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway reference data by ID.
        
        Args:
            id: The ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_ref_by_id(id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway reference by ID: {str(e)}"


    @mcp.tool()
    def bvbrc_pathway_ref_query_by_filters(filters_json: str, limit: int = _default_limit,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query pathway reference data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
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
            result = query_pathway_ref_by_filters(filters, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway reference by filters: {str(e)}"


    @mcp.tool()
    def bvbrc_pathway_ref_get_by_ec_number(ec_number: str, limit: int = _default_limit,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway reference data by EC number.
        
        Args:
            ec_number: The EC number to query (e.g., "1.1.1.1")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_ref_by_ec_number(ec_number, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway reference by EC number: {str(e)}"


    @mcp.tool()
    def bvbrc_pathway_ref_get_by_pathway_id(pathway_id: str, limit: int = _default_limit,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway reference data by pathway ID.
        
        Args:
            pathway_id: The pathway ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_ref_by_pathway_id(pathway_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway reference by pathway ID: {str(e)}"


    @mcp.tool()
    def bvbrc_pathway_ref_get_by_pathway_name(pathway_name: str, limit: int = _default_limit,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway reference data by pathway name.
        
        Args:
            pathway_name: The pathway name to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_ref_by_pathway_name(pathway_name, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway reference by pathway name: {str(e)}"


    @mcp.tool()
    def bvbrc_pathway_ref_get_by_pathway_class(pathway_class: str, limit: int = _default_limit,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway reference data by pathway class.
        
        Args:
            pathway_class: The pathway class to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_ref_by_pathway_class(pathway_class, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway reference by pathway class: {str(e)}"


    @mcp.tool()
    def bvbrc_pathway_ref_get_by_occurrence(occurrence: int, limit: int = _default_limit,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway reference data by occurrence.
        
        Args:
            occurrence: The occurrence to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_ref_by_occurrence(occurrence, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway reference by occurrence: {str(e)}"


    @mcp.tool()
    def bvbrc_pathway_ref_get_by_occurrence_range(min_occurrence: int, max_occurrence: int, limit: int = _default_limit,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway reference data by occurrence range.
        
        Args:
            min_occurrence: Minimum occurrence
            max_occurrence: Maximum occurrence
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_ref_by_occurrence_range(min_occurrence, max_occurrence, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway reference by occurrence range: {str(e)}"


    @mcp.tool()
    def bvbrc_pathway_ref_get_by_date_inserted_range(start_date: str, end_date: str, limit: int = _default_limit,
                                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway reference data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_ref_by_date_inserted_range(start_date, end_date, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway reference by date inserted range: {str(e)}"


    @mcp.tool()
    def bvbrc_pathway_ref_search_by_keyword(keyword: str, limit: int = _default_limit,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search pathway reference data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_ref_by_keyword(keyword, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching pathway reference by keyword: {str(e)}"


    @mcp.tool()
    def bvbrc_pathway_ref_get_all(limit: int = _default_limit,
                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all pathway reference data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_ref_all(options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all pathway reference data: {str(e)}"
