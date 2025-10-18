#!/usr/bin/env python3
"""
BV-BRC Genome Tools

This module contains MCP tools for querying genome data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None
_default_limit = None

from data_functions import (
    query_genome_by_id,
    query_genome_by_taxon_id,
    query_genome_by_genome_name,
    query_genome_by_species,
    query_genome_by_genus,
    query_genome_by_filters,
    format_query_result
)


def register_genome_tools(mcp: FastMCP, base_url: str, default_limit: int):
    """Register all genome-related MCP tools with the Flask app."""
    global _base_url, _default_limit
    _base_url = base_url
    _default_limit = default_limit
    

    
    @mcp.tool()
    def bvbrc_genome_get_by_id(genome_id: str, limit: int = _default_limit, 
                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome data by genome ID.
        
        Args:
            genome_id: The genome ID to query (e.g., "208964.12")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_by_id(genome_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome by ID: {str(e)}"


    @mcp.tool()
    def bvbrc_genome_get_by_taxon_id(taxon_id: int, limit: int = _default_limit,
                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query (e.g., 562)
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_by_taxon_id(taxon_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome by taxon ID: {str(e)}"


    @mcp.tool()
    def bvbrc_genome_get_by_genome_name(genome_name: str, limit: int = _default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome data by genome name.
        
        Args:
            genome_name: The genome name to query (e.g., "Escherichia coli")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_by_genome_name(genome_name, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome by genome name: {str(e)}"


    @mcp.tool()
    def bvbrc_genome_get_by_species(species: str, limit: int = _default_limit,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome data by species.
        
        Args:
            species: The species name to query (e.g., "coli")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_by_species(species, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome by species: {str(e)}"


    @mcp.tool()
    def bvbrc_genome_get_by_genus(genus: str, limit: int = _default_limit,
                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome data by genus.
        
        Args:
            genus: The genus name to query (e.g., "Escherichia")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_by_genus(genus, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome by genus: {str(e)}"


    @mcp.tool()
    def bvbrc_genome_query_by_filters(filters_json: str, limit: int = _default_limit,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query genome data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria (e.g., '{"genus": "Escherichia", "species": "coli"}')
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome data
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
            result = query_genome_by_filters(filters, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying genome by filters: {str(e)}"
