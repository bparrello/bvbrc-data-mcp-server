#!/usr/bin/env python3
"""
BV-BRC Miscellaneous NIAID SGC Tools

This module contains MCP tools for querying miscellaneous NIAID SGC data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None
_default_limit = None

from data_functions import (
    query_misc_niaid_sgc_by_id,
    query_misc_niaid_sgc_by_filters,
    query_misc_niaid_sgc_by_genus,
    query_misc_niaid_sgc_by_species,
    query_misc_niaid_sgc_by_taxon_id,
    query_misc_niaid_sgc_by_date_inserted_range,
    query_misc_niaid_sgc_by_date_modified_range,
    query_misc_niaid_sgc_by_keyword,
    query_misc_niaid_sgc_all,
    format_query_result
)


def register_misc_niaid_sgc_tools(mcp: FastMCP, base_url: str, default_limit: int):
    """Register all miscellaneous NIAID SGC-related MCP tools with the Flask app."""
    global _base_url, _default_limit
    _base_url = base_url
    _default_limit = default_limit
    

    
    @mcp.tool()
    def bvbrc_misc_niaid_sgc_get_by_id(target_id: str, limit: int = _default_limit,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get miscellaneous NIAID SGC data by target ID.
        
        Args:
            target_id: The target ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted miscellaneous NIAID SGC data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_misc_niaid_sgc_by_id(target_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying miscellaneous NIAID SGC by target ID: {str(e)}"


    @mcp.tool()
    def bvbrc_misc_niaid_sgc_query_by_filters(filters_json: str, limit: int = _default_limit,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query miscellaneous NIAID SGC data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted miscellaneous NIAID SGC data
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
            result = query_misc_niaid_sgc_by_filters(filters, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying miscellaneous NIAID SGC by filters: {str(e)}"


    @mcp.tool()
    def bvbrc_misc_niaid_sgc_get_by_genus(genus: str, limit: int = _default_limit,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get miscellaneous NIAID SGC data by genus.
        
        Args:
            genus: The genus to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted miscellaneous NIAID SGC data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_misc_niaid_sgc_by_genus(genus, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying miscellaneous NIAID SGC by genus: {str(e)}"


    @mcp.tool()
    def bvbrc_misc_niaid_sgc_get_by_species(species: str, limit: int = _default_limit,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get miscellaneous NIAID SGC data by species.
        
        Args:
            species: The species to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted miscellaneous NIAID SGC data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_misc_niaid_sgc_by_species(species, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying miscellaneous NIAID SGC by species: {str(e)}"


    @mcp.tool()
    def bvbrc_misc_niaid_sgc_get_by_taxon_id(taxon_id: int, limit: int = _default_limit,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get miscellaneous NIAID SGC data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted miscellaneous NIAID SGC data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_misc_niaid_sgc_by_taxon_id(taxon_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying miscellaneous NIAID SGC by taxon ID: {str(e)}"


    @mcp.tool()
    def bvbrc_misc_niaid_sgc_get_by_date_inserted_range(start_date: str, end_date: str, limit: int = _default_limit,
                                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get miscellaneous NIAID SGC data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted miscellaneous NIAID SGC data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_misc_niaid_sgc_by_date_inserted_range(start_date, end_date, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying miscellaneous NIAID SGC by date inserted range: {str(e)}"


    @mcp.tool()
    def bvbrc_misc_niaid_sgc_get_by_date_modified_range(start_date: str, end_date: str, limit: int = _default_limit,
                                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get miscellaneous NIAID SGC data by date modified range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted miscellaneous NIAID SGC data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_misc_niaid_sgc_by_date_modified_range(start_date, end_date, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying miscellaneous NIAID SGC by date modified range: {str(e)}"


    @mcp.tool()
    def bvbrc_misc_niaid_sgc_search_by_keyword(keyword: str, limit: int = _default_limit,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search miscellaneous NIAID SGC data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted miscellaneous NIAID SGC data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_misc_niaid_sgc_by_keyword(keyword, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching miscellaneous NIAID SGC by keyword: {str(e)}"


    @mcp.tool()
    def bvbrc_misc_niaid_sgc_get_all(limit: int = _default_limit,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all miscellaneous NIAID SGC data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted miscellaneous NIAID SGC data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_misc_niaid_sgc_all(options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all miscellaneous NIAID SGC data: {str(e)}"
