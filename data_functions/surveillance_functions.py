"""
BV-BRC Surveillance Functions

This module provides wrapper functions for the BV-BRC Solr API surveillance resource,
exposing surveillance querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_surveillance_by_id(id: str, options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query surveillance by ID.
    
    Args:
        id: The ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.get_by_id(id, options or {})


def query_surveillance_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query surveillance by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.query_by(filters, options or {})


def query_surveillance_by_host_species(host_species: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query surveillance by host species.
    
    Args:
        host_species: The host species to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.get_by_host_species(host_species, options or {})


def query_surveillance_by_host_common_name(host_common_name: str, options: Dict[str, Any] = None,
                                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query surveillance by host common name.
    
    Args:
        host_common_name: The host common name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.get_by_host_common_name(host_common_name, options or {})


def query_surveillance_by_sample_identifier(sample_identifier: str, options: Dict[str, Any] = None,
                                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query surveillance by sample identifier.
    
    Args:
        sample_identifier: The sample identifier to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.get_by_sample_identifier(sample_identifier, options or {})


def query_surveillance_by_sample_accession(sample_accession: str, options: Dict[str, Any] = None,
                                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query surveillance by sample accession.
    
    Args:
        sample_accession: The sample accession to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.get_by_sample_accession(sample_accession, options or {})


def query_surveillance_by_collection_country(collection_country: str, options: Dict[str, Any] = None,
                                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query surveillance by collection country.
    
    Args:
        collection_country: The collection country to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.get_by_collection_country(collection_country, options or {})


def query_surveillance_by_collection_city(collection_city: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query surveillance by collection city.
    
    Args:
        collection_city: The collection city to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.get_by_collection_city(collection_city, options or {})


def query_surveillance_by_collection_year(collection_year: str, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query surveillance by collection year.
    
    Args:
        collection_year: The collection year to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.get_by_collection_year(collection_year, options or {})


def query_surveillance_by_species(species: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query surveillance by species.
    
    Args:
        species: The species to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.get_by_species(species, options or {})


def query_surveillance_by_strain(strain: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query surveillance by strain.
    
    Args:
        strain: The strain to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.get_by_strain(strain, options or {})


def query_surveillance_by_subtype(subtype: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query surveillance by subtype.
    
    Args:
        subtype: The subtype to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.get_by_subtype(subtype, options or {})


def query_surveillance_by_pathogen_type(pathogen_type: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query surveillance by pathogen type.
    
    Args:
        pathogen_type: The pathogen type to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.get_by_pathogen_type(pathogen_type, options or {})


def query_surveillance_by_genome_id(genome_id: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query surveillance by genome ID.
    
    Args:
        genome_id: The genome ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.get_by_genome_id(genome_id, options or {})


def query_surveillance_by_disease_status(disease_status: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query surveillance by disease status.
    
    Args:
        disease_status: The disease status to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.get_by_disease_status(disease_status, options or {})


def query_surveillance_by_diagnosis(diagnosis: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query surveillance by diagnosis.
    
    Args:
        diagnosis: The diagnosis to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.get_by_diagnosis(diagnosis, options or {})


def query_surveillance_by_treatment(treatment: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query surveillance by treatment.
    
    Args:
        treatment: The treatment to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.get_by_treatment(treatment, options or {})


def query_surveillance_by_hospitalized(hospitalized: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query surveillance by hospitalized status.
    
    Args:
        hospitalized: The hospitalized status to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.get_by_hospitalized(hospitalized, options or {})


def query_surveillance_by_vaccination_type(vaccination_type: str, options: Dict[str, Any] = None,
                                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query surveillance by vaccination type.
    
    Args:
        vaccination_type: The vaccination type to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.get_by_vaccination_type(vaccination_type, options or {})


def query_surveillance_by_exposure(exposure: str, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query surveillance by exposure.
    
    Args:
        exposure: The exposure to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.get_by_exposure(exposure, options or {})


def query_surveillance_by_pathogen_test_type(pathogen_test_type: str, options: Dict[str, Any] = None,
                                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query surveillance by pathogen test type.
    
    Args:
        pathogen_test_type: The pathogen test type to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.get_by_pathogen_test_type(pathogen_test_type, options or {})


def query_surveillance_by_pathogen_test_result(pathogen_test_result: str, options: Dict[str, Any] = None,
                                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query surveillance by pathogen test result.
    
    Args:
        pathogen_test_result: The pathogen test result to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.get_by_pathogen_test_result(pathogen_test_result, options or {})


def query_surveillance_by_collection_date_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query surveillance by collection date range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.get_by_collection_date_range(start_date, end_date, options or {})


def query_surveillance_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query surveillance by date inserted range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.get_by_date_inserted_range(start_date, end_date, options or {})


def query_surveillance_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query surveillance by date modified range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.get_by_date_modified_range(start_date, end_date, options or {})


def query_surveillance_by_keyword(keyword: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search surveillance by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.search_by_keyword(keyword, options or {})


def query_surveillance_all(options: Dict[str, Any] = None,
                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all surveillance data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all surveillance records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.surveillance.get_all(options or {})
