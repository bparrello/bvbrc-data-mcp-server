"""
BV-BRC Gene Ontology Reference Functions

This module provides wrapper functions for the BV-BRC Solr API gene_ontology_ref resource,
exposing gene ontology reference querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_gene_ontology_ref_by_id(go_id: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query gene ontology reference by GO ID.
    
    Args:
        go_id: The GO ID to query (e.g., "GO:0008150")
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of gene ontology reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.gene_ontology_ref.get_by_id(go_id, options or {})


def query_gene_ontology_ref_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query gene ontology reference by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of gene ontology reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.gene_ontology_ref.query_by(filters, options or {})


def query_gene_ontology_ref_by_go_name(go_name: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query gene ontology reference by GO name.
    
    Args:
        go_name: The GO name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of gene ontology reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.gene_ontology_ref.get_by_go_name(go_name, options or {})


def query_gene_ontology_ref_by_definition(definition: str, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query gene ontology reference by definition.
    
    Args:
        definition: The definition to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of gene ontology reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.gene_ontology_ref.get_by_definition(definition, options or {})


def query_gene_ontology_ref_by_ontology(ontology: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query gene ontology reference by ontology.
    
    Args:
        ontology: The ontology to query (e.g., "biological_process", "molecular_function", "cellular_component")
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of gene ontology reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.gene_ontology_ref.get_by_ontology(ontology, options or {})


def query_gene_ontology_ref_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query gene ontology reference by date inserted range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of gene ontology reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.gene_ontology_ref.get_by_date_inserted_range(start_date, end_date, options or {})


def query_gene_ontology_ref_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query gene ontology reference by date modified range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of gene ontology reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.gene_ontology_ref.get_by_date_modified_range(start_date, end_date, options or {})


def query_gene_ontology_ref_by_keyword(keyword: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search gene ontology reference by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of gene ontology reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.gene_ontology_ref.search_by_keyword(keyword, options or {})


def query_gene_ontology_ref_all(options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all gene ontology reference data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all gene ontology reference records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.gene_ontology_ref.get_all(options or {})
