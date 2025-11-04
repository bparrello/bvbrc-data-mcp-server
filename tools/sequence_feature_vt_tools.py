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

def register_sequence_feature_vt_tools(mcp: FastMCP, base_url: str):
    """Register all sequence feature VT-related MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    
    @mcp.tool()
    def bvbrc_sequence_feature_vt_get_by_id(id: str,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature VT data by ID.
        
        Args:
            id: The ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature VT data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_vt_by_id(id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature VT by ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_vt_query_by_filters(filters_json: str,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query sequence feature VT data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature VT data
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
            result, count = query_sequence_feature_vt_by_filters(filters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature VT by filters: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_vt_get_by_sf_category(sf_category: str,
                                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature VT data by SF category.
        
        Args:
            sf_category: The SF category to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature VT data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_vt_by_sf_category(sf_category, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature VT by SF category: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_vt_get_by_genome_id(genome_id: str,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature VT data by genome ID.
        
        Args:
            genome_id: The genome ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature VT data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_vt_by_genome_id(genome_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature VT by genome ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_vt_get_by_taxon_id(taxon_id: int,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature VT data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature VT data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_vt_by_taxon_id(taxon_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature VT by taxon ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_vt_get_by_date_inserted_range(start_date: str, end_date: str,
                                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature VT data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature VT data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_vt_by_date_inserted_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature VT by date inserted range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_vt_get_by_date_modified_range(start_date: str, end_date: str,
                                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature VT data by date modified range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature VT data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_vt_by_date_modified_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature VT by date modified range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_vt_search_by_keyword(keyword: str,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search sequence feature VT data by keyword.
        
        Args:
            keyword: The keyword to search for
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature VT data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_vt_by_keyword(keyword, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error searching sequence feature VT by keyword: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_vt_get_all(select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all sequence feature VT data.
        
        Args:
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature VT data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_vt_all(options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying all sequence feature VT data: {str(e)}"
            }, indent=2)