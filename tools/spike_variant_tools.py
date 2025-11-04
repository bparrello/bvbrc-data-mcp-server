#!/usr/bin/env python3
"""
BV-BRC Spike Variant Tools

This module contains MCP tools for querying spike variant data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None

from data_functions import (
    query_spike_variant_by_id,
    query_spike_variant_by_filters,
    query_spike_variant_by_aa_variant,
    query_spike_variant_by_country,
    query_spike_variant_by_region,
    query_spike_variant_by_month,
    query_spike_variant_by_sequence_feature,
    query_spike_variant_by_growth_rate,
    query_spike_variant_by_prevalence,
    query_spike_variant_by_lineage_count,
    query_spike_variant_by_total_isolates,
    query_spike_variant_by_growth_rate_range,
    query_spike_variant_by_prevalence_range,
    query_spike_variant_by_lineage_count_range,
    query_spike_variant_by_total_isolates_range,
    query_spike_variant_by_date_range,
    query_spike_variant_by_modified_date_range,
    query_spike_variant_by_keyword,
    query_spike_variant_all,
    format_query_result
)

def register_spike_variant_tools(mcp: FastMCP, base_url: str):
    """Register all spike variant-related MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    
    @mcp.tool()
    def bvbrc_spike_variant_get_by_id(id: str,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike variant data by ID.
        
        Args:
            id: The ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_variant_by_id(id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike variant by ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_variant_query_by_filters(filters_json: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query spike variant data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
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
            result, count = query_spike_variant_by_filters(filters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike variant by filters: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_variant_get_by_aa_variant(aa_variant: str,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike variant data by amino acid variant.
        
        Args:
            aa_variant: The amino acid variant to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_variant_by_aa_variant(aa_variant, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike variant by amino acid variant: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_variant_get_by_country(country: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike variant data by country.
        
        Args:
            country: The country to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_variant_by_country(country, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike variant by country: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_variant_get_by_region(region: str,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike variant data by region.
        
        Args:
            region: The region to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_variant_by_region(region, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike variant by region: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_variant_get_by_month(month: str,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike variant data by month.
        
        Args:
            month: The month to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_variant_by_month(month, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike variant by month: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_variant_get_by_sequence_feature(sequence_feature: str,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike variant data by sequence feature.
        
        Args:
            sequence_feature: The sequence feature to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_variant_by_sequence_feature(sequence_feature, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike variant by sequence feature: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_variant_get_by_growth_rate(growth_rate: float,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike variant data by growth rate.
        
        Args:
            growth_rate: The growth rate to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_variant_by_growth_rate(growth_rate, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike variant by growth rate: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_variant_get_by_prevalence(prevalence: float,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike variant data by prevalence.
        
        Args:
            prevalence: The prevalence to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_variant_by_prevalence(prevalence, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike variant by prevalence: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_variant_get_by_lineage_count(lineage_count: int,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike variant data by lineage count.
        
        Args:
            lineage_count: The lineage count to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_variant_by_lineage_count(lineage_count, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike variant by lineage count: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_variant_get_by_total_isolates(total_isolates: int,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike variant data by total isolates.
        
        Args:
            total_isolates: The total isolates to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_variant_by_total_isolates(total_isolates, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike variant by total isolates: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_variant_get_by_growth_rate_range(min_growth_rate: float, max_growth_rate: float,
                                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike variant data by growth rate range.
        
        Args:
            min_growth_rate: Minimum growth rate
            max_growth_rate: Maximum growth rate
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_variant_by_growth_rate_range(min_growth_rate, max_growth_rate, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike variant by growth rate range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_variant_get_by_prevalence_range(min_prevalence: float, max_prevalence: float,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike variant data by prevalence range.
        
        Args:
            min_prevalence: Minimum prevalence
            max_prevalence: Maximum prevalence
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_variant_by_prevalence_range(min_prevalence, max_prevalence, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike variant by prevalence range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_variant_get_by_lineage_count_range(min_lineage_count: int, max_lineage_count: int,
                                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike variant data by lineage count range.
        
        Args:
            min_lineage_count: Minimum lineage count
            max_lineage_count: Maximum lineage count
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_variant_by_lineage_count_range(min_lineage_count, max_lineage_count, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike variant by lineage count range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_variant_get_by_total_isolates_range(min_total_isolates: int, max_total_isolates: int,
                                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike variant data by total isolates range.
        
        Args:
            min_total_isolates: Minimum total isolates
            max_total_isolates: Maximum total isolates
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_variant_by_total_isolates_range(min_total_isolates, max_total_isolates, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike variant by total isolates range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_variant_get_by_date_range(start_date: str, end_date: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike variant data by date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_variant_by_date_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike variant by date range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_variant_get_by_modified_date_range(start_date: str, end_date: str,
                                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get spike variant data by modified date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_variant_by_modified_date_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying spike variant by modified date range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_variant_search_by_keyword(keyword: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search spike variant data by keyword.
        
        Args:
            keyword: The keyword to search for
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_variant_by_keyword(keyword, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error searching spike variant by keyword: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_spike_variant_get_all(select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all spike variant data.
        
        Args:
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted spike variant data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_spike_variant_all(options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying all spike variant data: {str(e)}"
            }, indent=2)