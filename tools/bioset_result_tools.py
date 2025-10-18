#!/usr/bin/env python3
"""
BV-BRC Bioset Result Tools

This module contains MCP tools for querying bioset_result data from BV-BRC.
"""

import json
from typing import Optional

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


def register_bioset_result_tools(mcp, base_url: str, default_limit: int):
    """Register all bioset_result-related MCP tools with the Flask app."""

    def build_options(limit: int, select: Optional[str], sort: Optional[str]):
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        return options

    @mcp.tool()
    def bvbrc_bioset_result_get_by_id(id: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_id(id, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by id: {str(e)}"

    @mcp.tool()
    def bvbrc_bioset_result_query_by_filters(filters_json: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            filters = json.loads(filters_json)
        except json.JSONDecodeError as e:
            return f"Error parsing filters JSON: {str(e)}"
        try:
            return format_query_result(query_bioset_result_by_filters(filters, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by filters: {str(e)}"

    @mcp.tool()
    def bvbrc_bioset_result_get_by_bioset_id(bioset_id: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_bioset_id(bioset_id, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by bioset_id: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_bioset_name(bioset_name: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_bioset_name(bioset_name, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by bioset_name: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_bioset_description(bioset_description: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_bioset_description(bioset_description, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by bioset_description: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_bioset_type(bioset_type: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_bioset_type(bioset_type, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by bioset_type: {str(e)}"
    @mcp.tool()
    def bvbrc_bioset_result_get_by_entity_id(entity_id: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_entity_id(entity_id, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by entity_id: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_entity_name(entity_name: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_entity_name(entity_name, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by entity_name: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_entity_type(entity_type: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_entity_type(entity_type, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by entity_type: {str(e)}"
    @mcp.tool()
    def bvbrc_bioset_result_get_by_exp_id(exp_id: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_exp_id(exp_id, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by exp_id: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_exp_name(exp_name: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_exp_name(exp_name, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by exp_name: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_exp_title(exp_title: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_exp_title(exp_title, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by exp_title: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_exp_type(exp_type: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_exp_type(exp_type, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by exp_type: {str(e)}"
    @mcp.tool()
    def bvbrc_bioset_result_get_by_feature_id(feature_id: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_feature_id(feature_id, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by feature_id: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_gene(gene: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_gene(gene, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by gene: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_gene_id(gene_id: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_gene_id(gene_id, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by gene_id: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_genome_id(genome_id: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_genome_id(genome_id, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by genome_id: {str(e)}"
    @mcp.tool()
    def bvbrc_bioset_result_get_by_locus_tag(locus_tag: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_locus_tag(locus_tag, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by locus_tag: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_organism(organism: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_organism(organism, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by organism: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_patric_id(patric_id: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_patric_id(patric_id, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by patric_id: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_product(product: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_product(product, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by product: {str(e)}"
    @mcp.tool()
    def bvbrc_bioset_result_get_by_protein_id(protein_id: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_protein_id(protein_id, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by protein_id: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_result_type(result_type: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_result_type(result_type, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by result_type: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_strain(strain: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_strain(strain, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by strain: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_taxon_id(taxon_id: int, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_taxon_id(taxon_id, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by taxon_id: {str(e)}"
    @mcp.tool()
    def bvbrc_bioset_result_get_by_uniprot_id(uniprot_id: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_uniprot_id(uniprot_id, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by uniprot_id: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_other_id(other_id: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_other_id(other_id, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by other_id: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_treatment_name(treatment_name: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_treatment_name(treatment_name, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by treatment_name: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_treatment_type(treatment_type: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_treatment_type(treatment_type, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by treatment_type: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_treatment_amount(treatment_amount: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_treatment_amount(treatment_amount, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by treatment_amount: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_treatment_duration(treatment_duration: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_treatment_duration(treatment_duration, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by treatment_duration: {str(e)}"

    @mcp.tool()
    def bvbrc_bioset_result_get_by_counts_range(min_counts: float, max_counts: float, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_counts_range(min_counts, max_counts, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by counts range: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_fpkm_range(min_fpkm: float, max_fpkm: float, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_fpkm_range(min_fpkm, max_fpkm, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by fpkm range: {str(e)}"
    @mcp.tool()
    def bvbrc_bioset_result_get_by_log2_fc_range(min_log2_fc: float, max_log2_fc: float, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_log2_fc_range(min_log2_fc, max_log2_fc, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by log2_fc range: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_p_value_range(min_p_value: float, max_p_value: float, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_p_value_range(min_p_value, max_p_value, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by p_value range: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_tpm_range(min_tpm: float, max_tpm: float, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_tpm_range(min_tpm, max_tpm, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by tpm range: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_other_value_range(min_value: float, max_value: float, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_other_value_range(min_value, max_value, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by other_value range: {str(e)}"
    
    @mcp.tool()
    def bvbrc_bioset_result_get_by_z_score_range(min_z_score: float, max_z_score: float, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_z_score_range(min_z_score, max_z_score, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by z_score range: {str(e)}"

    @mcp.tool()
    def bvbrc_bioset_result_get_by_version(version: int, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_version(version, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by version: {str(e)}"

    @mcp.tool()
    def bvbrc_bioset_result_get_by_date_inserted_range(start_date: str, end_date: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_date_inserted_range(start_date, end_date, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by date_inserted range: {str(e)}"

    @mcp.tool()
    def bvbrc_bioset_result_get_by_date_modified_range(start_date: str, end_date: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_date_modified_range(start_date, end_date, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error querying bioset_result by date_modified range: {str(e)}"

    @mcp.tool()
    def bvbrc_bioset_result_search_by_keyword(keyword: str, limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_by_keyword(keyword, build_options(limit, select, sort), base_url))
        except Exception as e:
            return f"Error searching bioset_result by keyword: {str(e)}"

    @mcp.tool()
    def bvbrc_bioset_result_get_all(limit: int = default_limit, select: Optional[str] = None, sort: Optional[str] = None) -> str:
        try:
            return format_query_result(query_bioset_result_all({"limit": limit, **({"select": select.split(",")} if select else {}), **({"sort": sort} if sort else {})}, base_url))
        except Exception as e:
            return f"Error querying all bioset_result: {str(e)}"