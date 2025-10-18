#!/usr/bin/env python3
"""
BV-BRC Spike Lineage Tools

This module contains MCP tools for querying spike lineage data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None
_default_limit = None

from data_functions import (
    query_spike_lineage_by_id,
    query_spike_lineage_by_filters,
    query_spike_lineage_by_country,
    query_spike_lineage_by_growth_rate,
    query_spike_lineage_by_lineage,
    query_spike_lineage_by_lineage_count,
    query_spike_lineage_by_lineage_of_concern,
    query_spike_lineage_by_month,
    query_spike_lineage_by_prevalence,
    query_spike_lineage_by_region,
    query_spike_lineage_by_sequence_features,
    query_spike_lineage_by_total_isolates,
    query_spike_lineage_by_growth_rate_range,
    query_spike_lineage_by_lineage_count_range,
    query_spike_lineage_by_prevalence_range,
    query_spike_lineage_by_total_isolates_range,
    query_spike_lineage_by_date_inserted_range,
    query_spike_lineage_by_date_modified_range,
    query_spike_lineage_by_keyword,
    query_spike_lineage_all,
    format_query_result
)


def register_spike_lineage_tools(mcp: FastMCP, base_url: str, default_limit: int):
    """Register all spike lineage-related MCP tools with the Flask app."""
    global _base_url, _default_limit
    _base_url = base_url
    _default_limit = default_limit
    

    
    @mcp.tool()
    def bvbrc_spike_lineage_get_by_id(id: str, limit: int = _default_limit,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike lineage data by ID.
        
        Args:
            id: The ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_spike_lineage_by_id(id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying spike lineage by ID: {str(e)}"


    @mcp.tool()
    def bvbrc_spike_lineage_query_by_filters(filters_json: str, limit: int = _default_limit,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query spike lineage data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
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
            result = query_spike_lineage_by_filters(filters, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying spike lineage by filters: {str(e)}"


    @mcp.tool()
    def bvbrc_spike_lineage_get_by_country(country: str, limit: int = _default_limit,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike lineage data by country.
        
        Args:
            country: The country to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_spike_lineage_by_country(country, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying spike lineage by country: {str(e)}"


    @mcp.tool()
    def bvbrc_spike_lineage_get_by_lineage(lineage: str, limit: int = _default_limit,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike lineage data by lineage.
        
        Args:
            lineage: The lineage to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_spike_lineage_by_lineage(lineage, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying spike lineage by lineage: {str(e)}"


    @mcp.tool()
    def bvbrc_spike_lineage_get_by_region(region: str, limit: int = _default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike lineage data by region.
        
        Args:
            region: The region to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_spike_lineage_by_region(region, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying spike lineage by region: {str(e)}"


    @mcp.tool()
    def bvbrc_spike_lineage_get_by_growth_rate_range(min_growth_rate: float, max_growth_rate: float, limit: int = _default_limit,
                                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike lineage data by growth rate range.
        
        Args:
            min_growth_rate: Minimum growth rate
            max_growth_rate: Maximum growth rate
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_spike_lineage_by_growth_rate_range(min_growth_rate, max_growth_rate, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying spike lineage by growth rate range: {str(e)}"


    @mcp.tool()
    def bvbrc_spike_lineage_get_by_prevalence_range(min_prevalence: float, max_prevalence: float, limit: int = _default_limit,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike lineage data by prevalence range.
        
        Args:
            min_prevalence: Minimum prevalence
            max_prevalence: Maximum prevalence
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_spike_lineage_by_prevalence_range(min_prevalence, max_prevalence, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying spike lineage by prevalence range: {str(e)}"


    @mcp.tool()
    def bvbrc_spike_lineage_get_by_date_inserted_range(start_date: str, end_date: str, limit: int = _default_limit,
                                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike lineage data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_spike_lineage_by_date_inserted_range(start_date, end_date, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying spike lineage by date inserted range: {str(e)}"


    @mcp.tool()
    def bvbrc_spike_lineage_search_by_keyword(keyword: str, limit: int = _default_limit,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search spike lineage data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_spike_lineage_by_keyword(keyword, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching spike lineage by keyword: {str(e)}"


    @mcp.tool()
    def bvbrc_spike_lineage_get_all(limit: int = _default_limit,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all spike lineage data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_spike_lineage_all(options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all spike lineage data: {str(e)}"
