"""
BV-BRC Genome Feature Functions

This module provides genome feature querying functions for the BV-BRC Solr API.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_genome_feature_by_id(feature_id: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome feature by ID.
    
    Args:
        feature_id: The feature ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_feature.get_by_id(feature_id, options or {})


def query_genome_feature_by_genome_id(genome_id: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome features by genome ID.
    
    Args:
        genome_id: The genome ID to query features for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_feature.get_by_genome_id(genome_id, options or {})


def query_genome_feature_by_gene(gene_name: str, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome features by gene name.
    
    Args:
        gene_name: The gene name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_feature.get_by_gene(gene_name, options or {})


def query_genome_feature_by_product(product_name: str, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome features by product name.
    
    Args:
        product_name: The product name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_feature.get_by_product(product_name, options or {})


def query_genome_feature_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome features by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome feature records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_feature.query_by(filters, options or {})
