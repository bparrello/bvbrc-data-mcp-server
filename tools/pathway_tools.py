#!/usr/bin/env python3
"""
BV-BRC Pathway Tools

This module contains MCP tools for querying pathway data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None

from data_functions import (
    query_pathway_by_id,
    query_pathway_by_filters,
    query_pathway_by_accession,
    query_pathway_by_alt_locus_tag,
    query_pathway_by_annotation,
    query_pathway_by_ec_description,
    query_pathway_by_ec_number,
    query_pathway_by_feature_id,
    query_pathway_by_gene,
    query_pathway_by_genome_ec,
    query_pathway_by_genome_id,
    query_pathway_by_genome_name,
    query_pathway_by_owner,
    query_pathway_by_pathway_class,
    query_pathway_by_pathway_ec,
    query_pathway_by_pathway_id,
    query_pathway_by_pathway_name,
    query_pathway_by_patric_id,
    query_pathway_by_product,
    query_pathway_by_public_status,
    query_pathway_by_refseq_locus_tag,
    query_pathway_by_sequence_id,
    query_pathway_by_taxon_id,
    query_pathway_by_user_read,
    query_pathway_by_user_write,
    query_pathway_by_version,
    query_pathway_by_date_inserted_range,
    query_pathway_by_date_modified_range,
    query_pathway_by_keyword,
    query_pathway_all,
    format_query_result
)

def register_pathway_tools(mcp: FastMCP, base_url: str):
    """Register all pathway-related MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    
    @mcp.tool()
    def bvbrc_pathway_get_by_id(id: str,
                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by ID.
        
        Args:
            id: The ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_id(id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_query_by_filters(filters_json: str,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query pathway data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
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
            result, count = query_pathway_by_filters(filters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by filters: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_by_accession(accession: str,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by accession.
        
        Args:
            accession: The accession to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_accession(accession, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by accession: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_by_alt_locus_tag(alt_locus_tag: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by alternative locus tag.
        
        Args:
            alt_locus_tag: The alternative locus tag to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_alt_locus_tag(alt_locus_tag, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by alternative locus tag: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_by_annotation(annotation: str,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by annotation.
        
        Args:
            annotation: The annotation to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_annotation(annotation, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by annotation: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_by_ec_description(ec_description: str,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by EC description.
        
        Args:
            ec_description: The EC description to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_ec_description(ec_description, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by EC description: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_by_ec_number(ec_number: str,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by EC number.
        
        Args:
            ec_number: The EC number to query (e.g., "1.1.1.1")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_ec_number(ec_number, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by EC number: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_by_feature_id(feature_id: str,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by feature ID.
        
        Args:
            feature_id: The feature ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_feature_id(feature_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by feature ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_by_gene(gene: str,
                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by gene.
        
        Args:
            gene: The gene to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_gene(gene, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by gene: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_by_genome_ec(genome_ec: str,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by genome EC.
        
        Args:
            genome_ec: The genome EC to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_genome_ec(genome_ec, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by genome EC: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_by_genome_id(genome_id: str,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by genome ID.
        
        Args:
            genome_id: The genome ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_genome_id(genome_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by genome ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_by_genome_name(genome_name: str,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by genome name.
        
        Args:
            genome_name: The genome name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_genome_name(genome_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by genome name: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_by_owner(owner: str,
                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by owner.
        
        Args:
            owner: The owner to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_owner(owner, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by owner: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_by_pathway_class(pathway_class: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by pathway class.
        
        Args:
            pathway_class: The pathway class to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_pathway_class(pathway_class, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by pathway class: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_by_pathway_ec(pathway_ec: str,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by pathway EC.
        
        Args:
            pathway_ec: The pathway EC to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_pathway_ec(pathway_ec, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by pathway EC: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_by_pathway_id(pathway_id: str,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by pathway ID.
        
        Args:
            pathway_id: The pathway ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_pathway_id(pathway_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by pathway ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_by_pathway_name(pathway_name: str,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by pathway name.
        
        Args:
            pathway_name: The pathway name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_pathway_name(pathway_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by pathway name: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_by_patric_id(patric_id: str,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by PATRIC ID.
        
        Args:
            patric_id: The PATRIC ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_patric_id(patric_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by PATRIC ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_by_product(product: str,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by product.
        
        Args:
            product: The product to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_product(product, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by product: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_by_public_status(is_public: bool,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by public status.
        
        Args:
            is_public: The public status to query (True/False)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_public_status(is_public, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by public status: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_by_refseq_locus_tag(refseq_locus_tag: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by RefSeq locus tag.
        
        Args:
            refseq_locus_tag: The RefSeq locus tag to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_refseq_locus_tag(refseq_locus_tag, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by RefSeq locus tag: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_by_sequence_id(sequence_id: str,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by sequence ID.
        
        Args:
            sequence_id: The sequence ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_sequence_id(sequence_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by sequence ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_by_taxon_id(taxon_id: int,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_taxon_id(taxon_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by taxon ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_by_user_read(user_read: str,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by user read.
        
        Args:
            user_read: The user read to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_user_read(user_read, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by user read: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_by_user_write(user_write: str,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by user write.
        
        Args:
            user_write: The user write to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_user_write(user_write, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by user write: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_by_version(version: int,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by version.
        
        Args:
            version: The version to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_version(version, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by version: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_by_date_inserted_range(start_date: str, end_date: str,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_date_inserted_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by date inserted range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_by_date_modified_range(start_date: str, end_date: str,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get pathway data by date modified range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_date_modified_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying pathway by date modified range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_search_by_keyword(keyword: str,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search pathway data by keyword.
        
        Args:
            keyword: The keyword to search for
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_by_keyword(keyword, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error searching pathway by keyword: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_pathway_get_all(select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all pathway data.
        
        Args:
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted pathway data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_pathway_all(options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying all pathway data: {str(e)}"
            }, indent=2)