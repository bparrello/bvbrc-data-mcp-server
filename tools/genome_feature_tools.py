#!/usr/bin/env python3
"""
BV-BRC Genome Feature Tools

This module contains MCP tools for querying genome feature data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None

from data_functions import (
    query_genome_feature_by_id,
    query_genome_feature_by_genome_id,
    query_genome_feature_by_gene,
    query_genome_feature_by_product,
    query_genome_feature_by_filters,
    format_query_result
)

def register_genome_feature_tools(mcp: FastMCP, base_url: str):
    """Register all genome feature-related MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    
    @mcp.tool()
    def bvbrc_genome_feature_get_by_id(feature_id: str,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome feature data by feature ID.
        
        Args:
            feature_id: The feature ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_feature_by_id(feature_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome feature by ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_feature_get_by_genome_id(genome_id: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome feature data by genome ID.
        
        Args:
            genome_id: The genome ID to query features for (e.g., "208964.12")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_feature_by_genome_id(genome_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome features by genome ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_feature_get_by_gene(gene_name: str,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome feature data by gene name.
        
        Args:
            gene_name: The gene name to query (e.g., "lacZ")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_feature_by_gene(gene_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome features by gene: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_feature_get_by_product(product_name: str,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome feature data by product name.
        
        Args:
            product_name: The product name to query (e.g., "beta-galactosidase")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_feature_by_product(product_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome features by product: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_feature_query_by_filters(filters_json: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query genome feature data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria (e.g., '{"genome_id": "208964.12", "feature_type": "CDS"}')
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome feature data
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
            result, count = query_genome_feature_by_filters(filters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome features by filters: {str(e)}"
            }, indent=2)