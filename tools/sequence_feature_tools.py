#!/usr/bin/env python3
"""
BV-BRC Sequence Feature Tools

This module contains MCP tools for querying sequence feature data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None

from data_functions import (
    query_sequence_feature_by_id,
    query_sequence_feature_by_filters,
    query_sequence_feature_by_feature_id,
    query_sequence_feature_by_genome_id,
    query_sequence_feature_by_genome_name,
    query_sequence_feature_by_gene,
    query_sequence_feature_by_product,
    query_sequence_feature_by_patric_id,
    query_sequence_feature_by_genbank_accession,
    query_sequence_feature_by_refseq_locus_tag,
    query_sequence_feature_by_sf_category,
    query_sequence_feature_by_sf_id,
    query_sequence_feature_by_sf_name,
    query_sequence_feature_by_source,
    query_sequence_feature_by_source_id,
    query_sequence_feature_by_source_strain,
    query_sequence_feature_by_segment,
    query_sequence_feature_by_subtype,
    query_sequence_feature_by_taxon_id,
    query_sequence_feature_by_evidence_code,
    query_sequence_feature_by_aa_sequence_md5,
    query_sequence_feature_by_aa_variant,
    query_sequence_feature_by_sf_sequence_md5,
    query_sequence_feature_by_source_aa_sequence,
    query_sequence_feature_by_source_sf_location,
    query_sequence_feature_by_variant_types,
    query_sequence_feature_by_start,
    query_sequence_feature_by_end,
    query_sequence_feature_by_length,
    query_sequence_feature_by_position_range,
    query_sequence_feature_by_length_range,
    query_sequence_feature_by_date_range,
    query_sequence_feature_by_modified_date_range,
    query_sequence_feature_by_keyword,
    query_sequence_feature_all,
    format_query_result
)

def register_sequence_feature_tools(mcp: FastMCP, base_url: str):
    """Register all sequence feature-related MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    
    @mcp.tool()
    def bvbrc_sequence_feature_get_by_id(id: str,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by ID.
        
        Args:
            id: The ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_id(id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_query_by_filters(filters_json: str,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query sequence feature data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
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
            result, count = query_sequence_feature_by_filters(filters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by filters: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_feature_id(feature_id: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by feature ID.
        
        Args:
            feature_id: The feature ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_feature_id(feature_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by feature ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_genome_id(genome_id: str,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by genome ID.
        
        Args:
            genome_id: The genome ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_genome_id(genome_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by genome ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_genome_name(genome_name: str,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by genome name.
        
        Args:
            genome_name: The genome name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_genome_name(genome_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by genome name: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_gene(gene: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by gene.
        
        Args:
            gene: The gene to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_gene(gene, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by gene: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_product(product: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by product.
        
        Args:
            product: The product to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_product(product, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by product: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_patric_id(patric_id: str,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by PATRIC ID.
        
        Args:
            patric_id: The PATRIC ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_patric_id(patric_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by PATRIC ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_genbank_accession(genbank_accession: str,
                                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by GenBank accession.
        
        Args:
            genbank_accession: The GenBank accession to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_genbank_accession(genbank_accession, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by GenBank accession: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_refseq_locus_tag(refseq_locus_tag: str,
                                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by RefSeq locus tag.
        
        Args:
            refseq_locus_tag: The RefSeq locus tag to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_refseq_locus_tag(refseq_locus_tag, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by RefSeq locus tag: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_sf_category(sf_category: str,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by SF category.
        
        Args:
            sf_category: The SF category to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_sf_category(sf_category, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by SF category: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_sf_id(sf_id: str,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by SF ID.
        
        Args:
            sf_id: The SF ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_sf_id(sf_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by SF ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_sf_name(sf_name: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by SF name.
        
        Args:
            sf_name: The SF name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_sf_name(sf_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by SF name: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_source(source: str,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by source.
        
        Args:
            source: The source to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_source(source, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by source: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_source_id(source_id: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by source ID.
        
        Args:
            source_id: The source ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_source_id(source_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by source ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_source_strain(source_strain: str,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by source strain.
        
        Args:
            source_strain: The source strain to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_source_strain(source_strain, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by source strain: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_segment(segment: str,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by segment.
        
        Args:
            segment: The segment to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_segment(segment, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by segment: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_subtype(subtype: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by subtype.
        
        Args:
            subtype: The subtype to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_subtype(subtype, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by subtype: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_taxon_id(taxon_id: int,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_taxon_id(taxon_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by taxon ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_evidence_code(evidence_code: str,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by evidence code.
        
        Args:
            evidence_code: The evidence code to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_evidence_code(evidence_code, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by evidence code: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_aa_sequence_md5(aa_sequence_md5: str,
                                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by amino acid sequence MD5.
        
        Args:
            aa_sequence_md5: The amino acid sequence MD5 to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_aa_sequence_md5(aa_sequence_md5, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by amino acid sequence MD5: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_aa_variant(aa_variant: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by amino acid variant.
        
        Args:
            aa_variant: The amino acid variant to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_aa_variant(aa_variant, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by amino acid variant: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_sf_sequence_md5(sf_sequence_md5: str,
                                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by SF sequence MD5.
        
        Args:
            sf_sequence_md5: The SF sequence MD5 to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_sf_sequence_md5(sf_sequence_md5, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by SF sequence MD5: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_source_aa_sequence(source_aa_sequence: str,
                                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by source amino acid sequence.
        
        Args:
            source_aa_sequence: The source amino acid sequence to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_source_aa_sequence(source_aa_sequence, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by source amino acid sequence: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_source_sf_location(source_sf_location: str,
                                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by source SF location.
        
        Args:
            source_sf_location: The source SF location to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_source_sf_location(source_sf_location, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by source SF location: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_variant_types(variant_types: str,
                                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by variant types.
        
        Args:
            variant_types: The variant types to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_variant_types(variant_types, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by variant types: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_start(start: int,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by start position.
        
        Args:
            start: The start position to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_start(start, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by start position: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_end(end: int,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by end position.
        
        Args:
            end: The end position to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_end(end, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by end position: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_length(length: int,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by length.
        
        Args:
            length: The length to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_length(length, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by length: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_position_range(start: int, end: int,
                                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by position range.
        
        Args:
            start: Start position
            end: End position
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_position_range(start, end, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by position range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_length_range(min_length: int, max_length: int,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by length range.
        
        Args:
            min_length: Minimum length
            max_length: Maximum length
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_length_range(min_length, max_length, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by length range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_date_range(start_date: str, end_date: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_date_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by date range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_by_modified_date_range(start_date: str, end_date: str,
                                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get sequence feature data by modified date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_modified_date_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying sequence feature by modified date range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_search_by_keyword(keyword: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search sequence feature data by keyword.
        
        Args:
            keyword: The keyword to search for
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_by_keyword(keyword, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error searching sequence feature by keyword: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_sequence_feature_get_all(select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all sequence feature data.
        
        Args:
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted sequence feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_sequence_feature_all(options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying all sequence feature data: {str(e)}"
            }, indent=2)