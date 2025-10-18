#!/usr/bin/env python3
"""
BV-BRC Pathway Tools

This module contains MCP tools for querying pathway data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None
_default_limit = None

from data_functions import (
    query_pathway_by_id,
    query_pathway_by_filters,
    query_pathway_by_accession,
    query_pathway_by_alt_locus_tag,
    query_pathway_by_annotation,
    query_pathway_by_ec_description,
    query_pathway_by_ec_number,
    query_pathway_by_feature_id,
    query_pathway_by_gene,
    query_pathway_by_genome_ec,
    query_pathway_by_genome_id,
    query_pathway_by_genome_name,
    query_pathway_by_owner,
    query_pathway_by_pathway_class,
    query_pathway_by_pathway_ec,
    query_pathway_by_pathway_id,
    query_pathway_by_pathway_name,
    query_pathway_by_patric_id,
    query_pathway_by_product,
    query_pathway_by_public_status,
    query_pathway_by_refseq_locus_tag,
    query_pathway_by_sequence_id,
    query_pathway_by_taxon_id,
    query_pathway_by_user_read,
    query_pathway_by_user_write,
    query_pathway_by_version,
    query_pathway_by_date_inserted_range,
    query_pathway_by_date_modified_range,
    query_pathway_by_keyword,
    query_pathway_all,
    format_query_result
)


def register_pathway_tools(mcp: FastMCP, base_url: str, default_limit: int):
    """Register all pathway-related MCP tools with the Flask app."""
    global _base_url, _default_limit
    _base_url = base_url
    _default_limit = default_limit
    

    
    @mcp.tool()
    def bvbrc_pathway_get_by_id(id: str, limit: int = _default_limit,
                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by ID.
        
        Args:
            id: The ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_by_id(id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway by ID: {str(e)}"


    @mcp.tool()
    def bvbrc_pathway_query_by_filters(filters_json: str, limit: int = _default_limit,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query pathway data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
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
            result = query_pathway_by_filters(filters, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway by filters: {str(e)}"


    @mcp.tool()
    def bvbrc_pathway_get_by_genome_id(genome_id: str, limit: int = _default_limit,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by genome ID.
        
        Args:
            genome_id: The genome ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_by_genome_id(genome_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway by genome ID: {str(e)}"


    @mcp.tool()
    def bvbrc_pathway_get_by_genome_name(genome_name: str, limit: int = _default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by genome name.
        
        Args:
            genome_name: The genome name to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_by_genome_name(genome_name, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway by genome name: {str(e)}"


    @mcp.tool()
    def bvbrc_pathway_get_by_pathway_id(pathway_id: str, limit: int = _default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by pathway ID.
        
        Args:
            pathway_id: The pathway ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_by_pathway_id(pathway_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway by pathway ID: {str(e)}"


    @mcp.tool()
    def bvbrc_pathway_get_by_pathway_name(pathway_name: str, limit: int = _default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by pathway name.
        
        Args:
            pathway_name: The pathway name to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_by_pathway_name(pathway_name, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway by pathway name: {str(e)}"


    @mcp.tool()
    def bvbrc_pathway_get_by_ec_number(ec_number: str, limit: int = _default_limit,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by EC number.
        
        Args:
            ec_number: The EC number to query (e.g., "1.1.1.1")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_by_ec_number(ec_number, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway by EC number: {str(e)}"


    @mcp.tool()
    def bvbrc_pathway_get_by_gene(gene: str, limit: int = _default_limit,
                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by gene.
        
        Args:
            gene: The gene to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_by_gene(gene, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway by gene: {str(e)}"


    @mcp.tool()
    def bvbrc_pathway_get_by_taxon_id(taxon_id: int, limit: int = _default_limit,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_by_taxon_id(taxon_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway by taxon ID: {str(e)}"


    @mcp.tool()
    def bvbrc_pathway_get_by_date_inserted_range(start_date: str, end_date: str, limit: int = _default_limit,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_by_date_inserted_range(start_date, end_date, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying pathway by date inserted range: {str(e)}"


    @mcp.tool()
    def bvbrc_pathway_search_by_keyword(keyword: str, limit: int = _default_limit,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search pathway data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_by_keyword(keyword, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching pathway by keyword: {str(e)}"


    @mcp.tool()
    def bvbrc_pathway_get_all(limit: int = _default_limit,
                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all pathway data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_pathway_all(options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all pathway data: {str(e)}"
