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

from data_functions import (
    query_genome_by_id,
    query_genome_by_taxon_id,
    query_genome_by_genome_name,
    query_genome_by_species,
    query_genome_by_genus,
    query_genome_by_filters,
    format_query_result
)

def register_genome_tools(mcp: FastMCP, base_url: str):
    """Register all genome-related MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    
    @mcp.tool()
    def bvbrc_genome_get_by_id(genome_id: str, 
                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome data by genome ID.
        
        Args:
            genome_id: The genome ID to query (e.g., "208964.12")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_by_id(genome_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome by ID: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_genome_get_by_taxon_id(taxon_id: int,
                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query (e.g., 562)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_by_taxon_id(taxon_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome by taxon ID: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_genome_get_by_genome_name(genome_name: str,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome data by genome name.
        
        Args:
            genome_name: The genome name to query (e.g., "Escherichia coli")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_by_genome_name(genome_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome by genome name: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_genome_get_by_species(species: str,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome data by species.
        
        Args:
            species: The species name to query (e.g., "coli")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_by_species(species, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome by species: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_genome_get_by_genus(genus: str,
                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome data by genus.
        
        Args:
            genus: The genus name to query (e.g., "Escherichia")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_by_genus(genus, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome by genus: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_genome_query_by_filters(filters_json: str,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query genome data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria (e.g., '{"genus": "Escherichia", "species": "coli"}')
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome data
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
            result, count = query_genome_by_filters(filters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome by filters: {str(e)}"
            }, indent=2)


