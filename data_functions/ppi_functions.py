"""
BV-BRC Protein-Protein Interaction Functions

This module provides wrapper functions for the BV-BRC Solr API ppi resource,
exposing protein-protein interaction querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_ppi_by_id(id: str, options: Dict[str, Any] = None,
                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein-protein interaction by ID.
    
    Args:
        id: The ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.get_by_id(id, options or {})


def query_ppi_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein-protein interaction by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.query_by(filters, options or {})


def query_ppi_by_category(category: str, options: Dict[str, Any] = None,
                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein-protein interaction by category.
    
    Args:
        category: The category to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.get_by_category(category, options or {})


def query_ppi_by_detection_method(detection_method: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein-protein interaction by detection method.
    
    Args:
        detection_method: The detection method to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.get_by_detection_method(detection_method, options or {})


def query_ppi_by_domain_a(domain_a: str, options: Dict[str, Any] = None,
                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein-protein interaction by domain A.
    
    Args:
        domain_a: The domain A to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.get_by_domain_a(domain_a, options or {})


def query_ppi_by_domain_b(domain_b: str, options: Dict[str, Any] = None,
                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein-protein interaction by domain B.
    
    Args:
        domain_b: The domain B to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.get_by_domain_b(domain_b, options or {})


def query_ppi_by_evidence(evidence: str, options: Dict[str, Any] = None,
                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein-protein interaction by evidence.
    
    Args:
        evidence: The evidence to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.get_by_evidence(evidence, options or {})


def query_ppi_by_feature_id_a(feature_id_a: str, options: Dict[str, Any] = None,
                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein-protein interaction by feature ID A.
    
    Args:
        feature_id_a: The feature ID A to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.get_by_feature_id_a(feature_id_a, options or {})


def query_ppi_by_feature_id_b(feature_id_b: str, options: Dict[str, Any] = None,
                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein-protein interaction by feature ID B.
    
    Args:
        feature_id_b: The feature ID B to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.get_by_feature_id_b(feature_id_b, options or {})


def query_ppi_by_gene_a(gene_a: str, options: Dict[str, Any] = None,
                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein-protein interaction by gene A.
    
    Args:
        gene_a: The gene A to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.get_by_gene_a(gene_a, options or {})


def query_ppi_by_gene_b(gene_b: str, options: Dict[str, Any] = None,
                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein-protein interaction by gene B.
    
    Args:
        gene_b: The gene B to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.get_by_gene_b(gene_b, options or {})


def query_ppi_by_genome_id_a(genome_id_a: str, options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein-protein interaction by genome ID A.
    
    Args:
        genome_id_a: The genome ID A to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.get_by_genome_id_a(genome_id_a, options or {})


def query_ppi_by_genome_id_b(genome_id_b: str, options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein-protein interaction by genome ID B.
    
    Args:
        genome_id_b: The genome ID B to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.get_by_genome_id_b(genome_id_b, options or {})


def query_ppi_by_genome_name_a(genome_name_a: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein-protein interaction by genome name A.
    
    Args:
        genome_name_a: The genome name A to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.get_by_genome_name_a(genome_name_a, options or {})


def query_ppi_by_genome_name_b(genome_name_b: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein-protein interaction by genome name B.
    
    Args:
        genome_name_b: The genome name B to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.get_by_genome_name_b(genome_name_b, options or {})


def query_ppi_by_interaction_type(interaction_type: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein-protein interaction by interaction type.
    
    Args:
        interaction_type: The interaction type to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.get_by_interaction_type(interaction_type, options or {})


def query_ppi_by_interactor_a(interactor_a: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein-protein interaction by interactor A.
    
    Args:
        interactor_a: The interactor A to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.get_by_interactor_a(interactor_a, options or {})


def query_ppi_by_interactor_b(interactor_b: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein-protein interaction by interactor B.
    
    Args:
        interactor_b: The interactor B to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.get_by_interactor_b(interactor_b, options or {})


def query_ppi_by_pmid(pmid: str, options: Dict[str, Any] = None,
                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein-protein interaction by PMID.
    
    Args:
        pmid: The PMID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.get_by_pmid(pmid, options or {})


def query_ppi_by_source_db(source_db: str, options: Dict[str, Any] = None,
                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein-protein interaction by source database.
    
    Args:
        source_db: The source database to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.get_by_source_db(source_db, options or {})


def query_ppi_by_source_id(source_id: str, options: Dict[str, Any] = None,
                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein-protein interaction by source ID.
    
    Args:
        source_id: The source ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.get_by_source_id(source_id, options or {})


def query_ppi_by_taxon_id_a(taxon_id_a: int, options: Dict[str, Any] = None,
                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein-protein interaction by taxon ID A.
    
    Args:
        taxon_id_a: The taxon ID A to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.get_by_taxon_id_a(taxon_id_a, options or {})


def query_ppi_by_taxon_id_b(taxon_id_b: int, options: Dict[str, Any] = None,
                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein-protein interaction by taxon ID B.
    
    Args:
        taxon_id_b: The taxon ID B to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.get_by_taxon_id_b(taxon_id_b, options or {})


def query_ppi_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein-protein interaction by date inserted range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.get_by_date_inserted_range(start_date, end_date, options or {})


def query_ppi_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein-protein interaction by date modified range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.get_by_date_modified_range(start_date, end_date, options or {})


def query_ppi_by_keyword(keyword: str, options: Dict[str, Any] = None,
                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search protein-protein interaction by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.search_by_keyword(keyword, options or {})


def query_ppi_all(options: Dict[str, Any] = None,
                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all protein-protein interaction data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all protein-protein interaction records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.ppi.get_all(options or {})
