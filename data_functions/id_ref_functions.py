"""
BV-BRC ID Reference Functions

This module provides wrapper functions for the BV-BRC Solr API id_ref resource,
exposing ID reference querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_id_ref_by_id(id: str, options: Dict[str, Any] = None,
                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query ID reference by ID.
    
    Args:
        id: The ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of ID reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.id_ref.get_by_id(id, options or {})


def query_id_ref_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query ID reference by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of ID reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.id_ref.query_by(filters, options or {})


def query_id_ref_by_id_type(id_type: str, options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query ID reference by ID type.
    
    Args:
        id_type: The ID type to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of ID reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.id_ref.get_by_id_type(id_type, options or {})


def query_id_ref_by_id_value(id_value: str, options: Dict[str, Any] = None,
                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query ID reference by ID value.
    
    Args:
        id_value: The ID value to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of ID reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.id_ref.get_by_id_value(id_value, options or {})


def query_id_ref_by_uniprotkb_accession(uniprotkb_accession: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query ID reference by UniProtKB accession.
    
    Args:
        uniprotkb_accession: The UniProtKB accession to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of ID reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.id_ref.get_by_uniprotkb_accession(uniprotkb_accession, options or {})


def query_id_ref_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query ID reference by date inserted range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of ID reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.id_ref.get_by_date_inserted_range(start_date, end_date, options or {})


def query_id_ref_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query ID reference by date modified range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of ID reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.id_ref.get_by_date_modified_range(start_date, end_date, options or {})


def query_id_ref_by_keyword(keyword: str, options: Dict[str, Any] = None,
                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search ID reference by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of ID reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.id_ref.search_by_keyword(keyword, options or {})


def query_id_ref_all(options: Dict[str, Any] = None,
                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all ID reference data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all ID reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.id_ref.get_all(options or {})
