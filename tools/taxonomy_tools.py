#!/usr/bin/env python3
"""
BV-BRC Taxonomy Tools

This module contains MCP tools for querying taxonomy data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None
_default_limit = None

from data_functions import (
    query_taxonomy_by_id,
    query_taxonomy_by_filters,
    query_taxonomy_by_taxon_name,
    query_taxonomy_by_taxon_rank,
    query_taxonomy_by_lineage,
    query_taxonomy_by_lineage_ids,
    query_taxonomy_by_lineage_names,
    query_taxonomy_by_parent_id,
    query_taxonomy_by_division,
    query_taxonomy_by_genetic_code,
    query_taxonomy_by_genome_count,
    query_taxonomy_by_core_families,
    query_taxonomy_by_cds_mean,
    query_taxonomy_by_genome_length_mean,
    query_taxonomy_by_cds_mean_range,
    query_taxonomy_by_core_families_range,
    query_taxonomy_by_genetic_code_range,
    query_taxonomy_by_genome_count_range,
    query_taxonomy_by_genome_length_mean_range,
    query_taxonomy_by_parent_id_range,
    query_taxonomy_by_keyword,
    query_taxonomy_all,
    format_query_result
)


def register_taxonomy_tools(mcp: FastMCP, base_url: str, default_limit: int):
    """Register all taxonomy-related MCP tools with the Flask app."""
    global _base_url, _default_limit
    _base_url = base_url
    _default_limit = default_limit
    

    
    @mcp.tool()
    def bvbrc_taxonomy_get_by_id(taxon_id: str, limit: int = _default_limit,
                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get taxonomy data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted taxonomy data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_taxonomy_by_id(taxon_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying taxonomy by taxon ID: {str(e)}"


    @mcp.tool()
    def bvbrc_taxonomy_query_by_filters(filters_json: str, limit: int = _default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query taxonomy data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted taxonomy data
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
            result = query_taxonomy_by_filters(filters, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying taxonomy by filters: {str(e)}"


    @mcp.tool()
    def bvbrc_taxonomy_get_by_taxon_name(taxon_name: str, limit: int = _default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get taxonomy data by taxon name.
        
        Args:
            taxon_name: The taxon name to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted taxonomy data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_taxonomy_by_taxon_name(taxon_name, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying taxonomy by taxon name: {str(e)}"


    @mcp.tool()
    def bvbrc_taxonomy_get_by_taxon_rank(taxon_rank: str, limit: int = _default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get taxonomy data by taxon rank.
        
        Args:
            taxon_rank: The taxon rank to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted taxonomy data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_taxonomy_by_taxon_rank(taxon_rank, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying taxonomy by taxon rank: {str(e)}"


    @mcp.tool()
    def bvbrc_taxonomy_get_by_lineage(lineage: str, limit: int = _default_limit,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get taxonomy data by lineage.
        
        Args:
            lineage: The lineage to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted taxonomy data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_taxonomy_by_lineage(lineage, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying taxonomy by lineage: {str(e)}"


    @mcp.tool()
    def bvbrc_taxonomy_get_by_division(division: str, limit: int = _default_limit,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get taxonomy data by division.
        
        Args:
            division: The division to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted taxonomy data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_taxonomy_by_division(division, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying taxonomy by division: {str(e)}"


    @mcp.tool()
    def bvbrc_taxonomy_get_by_genetic_code(genetic_code: int, limit: int = _default_limit,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get taxonomy data by genetic code.
        
        Args:
            genetic_code: The genetic code to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted taxonomy data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_taxonomy_by_genetic_code(genetic_code, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying taxonomy by genetic code: {str(e)}"


    @mcp.tool()
    def bvbrc_taxonomy_get_by_genome_count(genome_count: int, limit: int = _default_limit,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get taxonomy data by genome count.
        
        Args:
            genome_count: The genome count to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted taxonomy data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_taxonomy_by_genome_count(genome_count, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying taxonomy by genome count: {str(e)}"


    @mcp.tool()
    def bvbrc_taxonomy_get_by_cds_mean_range(min_cds_mean: float, max_cds_mean: float, limit: int = _default_limit,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get taxonomy data by CDS mean range.
        
        Args:
            min_cds_mean: Minimum CDS mean
            max_cds_mean: Maximum CDS mean
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted taxonomy data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_taxonomy_by_cds_mean_range(min_cds_mean, max_cds_mean, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying taxonomy by CDS mean range: {str(e)}"


    @mcp.tool()
    def bvbrc_taxonomy_get_by_genome_count_range(min_genome_count: int, max_genome_count: int, limit: int = _default_limit,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get taxonomy data by genome count range.
        
        Args:
            min_genome_count: Minimum genome count
            max_genome_count: Maximum genome count
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted taxonomy data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_taxonomy_by_genome_count_range(min_genome_count, max_genome_count, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying taxonomy by genome count range: {str(e)}"


    @mcp.tool()
    def bvbrc_taxonomy_search_by_keyword(keyword: str, limit: int = _default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search taxonomy data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted taxonomy data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_taxonomy_by_keyword(keyword, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching taxonomy by keyword: {str(e)}"


    @mcp.tool()
    def bvbrc_taxonomy_get_all(limit: int = _default_limit,
                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all taxonomy data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted taxonomy data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_taxonomy_all(options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all taxonomy data: {str(e)}"
