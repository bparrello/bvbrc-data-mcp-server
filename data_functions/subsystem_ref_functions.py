"""
BV-BRC Subsystem Reference Functions

This module provides wrapper functions for the BV-BRC Solr API subsystem_ref resource,
exposing subsystem reference querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_subsystem_ref_by_id(id: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem reference by ID.
    
    Args:
        id: The ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem_ref.get_by_id(id, options or {})


def query_subsystem_ref_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem reference by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem_ref.query_by(filters, options or {})


def query_subsystem_ref_by_class(class_name: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem reference by class.
    
    Args:
        class_name: The class to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem_ref.get_by_class(class_name, options or {})


def query_subsystem_ref_by_description(description: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem reference by description.
    
    Args:
        description: The description to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem_ref.get_by_description(description, options or {})


def query_subsystem_ref_by_role(role: str, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem reference by role.
    
    Args:
        role: The role to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem_ref.get_by_role(role, options or {})


def query_subsystem_ref_by_role_id(role_id: str, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem reference by role ID.
    
    Args:
        role_id: The role ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem_ref.get_by_role_id(role_id, options or {})


def query_subsystem_ref_by_subsystem_id(subsystem_id: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem reference by subsystem ID.
    
    Args:
        subsystem_id: The subsystem ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem_ref.get_by_subsystem_id(subsystem_id, options or {})


def query_subsystem_ref_by_subsystem_name(subsystem_name: str, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem reference by subsystem name.
    
    Args:
        subsystem_name: The subsystem name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem_ref.get_by_subsystem_name(subsystem_name, options or {})


def query_subsystem_ref_by_superclass(superclass: str, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem reference by superclass.
    
    Args:
        superclass: The superclass to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem_ref.get_by_superclass(superclass, options or {})


def query_subsystem_ref_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem reference by date inserted range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem_ref.get_by_date_inserted_range(start_date, end_date, options or {})


def query_subsystem_ref_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem reference by date modified range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem_ref.get_by_date_modified_range(start_date, end_date, options or {})


def query_subsystem_ref_by_keyword(keyword: str, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search subsystem reference by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem_ref.search_by_keyword(keyword, options or {})


def query_subsystem_ref_all(options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all subsystem reference data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all subsystem reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem_ref.get_all(options or {})
