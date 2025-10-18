#!/usr/bin/env python3
"""
BV-BRC Sequence Feature VT Tools

This module contains MCP tools for querying sequence feature VT data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None
_default_limit = None

from data_functions import (
    query_sequence_feature_vt_by_id,
    query_sequence_feature_vt_by_filters,
    query_sequence_feature_vt_by_sf_category,
    query_sequence_feature_vt_by_genome_id,
    query_sequence_feature_vt_by_taxon_id,
    query_sequence_feature_vt_by_date_inserted_range,
    query_sequence_feature_vt_by_date_modified_range,
    query_sequence_feature_vt_by_keyword,
    query_sequence_feature_vt_all,
    format_query_result
)


def register_sequence_feature_vt_tools(mcp: FastMCP, base_url: str, default_limit: int):
    """Register all sequence feature VT-related MCP tools with the Flask app."""
    global _base_url, _default_limit
    _base_url = base_url
    _default_limit = default_limit
    

    
    @mcp.tool()
    def bvbrc_sequence_feature_vt_get_by_id(id: str, limit: int = _default_limit,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature VT data by ID.
        
        Args:
            id: The ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature VT data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sequence_feature_vt_by_id(id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying sequence feature VT by ID: {str(e)}"


    @mcp.tool()
    def bvbrc_sequence_feature_vt_query_by_filters(filters_json: str, limit: int = _default_limit,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query sequence feature VT data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature VT data
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
            result = query_sequence_feature_vt_by_filters(filters, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying sequence feature VT by filters: {str(e)}"


    @mcp.tool()
    def bvbrc_sequence_feature_vt_get_by_sf_category(sf_category: str, limit: int = _default_limit,
                                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature VT data by SF category.
        
        Args:
            sf_category: The SF category to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature VT data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sequence_feature_vt_by_sf_category(sf_category, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying sequence feature VT by SF category: {str(e)}"


    @mcp.tool()
    def bvbrc_sequence_feature_vt_get_by_genome_id(genome_id: str, limit: int = _default_limit,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature VT data by genome ID.
        
        Args:
            genome_id: The genome ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature VT data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sequence_feature_vt_by_genome_id(genome_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying sequence feature VT by genome ID: {str(e)}"


    @mcp.tool()
    def bvbrc_sequence_feature_vt_get_by_taxon_id(taxon_id: int, limit: int = _default_limit,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature VT data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature VT data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sequence_feature_vt_by_taxon_id(taxon_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying sequence feature VT by taxon ID: {str(e)}"


    @mcp.tool()
    def bvbrc_sequence_feature_vt_get_by_date_inserted_range(start_date: str, end_date: str, limit: int = _default_limit,
                                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature VT data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature VT data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sequence_feature_vt_by_date_inserted_range(start_date, end_date, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying sequence feature VT by date inserted range: {str(e)}"


    @mcp.tool()
    def bvbrc_sequence_feature_vt_search_by_keyword(keyword: str, limit: int = _default_limit,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search sequence feature VT data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature VT data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sequence_feature_vt_by_keyword(keyword, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching sequence feature VT by keyword: {str(e)}"


    @mcp.tool()
    def bvbrc_sequence_feature_vt_get_all(limit: int = _default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all sequence feature VT data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature VT data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sequence_feature_vt_all(options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all sequence feature VT data: {str(e)}"
