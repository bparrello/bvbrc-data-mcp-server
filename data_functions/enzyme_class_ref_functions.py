"""
BV-BRC Enzyme Class Reference Functions

This module provides wrapper functions for the BV-BRC Solr API enzyme_class_ref resource,
exposing enzyme class reference querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_enzyme_class_ref_by_ec_number(ec_number: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query enzyme class reference by EC number.
    
    Args:
        ec_number: The EC number to query (e.g., "1.1.1.1")
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of enzyme class reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.enzyme_class_ref.get_by_id(ec_number, options or {})


def query_enzyme_class_ref_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query enzyme class reference by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of enzyme class reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.enzyme_class_ref.query_by(filters, options or {})


def query_enzyme_class_ref_by_ec_description(ec_description: str, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query enzyme class reference by EC description.
    
    Args:
        ec_description: The EC description to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of enzyme class reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.enzyme_class_ref.get_by_ec_description(ec_description, options or {})


def query_enzyme_class_ref_by_go_term(go_term: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query enzyme class reference by GO term.
    
    Args:
        go_term: The GO term to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of enzyme class reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.enzyme_class_ref.get_by_go(go_term, options or {})


def query_enzyme_class_ref_by_version(version: int, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query enzyme class reference by version.
    
    Args:
        version: The version number to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of enzyme class reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.enzyme_class_ref.get_by_version(version, options or {})


def query_enzyme_class_ref_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query enzyme class reference by date inserted range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of enzyme class reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.enzyme_class_ref.get_by_date_inserted_range(start_date, end_date, options or {})


def query_enzyme_class_ref_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query enzyme class reference by date modified range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of enzyme class reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.enzyme_class_ref.get_by_date_modified_range(start_date, end_date, options or {})


def query_enzyme_class_ref_by_keyword(keyword: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search enzyme class reference by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of enzyme class reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.enzyme_class_ref.search_by_keyword(keyword, options or {})


def query_enzyme_class_ref_all(options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all enzyme class reference data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all enzyme class reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.enzyme_class_ref.get_all(options or {})
