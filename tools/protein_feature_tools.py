#!/usr/bin/env python3
"""
BV-BRC Protein Feature Tools

This module contains MCP tools for querying protein feature data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None

from data_functions import (
    query_protein_feature_by_id,
    query_protein_feature_by_filters,
    query_protein_feature_by_aa_sequence_md5,
    query_protein_feature_by_classification,
    query_protein_feature_by_comment,
    query_protein_feature_by_description,
    query_protein_feature_by_e_value,
    query_protein_feature_by_end,
    query_protein_feature_by_evidence,
    query_protein_feature_by_feature_id,
    query_protein_feature_by_feature_type,
    query_protein_feature_by_gene,
    query_protein_feature_by_genome_id,
    query_protein_feature_by_genome_name,
    query_protein_feature_by_interpro_description,
    query_protein_feature_by_interpro_id,
    query_protein_feature_by_length,
    query_protein_feature_by_patric_id,
    query_protein_feature_by_product,
    query_protein_feature_by_publication,
    query_protein_feature_by_refseq_locus_tag,
    query_protein_feature_by_score,
    query_protein_feature_by_segment,
    query_protein_feature_by_sequence,
    query_protein_feature_by_source,
    query_protein_feature_by_source_id,
    query_protein_feature_by_start,
    query_protein_feature_by_taxon_id,
    query_protein_feature_by_score_range,
    query_protein_feature_by_length_range,
    query_protein_feature_by_position_range,
    query_protein_feature_by_date_inserted_range,
    query_protein_feature_by_date_modified_range,
    query_protein_feature_by_keyword,
    query_protein_feature_all,
    format_query_result
)

def register_protein_feature_tools(mcp: FastMCP, base_url: str):
    """Register all protein feature-related MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    
    @mcp.tool()
    def bvbrc_protein_feature_get_by_id(id: str,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by ID.
        
        Args:
            id: The ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_id(id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_query_by_filters(filters_json: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query protein feature data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
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
            result, count = query_protein_feature_by_filters(filters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by filters: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_aa_sequence_md5(aa_sequence_md5: str,
                                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by amino acid sequence MD5.
        
        Args:
            aa_sequence_md5: The amino acid sequence MD5 to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_aa_sequence_md5(aa_sequence_md5, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by amino acid sequence MD5: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_classification(classification: str,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by classification.
        
        Args:
            classification: The classification to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_classification(classification, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by classification: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_comment(comment: str,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by comment.
        
        Args:
            comment: The comment to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_comment(comment, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by comment: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_description(description: str,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by description.
        
        Args:
            description: The description to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_description(description, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by description: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_e_value(e_value: str,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by E-value.
        
        Args:
            e_value: The E-value to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_e_value(e_value, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by E-value: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_end(end: int,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by end position.
        
        Args:
            end: The end position to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_end(end, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by end position: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_evidence(evidence: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by evidence.
        
        Args:
            evidence: The evidence to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_evidence(evidence, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by evidence: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_feature_id(feature_id: str,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by feature ID.
        
        Args:
            feature_id: The feature ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_feature_id(feature_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by feature ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_feature_type(feature_type: str,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by feature type.
        
        Args:
            feature_type: The feature type to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_feature_type(feature_type, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by feature type: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_gene(gene: str,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by gene.
        
        Args:
            gene: The gene to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_gene(gene, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by gene: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_genome_id(genome_id: str,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by genome ID.
        
        Args:
            genome_id: The genome ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_genome_id(genome_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by genome ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_genome_name(genome_name: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by genome name.
        
        Args:
            genome_name: The genome name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_genome_name(genome_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by genome name: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_interpro_description(interpro_description: str,
                                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by InterPro description.
        
        Args:
            interpro_description: The InterPro description to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_interpro_description(interpro_description, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by InterPro description: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_interpro_id(interpro_id: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by InterPro ID.
        
        Args:
            interpro_id: The InterPro ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_interpro_id(interpro_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by InterPro ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_length(length: int,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by length.
        
        Args:
            length: The length to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_length(length, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by length: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_patric_id(patric_id: str,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by PATRIC ID.
        
        Args:
            patric_id: The PATRIC ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_patric_id(patric_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by PATRIC ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_product(product: str,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by product.
        
        Args:
            product: The product to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_product(product, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by product: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_publication(publication: str,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by publication.
        
        Args:
            publication: The publication to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_publication(publication, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by publication: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_refseq_locus_tag(refseq_locus_tag: str,
                                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by RefSeq locus tag.
        
        Args:
            refseq_locus_tag: The RefSeq locus tag to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_refseq_locus_tag(refseq_locus_tag, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by RefSeq locus tag: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_score(score: float,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by score.
        
        Args:
            score: The score to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_score(score, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by score: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_segment(segment: str,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by segment.
        
        Args:
            segment: The segment to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_segment(segment, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by segment: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_sequence(sequence: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by sequence.
        
        Args:
            sequence: The sequence to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_sequence(sequence, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by sequence: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_source(source: str,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by source.
        
        Args:
            source: The source to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_source(source, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by source: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_source_id(source_id: str,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by source ID.
        
        Args:
            source_id: The source ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_source_id(source_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by source ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_start(start: int,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by start position.
        
        Args:
            start: The start position to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_start(start, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by start position: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_taxon_id(taxon_id: int,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_taxon_id(taxon_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by taxon ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_score_range(min_score: float, max_score: float,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by score range.
        
        Args:
            min_score: Minimum score
            max_score: Maximum score
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_score_range(min_score, max_score, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by score range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_length_range(min_length: int, max_length: int,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by length range.
        
        Args:
            min_length: Minimum length
            max_length: Maximum length
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_length_range(min_length, max_length, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by length range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_position_range(min_start: int, max_end: int,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by position range.
        
        Args:
            min_start: Minimum start position
            max_end: Maximum end position
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_position_range(min_start, max_end, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by position range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_date_inserted_range(start_date: str, end_date: str,
                                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_date_inserted_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by date inserted range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_by_date_modified_range(start_date: str, end_date: str,
                                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein feature data by date modified range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_date_modified_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein feature by date modified range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_search_by_keyword(keyword: str,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search protein feature data by keyword.
        
        Args:
            keyword: The keyword to search for
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_by_keyword(keyword, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error searching protein feature by keyword: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_protein_feature_get_all(select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all protein feature data.
        
        Args:
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein feature data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_protein_feature_all(options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying all protein feature data: {str(e)}"
            }, indent=2)