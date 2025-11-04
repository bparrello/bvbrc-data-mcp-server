#!/usr/bin/env python3
"""
BV-BRC Gene Ontology Reference Tools

This module contains MCP tools for querying gene ontology reference data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None

from data_functions import (
    query_gene_ontology_ref_by_id,
    query_gene_ontology_ref_by_filters,
    query_gene_ontology_ref_by_go_name,
    query_gene_ontology_ref_by_definition,
    query_gene_ontology_ref_by_ontology,
    query_gene_ontology_ref_by_date_inserted_range,
    query_gene_ontology_ref_by_date_modified_range,
    query_gene_ontology_ref_by_keyword,
    query_gene_ontology_ref_all,
    format_query_result
)

def register_gene_ontology_ref_tools(mcp: FastMCP, base_url: str):
    """Register all gene ontology reference-related MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    
    @mcp.tool()
    def bvbrc_gene_ontology_ref_get_by_id(go_id: str,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get gene ontology reference data by GO ID.
        
        Args:
            go_id: The GO ID to query (e.g., "GO:0008150")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted gene ontology reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_gene_ontology_ref_by_id(go_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying gene ontology reference by GO ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_gene_ontology_ref_query_by_filters(filters_json: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query gene ontology reference data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted gene ontology reference data
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
            result, count = query_gene_ontology_ref_by_filters(filters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying gene ontology reference by filters: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_gene_ontology_ref_get_by_go_name(go_name: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get gene ontology reference data by GO name.
        
        Args:
            go_name: The GO name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted gene ontology reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_gene_ontology_ref_by_go_name(go_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying gene ontology reference by GO name: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_gene_ontology_ref_get_by_definition(definition: str,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get gene ontology reference data by definition.
        
        Args:
            definition: The definition to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted gene ontology reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_gene_ontology_ref_by_definition(definition, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying gene ontology reference by definition: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_gene_ontology_ref_get_by_ontology(ontology: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get gene ontology reference data by ontology.
        
        Args:
            ontology: The ontology to query (e.g., "biological_process", "molecular_function", "cellular_component")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted gene ontology reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_gene_ontology_ref_by_ontology(ontology, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying gene ontology reference by ontology: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_gene_ontology_ref_get_by_date_inserted_range(start_date: str, end_date: str,
                                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get gene ontology reference data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted gene ontology reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_gene_ontology_ref_by_date_inserted_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying gene ontology reference by date inserted range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_gene_ontology_ref_get_by_date_modified_range(start_date: str, end_date: str,
                                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get gene ontology reference data by date modified range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted gene ontology reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_gene_ontology_ref_by_date_modified_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying gene ontology reference by date modified range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_gene_ontology_ref_search_by_keyword(keyword: str,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search gene ontology reference data by keyword.
        
        Args:
            keyword: The keyword to search for
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted gene ontology reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_gene_ontology_ref_by_keyword(keyword, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error searching gene ontology reference by keyword: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_gene_ontology_ref_get_all(select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all gene ontology reference data.
        
        Args:
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted gene ontology reference data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_gene_ontology_ref_all(options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying all gene ontology reference data: {str(e)}"
            }, indent=2)