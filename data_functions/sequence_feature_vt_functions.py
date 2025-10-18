"""
BV-BRC Sequence Feature VT Functions

This module provides wrapper functions for the BV-BRC Solr API sequence_feature_vt resource,
exposing sequence feature VT querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_sequence_feature_vt_by_id(id: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature VT by ID.
    
    Args:
        id: The ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature VT records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature_vt.get_by_id(id, options or {})


def query_sequence_feature_vt_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature VT by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature VT records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature_vt.query_by(filters, options or {})


def query_sequence_feature_vt_by_sf_category(sf_category: str, options: Dict[str, Any] = None,
                                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature VT by SF category.
    
    Args:
        sf_category: The SF category to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature VT records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature_vt.get_by_sf_category(sf_category, options or {})


def query_sequence_feature_vt_by_genome_id(genome_id: str, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature VT by genome ID.
    
    Args:
        genome_id: The genome ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature VT records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature_vt.get_by_genome_id(genome_id, options or {})


def query_sequence_feature_vt_by_taxon_id(taxon_id: int, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature VT by taxon ID.
    
    Args:
        taxon_id: The taxon ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature VT records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature_vt.get_by_taxon_id(taxon_id, options or {})


def query_sequence_feature_vt_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature VT by date inserted range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature VT records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature_vt.get_by_date_inserted_range(start_date, end_date, options or {})


def query_sequence_feature_vt_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query sequence feature VT by date modified range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature VT records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature_vt.get_by_date_modified_range(start_date, end_date, options or {})


def query_sequence_feature_vt_by_keyword(keyword: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search sequence feature VT by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of sequence feature VT records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature_vt.search_by_keyword(keyword, options or {})


def query_sequence_feature_vt_all(options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all sequence feature VT data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all sequence feature VT records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.sequence_feature_vt.get_all(options or {})
