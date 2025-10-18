#!/usr/bin/env python3
"""
BV-BRC Enzyme Class Reference Tools

This module contains MCP tools for querying enzyme class reference data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None
_default_limit = None

from data_functions import (
    query_enzyme_class_ref_by_ec_number,
    query_enzyme_class_ref_by_filters,
    query_enzyme_class_ref_by_ec_description,
    query_enzyme_class_ref_by_go_term,
    query_enzyme_class_ref_by_version,
    query_enzyme_class_ref_by_date_inserted_range,
    query_enzyme_class_ref_by_date_modified_range,
    query_enzyme_class_ref_by_keyword,
    query_enzyme_class_ref_all,
    format_query_result
)


def register_enzyme_class_ref_tools(mcp: FastMCP, base_url: str, default_limit: int):
    """Register all enzyme class reference-related MCP tools with the Flask app."""
    global _base_url, _default_limit
    _base_url = base_url
    _default_limit = default_limit
    

    
    @mcp.tool()
    def bvbrc_enzyme_class_ref_get_by_ec_number(ec_number: str, limit: int = _default_limit,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get enzyme class reference data by EC number.
        
        Args:
            ec_number: The EC number to query (e.g., "1.1.1.1")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted enzyme class reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_enzyme_class_ref_by_ec_number(ec_number, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying enzyme class reference by EC number: {str(e)}"


    @mcp.tool()
    def bvbrc_enzyme_class_ref_query_by_filters(filters_json: str, limit: int = _default_limit,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query enzyme class reference data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria (e.g., '{"ec_description": "alcohol dehydrogenase", "go": "GO:0004024"}')
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted enzyme class reference data
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
            result = query_enzyme_class_ref_by_filters(filters, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying enzyme class reference by filters: {str(e)}"


    @mcp.tool()
    def bvbrc_enzyme_class_ref_get_by_ec_description(ec_description: str, limit: int = _default_limit,
                                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get enzyme class reference data by EC description.
        
        Args:
            ec_description: The EC description to query (e.g., "alcohol dehydrogenase")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted enzyme class reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_enzyme_class_ref_by_ec_description(ec_description, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying enzyme class reference by EC description: {str(e)}"


    @mcp.tool()
    def bvbrc_enzyme_class_ref_get_by_go_term(go_term: str, limit: int = _default_limit,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get enzyme class reference data by GO term.
        
        Args:
            go_term: The GO term to query (e.g., "GO:0004024")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted enzyme class reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_enzyme_class_ref_by_go_term(go_term, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying enzyme class reference by GO term: {str(e)}"


    @mcp.tool()
    def bvbrc_enzyme_class_ref_get_by_version(version: int, limit: int = _default_limit,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get enzyme class reference data by version.
        
        Args:
            version: The version number to query (e.g., 1)
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted enzyme class reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_enzyme_class_ref_by_version(version, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying enzyme class reference by version: {str(e)}"


    @mcp.tool()
    def bvbrc_enzyme_class_ref_get_by_date_inserted_range(start_date: str, end_date: str, limit: int = _default_limit,
                                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get enzyme class reference data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted enzyme class reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_enzyme_class_ref_by_date_inserted_range(start_date, end_date, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying enzyme class reference by date inserted range: {str(e)}"


    @mcp.tool()
    def bvbrc_enzyme_class_ref_get_by_date_modified_range(start_date: str, end_date: str, limit: int = _default_limit,
                                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get enzyme class reference data by date modified range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted enzyme class reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_enzyme_class_ref_by_date_modified_range(start_date, end_date, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying enzyme class reference by date modified range: {str(e)}"


    @mcp.tool()
    def bvbrc_enzyme_class_ref_search_by_keyword(keyword: str, limit: int = _default_limit,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search enzyme class reference data by keyword.
        
        Args:
            keyword: The keyword to search for (e.g., "dehydrogenase")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted enzyme class reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_enzyme_class_ref_by_keyword(keyword, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching enzyme class reference by keyword: {str(e)}"


    @mcp.tool()
    def bvbrc_enzyme_class_ref_get_all(limit: int = _default_limit,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all enzyme class reference data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted enzyme class reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_enzyme_class_ref_all(options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all enzyme class reference data: {str(e)}"
