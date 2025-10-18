"""
BV-BRC Miscellaneous NIAID SGC Functions

This module provides wrapper functions for the BV-BRC Solr API misc_niaid_sgc resource,
exposing miscellaneous NIAID SGC querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_misc_niaid_sgc_by_id(target_id: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query miscellaneous NIAID SGC by target ID.
    
    Args:
        target_id: The target ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of miscellaneous NIAID SGC records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.misc_niaid_sgc.get_by_id(target_id, options or {})


def query_misc_niaid_sgc_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query miscellaneous NIAID SGC by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of miscellaneous NIAID SGC records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.misc_niaid_sgc.query_by(filters, options or {})


def query_misc_niaid_sgc_by_genus(genus: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query miscellaneous NIAID SGC by genus.
    
    Args:
        genus: The genus to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of miscellaneous NIAID SGC records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.misc_niaid_sgc.get_by_genus(genus, options or {})


def query_misc_niaid_sgc_by_species(species: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query miscellaneous NIAID SGC by species.
    
    Args:
        species: The species to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of miscellaneous NIAID SGC records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.misc_niaid_sgc.get_by_species(species, options or {})


def query_misc_niaid_sgc_by_taxon_id(taxon_id: int, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query miscellaneous NIAID SGC by taxon ID.
    
    Args:
        taxon_id: The taxon ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of miscellaneous NIAID SGC records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.misc_niaid_sgc.get_by_taxon_id(taxon_id, options or {})


def query_misc_niaid_sgc_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query miscellaneous NIAID SGC by date inserted range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of miscellaneous NIAID SGC records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.misc_niaid_sgc.get_by_date_inserted_range(start_date, end_date, options or {})


def query_misc_niaid_sgc_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query miscellaneous NIAID SGC by date modified range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of miscellaneous NIAID SGC records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.misc_niaid_sgc.get_by_date_modified_range(start_date, end_date, options or {})


def query_misc_niaid_sgc_by_keyword(keyword: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search miscellaneous NIAID SGC by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of miscellaneous NIAID SGC records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.misc_niaid_sgc.search_by_keyword(keyword, options or {})


def query_misc_niaid_sgc_all(options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all miscellaneous NIAID SGC data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all miscellaneous NIAID SGC records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.misc_niaid_sgc.get_all(options or {})
