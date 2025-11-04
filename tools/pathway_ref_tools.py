#!/usr/bin/env python3
"""
BV-BRC Pathway Reference Tools

This module contains MCP tools for querying pathway reference data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None

from data_functions import (
    query_pathway_ref_by_id,
    query_pathway_ref_by_filters,
    query_pathway_ref_by_ec_number,
    query_pathway_ref_by_ec_description,
    query_pathway_ref_by_map_location,
    query_pathway_ref_by_map_name,
    query_pathway_ref_by_map_type,
    query_pathway_ref_by_occurrence,
    query_pathway_ref_by_pathway_class,
    query_pathway_ref_by_pathway_id,
    query_pathway_ref_by_pathway_name,
    query_pathway_ref_by_occurrence_range,
    query_pathway_ref_by_date_inserted_range,
    query_pathway_ref_by_date_modified_range,
    query_pathway_ref_by_keyword,
    query_pathway_ref_all,
    format_query_result
)

def register_pathway_ref_tools(mcp: FastMCP, base_url: str):
    """Register all pathway reference-related MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    
    @mcp.tool()
    def bvbrc_pathway_ref_get_by_id(id: str,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway reference data by ID.
        
        Args:
            id: The ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_ref_by_id(id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway reference by ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_ref_query_by_filters(filters_json: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query pathway reference data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
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
            result, count = query_pathway_ref_by_filters(filters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway reference by filters: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_ref_get_by_ec_number(ec_number: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway reference data by EC number.
        
        Args:
            ec_number: The EC number to query (e.g., "1.1.1.1")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_ref_by_ec_number(ec_number, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway reference by EC number: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_ref_get_by_ec_description(ec_description: str,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway reference data by EC description.
        
        Args:
            ec_description: The EC description to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_ref_by_ec_description(ec_description, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway reference by EC description: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_ref_get_by_map_location(map_location: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway reference data by map location.
        
        Args:
            map_location: The map location to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_ref_by_map_location(map_location, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway reference by map location: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_ref_get_by_map_name(map_name: str,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway reference data by map name.
        
        Args:
            map_name: The map name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_ref_by_map_name(map_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway reference by map name: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_ref_get_by_map_type(map_type: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway reference data by map type.
        
        Args:
            map_type: The map type to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_ref_by_map_type(map_type, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway reference by map type: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_ref_get_by_occurrence(occurrence: int,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway reference data by occurrence.
        
        Args:
            occurrence: The occurrence to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_ref_by_occurrence(occurrence, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway reference by occurrence: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_ref_get_by_pathway_class(pathway_class: str,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway reference data by pathway class.
        
        Args:
            pathway_class: The pathway class to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_ref_by_pathway_class(pathway_class, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway reference by pathway class: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_ref_get_by_pathway_id(pathway_id: str,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway reference data by pathway ID.
        
        Args:
            pathway_id: The pathway ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_ref_by_pathway_id(pathway_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway reference by pathway ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_ref_get_by_pathway_name(pathway_name: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway reference data by pathway name.
        
        Args:
            pathway_name: The pathway name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_ref_by_pathway_name(pathway_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway reference by pathway name: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_ref_get_by_occurrence_range(min_occurrence: int, max_occurrence: int,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway reference data by occurrence range.
        
        Args:
            min_occurrence: Minimum occurrence
            max_occurrence: Maximum occurrence
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_ref_by_occurrence_range(min_occurrence, max_occurrence, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway reference by occurrence range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_ref_get_by_date_inserted_range(start_date: str, end_date: str,
                                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway reference data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_ref_by_date_inserted_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway reference by date inserted range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_ref_get_by_date_modified_range(start_date: str, end_date: str,
                                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway reference data by date modified range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_ref_by_date_modified_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway reference by date modified range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_ref_search_by_keyword(keyword: str,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search pathway reference data by keyword.
        
        Args:
            keyword: The keyword to search for
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_ref_by_keyword(keyword, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error searching pathway reference by keyword: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_ref_get_all(select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all pathway reference data.
        
        Args:
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_ref_all(options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying all pathway reference data: {str(e)}"
            }, indent=2)