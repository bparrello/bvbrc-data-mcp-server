"""
BV-BRC Protein Feature Functions

This module provides wrapper functions for the BV-BRC Solr API protein_feature resource,
exposing protein feature querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_protein_feature_by_id(id: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by ID.
    
    Args:
        id: The ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_id(id, options or {})


def query_protein_feature_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.query_by(filters, options or {})


def query_protein_feature_by_aa_sequence_md5(aa_sequence_md5: str, options: Dict[str, Any] = None,
                                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by amino acid sequence MD5.
    
    Args:
        aa_sequence_md5: The amino acid sequence MD5 to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_aa_sequence_md5(aa_sequence_md5, options or {})


def query_protein_feature_by_classification(classification: str, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by classification.
    
    Args:
        classification: The classification to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_classification(classification, options or {})


def query_protein_feature_by_comment(comment: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by comment.
    
    Args:
        comment: The comment to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_comment(comment, options or {})


def query_protein_feature_by_description(description: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by description.
    
    Args:
        description: The description to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_description(description, options or {})


def query_protein_feature_by_e_value(e_value: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by E-value.
    
    Args:
        e_value: The E-value to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_e_value(e_value, options or {})


def query_protein_feature_by_end(end: int, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by end position.
    
    Args:
        end: The end position to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_end(end, options or {})


def query_protein_feature_by_evidence(evidence: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by evidence.
    
    Args:
        evidence: The evidence to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_evidence(evidence, options or {})


def query_protein_feature_by_feature_id(feature_id: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by feature ID.
    
    Args:
        feature_id: The feature ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_feature_id(feature_id, options or {})


def query_protein_feature_by_feature_type(feature_type: str, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by feature type.
    
    Args:
        feature_type: The feature type to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_feature_type(feature_type, options or {})


def query_protein_feature_by_gene(gene: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by gene.
    
    Args:
        gene: The gene to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_gene(gene, options or {})


def query_protein_feature_by_genome_id(genome_id: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by genome ID.
    
    Args:
        genome_id: The genome ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_genome_id(genome_id, options or {})


def query_protein_feature_by_genome_name(genome_name: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by genome name.
    
    Args:
        genome_name: The genome name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_genome_name(genome_name, options or {})


def query_protein_feature_by_interpro_description(interpro_description: str, options: Dict[str, Any] = None,
                                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by InterPro description.
    
    Args:
        interpro_description: The InterPro description to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_interpro_description(interpro_description, options or {})


def query_protein_feature_by_interpro_id(interpro_id: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by InterPro ID.
    
    Args:
        interpro_id: The InterPro ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_interpro_id(interpro_id, options or {})


def query_protein_feature_by_length(length: int, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by length.
    
    Args:
        length: The length to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_length(length, options or {})


def query_protein_feature_by_patric_id(patric_id: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by PATRIC ID.
    
    Args:
        patric_id: The PATRIC ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_patric_id(patric_id, options or {})


def query_protein_feature_by_product(product: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by product.
    
    Args:
        product: The product to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_product(product, options or {})


def query_protein_feature_by_publication(publication: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by publication.
    
    Args:
        publication: The publication to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_publication(publication, options or {})


def query_protein_feature_by_refseq_locus_tag(refseq_locus_tag: str, options: Dict[str, Any] = None,
                                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by RefSeq locus tag.
    
    Args:
        refseq_locus_tag: The RefSeq locus tag to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_refseq_locus_tag(refseq_locus_tag, options or {})


def query_protein_feature_by_score(score: float, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by score.
    
    Args:
        score: The score to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_score(score, options or {})


def query_protein_feature_by_segment(segment: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by segment.
    
    Args:
        segment: The segment to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_segment(segment, options or {})


def query_protein_feature_by_sequence(sequence: str, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by sequence.
    
    Args:
        sequence: The sequence to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_sequence(sequence, options or {})


def query_protein_feature_by_source(source: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by source.
    
    Args:
        source: The source to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_source(source, options or {})


def query_protein_feature_by_source_id(source_id: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by source ID.
    
    Args:
        source_id: The source ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_source_id(source_id, options or {})


def query_protein_feature_by_start(start: int, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by start position.
    
    Args:
        start: The start position to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_start(start, options or {})


def query_protein_feature_by_taxon_id(taxon_id: int, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by taxon ID.
    
    Args:
        taxon_id: The taxon ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_taxon_id(taxon_id, options or {})


def query_protein_feature_by_score_range(min_score: float, max_score: float, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by score range.
    
    Args:
        min_score: Minimum score
        max_score: Maximum score
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_score_range(min_score, max_score, options or {})


def query_protein_feature_by_length_range(min_length: int, max_length: int, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by length range.
    
    Args:
        min_length: Minimum length
        max_length: Maximum length
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_length_range(min_length, max_length, options or {})


def query_protein_feature_by_position_range(min_start: int, max_end: int, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by position range.
    
    Args:
        min_start: Minimum start position
        max_end: Maximum end position
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_position_range(min_start, max_end, options or {})


def query_protein_feature_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by date inserted range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_date_inserted_range(start_date, end_date, options or {})


def query_protein_feature_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein feature by date modified range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_by_date_modified_range(start_date, end_date, options or {})


def query_protein_feature_by_keyword(keyword: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search protein feature by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.search_by_keyword(keyword, options or {})


def query_protein_feature_all(options: Dict[str, Any] = None,
                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all protein feature data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all protein feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_feature.get_all(options or {})
