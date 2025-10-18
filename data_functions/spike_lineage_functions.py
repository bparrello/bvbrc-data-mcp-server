"""
BV-BRC Spike Lineage Functions

This module provides wrapper functions for the BV-BRC Solr API spike_lineage resource,
exposing spike lineage querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_spike_lineage_by_id(id: str, options: Dict[str, Any] = None,
                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query spike lineage by ID.
    
    Args:
        id: The ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of spike lineage records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.spike_lineage.get_by_id(id, options or {})


def query_spike_lineage_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query spike lineage by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of spike lineage records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.spike_lineage.query_by(filters, options or {})


def query_spike_lineage_by_country(country: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query spike lineage by country.
    
    Args:
        country: The country to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of spike lineage records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.spike_lineage.get_by_country(country, options or {})


def query_spike_lineage_by_growth_rate(growth_rate: float, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query spike lineage by growth rate.
    
    Args:
        growth_rate: The growth rate to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of spike lineage records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.spike_lineage.get_by_growth_rate(growth_rate, options or {})


def query_spike_lineage_by_lineage(lineage: str, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query spike lineage by lineage.
    
    Args:
        lineage: The lineage to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of spike lineage records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.spike_lineage.get_by_lineage(lineage, options or {})


def query_spike_lineage_by_lineage_count(lineage_count: int, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query spike lineage by lineage count.
    
    Args:
        lineage_count: The lineage count to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of spike lineage records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.spike_lineage.get_by_lineage_count(lineage_count, options or {})


def query_spike_lineage_by_lineage_of_concern(lineage_of_concern: str, options: Dict[str, Any] = None,
                                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query spike lineage by lineage of concern.
    
    Args:
        lineage_of_concern: The lineage of concern to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of spike lineage records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.spike_lineage.get_by_lineage_of_concern(lineage_of_concern, options or {})


def query_spike_lineage_by_month(month: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query spike lineage by month.
    
    Args:
        month: The month to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of spike lineage records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.spike_lineage.get_by_month(month, options or {})


def query_spike_lineage_by_prevalence(prevalence: float, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query spike lineage by prevalence.
    
    Args:
        prevalence: The prevalence to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of spike lineage records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.spike_lineage.get_by_prevalence(prevalence, options or {})


def query_spike_lineage_by_region(region: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query spike lineage by region.
    
    Args:
        region: The region to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of spike lineage records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.spike_lineage.get_by_region(region, options or {})


def query_spike_lineage_by_sequence_features(sequence_features: str, options: Dict[str, Any] = None,
                                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query spike lineage by sequence features.
    
    Args:
        sequence_features: The sequence features to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of spike lineage records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.spike_lineage.get_by_sequence_features(sequence_features, options or {})


def query_spike_lineage_by_total_isolates(total_isolates: int, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query spike lineage by total isolates.
    
    Args:
        total_isolates: The total isolates to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of spike lineage records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.spike_lineage.get_by_total_isolates(total_isolates, options or {})


def query_spike_lineage_by_growth_rate_range(min_growth_rate: float, max_growth_rate: float, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query spike lineage by growth rate range.
    
    Args:
        min_growth_rate: Minimum growth rate
        max_growth_rate: Maximum growth rate
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of spike lineage records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.spike_lineage.get_by_growth_rate_range(min_growth_rate, max_growth_rate, options or {})


def query_spike_lineage_by_lineage_count_range(min_lineage_count: int, max_lineage_count: int, options: Dict[str, Any] = None,
                                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query spike lineage by lineage count range.
    
    Args:
        min_lineage_count: Minimum lineage count
        max_lineage_count: Maximum lineage count
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of spike lineage records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.spike_lineage.get_by_lineage_count_range(min_lineage_count, max_lineage_count, options or {})


def query_spike_lineage_by_prevalence_range(min_prevalence: float, max_prevalence: float, options: Dict[str, Any] = None,
                                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query spike lineage by prevalence range.
    
    Args:
        min_prevalence: Minimum prevalence
        max_prevalence: Maximum prevalence
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of spike lineage records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.spike_lineage.get_by_prevalence_range(min_prevalence, max_prevalence, options or {})


def query_spike_lineage_by_total_isolates_range(min_total_isolates: int, max_total_isolates: int, options: Dict[str, Any] = None,
                                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query spike lineage by total isolates range.
    
    Args:
        min_total_isolates: Minimum total isolates
        max_total_isolates: Maximum total isolates
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of spike lineage records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.spike_lineage.get_by_total_isolates_range(min_total_isolates, max_total_isolates, options or {})


def query_spike_lineage_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query spike lineage by date inserted range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of spike lineage records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.spike_lineage.get_by_date_inserted_range(start_date, end_date, options or {})


def query_spike_lineage_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query spike lineage by date modified range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of spike lineage records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.spike_lineage.get_by_date_modified_range(start_date, end_date, options or {})


def query_spike_lineage_by_keyword(keyword: str, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search spike lineage by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of spike lineage records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.spike_lineage.search_by_keyword(keyword, options or {})


def query_spike_lineage_all(options: Dict[str, Any] = None,
                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all spike lineage data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all spike lineage records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.spike_lineage.get_all(options or {})
