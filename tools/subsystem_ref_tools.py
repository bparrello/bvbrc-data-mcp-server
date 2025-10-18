#!/usr/bin/env python3
"""
BV-BRC Subsystem Reference Tools

This module contains MCP tools for querying subsystem reference data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None
_default_limit = None

from data_functions import (
    query_subsystem_ref_by_id,
    query_subsystem_ref_by_filters,
    query_subsystem_ref_by_class,
    query_subsystem_ref_by_description,
    query_subsystem_ref_by_role,
    query_subsystem_ref_by_role_id,
    query_subsystem_ref_by_subsystem_id,
    query_subsystem_ref_by_subsystem_name,
    query_subsystem_ref_by_superclass,
    query_subsystem_ref_by_date_inserted_range,
    query_subsystem_ref_by_date_modified_range,
    query_subsystem_ref_by_keyword,
    query_subsystem_ref_all,
    format_query_result
)


def register_subsystem_ref_tools(mcp: FastMCP, base_url: str, default_limit: int):
    """Register all subsystem reference-related MCP tools with the Flask app."""
    global _base_url, _default_limit
    _base_url = base_url
    _default_limit = default_limit
    

    
    @mcp.tool()
    def bvbrc_subsystem_ref_get_by_id(id: str, limit: int = _default_limit,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get subsystem reference data by ID.
        
        Args:
            id: The ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted subsystem reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_subsystem_ref_by_id(id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying subsystem reference by ID: {str(e)}"


    @mcp.tool()
    def bvbrc_subsystem_ref_query_by_filters(filters_json: str, limit: int = _default_limit,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query subsystem reference data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted subsystem reference data
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
            result = query_subsystem_ref_by_filters(filters, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying subsystem reference by filters: {str(e)}"


    @mcp.tool()
    def bvbrc_subsystem_ref_get_by_subsystem_name(subsystem_name: str, limit: int = _default_limit,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get subsystem reference data by subsystem name.
        
        Args:
            subsystem_name: The subsystem name to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted subsystem reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_subsystem_ref_by_subsystem_name(subsystem_name, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying subsystem reference by subsystem name: {str(e)}"


    @mcp.tool()
    def bvbrc_subsystem_ref_get_by_role(role: str, limit: int = _default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get subsystem reference data by role.
        
        Args:
            role: The role to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted subsystem reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_subsystem_ref_by_role(role, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying subsystem reference by role: {str(e)}"


    @mcp.tool()
    def bvbrc_subsystem_ref_get_by_class(class_name: str, limit: int = _default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get subsystem reference data by class.
        
        Args:
            class_name: The class to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted subsystem reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_subsystem_ref_by_class(class_name, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying subsystem reference by class: {str(e)}"


    @mcp.tool()
    def bvbrc_subsystem_ref_get_by_superclass(superclass: str, limit: int = _default_limit,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get subsystem reference data by superclass.
        
        Args:
            superclass: The superclass to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted subsystem reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_subsystem_ref_by_superclass(superclass, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying subsystem reference by superclass: {str(e)}"


    @mcp.tool()
    def bvbrc_subsystem_ref_get_by_date_inserted_range(start_date: str, end_date: str, limit: int = _default_limit,
                                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get subsystem reference data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted subsystem reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_subsystem_ref_by_date_inserted_range(start_date, end_date, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying subsystem reference by date inserted range: {str(e)}"


    @mcp.tool()
    def bvbrc_subsystem_ref_search_by_keyword(keyword: str, limit: int = _default_limit,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search subsystem reference data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted subsystem reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_subsystem_ref_by_keyword(keyword, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching subsystem reference by keyword: {str(e)}"


    @mcp.tool()
    def bvbrc_subsystem_ref_get_all(limit: int = _default_limit,
                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all subsystem reference data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted subsystem reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_subsystem_ref_all(options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all subsystem reference data: {str(e)}"
