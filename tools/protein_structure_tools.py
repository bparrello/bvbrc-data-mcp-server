#!/usr/bin/env python3
"""
BV-BRC Protein Structure Tools

This module contains MCP tools for querying protein structure data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None
_default_limit = None

from data_functions import (
    query_protein_structure_by_id,
    query_protein_structure_by_filters,
    query_protein_structure_by_feature_id,
    query_protein_structure_by_genome_id,
    query_protein_structure_by_patric_id,
    query_protein_structure_by_organism_name,
    query_protein_structure_by_title,
    query_protein_structure_by_resolution,
    query_protein_structure_by_institution,
    query_protein_structure_by_file_path,
    query_protein_structure_by_author,
    query_protein_structure_by_method,
    query_protein_structure_by_gene,
    query_protein_structure_by_product,
    query_protein_structure_by_sequence,
    query_protein_structure_by_sequence_md5,
    query_protein_structure_by_uniprotkb_accession,
    query_protein_structure_by_pmid,
    query_protein_structure_by_taxon_id,
    query_protein_structure_by_taxon_lineage_id,
    query_protein_structure_by_taxon_lineage_name,
    query_protein_structure_by_alignment,
    query_protein_structure_by_release_date_range,
    query_protein_structure_by_date_inserted_range,
    query_protein_structure_by_date_modified_range,
    query_protein_structure_by_keyword,
    query_protein_structure_all,
    format_query_result
)


def register_protein_structure_tools(mcp: FastMCP, base_url: str, default_limit: int):
    """Register all protein structure-related MCP tools with the Flask app."""
    global _base_url, _default_limit
    _base_url = base_url
    _default_limit = default_limit
    

    
    @mcp.tool()
    def bvbrc_protein_structure_get_by_id(pdb_id: str, limit: int = _default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by PDB ID.
        
        Args:
            pdb_id: The PDB ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_structure_by_id(pdb_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein structure by PDB ID: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_structure_query_by_filters(filters_json: str, limit: int = _default_limit,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query protein structure data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
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
            result = query_protein_structure_by_filters(filters, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein structure by filters: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_structure_get_by_feature_id(feature_id: str, limit: int = _default_limit,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by feature ID.
        
        Args:
            feature_id: The feature ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_structure_by_feature_id(feature_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein structure by feature ID: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_structure_get_by_genome_id(genome_id: str, limit: int = _default_limit,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by genome ID.
        
        Args:
            genome_id: The genome ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_structure_by_genome_id(genome_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein structure by genome ID: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_structure_get_by_organism_name(organism_name: str, limit: int = _default_limit,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by organism name.
        
        Args:
            organism_name: The organism name to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_structure_by_organism_name(organism_name, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein structure by organism name: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_structure_get_by_title(title: str, limit: int = _default_limit,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by title.
        
        Args:
            title: The title to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_structure_by_title(title, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein structure by title: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_structure_get_by_resolution(resolution: str, limit: int = _default_limit,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by resolution.
        
        Args:
            resolution: The resolution to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_structure_by_resolution(resolution, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein structure by resolution: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_structure_get_by_taxon_id(taxon_id: int, limit: int = _default_limit,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_structure_by_taxon_id(taxon_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein structure by taxon ID: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_structure_get_by_pmid(pmid: str, limit: int = _default_limit,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by PMID.
        
        Args:
            pmid: The PMID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_structure_by_pmid(pmid, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein structure by PMID: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_structure_get_by_release_date_range(start_date: str, end_date: str, limit: int = _default_limit,
                                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by release date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_structure_by_release_date_range(start_date, end_date, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying protein structure by release date range: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_structure_search_by_keyword(keyword: str, limit: int = _default_limit,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search protein structure data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_structure_by_keyword(keyword, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching protein structure by keyword: {str(e)}"


    @mcp.tool()
    def bvbrc_protein_structure_get_all(limit: int = _default_limit,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all protein structure data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_protein_structure_all(options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all protein structure data: {str(e)}"
