#!/usr/bin/env python3
"""
BV-BRC Strain Tools

This module contains MCP tools for querying strain data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None
_default_limit = None

from data_functions import (
    query_strain_by_id,
    query_strain_by_filters,
    query_strain_by_collection_date,
    query_strain_by_collection_year,
    query_strain_by_family,
    query_strain_by_genus,
    query_strain_by_species,
    query_strain_by_strain,
    query_strain_by_subtype,
    query_strain_by_taxon_id,
    query_strain_by_geographic_group,
    query_strain_by_isolation_country,
    query_strain_by_host_common_name,
    query_strain_by_host_group,
    query_strain_by_host_name,
    query_strain_by_lab_host,
    query_strain_by_owner,
    query_strain_by_status,
    query_strain_by_public,
    query_strain_by_collection_year_range,
    query_strain_by_date_inserted_range,
    query_strain_by_date_modified_range,
    query_strain_by_h_type_range,
    query_strain_by_n_type_range,
    query_strain_by_segment_count_range,
    query_strain_by_taxon_id_range,
    query_strain_by_keyword,
    query_strain_all,
    format_query_result
)


def register_strain_tools(mcp: FastMCP, base_url: str, default_limit: int):
    """Register all strain-related MCP tools with the Flask app."""
    global _base_url, _default_limit
    _base_url = base_url
    _default_limit = default_limit
    

    
    @mcp.tool()
    def bvbrc_strain_get_by_id(id: str, limit: int = _default_limit,
                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get strain data by ID.
        
        Args:
            id: The ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted strain data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_strain_by_id(id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying strain by ID: {str(e)}"


    @mcp.tool()
    def bvbrc_strain_query_by_filters(filters_json: str, limit: int = _default_limit,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query strain data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted strain data
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
            result = query_strain_by_filters(filters, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying strain by filters: {str(e)}"


    @mcp.tool()
    def bvbrc_strain_get_by_species(species: str, limit: int = _default_limit,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get strain data by species.
        
        Args:
            species: The species to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted strain data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_strain_by_species(species, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying strain by species: {str(e)}"


    @mcp.tool()
    def bvbrc_strain_get_by_strain(strain: str, limit: int = _default_limit,
                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get strain data by strain name.
        
        Args:
            strain: The strain name to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted strain data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_strain_by_strain(strain, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying strain by strain name: {str(e)}"


    @mcp.tool()
    def bvbrc_strain_get_by_subtype(subtype: str, limit: int = _default_limit,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get strain data by subtype.
        
        Args:
            subtype: The subtype to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted strain data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_strain_by_subtype(subtype, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying strain by subtype: {str(e)}"


    @mcp.tool()
    def bvbrc_strain_get_by_taxon_id(taxon_id: int, limit: int = _default_limit,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get strain data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted strain data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_strain_by_taxon_id(taxon_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying strain by taxon ID: {str(e)}"


    @mcp.tool()
    def bvbrc_strain_get_by_collection_year_range(start_year: int, end_year: int, limit: int = _default_limit,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get strain data by collection year range.
        
        Args:
            start_year: Start year
            end_year: End year
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted strain data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_strain_by_collection_year_range(start_year, end_year, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying strain by collection year range: {str(e)}"


    @mcp.tool()
    def bvbrc_strain_get_by_date_inserted_range(start_date: str, end_date: str, limit: int = _default_limit,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get strain data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted strain data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_strain_by_date_inserted_range(start_date, end_date, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying strain by date inserted range: {str(e)}"


    @mcp.tool()
    def bvbrc_strain_search_by_keyword(keyword: str, limit: int = _default_limit,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search strain data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted strain data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_strain_by_keyword(keyword, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching strain by keyword: {str(e)}"


    @mcp.tool()
    def bvbrc_strain_get_all(limit: int = _default_limit,
                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all strain data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted strain data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_strain_all(options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all strain data: {str(e)}"
