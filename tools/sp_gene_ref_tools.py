#!/usr/bin/env python3
"""
BV-BRC SP Gene Reference Tools

This module contains MCP tools for querying SP gene reference data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None
_default_limit = None

from data_functions import (
    query_sp_gene_ref_by_id,
    query_sp_gene_ref_by_filters,
    query_sp_gene_ref_by_antibiotics,
    query_sp_gene_ref_by_gene_symbol,
    query_sp_gene_ref_by_source,
    query_sp_gene_ref_by_taxon_id,
    query_sp_gene_ref_by_date_inserted_range,
    query_sp_gene_ref_by_date_modified_range,
    query_sp_gene_ref_by_keyword,
    query_sp_gene_ref_all,
    format_query_result
)


def register_sp_gene_ref_tools(mcp: FastMCP, base_url: str, default_limit: int):
    """Register all SP gene reference-related MCP tools with the Flask app."""
    global _base_url, _default_limit
    _base_url = base_url
    _default_limit = default_limit
    

    
    @mcp.tool()
    def bvbrc_sp_gene_ref_get_by_id(id: str, limit: int = _default_limit,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get SP gene reference data by ID.
        
        Args:
            id: The ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted SP gene reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sp_gene_ref_by_id(id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying SP gene reference by ID: {str(e)}"


    @mcp.tool()
    def bvbrc_sp_gene_ref_query_by_filters(filters_json: str, limit: int = _default_limit,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query SP gene reference data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted SP gene reference data
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
            result = query_sp_gene_ref_by_filters(filters, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying SP gene reference by filters: {str(e)}"


    @mcp.tool()
    def bvbrc_sp_gene_ref_get_by_antibiotics(antibiotics: str, limit: int = _default_limit,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get SP gene reference data by antibiotics.
        
        Args:
            antibiotics: The antibiotics to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted SP gene reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sp_gene_ref_by_antibiotics(antibiotics, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying SP gene reference by antibiotics: {str(e)}"


    @mcp.tool()
    def bvbrc_sp_gene_ref_get_by_gene_symbol(gene_symbol: str, limit: int = _default_limit,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get SP gene reference data by gene symbol.
        
        Args:
            gene_symbol: The gene symbol to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted SP gene reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sp_gene_ref_by_gene_symbol(gene_symbol, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying SP gene reference by gene symbol: {str(e)}"


    @mcp.tool()
    def bvbrc_sp_gene_ref_get_by_taxon_id(taxon_id: int, limit: int = _default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get SP gene reference data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted SP gene reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sp_gene_ref_by_taxon_id(taxon_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying SP gene reference by taxon ID: {str(e)}"


    @mcp.tool()
    def bvbrc_sp_gene_ref_get_by_date_inserted_range(start_date: str, end_date: str, limit: int = _default_limit,
                                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get SP gene reference data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted SP gene reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sp_gene_ref_by_date_inserted_range(start_date, end_date, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying SP gene reference by date inserted range: {str(e)}"


    @mcp.tool()
    def bvbrc_sp_gene_ref_search_by_keyword(keyword: str, limit: int = _default_limit,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search SP gene reference data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted SP gene reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sp_gene_ref_by_keyword(keyword, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching SP gene reference by keyword: {str(e)}"


    @mcp.tool()
    def bvbrc_sp_gene_ref_get_all(limit: int = _default_limit,
                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all SP gene reference data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted SP gene reference data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_sp_gene_ref_all(options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all SP gene reference data: {str(e)}"
