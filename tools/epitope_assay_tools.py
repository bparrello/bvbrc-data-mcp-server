#!/usr/bin/env python3
"""
BV-BRC Epitope Assay Tools

This module contains MCP tools for querying epitope assay data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None
_default_limit = None

from data_functions import (
    query_epitope_assay_by_id,
    query_epitope_assay_by_filters,
    query_epitope_assay_by_assay_group,
    query_epitope_assay_by_assay_measurement,
    query_epitope_assay_by_assay_measurement_unit,
    query_epitope_assay_by_assay_method,
    query_epitope_assay_by_assay_result,
    query_epitope_assay_by_assay_type,
    query_epitope_assay_by_authors,
    query_epitope_assay_by_epitope_id,
    query_epitope_assay_by_epitope_sequence,
    query_epitope_assay_by_epitope_type,
    query_epitope_assay_by_host_name,
    query_epitope_assay_by_host_taxon_id,
    query_epitope_assay_by_mhc_allele,
    query_epitope_assay_by_mhc_allele_class,
    query_epitope_assay_by_organism,
    query_epitope_assay_by_pdb_id,
    query_epitope_assay_by_pmid,
    query_epitope_assay_by_protein_accession,
    query_epitope_assay_by_protein_id,
    query_epitope_assay_by_protein_name,
    query_epitope_assay_by_start,
    query_epitope_assay_by_end,
    query_epitope_assay_by_taxon_id,
    query_epitope_assay_by_taxon_lineage_id,
    query_epitope_assay_by_taxon_lineage_name,
    query_epitope_assay_by_title,
    query_epitope_assay_by_position_range,
    query_epitope_assay_by_date_inserted_range,
    query_epitope_assay_by_date_modified_range,
    query_epitope_assay_by_keyword,
    query_epitope_assay_all,
    format_query_result
)


def register_epitope_assay_tools(mcp: FastMCP, base_url: str, default_limit: int):
    """Register all epitope assay-related MCP tools with the Flask app."""
    global _base_url, _default_limit
    _base_url = base_url
    _default_limit = default_limit
    

    
    @mcp.tool()
    def bvbrc_epitope_assay_get_by_id(assay_id: str, limit: int = _default_limit,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by assay ID.
        
        Args:
            assay_id: The assay ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_assay_by_id(assay_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying epitope assay by ID: {str(e)}"


    @mcp.tool()
    def bvbrc_epitope_assay_query_by_filters(filters_json: str, limit: int = _default_limit,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query epitope assay data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
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
            result = query_epitope_assay_by_filters(filters, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying epitope assay by filters: {str(e)}"


    @mcp.tool()
    def bvbrc_epitope_assay_get_by_assay_group(assay_group: str, limit: int = _default_limit,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by assay group.
        
        Args:
            assay_group: The assay group to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_assay_by_assay_group(assay_group, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying epitope assay by assay group: {str(e)}"


    @mcp.tool()
    def bvbrc_epitope_assay_get_by_assay_measurement(assay_measurement: str, limit: int = _default_limit,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by assay measurement.
        
        Args:
            assay_measurement: The assay measurement to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_assay_by_assay_measurement(assay_measurement, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying epitope assay by assay measurement: {str(e)}"


    @mcp.tool()
    def bvbrc_epitope_assay_get_by_assay_method(assay_method: str, limit: int = _default_limit,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by assay method.
        
        Args:
            assay_method: The assay method to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_assay_by_assay_method(assay_method, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying epitope assay by assay method: {str(e)}"


    @mcp.tool()
    def bvbrc_epitope_assay_get_by_assay_result(assay_result: str, limit: int = _default_limit,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by assay result.
        
        Args:
            assay_result: The assay result to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_assay_by_assay_result(assay_result, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying epitope assay by assay result: {str(e)}"


    @mcp.tool()
    def bvbrc_epitope_assay_get_by_assay_type(assay_type: str, limit: int = _default_limit,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by assay type.
        
        Args:
            assay_type: The assay type to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_assay_by_assay_type(assay_type, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying epitope assay by assay type: {str(e)}"


    @mcp.tool()
    def bvbrc_epitope_assay_get_by_epitope_id(epitope_id: str, limit: int = _default_limit,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by epitope ID.
        
        Args:
            epitope_id: The epitope ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_assay_by_epitope_id(epitope_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying epitope assay by epitope ID: {str(e)}"


    @mcp.tool()
    def bvbrc_epitope_assay_get_by_epitope_sequence(epitope_sequence: str, limit: int = _default_limit,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by epitope sequence.
        
        Args:
            epitope_sequence: The epitope sequence to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_assay_by_epitope_sequence(epitope_sequence, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying epitope assay by epitope sequence: {str(e)}"


    @mcp.tool()
    def bvbrc_epitope_assay_get_by_organism(organism: str, limit: int = _default_limit,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by organism.
        
        Args:
            organism: The organism to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_assay_by_organism(organism, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying epitope assay by organism: {str(e)}"


    @mcp.tool()
    def bvbrc_epitope_assay_get_by_pmid(pmid: str, limit: int = _default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by PMID.
        
        Args:
            pmid: The PMID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_assay_by_pmid(pmid, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying epitope assay by PMID: {str(e)}"


    @mcp.tool()
    def bvbrc_epitope_assay_get_by_protein_accession(protein_accession: str, limit: int = _default_limit,
                                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by protein accession.
        
        Args:
            protein_accession: The protein accession to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_assay_by_protein_accession(protein_accession, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying epitope assay by protein accession: {str(e)}"


    @mcp.tool()
    def bvbrc_epitope_assay_get_by_position_range(min_start: int, max_end: int, limit: int = _default_limit,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by position range.
        
        Args:
            min_start: Minimum start position
            max_end: Maximum end position
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_assay_by_position_range(min_start, max_end, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying epitope assay by position range: {str(e)}"


    @mcp.tool()
    def bvbrc_epitope_assay_get_by_date_inserted_range(start_date: str, end_date: str, limit: int = _default_limit,
                                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_assay_by_date_inserted_range(start_date, end_date, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying epitope assay by date inserted range: {str(e)}"


    @mcp.tool()
    def bvbrc_epitope_assay_search_by_keyword(keyword: str, limit: int = _default_limit,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search epitope assay data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_assay_by_keyword(keyword, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching epitope assay by keyword: {str(e)}"


    @mcp.tool()
    def bvbrc_epitope_assay_get_all(limit: int = _default_limit,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all epitope assay data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_epitope_assay_all(options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all epitope assay data: {str(e)}"
