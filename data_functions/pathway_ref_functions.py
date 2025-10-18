"""
BV-BRC Pathway Reference Functions

This module provides wrapper functions for the BV-BRC Solr API pathway_ref resource,
exposing pathway reference querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_pathway_ref_by_id(id: str, options: Dict[str, Any] = None,
                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway reference by ID.
    
    Args:
        id: The ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway_ref.get_by_id(id, options or {})


def query_pathway_ref_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway reference by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway_ref.query_by(filters, options or {})


def query_pathway_ref_by_ec_number(ec_number: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway reference by EC number.
    
    Args:
        ec_number: The EC number to query (e.g., "1.1.1.1")
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway_ref.get_by_ec_number(ec_number, options or {})


def query_pathway_ref_by_ec_description(ec_description: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway reference by EC description.
    
    Args:
        ec_description: The EC description to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway_ref.get_by_ec_description(ec_description, options or {})


def query_pathway_ref_by_map_location(map_location: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway reference by map location.
    
    Args:
        map_location: The map location to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway_ref.get_by_map_location(map_location, options or {})


def query_pathway_ref_by_map_name(map_name: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway reference by map name.
    
    Args:
        map_name: The map name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway_ref.get_by_map_name(map_name, options or {})


def query_pathway_ref_by_map_type(map_type: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway reference by map type.
    
    Args:
        map_type: The map type to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway_ref.get_by_map_type(map_type, options or {})


def query_pathway_ref_by_occurrence(occurrence: int, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway reference by occurrence.
    
    Args:
        occurrence: The occurrence to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway_ref.get_by_occurrence(occurrence, options or {})


def query_pathway_ref_by_pathway_class(pathway_class: str, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway reference by pathway class.
    
    Args:
        pathway_class: The pathway class to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway_ref.get_by_pathway_class(pathway_class, options or {})


def query_pathway_ref_by_pathway_id(pathway_id: str, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway reference by pathway ID.
    
    Args:
        pathway_id: The pathway ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway_ref.get_by_pathway_id(pathway_id, options or {})


def query_pathway_ref_by_pathway_name(pathway_name: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway reference by pathway name.
    
    Args:
        pathway_name: The pathway name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway_ref.get_by_pathway_name(pathway_name, options or {})


def query_pathway_ref_by_occurrence_range(min_occurrence: int, max_occurrence: int, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway reference by occurrence range.
    
    Args:
        min_occurrence: Minimum occurrence
        max_occurrence: Maximum occurrence
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway_ref.get_by_occurrence_range(min_occurrence, max_occurrence, options or {})


def query_pathway_ref_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway reference by date inserted range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway_ref.get_by_date_inserted_range(start_date, end_date, options or {})


def query_pathway_ref_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query pathway reference by date modified range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway_ref.get_by_date_modified_range(start_date, end_date, options or {})


def query_pathway_ref_by_keyword(keyword: str, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search pathway reference by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of pathway reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway_ref.search_by_keyword(keyword, options or {})


def query_pathway_ref_all(options: Dict[str, Any] = None,
                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all pathway reference data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all pathway reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.pathway_ref.get_all(options or {})
