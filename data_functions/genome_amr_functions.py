"""
BV-BRC Genome AMR Functions

This module provides wrapper functions for the BV-BRC Solr API genome_amr resource,
exposing genome antimicrobial resistance querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_genome_amr_by_id(id: str, options: Dict[str, Any] = None,
                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome AMR by ID.
    
    Args:
        id: The AMR record ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.get_by_id(id, options or {})


def query_genome_amr_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome AMR by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.query_by(filters, options or {})


def query_genome_amr_by_antibiotic(antibiotic: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome AMR by antibiotic.
    
    Args:
        antibiotic: The antibiotic to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.get_by_antibiotic(antibiotic, options or {})


def query_genome_amr_by_computational_method(computational_method: str, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome AMR by computational method.
    
    Args:
        computational_method: The computational method to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.get_by_computational_method(computational_method, options or {})


def query_genome_amr_by_computational_method_version(computational_method_version: str, options: Dict[str, Any] = None,
                                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome AMR by computational method version.
    
    Args:
        computational_method_version: The computational method version to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.get_by_computational_method_version(computational_method_version, options or {})


def query_genome_amr_by_evidence(evidence: str, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome AMR by evidence.
    
    Args:
        evidence: The evidence to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.get_by_evidence(evidence, options or {})


def query_genome_amr_by_genome_id(genome_id: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome AMR by genome ID.
    
    Args:
        genome_id: The genome ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.get_by_genome_id(genome_id, options or {})


def query_genome_amr_by_genome_name(genome_name: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome AMR by genome name.
    
    Args:
        genome_name: The genome name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.get_by_genome_name(genome_name, options or {})


def query_genome_amr_by_laboratory_typing_method(laboratory_typing_method: str, options: Dict[str, Any] = None,
                                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome AMR by laboratory typing method.
    
    Args:
        laboratory_typing_method: The laboratory typing method to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.get_by_laboratory_typing_method(laboratory_typing_method, options or {})


def query_genome_amr_by_laboratory_typing_method_version(laboratory_typing_method_version: str, options: Dict[str, Any] = None,
                                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome AMR by laboratory typing method version.
    
    Args:
        laboratory_typing_method_version: The laboratory typing method version to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.get_by_laboratory_typing_method_version(laboratory_typing_method_version, options or {})


def query_genome_amr_by_laboratory_typing_platform(laboratory_typing_platform: str, options: Dict[str, Any] = None,
                                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome AMR by laboratory typing platform.
    
    Args:
        laboratory_typing_platform: The laboratory typing platform to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.get_by_laboratory_typing_platform(laboratory_typing_platform, options or {})


def query_genome_amr_by_measurement(measurement: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome AMR by measurement.
    
    Args:
        measurement: The measurement to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.get_by_measurement(measurement, options or {})


def query_genome_amr_by_measurement_sign(measurement_sign: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome AMR by measurement sign.
    
    Args:
        measurement_sign: The measurement sign to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.get_by_measurement_sign(measurement_sign, options or {})


def query_genome_amr_by_measurement_unit(measurement_unit: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome AMR by measurement unit.
    
    Args:
        measurement_unit: The measurement unit to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.get_by_measurement_unit(measurement_unit, options or {})


def query_genome_amr_by_measurement_value(measurement_value: str, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome AMR by measurement value.
    
    Args:
        measurement_value: The measurement value to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.get_by_measurement_value(measurement_value, options or {})


def query_genome_amr_by_owner(owner: str, options: Dict[str, Any] = None,
                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome AMR by owner.
    
    Args:
        owner: The owner to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.get_by_owner(owner, options or {})


def query_genome_amr_by_pmid(pmid: int, options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome AMR by PMID.
    
    Args:
        pmid: The PMID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.get_by_pmid(pmid, options or {})


def query_genome_amr_by_public_status(is_public: bool, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome AMR by public status.
    
    Args:
        is_public: The public status to query (True/False)
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.get_by_public_status(is_public, options or {})


def query_genome_amr_by_resistant_phenotype(resistant_phenotype: str, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome AMR by resistant phenotype.
    
    Args:
        resistant_phenotype: The resistant phenotype to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.get_by_resistant_phenotype(resistant_phenotype, options or {})


def query_genome_amr_by_source(source: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome AMR by source.
    
    Args:
        source: The source to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.get_by_source(source, options or {})


def query_genome_amr_by_taxon_id(taxon_id: int, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome AMR by taxon ID.
    
    Args:
        taxon_id: The taxon ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.get_by_taxon_id(taxon_id, options or {})


def query_genome_amr_by_testing_standard(testing_standard: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome AMR by testing standard.
    
    Args:
        testing_standard: The testing standard to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.get_by_testing_standard(testing_standard, options or {})


def query_genome_amr_by_testing_standard_year(testing_standard_year: int, options: Dict[str, Any] = None,
                                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome AMR by testing standard year.
    
    Args:
        testing_standard_year: The testing standard year to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.get_by_testing_standard_year(testing_standard_year, options or {})


def query_genome_amr_by_vendor(vendor: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome AMR by vendor.
    
    Args:
        vendor: The vendor to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.get_by_vendor(vendor, options or {})


def query_genome_amr_by_date_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome AMR by date range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.get_by_date_range(start_date, end_date, options or {})


def query_genome_amr_by_modified_date_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome AMR by modified date range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.get_by_modified_date_range(start_date, end_date, options or {})


def query_genome_amr_by_keyword(keyword: str, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search genome AMR by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.search_by_keyword(keyword, options or {})


def query_genome_amr_all(options: Dict[str, Any] = None,
                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all genome AMR data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all genome AMR records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_amr.get_all(options or {})
