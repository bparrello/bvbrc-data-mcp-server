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

def register_spike_lineage_tools(mcp: FastMCP, base_url: str):
    """Register all spike lineage-related MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    
    @mcp.tool()
    def bvbrc_spike_lineage_get_by_id(id: str,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike lineage data by ID.
        
        Args:
            id: The ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_lineage_by_id(id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike lineage by ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_lineage_query_by_filters(filters_json: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query spike lineage data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        try:
            filters = json.loads(filters_json)
        except json.JSONDecodeError as e:
            return f"Error parsing filters JSON: {str(e)}"
        
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_lineage_by_filters(filters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike lineage by filters: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_lineage_get_by_country(country: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike lineage data by country.
        
        Args:
            country: The country to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_lineage_by_country(country, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike lineage by country: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_lineage_get_by_growth_rate(growth_rate: float,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike lineage data by growth rate.
        
        Args:
            growth_rate: The growth rate to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_lineage_by_growth_rate(growth_rate, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike lineage by growth rate: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_lineage_get_by_lineage(lineage: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike lineage data by lineage.
        
        Args:
            lineage: The lineage to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_lineage_by_lineage(lineage, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike lineage by lineage: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_lineage_get_by_lineage_count(lineage_count: int,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike lineage data by lineage count.
        
        Args:
            lineage_count: The lineage count to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_lineage_by_lineage_count(lineage_count, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike lineage by lineage count: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_lineage_get_by_lineage_of_concern(lineage_of_concern: str,
                                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike lineage data by lineage of concern.
        
        Args:
            lineage_of_concern: The lineage of concern to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_lineage_by_lineage_of_concern(lineage_of_concern, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike lineage by lineage of concern: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_lineage_get_by_month(month: str,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike lineage data by month.
        
        Args:
            month: The month to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_lineage_by_month(month, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike lineage by month: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_lineage_get_by_prevalence(prevalence: float,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike lineage data by prevalence.
        
        Args:
            prevalence: The prevalence to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_lineage_by_prevalence(prevalence, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike lineage by prevalence: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_lineage_get_by_region(region: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike lineage data by region.
        
        Args:
            region: The region to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_lineage_by_region(region, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike lineage by region: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_lineage_get_by_sequence_features(sequence_features: str,
                                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike lineage data by sequence features.
        
        Args:
            sequence_features: The sequence features to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_lineage_by_sequence_features(sequence_features, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike lineage by sequence features: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_lineage_get_by_total_isolates(total_isolates: int,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike lineage data by total isolates.
        
        Args:
            total_isolates: The total isolates to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_lineage_by_total_isolates(total_isolates, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike lineage by total isolates: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_lineage_get_by_growth_rate_range(min_growth_rate: float, max_growth_rate: float,
                                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike lineage data by growth rate range.
        
        Args:
            min_growth_rate: Minimum growth rate
            max_growth_rate: Maximum growth rate
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_lineage_by_growth_rate_range(min_growth_rate, max_growth_rate, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike lineage by growth rate range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_lineage_get_by_lineage_count_range(min_lineage_count: int, max_lineage_count: int,
                                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike lineage data by lineage count range.
        
        Args:
            min_lineage_count: Minimum lineage count
            max_lineage_count: Maximum lineage count
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_lineage_by_lineage_count_range(min_lineage_count, max_lineage_count, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike lineage by lineage count range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_lineage_get_by_prevalence_range(min_prevalence: float, max_prevalence: float,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike lineage data by prevalence range.
        
        Args:
            min_prevalence: Minimum prevalence
            max_prevalence: Maximum prevalence
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_lineage_by_prevalence_range(min_prevalence, max_prevalence, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike lineage by prevalence range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_lineage_get_by_total_isolates_range(min_total_isolates: int, max_total_isolates: int,
                                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike lineage data by total isolates range.
        
        Args:
            min_total_isolates: Minimum total isolates
            max_total_isolates: Maximum total isolates
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_lineage_by_total_isolates_range(min_total_isolates, max_total_isolates, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike lineage by total isolates range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_lineage_get_by_date_inserted_range(start_date: str, end_date: str,
                                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike lineage data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_lineage_by_date_inserted_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike lineage by date inserted range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_lineage_get_by_date_modified_range(start_date: str, end_date: str,
                                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike lineage data by date modified range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_lineage_by_date_modified_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike lineage by date modified range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_lineage_search_by_keyword(keyword: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search spike lineage data by keyword.
        
        Args:
            keyword: The keyword to search for
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_lineage_by_keyword(keyword, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error searching spike lineage by keyword: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_lineage_get_all(select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all spike lineage data.
        
        Args:
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike lineage data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_lineage_all(options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying all spike lineage data: {str(e)}"
            }, indent=2)