#!/usr/bin/env python3
"""
BV-BRC Protein Family Reference Tools

This module contains MCP tools for querying protein family reference data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None

from data_functions import (
    query_protein_family_ref_by_id,
    query_protein_family_ref_by_filters,
    query_protein_family_ref_by_family_product,
    query_protein_family_ref_by_family_type,
    query_protein_family_ref_by_date_inserted_range,
    query_protein_family_ref_by_date_modified_range,
    query_protein_family_ref_by_keyword,
    query_protein_family_ref_all,
    format_query_result
)

def register_protein_family_ref_tools(mcp: FastMCP, base_url: str):
    """Register all protein family reference-related MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    
    @mcp.tool()
    def bvbrc_protein_family_ref_get_by_id(family_id: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein family reference data by family ID.
        
        Args:
            family_id: The family ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein family reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_family_ref_by_id(family_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein family reference by family ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_family_ref_query_by_filters(filters_json: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query protein family reference data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein family reference data
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
            result, count = query_protein_family_ref_by_filters(filters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein family reference by filters: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_family_ref_get_by_family_product(family_product: str,
                                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein family reference data by family product.
        
        Args:
            family_product: The family product to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein family reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_family_ref_by_family_product(family_product, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein family reference by family product: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_family_ref_get_by_family_type(family_type: str,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein family reference data by family type.
        
        Args:
            family_type: The family type to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein family reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_family_ref_by_family_type(family_type, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein family reference by family type: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_family_ref_get_by_date_inserted_range(start_date: str, end_date: str,
                                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein family reference data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein family reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_family_ref_by_date_inserted_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein family reference by date inserted range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_family_ref_get_by_date_modified_range(start_date: str, end_date: str,
                                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein family reference data by date modified range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein family reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_family_ref_by_date_modified_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein family reference by date modified range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_family_ref_search_by_keyword(keyword: str,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search protein family reference data by keyword.
        
        Args:
            keyword: The keyword to search for
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein family reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_family_ref_by_keyword(keyword, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error searching protein family reference by keyword: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_family_ref_get_all(select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all protein family reference data.
        
        Args:
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein family reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_family_ref_all(options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying all protein family reference data: {str(e)}"
            }, indent=2)