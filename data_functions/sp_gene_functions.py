"""
BV-BRC SP Gene Functions

This module provides wrapper functions for the BV-BRC Solr API sp_gene resource,
exposing SP gene querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_sp_gene_by_id(id: str, options: Dict[str, Any] = None,
                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query SP gene by ID.
    
    Args:
        id: The ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of SP gene records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sp_gene.get_by_id(id, options or {})


def query_sp_gene_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query SP gene by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of SP gene records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sp_gene.query_by(filters, options or {})


def query_sp_gene_by_genome_id(genome_id: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query SP gene by genome ID.
    
    Args:
        genome_id: The genome ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of SP gene records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sp_gene.get_by_genome_id(genome_id, options or {})


def query_sp_gene_by_gene(gene: str, options: Dict[str, Any] = None,
                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query SP gene by gene.
    
    Args:
        gene: The gene to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of SP gene records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sp_gene.get_by_gene(gene, options or {})


def query_sp_gene_by_taxon_id(taxon_id: int, options: Dict[str, Any] = None,
                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query SP gene by taxon ID.
    
    Args:
        taxon_id: The taxon ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of SP gene records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sp_gene.get_by_taxon_id(taxon_id, options or {})


def query_sp_gene_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query SP gene by date inserted range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of SP gene records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sp_gene.get_by_date_inserted_range(start_date, end_date, options or {})


def query_sp_gene_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query SP gene by date modified range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of SP gene records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sp_gene.get_by_date_modified_range(start_date, end_date, options or {})


def query_sp_gene_by_keyword(keyword: str, options: Dict[str, Any] = None,
                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search SP gene by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of SP gene records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sp_gene.search_by_keyword(keyword, options or {})


def query_sp_gene_all(options: Dict[str, Any] = None,
                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all SP gene data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all SP gene records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sp_gene.get_all(options or {})
