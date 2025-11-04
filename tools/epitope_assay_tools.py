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

def register_epitope_assay_tools(mcp: FastMCP, base_url: str):
    """Register all epitope assay-related MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    
    @mcp.tool()
    def bvbrc_epitope_assay_get_by_id(assay_id: str,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by assay ID.
        
        Args:
            assay_id: The assay ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_id(assay_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_query_by_filters(filters_json: str,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query epitope assay data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
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
            result, count = query_epitope_assay_by_filters(filters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by filters: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_assay_group(assay_group: str,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by assay group.
        
        Args:
            assay_group: The assay group to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_assay_group(assay_group, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by assay group: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_assay_measurement(assay_measurement: str,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by assay measurement.
        
        Args:
            assay_measurement: The assay measurement to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_assay_measurement(assay_measurement, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by assay measurement: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_assay_measurement_unit(assay_measurement_unit: str,
                                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by assay measurement unit.
        
        Args:
            assay_measurement_unit: The assay measurement unit to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_assay_measurement_unit(assay_measurement_unit, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by assay measurement unit: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_assay_method(assay_method: str,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by assay method.
        
        Args:
            assay_method: The assay method to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_assay_method(assay_method, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by assay method: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_assay_result(assay_result: str,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by assay result.
        
        Args:
            assay_result: The assay result to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_assay_result(assay_result, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by assay result: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_assay_type(assay_type: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by assay type.
        
        Args:
            assay_type: The assay type to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_assay_type(assay_type, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by assay type: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_authors(authors: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by authors.
        
        Args:
            authors: The authors to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_authors(authors, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by authors: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_epitope_id(epitope_id: str,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by epitope ID.
        
        Args:
            epitope_id: The epitope ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_epitope_id(epitope_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by epitope ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_epitope_sequence(epitope_sequence: str,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by epitope sequence.
        
        Args:
            epitope_sequence: The epitope sequence to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_epitope_sequence(epitope_sequence, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by epitope sequence: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_epitope_type(epitope_type: str,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by epitope type.
        
        Args:
            epitope_type: The epitope type to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_epitope_type(epitope_type, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by epitope type: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_host_name(host_name: str,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by host name.
        
        Args:
            host_name: The host name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_host_name(host_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by host name: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_host_taxon_id(host_taxon_id: str,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by host taxon ID.
        
        Args:
            host_taxon_id: The host taxon ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_host_taxon_id(host_taxon_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by host taxon ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_mhc_allele(mhc_allele: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by MHC allele.
        
        Args:
            mhc_allele: The MHC allele to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_mhc_allele(mhc_allele, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by MHC allele: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_mhc_allele_class(mhc_allele_class: str,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by MHC allele class.
        
        Args:
            mhc_allele_class: The MHC allele class to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_mhc_allele_class(mhc_allele_class, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by MHC allele class: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_organism(organism: str,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by organism.
        
        Args:
            organism: The organism to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_organism(organism, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by organism: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_pdb_id(pdb_id: str,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by PDB ID.
        
        Args:
            pdb_id: The PDB ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_pdb_id(pdb_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by PDB ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_pmid(pmid: str,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by PMID.
        
        Args:
            pmid: The PMID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_pmid(pmid, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by PMID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_protein_accession(protein_accession: str,
                                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by protein accession.
        
        Args:
            protein_accession: The protein accession to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_protein_accession(protein_accession, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by protein accession: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_protein_id(protein_id: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by protein ID.
        
        Args:
            protein_id: The protein ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_protein_id(protein_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by protein ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_protein_name(protein_name: str,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by protein name.
        
        Args:
            protein_name: The protein name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_protein_name(protein_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by protein name: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_start(start: int,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by start position.
        
        Args:
            start: The start position to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_start(start, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by start position: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_end(end: int,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by end position.
        
        Args:
            end: The end position to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_end(end, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by end position: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_taxon_id(taxon_id: int,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_taxon_id(taxon_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by taxon ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_taxon_lineage_id(taxon_lineage_id: str,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by taxon lineage ID.
        
        Args:
            taxon_lineage_id: The taxon lineage ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_taxon_lineage_id(taxon_lineage_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by taxon lineage ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_taxon_lineage_name(taxon_lineage_name: str,
                                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by taxon lineage name.
        
        Args:
            taxon_lineage_name: The taxon lineage name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_taxon_lineage_name(taxon_lineage_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by taxon lineage name: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_title(title: str,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by title.
        
        Args:
            title: The title to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_title(title, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by title: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_position_range(min_start: int, max_end: int,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by position range.
        
        Args:
            min_start: Minimum start position
            max_end: Maximum end position
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_position_range(min_start, max_end, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by position range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_date_inserted_range(start_date: str, end_date: str,
                                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_date_inserted_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by date inserted range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_by_date_modified_range(start_date: str, end_date: str,
                                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get epitope assay data by date modified range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_date_modified_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying epitope assay by date modified range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_search_by_keyword(keyword: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search epitope assay data by keyword.
        
        Args:
            keyword: The keyword to search for
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_by_keyword(keyword, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error searching epitope assay by keyword: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_epitope_assay_get_all(select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all epitope assay data.
        
        Args:
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted epitope assay data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_epitope_assay_all(options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying all epitope assay data: {str(e)}"
            }, indent=2)