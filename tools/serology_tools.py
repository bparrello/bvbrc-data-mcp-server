#!/usr/bin/env python3
"""
BV-BRC Serology Tools

This module contains MCP tools for querying serology data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None
_default_limit = None

from data_functions import (
    query_serology_by_id,
    query_serology_by_filters,
    query_serology_by_collection_city,
    query_serology_by_collection_country,
    query_serology_by_collection_state,
    query_serology_by_collection_year,
    query_serology_by_host_species,
    query_serology_by_host_type,
    query_serology_by_serotype,
    query_serology_by_strain,
    query_serology_by_test_type,
    query_serology_by_test_result,
    query_serology_by_test_interpretation,
    query_serology_by_test_pathogen,
    query_serology_by_test_antigen,
    query_serology_by_sample_accession,
    query_serology_by_sample_identifier,
    query_serology_by_virus_identifier,
    query_serology_by_project_identifier,
    query_serology_by_contributing_institution,
    query_serology_by_geographic_group,
    query_serology_by_host_common_name,
    query_serology_by_host_health,
    query_serology_by_host_identifier,
    query_serology_by_host_sex,
    query_serology_by_host_age,
    query_serology_by_host_age_group,
    query_serology_by_positive_definition,
    query_serology_by_taxon_lineage_id,
    query_serology_by_collection_date_range,
    query_serology_by_date_inserted_range,
    query_serology_by_date_modified_range,
    query_serology_by_keyword,
    query_serology_all,
    format_query_result
)


def register_serology_tools(mcp: FastMCP, base_url: str, default_limit: int):
    """Register all serology-related MCP tools with the Flask app."""
    global _base_url, _default_limit
    _base_url = base_url
    _default_limit = default_limit
    

    
    @mcp.tool()
    def bvbrc_serology_get_by_id(id: str, limit: int = _default_limit,
                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by ID.
        
        Args:
            id: The ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_serology_by_id(id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying serology by ID: {str(e)}"


    @mcp.tool()
    def bvbrc_serology_query_by_filters(filters_json: str, limit: int = _default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query serology data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
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
            result = query_serology_by_filters(filters, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying serology by filters: {str(e)}"


    @mcp.tool()
    def bvbrc_serology_get_by_collection_country(collection_country: str, limit: int = _default_limit,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by collection country.
        
        Args:
            collection_country: The collection country to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_serology_by_collection_country(collection_country, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying serology by collection country: {str(e)}"


    @mcp.tool()
    def bvbrc_serology_get_by_host_species(host_species: str, limit: int = _default_limit,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by host species.
        
        Args:
            host_species: The host species to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_serology_by_host_species(host_species, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying serology by host species: {str(e)}"


    @mcp.tool()
    def bvbrc_serology_get_by_serotype(serotype: str, limit: int = _default_limit,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by serotype.
        
        Args:
            serotype: The serotype to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_serology_by_serotype(serotype, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying serology by serotype: {str(e)}"


    @mcp.tool()
    def bvbrc_serology_get_by_test_type(test_type: str, limit: int = _default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by test type.
        
        Args:
            test_type: The test type to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_serology_by_test_type(test_type, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying serology by test type: {str(e)}"


    @mcp.tool()
    def bvbrc_serology_get_by_test_result(test_result: str, limit: int = _default_limit,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by test result.
        
        Args:
            test_result: The test result to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_serology_by_test_result(test_result, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying serology by test result: {str(e)}"


    @mcp.tool()
    def bvbrc_serology_get_by_collection_date_range(start_date: str, end_date: str, limit: int = _default_limit,
                                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by collection date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_serology_by_collection_date_range(start_date, end_date, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying serology by collection date range: {str(e)}"


    @mcp.tool()
    def bvbrc_serology_search_by_keyword(keyword: str, limit: int = _default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search serology data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_serology_by_keyword(keyword, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching serology by keyword: {str(e)}"


    @mcp.tool()
    def bvbrc_serology_get_all(limit: int = _default_limit,
                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all serology data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_serology_all(options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all serology data: {str(e)}"
