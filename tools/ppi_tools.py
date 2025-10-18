#!/usr/bin/env python3
"""
BV-BRC Protein-Protein Interaction Tools

This module contains MCP tools for querying protein-protein interaction data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None
_default_limit = None

from data_functions import (
    query_ppi_by_id,
    query_ppi_by_filters,
    query_ppi_by_category,
    query_ppi_by_detection_method,
    query_ppi_by_domain_a,
    query_ppi_by_domain_b,
    query_ppi_by_evidence,
    query_ppi_by_feature_id_a,
    query_ppi_by_feature_id_b,
    query_ppi_by_gene_a,
    query_ppi_by_gene_b,
    query_ppi_by_genome_id_a,
    query_ppi_by_genome_id_b,
    query_ppi_by_genome_name_a,
    query_ppi_by_genome_name_b,
    query_ppi_by_interaction_type,
    query_ppi_by_interactor_a,
    query_ppi_by_interactor_b,
    query_ppi_by_pmid,
    query_ppi_by_source_db,
    query_ppi_by_source_id,
    query_ppi_by_taxon_id_a,
    query_ppi_by_taxon_id_b,
    query_ppi_by_date_inserted_range,
    query_ppi_by_date_modified_range,
    query_ppi_by_keyword,
    query_ppi_all,
    format_query_result
)


def register_ppi_tools(mcp: FastMCP, base_url: str, default_limit: int):
    """Register all protein-protein interaction-related MCP tools with the Flask app."""
    global _base_url, _default_limit
    _base_url = base_url
    _default_limit = default_limit
    

    
    @mcp.tool()
    def bvbrc_ppi_get_by_id(id: str, limit: int = _default_limit,
                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by ID.
        
        Args:
            id: The ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_ppi_by_id(id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein-protein interaction by ID: {str(e)}"


    @mcp.tool()
    def bvbrc_ppi_query_by_filters(filters_json: str, limit: int = _default_limit,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query protein-protein interaction data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
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
            result = query_ppi_by_filters(filters, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein-protein interaction by filters: {str(e)}"


    @mcp.tool()
    def bvbrc_ppi_get_by_interactor_a(interactor_a: str, limit: int = _default_limit,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by interactor A.
        
        Args:
            interactor_a: The interactor A to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_ppi_by_interactor_a(interactor_a, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein-protein interaction by interactor A: {str(e)}"


    @mcp.tool()
    def bvbrc_ppi_get_by_interactor_b(interactor_b: str, limit: int = _default_limit,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by interactor B.
        
        Args:
            interactor_b: The interactor B to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_ppi_by_interactor_b(interactor_b, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein-protein interaction by interactor B: {str(e)}"


    @mcp.tool()
    def bvbrc_ppi_get_by_genome_id_a(genome_id_a: str, limit: int = _default_limit,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by genome ID A.
        
        Args:
            genome_id_a: The genome ID A to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_ppi_by_genome_id_a(genome_id_a, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein-protein interaction by genome ID A: {str(e)}"


    @mcp.tool()
    def bvbrc_ppi_get_by_genome_id_b(genome_id_b: str, limit: int = _default_limit,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by genome ID B.
        
        Args:
            genome_id_b: The genome ID B to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_ppi_by_genome_id_b(genome_id_b, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein-protein interaction by genome ID B: {str(e)}"


    @mcp.tool()
    def bvbrc_ppi_get_by_interaction_type(interaction_type: str, limit: int = _default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by interaction type.
        
        Args:
            interaction_type: The interaction type to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_ppi_by_interaction_type(interaction_type, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein-protein interaction by interaction type: {str(e)}"


    @mcp.tool()
    def bvbrc_ppi_get_by_pmid(pmid: str, limit: int = _default_limit,
                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by PMID.
        
        Args:
            pmid: The PMID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_ppi_by_pmid(pmid, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein-protein interaction by PMID: {str(e)}"


    @mcp.tool()
    def bvbrc_ppi_get_by_source_db(source_db: str, limit: int = _default_limit,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by source database.
        
        Args:
            source_db: The source database to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_ppi_by_source_db(source_db, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein-protein interaction by source database: {str(e)}"


    @mcp.tool()
    def bvbrc_ppi_get_by_taxon_id_a(taxon_id_a: int, limit: int = _default_limit,
                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by taxon ID A.
        
        Args:
            taxon_id_a: The taxon ID A to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_ppi_by_taxon_id_a(taxon_id_a, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein-protein interaction by taxon ID A: {str(e)}"


    @mcp.tool()
    def bvbrc_ppi_get_by_taxon_id_b(taxon_id_b: int, limit: int = _default_limit,
                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by taxon ID B.
        
        Args:
            taxon_id_b: The taxon ID B to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_ppi_by_taxon_id_b(taxon_id_b, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein-protein interaction by taxon ID B: {str(e)}"


    @mcp.tool()
    def bvbrc_ppi_get_by_date_inserted_range(start_date: str, end_date: str, limit: int = _default_limit,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_ppi_by_date_inserted_range(start_date, end_date, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein-protein interaction by date inserted range: {str(e)}"


    @mcp.tool()
    def bvbrc_ppi_search_by_keyword(keyword: str, limit: int = _default_limit,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search protein-protein interaction data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_ppi_by_keyword(keyword, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching protein-protein interaction by keyword: {str(e)}"


    @mcp.tool()
    def bvbrc_ppi_get_all(limit: int = _default_limit,
                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all protein-protein interaction data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_ppi_all(options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all protein-protein interaction data: {str(e)}"
