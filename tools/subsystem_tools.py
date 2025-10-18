#!/usr/bin/env python3
"""
BV-BRC Subsystem Tools

This module contains MCP tools for querying subsystem data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None
_default_limit = None

from data_functions import (
    query_subsystem_by_id,
    query_subsystem_by_filters,
    query_subsystem_by_active,
    query_subsystem_by_class,
    query_subsystem_by_feature_id,
    query_subsystem_by_gene,
    query_subsystem_by_genome_id,
    query_subsystem_by_genome_name,
    query_subsystem_by_owner,
    query_subsystem_by_patric_id,
    query_subsystem_by_product,
    query_subsystem_by_public_status,
    query_subsystem_by_refseq_locus_tag,
    query_subsystem_by_role_id,
    query_subsystem_by_role_name,
    query_subsystem_by_subclass,
    query_subsystem_by_subsystem_id,
    query_subsystem_by_subsystem_name,
    query_subsystem_by_superclass,
    query_subsystem_by_taxon_id,
    query_subsystem_by_user_read,
    query_subsystem_by_user_write,
    query_subsystem_by_date_inserted_range,
    query_subsystem_by_date_modified_range,
    query_subsystem_by_keyword,
    query_subsystem_all,
    format_query_result
)


def register_subsystem_tools(mcp: FastMCP, base_url: str, default_limit: int):
    """Register all subsystem-related MCP tools with the Flask app."""
    global _base_url, _default_limit
    _base_url = base_url
    _default_limit = default_limit
    

    
    @mcp.tool()
    def bvbrc_subsystem_get_by_id(id: str, limit: int = _default_limit,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get subsystem data by ID.
        
        Args:
            id: The ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted subsystem data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_subsystem_by_id(id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying subsystem by ID: {str(e)}"


    @mcp.tool()
    def bvbrc_subsystem_query_by_filters(filters_json: str, limit: int = _default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query subsystem data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted subsystem data
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
            result = query_subsystem_by_filters(filters, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying subsystem by filters: {str(e)}"


    @mcp.tool()
    def bvbrc_subsystem_get_by_subsystem_name(subsystem_name: str, limit: int = _default_limit,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get subsystem data by subsystem name.
        
        Args:
            subsystem_name: The subsystem name to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted subsystem data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_subsystem_by_subsystem_name(subsystem_name, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying subsystem by subsystem name: {str(e)}"


    @mcp.tool()
    def bvbrc_subsystem_get_by_genome_id(genome_id: str, limit: int = _default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get subsystem data by genome ID.
        
        Args:
            genome_id: The genome ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted subsystem data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_subsystem_by_genome_id(genome_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying subsystem by genome ID: {str(e)}"


    @mcp.tool()
    def bvbrc_subsystem_get_by_gene(gene: str, limit: int = _default_limit,
                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get subsystem data by gene.
        
        Args:
            gene: The gene to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted subsystem data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_subsystem_by_gene(gene, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying subsystem by gene: {str(e)}"


    @mcp.tool()
    def bvbrc_subsystem_get_by_role_name(role_name: str, limit: int = _default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get subsystem data by role name.
        
        Args:
            role_name: The role name to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted subsystem data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_subsystem_by_role_name(role_name, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying subsystem by role name: {str(e)}"


    @mcp.tool()
    def bvbrc_subsystem_get_by_class(class_name: str, limit: int = _default_limit,
                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get subsystem data by class.
        
        Args:
            class_name: The class to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted subsystem data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_subsystem_by_class(class_name, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying subsystem by class: {str(e)}"


    @mcp.tool()
    def bvbrc_subsystem_get_by_superclass(superclass: str, limit: int = _default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get subsystem data by superclass.
        
        Args:
            superclass: The superclass to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted subsystem data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_subsystem_by_superclass(superclass, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying subsystem by superclass: {str(e)}"


    @mcp.tool()
    def bvbrc_subsystem_get_by_date_inserted_range(start_date: str, end_date: str, limit: int = _default_limit,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get subsystem data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted subsystem data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_subsystem_by_date_inserted_range(start_date, end_date, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying subsystem by date inserted range: {str(e)}"


    @mcp.tool()
    def bvbrc_subsystem_search_by_keyword(keyword: str, limit: int = _default_limit,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search subsystem data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted subsystem data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_subsystem_by_keyword(keyword, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching subsystem by keyword: {str(e)}"


    @mcp.tool()
    def bvbrc_subsystem_get_all(limit: int = _default_limit,
                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all subsystem data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted subsystem data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_subsystem_all(options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all subsystem data: {str(e)}"
