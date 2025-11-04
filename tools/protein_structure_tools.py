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

def register_protein_structure_tools(mcp: FastMCP, base_url: str):
    """Register all protein structure-related MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    
    @mcp.tool()
    def bvbrc_protein_structure_get_by_id(pdb_id: str,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by PDB ID.
        
        Args:
            pdb_id: The PDB ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_structure_by_id(pdb_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein structure by PDB ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_structure_query_by_filters(filters_json: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query protein structure data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
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
            result, count = query_protein_structure_by_filters(filters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein structure by filters: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_structure_get_by_feature_id(feature_id: str,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by feature ID.
        
        Args:
            feature_id: The feature ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_structure_by_feature_id(feature_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein structure by feature ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_structure_get_by_genome_id(genome_id: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by genome ID.
        
        Args:
            genome_id: The genome ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_structure_by_genome_id(genome_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein structure by genome ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_structure_get_by_patric_id(patric_id: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by PATRIC ID.
        
        Args:
            patric_id: The PATRIC ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_structure_by_patric_id(patric_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein structure by PATRIC ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_structure_get_by_organism_name(organism_name: str,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by organism name.
        
        Args:
            organism_name: The organism name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_structure_by_organism_name(organism_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein structure by organism name: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_structure_get_by_title(title: str,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by title.
        
        Args:
            title: The title to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_structure_by_title(title, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein structure by title: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_structure_get_by_resolution(resolution: str,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by resolution.
        
        Args:
            resolution: The resolution to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_structure_by_resolution(resolution, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein structure by resolution: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_structure_get_by_institution(institution: str,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by institution.
        
        Args:
            institution: The institution to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_structure_by_institution(institution, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein structure by institution: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_structure_get_by_file_path(file_path: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by file path.
        
        Args:
            file_path: The file path to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_structure_by_file_path(file_path, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein structure by file path: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_structure_get_by_author(author: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by author.
        
        Args:
            author: The author to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_structure_by_author(author, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein structure by author: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_structure_get_by_method(method: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by method.
        
        Args:
            method: The method to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_structure_by_method(method, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein structure by method: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_structure_get_by_gene(gene: str,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by gene.
        
        Args:
            gene: The gene to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_structure_by_gene(gene, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein structure by gene: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_structure_get_by_product(product: str,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by product.
        
        Args:
            product: The product to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_structure_by_product(product, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein structure by product: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_structure_get_by_sequence(sequence: str,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by sequence.
        
        Args:
            sequence: The sequence to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_structure_by_sequence(sequence, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein structure by sequence: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_structure_get_by_sequence_md5(sequence_md5: str,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by sequence MD5.
        
        Args:
            sequence_md5: The sequence MD5 to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_structure_by_sequence_md5(sequence_md5, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein structure by sequence MD5: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_structure_get_by_uniprotkb_accession(uniprotkb_accession: str,
                                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by UniProtKB accession.
        
        Args:
            uniprotkb_accession: The UniProtKB accession to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_structure_by_uniprotkb_accession(uniprotkb_accession, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein structure by UniProtKB accession: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_structure_get_by_pmid(pmid: str,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by PMID.
        
        Args:
            pmid: The PMID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_structure_by_pmid(pmid, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein structure by PMID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_structure_get_by_taxon_id(taxon_id: int,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_structure_by_taxon_id(taxon_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein structure by taxon ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_structure_get_by_taxon_lineage_id(taxon_lineage_id: str,
                                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by taxon lineage ID.
        
        Args:
            taxon_lineage_id: The taxon lineage ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_structure_by_taxon_lineage_id(taxon_lineage_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein structure by taxon lineage ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_structure_get_by_taxon_lineage_name(taxon_lineage_name: str,
                                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by taxon lineage name.
        
        Args:
            taxon_lineage_name: The taxon lineage name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_structure_by_taxon_lineage_name(taxon_lineage_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein structure by taxon lineage name: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_structure_get_by_alignment(alignment: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by alignment.
        
        Args:
            alignment: The alignment to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_structure_by_alignment(alignment, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein structure by alignment: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_structure_get_by_release_date_range(start_date: str, end_date: str,
                                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by release date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_structure_by_release_date_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein structure by release date range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_structure_get_by_date_inserted_range(start_date: str, end_date: str,
                                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_structure_by_date_inserted_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein structure by date inserted range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_structure_get_by_date_modified_range(start_date: str, end_date: str,
                                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein structure data by date modified range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_structure_by_date_modified_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein structure by date modified range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_structure_search_by_keyword(keyword: str,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search protein structure data by keyword.
        
        Args:
            keyword: The keyword to search for
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_structure_by_keyword(keyword, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error searching protein structure by keyword: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_structure_get_all(select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all protein structure data.
        
        Args:
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein structure data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_structure_all(options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying all protein structure data: {str(e)}"
            }, indent=2)