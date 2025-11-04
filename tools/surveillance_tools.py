#!/usr/bin/env python3
"""
BV-BRC Surveillance Tools

This module contains MCP tools for querying surveillance data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None

from data_functions import (
    query_surveillance_by_id,
    query_surveillance_by_filters,
    query_surveillance_by_host_species,
    query_surveillance_by_host_common_name,
    query_surveillance_by_sample_identifier,
    query_surveillance_by_sample_accession,
    query_surveillance_by_collection_country,
    query_surveillance_by_collection_city,
    query_surveillance_by_collection_year,
    query_surveillance_by_species,
    query_surveillance_by_strain,
    query_surveillance_by_subtype,
    query_surveillance_by_pathogen_type,
    query_surveillance_by_genome_id,
    query_surveillance_by_disease_status,
    query_surveillance_by_diagnosis,
    query_surveillance_by_treatment,
    query_surveillance_by_hospitalized,
    query_surveillance_by_vaccination_type,
    query_surveillance_by_exposure,
    query_surveillance_by_pathogen_test_type,
    query_surveillance_by_pathogen_test_result,
    query_surveillance_by_collection_date_range,
    query_surveillance_by_date_inserted_range,
    query_surveillance_by_date_modified_range,
    query_surveillance_by_keyword,
    query_surveillance_all,
    format_query_result
)

def register_surveillance_tools(mcp: FastMCP, base_url: str):
    """Register all surveillance-related MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    
    @mcp.tool()
    def bvbrc_surveillance_get_by_id(id: str,
                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get surveillance data by ID.
        
        Args:
            id: The ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted surveillance data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_surveillance_by_id(id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying surveillance by ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_surveillance_query_by_filters(filters_json: str,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query surveillance data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted surveillance data
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
            result, count = query_surveillance_by_filters(filters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying surveillance by filters: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_surveillance_get_by_host_species(host_species: str,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get surveillance data by host species.
        
        Args:
            host_species: The host species to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted surveillance data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_surveillance_by_host_species(host_species, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying surveillance by host species: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_surveillance_get_by_collection_country(collection_country: str,
                                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get surveillance data by collection country.
        
        Args:
            collection_country: The collection country to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted surveillance data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_surveillance_by_collection_country(collection_country, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying surveillance by collection country: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_surveillance_get_by_species(species: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get surveillance data by species.
        
        Args:
            species: The species to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted surveillance data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_surveillance_by_species(species, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying surveillance by species: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_surveillance_get_by_strain(strain: str,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get surveillance data by strain.
        
        Args:
            strain: The strain to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted surveillance data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_surveillance_by_strain(strain, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying surveillance by strain: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_surveillance_get_by_disease_status(disease_status: str,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get surveillance data by disease status.
        
        Args:
            disease_status: The disease status to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted surveillance data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_surveillance_by_disease_status(disease_status, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying surveillance by disease status: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_surveillance_get_by_collection_date_range(start_date: str, end_date: str,
                                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get surveillance data by collection date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted surveillance data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_surveillance_by_collection_date_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying surveillance by collection date range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_surveillance_search_by_keyword(keyword: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search surveillance data by keyword.
        
        Args:
            keyword: The keyword to search for
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted surveillance data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_surveillance_by_keyword(keyword, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error searching surveillance by keyword: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_surveillance_get_all(select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all surveillance data.
        
        Args:
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted surveillance data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_surveillance_all(options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying all surveillance data: {str(e)}"
            }, indent=2)