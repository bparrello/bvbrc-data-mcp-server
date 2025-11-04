#!/usr/bin/env python3
"""
BV-BRC Epitope Tools

This module contains MCP tools for querying epitope data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None

from data_functions import (
    query_epitope_by_id,
    query_epitope_by_filters,
    query_epitope_by_epitope_sequence,
    query_epitope_by_epitope_type,
    query_epitope_by_host_name,
    query_epitope_by_organism,
    query_epitope_by_protein_accession,
    query_epitope_by_protein_id,
    query_epitope_by_protein_name,
    query_epitope_by_start,
    query_epitope_by_end,
    query_epitope_by_taxon_id,
    query_epitope_by_bcell_assays,
    query_epitope_by_mhc_assays,
    query_epitope_by_tcell_assays,
    query_epitope_by_total_assays,
    query_epitope_by_comment,
    query_epitope_by_assay_result,
    query_epitope_by_taxon_lineage_id,
    query_epitope_by_taxon_lineage_name,
    query_epitope_by_position_range,
    query_epitope_by_total_assays_range,
    query_epitope_by_date_inserted_range,
    query_epitope_by_date_modified_range,
    query_epitope_by_keyword,
    query_epitope_all,
    format_query_result
)

def register_epitope_tools(mcp: FastMCP, base_url: str):
    """Register all epitope-related MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    
    @mcp.tool()
    def bvbrc_epitope_get_by_id(epitope_id: str,
                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by epitope ID.
        
        Args:
            epitope_id: The epitope ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_by_id(epitope_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope by ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_query_by_filters(filters_json: str,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query epitope data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
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
            result, count = query_epitope_by_filters(filters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope by filters: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_get_by_epitope_sequence(epitope_sequence: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by epitope sequence.
        
        Args:
            epitope_sequence: The epitope sequence to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_by_epitope_sequence(epitope_sequence, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope by epitope sequence: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_get_by_epitope_type(epitope_type: str,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by epitope type.
        
        Args:
            epitope_type: The epitope type to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_by_epitope_type(epitope_type, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope by epitope type: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_get_by_host_name(host_name: str,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by host name.
        
        Args:
            host_name: The host name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_by_host_name(host_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope by host name: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_get_by_organism(organism: str,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by organism.
        
        Args:
            organism: The organism to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_by_organism(organism, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope by organism: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_get_by_protein_accession(protein_accession: str,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by protein accession.
        
        Args:
            protein_accession: The protein accession to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_by_protein_accession(protein_accession, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope by protein accession: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_get_by_protein_id(protein_id: str,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by protein ID.
        
        Args:
            protein_id: The protein ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_by_protein_id(protein_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope by protein ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_get_by_protein_name(protein_name: str,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by protein name.
        
        Args:
            protein_name: The protein name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_by_protein_name(protein_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope by protein name: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_get_by_start(start: int,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by start position.
        
        Args:
            start: The start position to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_by_start(start, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope by start position: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_get_by_end(end: int,
                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by end position.
        
        Args:
            end: The end position to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_by_end(end, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope by end position: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_get_by_taxon_id(taxon_id: int,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_by_taxon_id(taxon_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope by taxon ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_get_by_bcell_assays(bcell_assays: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by B-cell assays.
        
        Args:
            bcell_assays: The B-cell assays to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_by_bcell_assays(bcell_assays, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope by B-cell assays: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_get_by_mhc_assays(mhc_assays: str,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by MHC assays.
        
        Args:
            mhc_assays: The MHC assays to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_by_mhc_assays(mhc_assays, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope by MHC assays: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_get_by_tcell_assays(tcell_assays: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by T-cell assays.
        
        Args:
            tcell_assays: The T-cell assays to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_by_tcell_assays(tcell_assays, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope by T-cell assays: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_get_by_total_assays(total_assays: int,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by total assays.
        
        Args:
            total_assays: The total assays to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_by_total_assays(total_assays, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope by total assays: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_get_by_comment(comment: str,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by comment.
        
        Args:
            comment: The comment to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_by_comment(comment, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope by comment: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_get_by_assay_result(assay_result: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by assay result.
        
        Args:
            assay_result: The assay result to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_by_assay_result(assay_result, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope by assay result: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_get_by_taxon_lineage_id(taxon_lineage_id: str,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by taxon lineage ID.
        
        Args:
            taxon_lineage_id: The taxon lineage ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_by_taxon_lineage_id(taxon_lineage_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope by taxon lineage ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_get_by_taxon_lineage_name(taxon_lineage_name: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by taxon lineage name.
        
        Args:
            taxon_lineage_name: The taxon lineage name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_by_taxon_lineage_name(taxon_lineage_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope by taxon lineage name: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_get_by_position_range(min_start: int, max_end: int,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by position range.
        
        Args:
            min_start: Minimum start position
            max_end: Maximum end position
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_by_position_range(min_start, max_end, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope by position range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_get_by_total_assays_range(min_assays: int, max_assays: int,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by total assays range.
        
        Args:
            min_assays: Minimum total assays
            max_assays: Maximum total assays
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_by_total_assays_range(min_assays, max_assays, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope by total assays range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_get_by_date_inserted_range(start_date: str, end_date: str,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_by_date_inserted_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope by date inserted range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_get_by_date_modified_range(start_date: str, end_date: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope data by date modified range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_by_date_modified_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope by date modified range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_search_by_keyword(keyword: str,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search epitope data by keyword.
        
        Args:
            keyword: The keyword to search for
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_by_keyword(keyword, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error searching epitope by keyword: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_get_all(select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all epitope data.
        
        Args:
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_all(options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying all epitope data: {str(e)}"
            }, indent=2)