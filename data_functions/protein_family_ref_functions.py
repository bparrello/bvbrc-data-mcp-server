"""
BV-BRC Protein Family Reference Functions

This module provides wrapper functions for the BV-BRC Solr API protein_family_ref resource,
exposing protein family reference querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_protein_family_ref_by_id(family_id: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein family reference by family ID.
    
    Args:
        family_id: The family ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein family reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_family_ref.get_by_id(family_id, options or {})


def query_protein_family_ref_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein family reference by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein family reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_family_ref.query_by(filters, options or {})


def query_protein_family_ref_by_family_product(family_product: str, options: Dict[str, Any] = None,
                                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein family reference by family product.
    
    Args:
        family_product: The family product to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein family reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_family_ref.get_by_family_product(family_product, options or {})


def query_protein_family_ref_by_family_type(family_type: str, options: Dict[str, Any] = None,
                                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein family reference by family type.
    
    Args:
        family_type: The family type to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein family reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_family_ref.get_by_family_type(family_type, options or {})


def query_protein_family_ref_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein family reference by date inserted range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein family reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_family_ref.get_by_date_inserted_range(start_date, end_date, options or {})


def query_protein_family_ref_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein family reference by date modified range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein family reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_family_ref.get_by_date_modified_range(start_date, end_date, options or {})


def query_protein_family_ref_by_keyword(keyword: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search protein family reference by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein family reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_family_ref.search_by_keyword(keyword, options or {})


def query_protein_family_ref_all(options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all protein family reference data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all protein family reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_family_ref.get_all(options or {})
