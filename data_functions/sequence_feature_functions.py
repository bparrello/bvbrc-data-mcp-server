"""
BV-BRC Sequence Feature Functions

This module provides wrapper functions for the BV-BRC Solr API sequence_feature resource,
exposing sequence feature querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_sequence_feature_by_id(id: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by ID.
    
    Args:
        id: The ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_id(id, options or {})


def query_sequence_feature_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.query_by(filters, options or {})


def query_sequence_feature_by_feature_id(feature_id: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by feature ID.
    
    Args:
        feature_id: The feature ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_feature_id(feature_id, options or {})


def query_sequence_feature_by_genome_id(genome_id: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by genome ID.
    
    Args:
        genome_id: The genome ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_genome_id(genome_id, options or {})


def query_sequence_feature_by_genome_name(genome_name: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by genome name.
    
    Args:
        genome_name: The genome name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_genome_name(genome_name, options or {})


def query_sequence_feature_by_gene(gene: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by gene.
    
    Args:
        gene: The gene to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_gene(gene, options or {})


def query_sequence_feature_by_product(product: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by product.
    
    Args:
        product: The product to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_product(product, options or {})


def query_sequence_feature_by_patric_id(patric_id: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by PATRIC ID.
    
    Args:
        patric_id: The PATRIC ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_patric_id(patric_id, options or {})


def query_sequence_feature_by_genbank_accession(genbank_accession: str, options: Dict[str, Any] = None,
                                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by GenBank accession.
    
    Args:
        genbank_accession: The GenBank accession to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_genbank_accession(genbank_accession, options or {})


def query_sequence_feature_by_refseq_locus_tag(refseq_locus_tag: str, options: Dict[str, Any] = None,
                                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by RefSeq locus tag.
    
    Args:
        refseq_locus_tag: The RefSeq locus tag to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_refseq_locus_tag(refseq_locus_tag, options or {})


def query_sequence_feature_by_sf_category(sf_category: str, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by SF category.
    
    Args:
        sf_category: The SF category to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_sf_category(sf_category, options or {})


def query_sequence_feature_by_sf_id(sf_id: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by SF ID.
    
    Args:
        sf_id: The SF ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_sf_id(sf_id, options or {})


def query_sequence_feature_by_sf_name(sf_name: str, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by SF name.
    
    Args:
        sf_name: The SF name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_sf_name(sf_name, options or {})


def query_sequence_feature_by_source(source: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by source.
    
    Args:
        source: The source to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_source(source, options or {})


def query_sequence_feature_by_source_id(source_id: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by source ID.
    
    Args:
        source_id: The source ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_source_id(source_id, options or {})


def query_sequence_feature_by_source_strain(source_strain: str, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by source strain.
    
    Args:
        source_strain: The source strain to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_source_strain(source_strain, options or {})


def query_sequence_feature_by_segment(segment: str, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by segment.
    
    Args:
        segment: The segment to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_segment(segment, options or {})


def query_sequence_feature_by_subtype(subtype: str, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by subtype.
    
    Args:
        subtype: The subtype to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_subtype(subtype, options or {})


def query_sequence_feature_by_taxon_id(taxon_id: int, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by taxon ID.
    
    Args:
        taxon_id: The taxon ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_taxon_id(taxon_id, options or {})


def query_sequence_feature_by_evidence_code(evidence_code: str, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by evidence code.
    
    Args:
        evidence_code: The evidence code to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_evidence_code(evidence_code, options or {})


def query_sequence_feature_by_aa_sequence_md5(aa_sequence_md5: str, options: Dict[str, Any] = None,
                                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by amino acid sequence MD5.
    
    Args:
        aa_sequence_md5: The amino acid sequence MD5 to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_aa_sequence_md5(aa_sequence_md5, options or {})


def query_sequence_feature_by_aa_variant(aa_variant: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by amino acid variant.
    
    Args:
        aa_variant: The amino acid variant to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_aa_variant(aa_variant, options or {})


def query_sequence_feature_by_sf_sequence_md5(sf_sequence_md5: str, options: Dict[str, Any] = None,
                                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by SF sequence MD5.
    
    Args:
        sf_sequence_md5: The SF sequence MD5 to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_sf_sequence_md5(sf_sequence_md5, options or {})


def query_sequence_feature_by_source_aa_sequence(source_aa_sequence: str, options: Dict[str, Any] = None,
                                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by source amino acid sequence.
    
    Args:
        source_aa_sequence: The source amino acid sequence to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_source_aa_sequence(source_aa_sequence, options or {})


def query_sequence_feature_by_source_sf_location(source_sf_location: str, options: Dict[str, Any] = None,
                                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by source SF location.
    
    Args:
        source_sf_location: The source SF location to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_source_sf_location(source_sf_location, options or {})


def query_sequence_feature_by_variant_types(variant_types: str, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by variant types.
    
    Args:
        variant_types: The variant types to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_variant_types(variant_types, options or {})


def query_sequence_feature_by_start(start: int, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by start position.
    
    Args:
        start: The start position to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_start(start, options or {})


def query_sequence_feature_by_end(end: int, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by end position.
    
    Args:
        end: The end position to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_end(end, options or {})


def query_sequence_feature_by_length(length: int, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by length.
    
    Args:
        length: The length to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_length(length, options or {})


def query_sequence_feature_by_position_range(start: int, end: int, options: Dict[str, Any] = None,
                                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by position range.
    
    Args:
        start: Start position
        end: End position
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_position_range(start, end, options or {})


def query_sequence_feature_by_length_range(min_length: int, max_length: int, options: Dict[str, Any] = None,
                                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by length range.
    
    Args:
        min_length: Minimum length
        max_length: Maximum length
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_length_range(min_length, max_length, options or {})


def query_sequence_feature_by_date_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by date range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_date_range(start_date, end_date, options or {})


def query_sequence_feature_by_modified_date_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature by modified date range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_by_modified_date_range(start_date, end_date, options or {})


def query_sequence_feature_by_keyword(keyword: str, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search sequence feature by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.search_by_keyword(keyword, options or {})


def query_sequence_feature_all(options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all sequence feature data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all sequence feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature.get_all(options or {})
