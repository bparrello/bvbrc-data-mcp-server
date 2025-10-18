"""
BV-BRC Strain Functions

This module provides wrapper functions for the BV-BRC Solr API strain resource,
exposing strain querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_strain_by_id(id: str, options: Dict[str, Any] = None,
                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query strain by ID.
    
    Args:
        id: The ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.get_by_id(id, options or {})


def query_strain_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query strain by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.query_by(filters, options or {})


def query_strain_by_collection_date(collection_date: str, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query strain by collection date.
    
    Args:
        collection_date: The collection date to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.get_by_collection_date(collection_date, options or {})


def query_strain_by_collection_year(collection_year: int, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query strain by collection year.
    
    Args:
        collection_year: The collection year to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.get_by_collection_year(collection_year, options or {})


def query_strain_by_family(family: str, options: Dict[str, Any] = None,
                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query strain by family.
    
    Args:
        family: The family to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.get_by_family(family, options or {})


def query_strain_by_genus(genus: str, options: Dict[str, Any] = None,
                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query strain by genus.
    
    Args:
        genus: The genus to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.get_by_genus(genus, options or {})


def query_strain_by_species(species: str, options: Dict[str, Any] = None,
                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query strain by species.
    
    Args:
        species: The species to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.get_by_species(species, options or {})


def query_strain_by_strain(strain: str, options: Dict[str, Any] = None,
                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query strain by strain name.
    
    Args:
        strain: The strain name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.get_by_strain(strain, options or {})


def query_strain_by_subtype(subtype: str, options: Dict[str, Any] = None,
                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query strain by subtype.
    
    Args:
        subtype: The subtype to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.get_by_subtype(subtype, options or {})


def query_strain_by_taxon_id(taxon_id: int, options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query strain by taxon ID.
    
    Args:
        taxon_id: The taxon ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.get_by_taxon_id(taxon_id, options or {})


def query_strain_by_geographic_group(geographic_group: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query strain by geographic group.
    
    Args:
        geographic_group: The geographic group to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.get_by_geographic_group(geographic_group, options or {})


def query_strain_by_isolation_country(isolation_country: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query strain by isolation country.
    
    Args:
        isolation_country: The isolation country to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.get_by_isolation_country(isolation_country, options or {})


def query_strain_by_host_common_name(host_common_name: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query strain by host common name.
    
    Args:
        host_common_name: The host common name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.get_by_host_common_name(host_common_name, options or {})


def query_strain_by_host_group(host_group: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query strain by host group.
    
    Args:
        host_group: The host group to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.get_by_host_group(host_group, options or {})


def query_strain_by_host_name(host_name: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query strain by host name.
    
    Args:
        host_name: The host name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.get_by_host_name(host_name, options or {})


def query_strain_by_lab_host(lab_host: str, options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query strain by lab host.
    
    Args:
        lab_host: The lab host to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.get_by_lab_host(lab_host, options or {})


def query_strain_by_owner(owner: str, options: Dict[str, Any] = None,
                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query strain by owner.
    
    Args:
        owner: The owner to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.get_by_owner(owner, options or {})


def query_strain_by_status(status: str, options: Dict[str, Any] = None,
                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query strain by status.
    
    Args:
        status: The status to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.get_by_status(status, options or {})


def query_strain_by_public(is_public: bool, options: Dict[str, Any] = None,
                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query strain by public status.
    
    Args:
        is_public: The public status to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.get_by_public(is_public, options or {})


def query_strain_by_collection_year_range(start_year: int, end_year: int, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query strain by collection year range.
    
    Args:
        start_year: Start year
        end_year: End year
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.get_by_collection_year_range(start_year, end_year, options or {})


def query_strain_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query strain by date inserted range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.get_by_date_inserted_range(start_date, end_date, options or {})


def query_strain_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query strain by date modified range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.get_by_date_modified_range(start_date, end_date, options or {})


def query_strain_by_h_type_range(min_h_type: int, max_h_type: int, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query strain by H type range.
    
    Args:
        min_h_type: Minimum H type
        max_h_type: Maximum H type
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.get_by_h_type_range(min_h_type, max_h_type, options or {})


def query_strain_by_n_type_range(min_n_type: int, max_n_type: int, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query strain by N type range.
    
    Args:
        min_n_type: Minimum N type
        max_n_type: Maximum N type
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.get_by_n_type_range(min_n_type, max_n_type, options or {})


def query_strain_by_segment_count_range(min_segment_count: int, max_segment_count: int, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query strain by segment count range.
    
    Args:
        min_segment_count: Minimum segment count
        max_segment_count: Maximum segment count
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.get_by_segment_count_range(min_segment_count, max_segment_count, options or {})


def query_strain_by_taxon_id_range(min_taxon_id: int, max_taxon_id: int, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query strain by taxon ID range.
    
    Args:
        min_taxon_id: Minimum taxon ID
        max_taxon_id: Maximum taxon ID
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.get_by_taxon_id_range(min_taxon_id, max_taxon_id, options or {})


def query_strain_by_keyword(keyword: str, options: Dict[str, Any] = None,
                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search strain by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.search_by_keyword(keyword, options or {})


def query_strain_all(options: Dict[str, Any] = None,
                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all strain data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all strain records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.strain.get_all(options or {})
