"""
BV-BRC Serology Functions

This module provides wrapper functions for the BV-BRC Solr API serology resource,
exposing serology querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_serology_by_id(id: str, options: Dict[str, Any] = None,
                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by ID.
    
    Args:
        id: The ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_id(id, options or {})


def query_serology_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.query_by(filters, options or {})


def query_serology_by_additional_metadata(additional_metadata: str, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by additional metadata.
    
    Args:
        additional_metadata: The additional metadata to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_additional_metadata(additional_metadata, options or {})


def query_serology_by_collection_city(collection_city: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by collection city.
    
    Args:
        collection_city: The collection city to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_collection_city(collection_city, options or {})


def query_serology_by_collection_country(collection_country: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by collection country.
    
    Args:
        collection_country: The collection country to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_collection_country(collection_country, options or {})


def query_serology_by_collection_state(collection_state: str, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by collection state.
    
    Args:
        collection_state: The collection state to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_collection_state(collection_state, options or {})


def query_serology_by_collection_year(collection_year: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by collection year.
    
    Args:
        collection_year: The collection year to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_collection_year(collection_year, options or {})


def query_serology_by_comments(comments: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by comments.
    
    Args:
        comments: The comments to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_comments(comments, options or {})


def query_serology_by_contributing_institution(contributing_institution: str, options: Dict[str, Any] = None,
                                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by contributing institution.
    
    Args:
        contributing_institution: The contributing institution to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_contributing_institution(contributing_institution, options or {})


def query_serology_by_genbank_accession(genbank_accession: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by GenBank accession.
    
    Args:
        genbank_accession: The GenBank accession to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_genbank_accession(genbank_accession, options or {})


def query_serology_by_geographic_group(geographic_group: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by geographic group.
    
    Args:
        geographic_group: The geographic group to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_geographic_group(geographic_group, options or {})


def query_serology_by_host_age(host_age: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by host age.
    
    Args:
        host_age: The host age to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_host_age(host_age, options or {})


def query_serology_by_host_age_group(host_age_group: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by host age group.
    
    Args:
        host_age_group: The host age group to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_host_age_group(host_age_group, options or {})


def query_serology_by_host_common_name(host_common_name: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by host common name.
    
    Args:
        host_common_name: The host common name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_host_common_name(host_common_name, options or {})


def query_serology_by_host_health(host_health: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by host health.
    
    Args:
        host_health: The host health to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_host_health(host_health, options or {})


def query_serology_by_host_identifier(host_identifier: str, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by host identifier.
    
    Args:
        host_identifier: The host identifier to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_host_identifier(host_identifier, options or {})


def query_serology_by_host_sex(host_sex: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by host sex.
    
    Args:
        host_sex: The host sex to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_host_sex(host_sex, options or {})


def query_serology_by_host_species(host_species: str, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by host species.
    
    Args:
        host_species: The host species to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_host_species(host_species, options or {})


def query_serology_by_host_type(host_type: str, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by host type.
    
    Args:
        host_type: The host type to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_host_type(host_type, options or {})


def query_serology_by_positive_definition(positive_definition: str, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by positive definition.
    
    Args:
        positive_definition: The positive definition to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_positive_definition(positive_definition, options or {})


def query_serology_by_project_identifier(project_identifier: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by project identifier.
    
    Args:
        project_identifier: The project identifier to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_project_identifier(project_identifier, options or {})


def query_serology_by_sample_accession(sample_accession: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by sample accession.
    
    Args:
        sample_accession: The sample accession to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_sample_accession(sample_accession, options or {})


def query_serology_by_sample_identifier(sample_identifier: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by sample identifier.
    
    Args:
        sample_identifier: The sample identifier to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_sample_identifier(sample_identifier, options or {})


def query_serology_by_serotype(serotype: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by serotype.
    
    Args:
        serotype: The serotype to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_serotype(serotype, options or {})


def query_serology_by_strain(strain: str, options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by strain.
    
    Args:
        strain: The strain to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_strain(strain, options or {})


def query_serology_by_taxon_lineage_id(taxon_lineage_id: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by taxon lineage ID.
    
    Args:
        taxon_lineage_id: The taxon lineage ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_taxon_lineage_id(taxon_lineage_id, options or {})


def query_serology_by_test_antigen(test_antigen: str, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by test antigen.
    
    Args:
        test_antigen: The test antigen to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_test_antigen(test_antigen, options or {})


def query_serology_by_test_interpretation(test_interpretation: str, options: Dict[str, Any] = None,
                                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by test interpretation.
    
    Args:
        test_interpretation: The test interpretation to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_test_interpretation(test_interpretation, options or {})


def query_serology_by_test_pathogen(test_pathogen: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by test pathogen.
    
    Args:
        test_pathogen: The test pathogen to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_test_pathogen(test_pathogen, options or {})


def query_serology_by_test_result(test_result: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by test result.
    
    Args:
        test_result: The test result to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_test_result(test_result, options or {})


def query_serology_by_test_type(test_type: str, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by test type.
    
    Args:
        test_type: The test type to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_test_type(test_type, options or {})


def query_serology_by_virus_identifier(virus_identifier: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by virus identifier.
    
    Args:
        virus_identifier: The virus identifier to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_virus_identifier(virus_identifier, options or {})


def query_serology_by_collection_date_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by collection date range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_collection_date_range(start_date, end_date, options or {})


def query_serology_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by date inserted range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_date_inserted_range(start_date, end_date, options or {})


def query_serology_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query serology by date modified range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_by_date_modified_range(start_date, end_date, options or {})


def query_serology_by_keyword(keyword: str, options: Dict[str, Any] = None,
                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search serology by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.search_by_keyword(keyword, options or {})


def query_serology_all(options: Dict[str, Any] = None,
                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all serology data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all serology records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.serology.get_all(options or {})
