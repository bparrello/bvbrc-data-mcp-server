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

def register_strain_tools(mcp: FastMCP, base_url: str):
    """Register all strain-related MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    
    @mcp.tool()
    def bvbrc_strain_get_by_id(id: str,
                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get strain data by ID.
        
        Args:
            id: The ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted strain data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_strain_by_id(id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying strain by ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_strain_query_by_filters(filters_json: str,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query strain data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted strain data
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
            result, count = query_strain_by_filters(filters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying strain by filters: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_strain_get_by_species(species: str,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get strain data by species.
        
        Args:
            species: The species to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted strain data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_strain_by_species(species, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying strain by species: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_strain_get_by_strain(strain: str,
                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get strain data by strain name.
        
        Args:
            strain: The strain name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted strain data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_strain_by_strain(strain, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying strain by strain name: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_strain_get_by_subtype(subtype: str,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get strain data by subtype.
        
        Args:
            subtype: The subtype to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted strain data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_strain_by_subtype(subtype, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying strain by subtype: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_strain_get_by_taxon_id(taxon_id: int,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get strain data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted strain data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_strain_by_taxon_id(taxon_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying strain by taxon ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_strain_get_by_collection_year_range(start_year: int, end_year: int,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get strain data by collection year range.
        
        Args:
            start_year: Start year
            end_year: End year
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted strain data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_strain_by_collection_year_range(start_year, end_year, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying strain by collection year range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_strain_get_by_date_inserted_range(start_date: str, end_date: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get strain data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted strain data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_strain_by_date_inserted_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying strain by date inserted range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_strain_search_by_keyword(keyword: str,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search strain data by keyword.
        
        Args:
            keyword: The keyword to search for
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted strain data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_strain_by_keyword(keyword, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error searching strain by keyword: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_strain_get_all(select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all strain data.
        
        Args:
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted strain data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_strain_all(options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying all strain data: {str(e)}"
            }, indent=2)