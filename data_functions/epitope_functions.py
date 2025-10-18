"""
BV-BRC Epitope Functions

This module provides wrapper functions for the BV-BRC Solr API epitope resource,
exposing epitope querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_epitope_by_id(epitope_id: str, options: Dict[str, Any] = None,
                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope by epitope ID.
    
    Args:
        epitope_id: The epitope ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope.get_by_id(epitope_id, options or {})


def query_epitope_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope.query_by(filters, options or {})


def query_epitope_by_epitope_sequence(epitope_sequence: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope by epitope sequence.
    
    Args:
        epitope_sequence: The epitope sequence to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope.get_by_epitope_sequence(epitope_sequence, options or {})


def query_epitope_by_epitope_type(epitope_type: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope by epitope type.
    
    Args:
        epitope_type: The epitope type to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope.get_by_epitope_type(epitope_type, options or {})


def query_epitope_by_host_name(host_name: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope by host name.
    
    Args:
        host_name: The host name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope.get_by_host_name(host_name, options or {})


def query_epitope_by_organism(organism: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope by organism.
    
    Args:
        organism: The organism to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope.get_by_organism(organism, options or {})


def query_epitope_by_protein_accession(protein_accession: str, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope by protein accession.
    
    Args:
        protein_accession: The protein accession to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope.get_by_protein_accession(protein_accession, options or {})


def query_epitope_by_protein_id(protein_id: str, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope by protein ID.
    
    Args:
        protein_id: The protein ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope.get_by_protein_id(protein_id, options or {})


def query_epitope_by_protein_name(protein_name: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope by protein name.
    
    Args:
        protein_name: The protein name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope.get_by_protein_name(protein_name, options or {})


def query_epitope_by_start(start: int, options: Dict[str, Any] = None,
                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope by start position.
    
    Args:
        start: The start position to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope.get_by_start(start, options or {})


def query_epitope_by_end(end: int, options: Dict[str, Any] = None,
                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope by end position.
    
    Args:
        end: The end position to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope.get_by_end(end, options or {})


def query_epitope_by_taxon_id(taxon_id: int, options: Dict[str, Any] = None,
                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope by taxon ID.
    
    Args:
        taxon_id: The taxon ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope.get_by_taxon_id(taxon_id, options or {})


def query_epitope_by_bcell_assays(bcell_assays: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope by B-cell assays.
    
    Args:
        bcell_assays: The B-cell assays to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope.get_by_bcell_assays(bcell_assays, options or {})


def query_epitope_by_mhc_assays(mhc_assays: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope by MHC assays.
    
    Args:
        mhc_assays: The MHC assays to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope.get_by_mhc_assays(mhc_assays, options or {})


def query_epitope_by_tcell_assays(tcell_assays: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope by T-cell assays.
    
    Args:
        tcell_assays: The T-cell assays to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope.get_by_tcell_assays(tcell_assays, options or {})


def query_epitope_by_total_assays(total_assays: int, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope by total assays.
    
    Args:
        total_assays: The total assays to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope.get_by_total_assays(total_assays, options or {})


def query_epitope_by_comment(comment: str, options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope by comment.
    
    Args:
        comment: The comment to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope.get_by_comment(comment, options or {})


def query_epitope_by_assay_result(assay_result: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope by assay result.
    
    Args:
        assay_result: The assay result to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope.get_by_assay_result(assay_result, options or {})


def query_epitope_by_taxon_lineage_id(taxon_lineage_id: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope by taxon lineage ID.
    
    Args:
        taxon_lineage_id: The taxon lineage ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope.get_by_taxon_lineage_id(taxon_lineage_id, options or {})


def query_epitope_by_taxon_lineage_name(taxon_lineage_name: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope by taxon lineage name.
    
    Args:
        taxon_lineage_name: The taxon lineage name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope.get_by_taxon_lineage_name(taxon_lineage_name, options or {})


def query_epitope_by_position_range(min_start: int, max_end: int, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope by position range.
    
    Args:
        min_start: Minimum start position
        max_end: Maximum end position
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope.get_by_position_range(min_start, max_end, options or {})


def query_epitope_by_total_assays_range(min_assays: int, max_assays: int, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope by total assays range.
    
    Args:
        min_assays: Minimum total assays
        max_assays: Maximum total assays
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope.get_by_total_assays_range(min_assays, max_assays, options or {})


def query_epitope_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope by date inserted range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope.get_by_date_inserted_range(start_date, end_date, options or {})


def query_epitope_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope by date modified range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope.get_by_date_modified_range(start_date, end_date, options or {})


def query_epitope_by_keyword(keyword: str, options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search epitope by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope.search_by_keyword(keyword, options or {})


def query_epitope_all(options: Dict[str, Any] = None,
                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all epitope data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all epitope records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope.get_all(options or {})
