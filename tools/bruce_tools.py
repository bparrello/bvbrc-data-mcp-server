#!/usr/bin/env python3
"""
BV-BRC Common Tools

This module contains shared MCP tools for BV-BRC data access.
"""

from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None
_default_limit = None

from data_functions import (
    query_genome_by_id,
    query_genome_by_species,
    query_genome_by_genome_name,
    query_genome_feature_by_genome_id,
    query_genome_feature_by_id,
    query_genome_feature_by_filters,
    query_genome_amr_by_filters,
    format_query_result
)


def register_bruce_tools(mcp: FastMCP, base_url: str, default_limit: int):
    """Register common MCP tools with the Flask app."""
    global _base_url, _default_limit
    _base_url = base_url
    _default_limit = default_limit
    

    
#    @mcp.tool()
#    def bvbrc_query_direct(core: str, filter_str: str = "", limit: int = _default_limit,
#                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
#        """
#        Query BV-BRC data directly using core name and filter string.
#        
#        Args:
#            core: The core/collection name (e.g., "genome", "genome_feature")
#            filter_str: RQL filter string (e.g., "eq(genome_id,123.45)")
#            limit: Maximum number of results to return (default: 1000)
#            select: Comma-separated list of fields to select (optional)
#            sort: Field to sort by (optional)
#        
#        Returns:
#            Formatted query results
#        """
#        options = {"limit": limit}
#        if select:
#            options["select"] = select.split(",")
#        if sort:
#            options["sort"] = sort
#        
#        try:
#            result = query_direct(core, filter_str, options, _base_url)
#            return format_query_result(result)
#        except Exception as e:
#            return f"Error querying {core}: {str(e)}"

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
        print(f"Get by ID: {genome_id}")
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_by_id(genome_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            message = f"Error querying genome by ID: {str(e)}"
            print(message)
            return message


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
        print(f"Get by name: {genome_name}")
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_by_genome_name(genome_name, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            message = f"Error querying genome by genome name: {str(e)}"
            print(message)
            return message


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
        print(f"Get by species: {species}")
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_by_species(species, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            message = f"Error querying genome by species: {str(e)}"
            print(message)
            return message

    
    @mcp.tool()
    def bvbrc_genome_feature_get_by_id(feature_id: str, limit: int = _default_limit,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome feature data by feature ID.
        
        Args:
            feature_id: The feature ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome feature data
        """
        print(f"Get feature by ID: {feature_id}")
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_feature_by_id(feature_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            message = f"Error querying genome feature by ID: {str(e)}"
            print(message)
            return message


    @mcp.tool()
    def bvbrc_genome_feature_get_by_genome_id(genome_id: str, limit: int = 6000,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome feature data by genome ID.
        
        Args:
            genome_id: The genome ID to query features for (e.g., "208964.12")
            limit: Maximum number of results to return (default: 6000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome feature data
        """
        print(f"Get feature by genome ID: {genome_id}")
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_genome_feature_by_genome_id(genome_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            message = f"Error querying genome features by genome ID: {str(e)}"
            print(message)
            return message


    @mcp.tool()
    def bvbrc_genome_feature_get_by_gene_in_genome(gene_name: str, genome_id: str, limit: int = _default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome feature data by gene name within a genome.
        
        Args:
            gene_name: The gene name to query (e.g., "lacZ")
            genome_id: ID of a genome that must contain the feature
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome feature data
        """
        print(f"Get feature in {genome_id} by gene name: {gene_name}")
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        filter_spec = { "gene" : gene_name, "genome_id" : genome_id }

        try:
            result = query_genome_feature_by_filters(filter_spec, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            message = f"Error querying genome features by gene: {str(e)}"
            print(message)
            return message


    @mcp.tool()
    def bvbrc_genome_feature_get_by_product_in_genome(product_name: str, genome_id: str, limit: int = _default_limit,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome feature data by product name within a specific genome.
        
        Args:
            product_name: The product name to query (e.g., "beta-galactosidase")
            limit: Maximum number of results to return (default: 1000)
            genome_id: ID of a genome that must contain the features
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome feature data
        """
        print(f"Get feature in genome {genome_id} by product: {product_name}")
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        filter_spec = { "product" : product_name, "genome_id" : genome_id }

        try:
            result = query_genome_feature_by_filters(filter_spec, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            message = f"Error querying genome features by product: {str(e)}"
            print(message)
            return message

    @mcp.tool()
    def bvbrc_genome_amr_get_by_genome_id(genome_id: str, limit: int = _default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome anti-microbial resistance data by genome ID.
        
        Args:
            genome_id: The genome ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Data for antibiotic drugs to which the genome is susceptible or resistant
        """
        print(f"Get amr data for {genome_id}")
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        filter_spec = { "genome_id" : genome_id }

        try:
            result = query_genome_amr_by_filters(filter_spec, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            message = f"Error querying genome amr data by genome ID: {str(e)}"
            print(message)
            return message


