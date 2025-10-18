"""
BV-BRC Pathway Functions

This module provides wrapper functions for the BV-BRC Solr API pathway resource,
exposing pathway querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_pathway_by_id(id: str, options: Dict[str, Any] = None,
                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by ID.
    
    Args:
        id: The ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_id(id, options or {})


def query_pathway_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.query_by(filters, options or {})


def query_pathway_by_accession(accession: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by accession.
    
    Args:
        accession: The accession to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_accession(accession, options or {})


def query_pathway_by_alt_locus_tag(alt_locus_tag: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by alternative locus tag.
    
    Args:
        alt_locus_tag: The alternative locus tag to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_alt_locus_tag(alt_locus_tag, options or {})


def query_pathway_by_annotation(annotation: str, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by annotation.
    
    Args:
        annotation: The annotation to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_annotation(annotation, options or {})


def query_pathway_by_ec_description(ec_description: str, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by EC description.
    
    Args:
        ec_description: The EC description to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_ec_description(ec_description, options or {})


def query_pathway_by_ec_number(ec_number: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by EC number.
    
    Args:
        ec_number: The EC number to query (e.g., "1.1.1.1")
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_ec_number(ec_number, options or {})


def query_pathway_by_feature_id(feature_id: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by feature ID.
    
    Args:
        feature_id: The feature ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_feature_id(feature_id, options or {})


def query_pathway_by_gene(gene: str, options: Dict[str, Any] = None,
                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by gene.
    
    Args:
        gene: The gene to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_gene(gene, options or {})


def query_pathway_by_genome_ec(genome_ec: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by genome EC.
    
    Args:
        genome_ec: The genome EC to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_genome_ec(genome_ec, options or {})


def query_pathway_by_genome_id(genome_id: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by genome ID.
    
    Args:
        genome_id: The genome ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_genome_id(genome_id, options or {})


def query_pathway_by_genome_name(genome_name: str, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by genome name.
    
    Args:
        genome_name: The genome name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_genome_name(genome_name, options or {})


def query_pathway_by_owner(owner: str, options: Dict[str, Any] = None,
                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by owner.
    
    Args:
        owner: The owner to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_owner(owner, options or {})


def query_pathway_by_pathway_class(pathway_class: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by pathway class.
    
    Args:
        pathway_class: The pathway class to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_pathway_class(pathway_class, options or {})


def query_pathway_by_pathway_ec(pathway_ec: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by pathway EC.
    
    Args:
        pathway_ec: The pathway EC to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_pathway_ec(pathway_ec, options or {})


def query_pathway_by_pathway_id(pathway_id: str, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by pathway ID.
    
    Args:
        pathway_id: The pathway ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_pathway_id(pathway_id, options or {})


def query_pathway_by_pathway_name(pathway_name: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by pathway name.
    
    Args:
        pathway_name: The pathway name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_pathway_name(pathway_name, options or {})


def query_pathway_by_patric_id(patric_id: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by PATRIC ID.
    
    Args:
        patric_id: The PATRIC ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_patric_id(patric_id, options or {})


def query_pathway_by_product(product: str, options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by product.
    
    Args:
        product: The product to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_product(product, options or {})


def query_pathway_by_public_status(is_public: bool, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by public status.
    
    Args:
        is_public: The public status to query (True/False)
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_public_status(is_public, options or {})


def query_pathway_by_refseq_locus_tag(refseq_locus_tag: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by RefSeq locus tag.
    
    Args:
        refseq_locus_tag: The RefSeq locus tag to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_refseq_locus_tag(refseq_locus_tag, options or {})


def query_pathway_by_sequence_id(sequence_id: str, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by sequence ID.
    
    Args:
        sequence_id: The sequence ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_sequence_id(sequence_id, options or {})


def query_pathway_by_taxon_id(taxon_id: int, options: Dict[str, Any] = None,
                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by taxon ID.
    
    Args:
        taxon_id: The taxon ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_taxon_id(taxon_id, options or {})


def query_pathway_by_user_read(user_read: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by user read.
    
    Args:
        user_read: The user read to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_user_read(user_read, options or {})


def query_pathway_by_user_write(user_write: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by user write.
    
    Args:
        user_write: The user write to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_user_write(user_write, options or {})


def query_pathway_by_version(version: int, options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by version.
    
    Args:
        version: The version to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_version(version, options or {})


def query_pathway_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by date inserted range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_date_inserted_range(start_date, end_date, options or {})


def query_pathway_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway by date modified range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_by_date_modified_range(start_date, end_date, options or {})


def query_pathway_by_keyword(keyword: str, options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search pathway by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.search_by_keyword(keyword, options or {})


def query_pathway_all(options: Dict[str, Any] = None,
                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all pathway data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all pathway records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway.get_all(options or {})
