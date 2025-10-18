"""
BV-BRC Antibiotics Functions

This module provides antibiotics querying functions for the BV-BRC Solr API.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_antibiotics_by_pubchem_cid(pubchem_cid: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query antibiotics by PubChem CID.
    
    Args:
        pubchem_cid: The PubChem CID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of antibiotic records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.antibiotics.get_by_pubchem_cid(pubchem_cid, options or {})


def query_antibiotics_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query antibiotics by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of antibiotic records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.antibiotics.query_by(filters, options or {})


def query_antibiotics_by_keyword(keyword: str, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query antibiotics by keyword search.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of antibiotic records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.antibiotics.search_by_keyword(keyword, options or {})


def query_antibiotics_by_name(antibiotic_name: str, options: Dict[str, Any] = None,
                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query antibiotics by antibiotic name.
    
    Args:
        antibiotic_name: The antibiotic name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of antibiotic records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.antibiotics.get_by_antibiotic_name(antibiotic_name, options or {})


def query_antibiotics_by_cas_id(cas_id: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query antibiotics by CAS ID.
    
    Args:
        cas_id: The CAS ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of antibiotic records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.antibiotics.get_by_cas_id(cas_id, options or {})


def query_antibiotics_by_molecular_formula(molecular_formula: str, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query antibiotics by molecular formula.
    
    Args:
        molecular_formula: The molecular formula to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of antibiotic records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.antibiotics.get_by_molecular_formula(molecular_formula, options or {})


def query_antibiotics_by_atc_classification(atc_classification: str, options: Dict[str, Any] = None,
                                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query antibiotics by ATC classification.
    
    Args:
        atc_classification: The ATC classification to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of antibiotic records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.antibiotics.get_by_atc_classification(atc_classification, options or {})


def query_antibiotics_by_mechanism_of_action(mechanism_of_action: str, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query antibiotics by mechanism of action.
    
    Args:
        mechanism_of_action: The mechanism of action to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of antibiotic records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.antibiotics.get_by_mechanism_of_action(mechanism_of_action, options or {})


def query_antibiotics_by_pharmacological_class(pharmacological_class: str, options: Dict[str, Any] = None,
                                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query antibiotics by pharmacological class.
    
    Args:
        pharmacological_class: The pharmacological class to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of antibiotic records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.antibiotics.get_by_pharmacological_class(pharmacological_class, options or {})


def query_antibiotics_by_synonym(synonym: str, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query antibiotics by synonym.
    
    Args:
        synonym: The synonym to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of antibiotic records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.antibiotics.get_by_synonym(synonym, options or {})


def query_antibiotics_by_molecular_weight_range(min_weight: float, max_weight: float, options: Dict[str, Any] = None,
                                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query antibiotics by molecular weight range.
    
    Args:
        min_weight: Minimum molecular weight
        max_weight: Maximum molecular weight
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of antibiotic records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.antibiotics.get_by_molecular_weight_range(min_weight, max_weight, options or {})


def query_antibiotics_by_date_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query antibiotics by date range.
    
    Args:
        start_date: Start date (YYYY-MM-DD format)
        end_date: End date (YYYY-MM-DD format)
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of antibiotic records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.antibiotics.get_by_date_range(start_date, end_date, options or {})


def query_antibiotics_all(options: Dict[str, Any] = None,
                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query all antibiotics.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of antibiotic records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.antibiotics.get_all(options or {})
