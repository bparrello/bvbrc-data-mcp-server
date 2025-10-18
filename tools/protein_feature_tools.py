#!/usr/bin/env python3
"""
BV-BRC Protein Feature Tools

This module contains MCP tools for querying protein feature data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None
_default_limit = None

from data_functions import (
    query_protein_feature_by_id,
    query_protein_feature_by_filters,
    query_protein_feature_by_aa_sequence_md5,
    query_protein_feature_by_classification,
    query_protein_feature_by_comment,
    query_protein_feature_by_description,
    query_protein_feature_by_e_value,
    query_protein_feature_by_end,
    query_protein_feature_by_evidence,
    query_protein_feature_by_feature_id,
    query_protein_feature_by_feature_type,
    query_protein_feature_by_gene,
    query_protein_feature_by_genome_id,
    query_protein_feature_by_genome_name,
    query_protein_feature_by_interpro_description,
    query_protein_feature_by_interpro_id,
    query_protein_feature_by_length,
    query_protein_feature_by_patric_id,
    query_protein_feature_by_product,
    query_protein_feature_by_publication,
    query_protein_feature_by_refseq_locus_tag,
    query_protein_feature_by_score,
    query_protein_feature_by_segment,
    query_protein_feature_by_sequence,
    query_protein_feature_by_source,
    query_protein_feature_by_source_id,
    query_protein_feature_by_start,
    query_protein_feature_by_taxon_id,
    query_protein_feature_by_score_range,
    query_protein_feature_by_length_range,
    query_protein_feature_by_position_range,
    query_protein_feature_by_date_inserted_range,
    query_protein_feature_by_date_modified_range,
    query_protein_feature_by_keyword,
    query_protein_feature_all,
    format_query_result
)


def register_protein_feature_tools(mcp: FastMCP, base_url: str, default_limit: int):
    """Register all protein feature-related MCP tools with the Flask app."""
    global _base_url, _default_limit
    _base_url = base_url
    _default_limit = default_limit
    

    
    @mcp.tool()
    def bvbrc_protein_feature_get_by_id(id: str, limit: int = _default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by ID.
        
        Args:
            id: The ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_feature_by_id(id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein feature by ID: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_feature_query_by_filters(filters_json: str, limit: int = _default_limit,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query protein feature data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
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
            result = query_protein_feature_by_filters(filters, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein feature by filters: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_feature_get_by_genome_id(genome_id: str, limit: int = _default_limit,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by genome ID.
        
        Args:
            genome_id: The genome ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_feature_by_genome_id(genome_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein feature by genome ID: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_feature_get_by_genome_name(genome_name: str, limit: int = _default_limit,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by genome name.
        
        Args:
            genome_name: The genome name to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_feature_by_genome_name(genome_name, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein feature by genome name: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_feature_get_by_feature_id(feature_id: str, limit: int = _default_limit,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by feature ID.
        
        Args:
            feature_id: The feature ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_feature_by_feature_id(feature_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein feature by feature ID: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_feature_get_by_gene(gene: str, limit: int = _default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by gene.
        
        Args:
            gene: The gene to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_feature_by_gene(gene, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein feature by gene: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_feature_get_by_taxon_id(taxon_id: int, limit: int = _default_limit,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_feature_by_taxon_id(taxon_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein feature by taxon ID: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_feature_get_by_feature_type(feature_type: str, limit: int = _default_limit,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by feature type.
        
        Args:
            feature_type: The feature type to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_feature_by_feature_type(feature_type, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein feature by feature type: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_feature_get_by_score_range(min_score: float, max_score: float, limit: int = _default_limit,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by score range.
        
        Args:
            min_score: Minimum score
            max_score: Maximum score
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_feature_by_score_range(min_score, max_score, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein feature by score range: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_feature_get_by_length_range(min_length: int, max_length: int, limit: int = _default_limit,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by length range.
        
        Args:
            min_length: Minimum length
            max_length: Maximum length
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_feature_by_length_range(min_length, max_length, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein feature by length range: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_feature_get_by_date_inserted_range(start_date: str, end_date: str, limit: int = _default_limit,
                                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_feature_by_date_inserted_range(start_date, end_date, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein feature by date inserted range: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_feature_search_by_keyword(keyword: str, limit: int = _default_limit,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search protein feature data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_feature_by_keyword(keyword, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching protein feature by keyword: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_feature_get_all(limit: int = _default_limit,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all protein feature data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_feature_all(options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all protein feature data: {str(e)}"
