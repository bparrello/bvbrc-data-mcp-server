#!/usr/bin/env python3
"""
BV-BRC ID Reference Tools

This module contains MCP tools for querying ID reference data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None

from data_functions import (
    query_id_ref_by_id,
    query_id_ref_by_filters,
    query_id_ref_by_id_type,
    query_id_ref_by_id_value,
    query_id_ref_by_uniprotkb_accession,
    query_id_ref_by_date_inserted_range,
    query_id_ref_by_date_modified_range,
    query_id_ref_by_keyword,
    query_id_ref_all,
    format_query_result
)

def register_id_ref_tools(mcp: FastMCP, base_url: str):
    """Register all ID reference-related MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    
    @mcp.tool()
    def bvbrc_id_ref_get_by_id(id: str,
                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get ID reference data by ID.
        
        Args:
            id: The ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted ID reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_id_ref_by_id(id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying ID reference by ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_id_ref_query_by_filters(filters_json: str,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query ID reference data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted ID reference data
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
            result, count = query_id_ref_by_filters(filters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying ID reference by filters: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_id_ref_get_by_id_type(id_type: str,
                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get ID reference data by ID type.
        
        Args:
            id_type: The ID type to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted ID reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_id_ref_by_id_type(id_type, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying ID reference by ID type: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_id_ref_get_by_id_value(id_value: str,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get ID reference data by ID value.
        
        Args:
            id_value: The ID value to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted ID reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_id_ref_by_id_value(id_value, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying ID reference by ID value: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_id_ref_get_by_uniprotkb_accession(uniprotkb_accession: str,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get ID reference data by UniProtKB accession.
        
        Args:
            uniprotkb_accession: The UniProtKB accession to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted ID reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_id_ref_by_uniprotkb_accession(uniprotkb_accession, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying ID reference by UniProtKB accession: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_id_ref_get_by_date_inserted_range(start_date: str, end_date: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get ID reference data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted ID reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_id_ref_by_date_inserted_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying ID reference by date inserted range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_id_ref_get_by_date_modified_range(start_date: str, end_date: str,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get ID reference data by date modified range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted ID reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_id_ref_by_date_modified_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying ID reference by date modified range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_id_ref_search_by_keyword(keyword: str,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search ID reference data by keyword.
        
        Args:
            keyword: The keyword to search for
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted ID reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_id_ref_by_keyword(keyword, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error searching ID reference by keyword: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_id_ref_get_all(select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all ID reference data.
        
        Args:
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted ID reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_id_ref_all(options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying all ID reference data: {str(e)}"
            }, indent=2)