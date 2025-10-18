"""
BV-BRC Bioset Result Functions

This module provides bioset_result querying functions for the BV-BRC Solr API.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_bioset_result_by_id(id: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query bioset_result by document id.
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_id(id, options or {})


def query_bioset_result_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query bioset_result by custom filters.
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.query_by(filters, options or {})


def query_bioset_result_by_bioset_id(bioset_id: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_bioset_id(bioset_id, options or {})


def query_bioset_result_by_bioset_name(bioset_name: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_bioset_name(bioset_name, options or {})


def query_bioset_result_by_bioset_description(bioset_description: str, options: Dict[str, Any] = None,
                                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_bioset_description(bioset_description, options or {})


def query_bioset_result_by_bioset_type(bioset_type: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_bioset_type(bioset_type, options or {})


def query_bioset_result_by_entity_id(entity_id: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_entity_id(entity_id, options or {})


def query_bioset_result_by_entity_name(entity_name: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_entity_name(entity_name, options or {})


def query_bioset_result_by_entity_type(entity_type: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_entity_type(entity_type, options or {})


def query_bioset_result_by_exp_id(exp_id: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_exp_id(exp_id, options or {})


def query_bioset_result_by_exp_name(exp_name: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_exp_name(exp_name, options or {})


def query_bioset_result_by_exp_title(exp_title: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_exp_title(exp_title, options or {})


def query_bioset_result_by_exp_type(exp_type: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_exp_type(exp_type, options or {})


def query_bioset_result_by_feature_id(feature_id: str, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_feature_id(feature_id, options or {})


def query_bioset_result_by_gene(gene: str, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_gene(gene, options or {})


def query_bioset_result_by_gene_id(gene_id: str, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_gene_id(gene_id, options or {})


def query_bioset_result_by_genome_id(genome_id: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_genome_id(genome_id, options or {})


def query_bioset_result_by_locus_tag(locus_tag: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_locus_tag(locus_tag, options or {})


def query_bioset_result_by_organism(organism: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_organism(organism, options or {})


def query_bioset_result_by_patric_id(patric_id: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_patric_id(patric_id, options or {})


def query_bioset_result_by_product(product: str, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_product(product, options or {})


def query_bioset_result_by_protein_id(protein_id: str, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_protein_id(protein_id, options or {})


def query_bioset_result_by_result_type(result_type: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_result_type(result_type, options or {})


def query_bioset_result_by_strain(strain: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_strain(strain, options or {})


def query_bioset_result_by_taxon_id(taxon_id: int, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_taxon_id(taxon_id, options or {})


def query_bioset_result_by_uniprot_id(uniprot_id: str, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_uniprot_id(uniprot_id, options or {})


def query_bioset_result_by_other_id(other_id: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_other_id(other_id, options or {})


def query_bioset_result_by_treatment_name(treatment_name: str, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_treatment_name(treatment_name, options or {})


def query_bioset_result_by_treatment_type(treatment_type: str, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_treatment_type(treatment_type, options or {})


def query_bioset_result_by_treatment_amount(treatment_amount: str, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_treatment_amount(treatment_amount, options or {})


def query_bioset_result_by_treatment_duration(treatment_duration: str, options: Dict[str, Any] = None,
                                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_treatment_duration(treatment_duration, options or {})


def query_bioset_result_by_counts_range(min_counts: float, max_counts: float, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_counts_range(min_counts, max_counts, options or {})


def query_bioset_result_by_fpkm_range(min_fpkm: float, max_fpkm: float, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_fpkm_range(min_fpkm, max_fpkm, options or {})


def query_bioset_result_by_log2_fc_range(min_log2_fc: float, max_log2_fc: float, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_log2_fc_range(min_log2_fc, max_log2_fc, options or {})


def query_bioset_result_by_p_value_range(min_p_value: float, max_p_value: float, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_p_value_range(min_p_value, max_p_value, options or {})


def query_bioset_result_by_tpm_range(min_tpm: float, max_tpm: float, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_tpm_range(min_tpm, max_tpm, options or {})


def query_bioset_result_by_other_value_range(min_value: float, max_value: float, options: Dict[str, Any] = None,
                                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_other_value_range(min_value, max_value, options or {})


def query_bioset_result_by_z_score_range(min_z_score: float, max_z_score: float, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_z_score_range(min_z_score, max_z_score, options or {})


def query_bioset_result_by_version(version: int, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_version(version, options or {})


def query_bioset_result_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_date_inserted_range(start_date, end_date, options or {})


def query_bioset_result_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_by_date_modified_range(start_date, end_date, options or {})


def query_bioset_result_by_keyword(keyword: str, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.search_by_keyword(keyword, options or {})


def query_bioset_result_all(options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    client = create_bvbrc_client(base_url, headers)
    return client.bioset_result.get_all(options or {})


