"""
BV-BRC SP Gene Reference Functions

This module provides wrapper functions for the BV-BRC Solr API sp_gene_ref resource,
exposing SP gene reference querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_sp_gene_ref_by_id(id: str, options: Dict[str, Any] = None,
                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query SP gene reference by ID.
    
    Args:
        id: The ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of SP gene reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sp_gene_ref.get_by_id(id, options or {})


def query_sp_gene_ref_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query SP gene reference by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of SP gene reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sp_gene_ref.query_by(filters, options or {})


def query_sp_gene_ref_by_antibiotics(antibiotics: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query SP gene reference by antibiotics.
    
    Args:
        antibiotics: The antibiotics to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of SP gene reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sp_gene_ref.get_by_antibiotics(antibiotics, options or {})


def query_sp_gene_ref_by_gene_symbol(gene_symbol: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query SP gene reference by gene symbol.
    
    Args:
        gene_symbol: The gene symbol to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of SP gene reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sp_gene_ref.get_by_gene_symbol(gene_symbol, options or {})


def query_sp_gene_ref_by_source(source: str, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query SP gene reference by source.
    
    Args:
        source: The source to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of SP gene reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sp_gene_ref.get_by_source(source, options or {})


def query_sp_gene_ref_by_taxon_id(taxon_id: int, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query SP gene reference by taxon ID.
    
    Args:
        taxon_id: The taxon ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of SP gene reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sp_gene_ref.get_by_taxon_id(taxon_id, options or {})


def query_sp_gene_ref_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query SP gene reference by date inserted range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of SP gene reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sp_gene_ref.get_by_date_inserted_range(start_date, end_date, options or {})


def query_sp_gene_ref_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query SP gene reference by date modified range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of SP gene reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sp_gene_ref.get_by_date_modified_range(start_date, end_date, options or {})


def query_sp_gene_ref_by_keyword(keyword: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search SP gene reference by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of SP gene reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sp_gene_ref.search_by_keyword(keyword, options or {})


def query_sp_gene_ref_all(options: Dict[str, Any] = None,
                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all SP gene reference data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all SP gene reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sp_gene_ref.get_all(options or {})
