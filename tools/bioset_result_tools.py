#!/usr/bin/env python3
"""
BV-BRC Bioset Result Tools

This module contains MCP tools for querying bioset_result data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None

from data_functions import (
    query_bioset_result_by_id,
    query_bioset_result_by_filters,
    query_bioset_result_by_bioset_id,
    query_bioset_result_by_bioset_name,
    query_bioset_result_by_bioset_description,
    query_bioset_result_by_bioset_type,
    query_bioset_result_by_entity_id,
    query_bioset_result_by_entity_name,
    query_bioset_result_by_entity_type,
    query_bioset_result_by_exp_id,
    query_bioset_result_by_exp_name,
    query_bioset_result_by_exp_title,
    query_bioset_result_by_exp_type,
    query_bioset_result_by_feature_id,
    query_bioset_result_by_gene,
    query_bioset_result_by_gene_id,
    query_bioset_result_by_genome_id,
    query_bioset_result_by_locus_tag,
    query_bioset_result_by_organism,
    query_bioset_result_by_patric_id,
    query_bioset_result_by_product,
    query_bioset_result_by_protein_id,
    query_bioset_result_by_result_type,
    query_bioset_result_by_strain,
    query_bioset_result_by_taxon_id,
    query_bioset_result_by_uniprot_id,
    query_bioset_result_by_other_id,
    query_bioset_result_by_treatment_name,
    query_bioset_result_by_treatment_type,
    query_bioset_result_by_treatment_amount,
    query_bioset_result_by_treatment_duration,
    query_bioset_result_by_counts_range,
    query_bioset_result_by_fpkm_range,
    query_bioset_result_by_log2_fc_range,
    query_bioset_result_by_p_value_range,
    query_bioset_result_by_tpm_range,
    query_bioset_result_by_other_value_range,
    query_bioset_result_by_z_score_range,
    query_bioset_result_by_version,
    query_bioset_result_by_date_inserted_range,
    query_bioset_result_by_date_modified_range,
    query_bioset_result_by_keyword,
    query_bioset_result_all,
    format_query_result
)

def register_bioset_result_tools(mcp: FastMCP, base_url: str):
    """Register all bioset_result-related MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_id(id: str, 
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by ID.
        
        Args:
            id: The bioset_result ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_id(id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by ID: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_bioset_result_query_by_filters(filters_json: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query bioset_result data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria (e.g., '{"bioset_id": "123", "organism": "E. coli"}')
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
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
            result, count = query_bioset_result_by_filters(filters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by filters: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_bioset_result_get_by_bioset_id(bioset_id: str,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by bioset ID.
        
        Args:
            bioset_id: The bioset ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_bioset_id(bioset_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by bioset ID: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_bioset_name(bioset_name: str,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by bioset name.
        
        Args:
            bioset_name: The bioset name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_bioset_name(bioset_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by bioset name: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_bioset_description(bioset_description: str,
                                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by bioset description.
        
        Args:
            bioset_description: The bioset description to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_bioset_description(bioset_description, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by bioset description: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_bioset_type(bioset_type: str,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by bioset type.
        
        Args:
            bioset_type: The bioset type to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_bioset_type(bioset_type, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by bioset type: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_bioset_result_get_by_entity_id(entity_id: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by entity ID.
        
        Args:
            entity_id: The entity ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_entity_id(entity_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by entity ID: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_entity_name(entity_name: str,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by entity name.
        
        Args:
            entity_name: The entity name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_entity_name(entity_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by entity name: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_entity_type(entity_type: str,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by entity type.
        
        Args:
            entity_type: The entity type to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_entity_type(entity_type, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by entity type: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_bioset_result_get_by_exp_id(exp_id: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by experiment ID.
        
        Args:
            exp_id: The experiment ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_exp_id(exp_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by experiment ID: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_exp_name(exp_name: str,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by experiment name.
        
        Args:
            exp_name: The experiment name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_exp_name(exp_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by experiment name: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_exp_title(exp_title: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by experiment title.
        
        Args:
            exp_title: The experiment title to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_exp_title(exp_title, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by experiment title: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_exp_type(exp_type: str,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by experiment type.
        
        Args:
            exp_type: The experiment type to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_exp_type(exp_type, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by experiment type: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_bioset_result_get_by_feature_id(feature_id: str,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by feature ID.
        
        Args:
            feature_id: The feature ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_feature_id(feature_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by feature ID: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_gene(gene: str,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by gene.
        
        Args:
            gene: The gene to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_gene(gene, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by gene: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_gene_id(gene_id: str,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by gene ID.
        
        Args:
            gene_id: The gene ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_gene_id(gene_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by gene ID: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_genome_id(genome_id: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by genome ID.
        
        Args:
            genome_id: The genome ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_genome_id(genome_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by genome ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_bioset_result_get_by_locus_tag(locus_tag: str,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by locus tag.
        
        Args:
            locus_tag: The locus tag to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_locus_tag(locus_tag, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by locus tag: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_organism(organism: str,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by organism.
        
        Args:
            organism: The organism to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_organism(organism, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by organism: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_patric_id(patric_id: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by PATRIC ID.
        
        Args:
            patric_id: The PATRIC ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_patric_id(patric_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by PATRIC ID: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_product(product: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by product.
        
        Args:
            product: The product to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_product(product, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by product: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_bioset_result_get_by_protein_id(protein_id: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by protein ID.
        
        Args:
            protein_id: The protein ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_protein_id(protein_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by protein ID: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_result_type(result_type: str,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by result type.
        
        Args:
            result_type: The result type to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_result_type(result_type, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by result type: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_strain(strain: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by strain.
        
        Args:
            strain: The strain to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_strain(strain, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by strain: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_taxon_id(taxon_id: int,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_taxon_id(taxon_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by taxon ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_bioset_result_get_by_uniprot_id(uniprot_id: str,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by UniProt ID.
        
        Args:
            uniprot_id: The UniProt ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_uniprot_id(uniprot_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by UniProt ID: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_other_id(other_id: str,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by other ID.
        
        Args:
            other_id: The other ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_other_id(other_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by other ID: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_treatment_name(treatment_name: str,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by treatment name.
        
        Args:
            treatment_name: The treatment name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_treatment_name(treatment_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by treatment name: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_treatment_type(treatment_type: str,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by treatment type.
        
        Args:
            treatment_type: The treatment type to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_treatment_type(treatment_type, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by treatment type: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_treatment_amount(treatment_amount: str,
                                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by treatment amount.
        
        Args:
            treatment_amount: The treatment amount to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_treatment_amount(treatment_amount, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by treatment amount: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_treatment_duration(treatment_duration: str,
                                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by treatment duration.
        
        Args:
            treatment_duration: The treatment duration to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_treatment_duration(treatment_duration, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by treatment duration: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_bioset_result_get_by_counts_range(min_counts: float, max_counts: float,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by counts range.
        
        Args:
            min_counts: Minimum counts value
            max_counts: Maximum counts value
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_counts_range(min_counts, max_counts, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by counts range: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_fpkm_range(min_fpkm: float, max_fpkm: float,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by FPKM range.
        
        Args:
            min_fpkm: Minimum FPKM value
            max_fpkm: Maximum FPKM value
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_fpkm_range(min_fpkm, max_fpkm, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by FPKM range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_bioset_result_get_by_log2_fc_range(min_log2_fc: float, max_log2_fc: float,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by log2 fold change range.
        
        Args:
            min_log2_fc: Minimum log2 fold change value
            max_log2_fc: Maximum log2 fold change value
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_log2_fc_range(min_log2_fc, max_log2_fc, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by log2 fold change range: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_p_value_range(min_p_value: float, max_p_value: float,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by p-value range.
        
        Args:
            min_p_value: Minimum p-value
            max_p_value: Maximum p-value
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_p_value_range(min_p_value, max_p_value, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by p-value range: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_tpm_range(min_tpm: float, max_tpm: float,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by TPM range.
        
        Args:
            min_tpm: Minimum TPM value
            max_tpm: Maximum TPM value
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_tpm_range(min_tpm, max_tpm, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by TPM range: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_other_value_range(min_value: float, max_value: float,
                                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by other value range.
        
        Args:
            min_value: Minimum other value
            max_value: Maximum other value
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_other_value_range(min_value, max_value, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by other value range: {str(e)}"
            }, indent=2)
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_z_score_range(min_z_score: float, max_z_score: float,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by z-score range.
        
        Args:
            min_z_score: Minimum z-score value
            max_z_score: Maximum z-score value
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_z_score_range(min_z_score, max_z_score, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by z-score range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_bioset_result_get_by_version(version: int,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by version.
        
        Args:
            version: The version to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_version(version, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by version: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_bioset_result_get_by_date_inserted_range(start_date: str, end_date: str,
                                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by date inserted range.
        
        Args:
            start_date: Start date for the range
            end_date: End date for the range
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_date_inserted_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by date inserted range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_bioset_result_get_by_date_modified_range(start_date: str, end_date: str,
                                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset_result data by date modified range.
        
        Args:
            start_date: Start date for the range
            end_date: End date for the range
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_date_modified_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset_result by date modified range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_bioset_result_search_by_keyword(keyword: str,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search bioset_result data by keyword.
        
        Args:
            keyword: The keyword to search for
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_by_keyword(keyword, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error searching bioset_result by keyword: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_bioset_result_get_all(select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all bioset_result data.
        
        Args:
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset_result data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_result_all(options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying all bioset_result: {str(e)}"
            }, indent=2)