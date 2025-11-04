#!/usr/bin/env python3
"""
BV-BRC Structured Assertion Tools

This module contains MCP tools for querying structured assertion data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None

from data_functions import (
    query_structured_assertion_by_id,
    query_structured_assertion_by_filters,
    query_structured_assertion_by_comment,
    query_structured_assertion_by_evidence_code,
    query_structured_assertion_by_feature_id,
    query_structured_assertion_by_owner,
    query_structured_assertion_by_patric_id,
    query_structured_assertion_by_pmid,
    query_structured_assertion_by_property,
    query_structured_assertion_by_public_status,
    query_structured_assertion_by_refseq_locus_tag,
    query_structured_assertion_by_score,
    query_structured_assertion_by_source,
    query_structured_assertion_by_value,
    query_structured_assertion_by_user_read,
    query_structured_assertion_by_user_write,
    query_structured_assertion_by_version,
    query_structured_assertion_by_date_inserted_range,
    query_structured_assertion_by_date_modified_range,
    query_structured_assertion_by_keyword,
    query_structured_assertion_all,
    format_query_result
)

def register_structured_assertion_tools(mcp: FastMCP, base_url: str):
    """Register all structured assertion-related MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    
    @mcp.tool()
    def bvbrc_structured_assertion_get_by_id(id: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get structured assertion data by ID.
        
        Args:
            id: The ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted structured assertion data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_structured_assertion_by_id(id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying structured assertion by ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_structured_assertion_query_by_filters(filters_json: str,
                                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query structured assertion data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted structured assertion data
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
            result, count = query_structured_assertion_by_filters(filters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying structured assertion by filters: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_structured_assertion_get_by_feature_id(feature_id: str,
                                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get structured assertion data by feature ID.
        
        Args:
            feature_id: The feature ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted structured assertion data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_structured_assertion_by_feature_id(feature_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying structured assertion by feature ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_structured_assertion_get_by_patric_id(patric_id: str,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get structured assertion data by PATRIC ID.
        
        Args:
            patric_id: The PATRIC ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted structured assertion data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_structured_assertion_by_patric_id(patric_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying structured assertion by PATRIC ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_structured_assertion_get_by_property(property: str,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get structured assertion data by property.
        
        Args:
            property: The property to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted structured assertion data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_structured_assertion_by_property(property, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying structured assertion by property: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_structured_assertion_get_by_evidence_code(evidence_code: str,
                                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get structured assertion data by evidence code.
        
        Args:
            evidence_code: The evidence code to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted structured assertion data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_structured_assertion_by_evidence_code(evidence_code, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying structured assertion by evidence code: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_structured_assertion_get_by_date_inserted_range(start_date: str, end_date: str,
                                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get structured assertion data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted structured assertion data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_structured_assertion_by_date_inserted_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying structured assertion by date inserted range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_structured_assertion_search_by_keyword(keyword: str,
                                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search structured assertion data by keyword.
        
        Args:
            keyword: The keyword to search for
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted structured assertion data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_structured_assertion_by_keyword(keyword, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error searching structured assertion by keyword: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_structured_assertion_get_all(select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all structured assertion data.
        
        Args:
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted structured assertion data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_structured_assertion_all(options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying all structured assertion data: {str(e)}"
            }, indent=2)