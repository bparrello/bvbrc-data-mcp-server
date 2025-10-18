"""
BV-BRC Epitope Assay Functions

This module provides wrapper functions for the BV-BRC Solr API epitope_assay resource,
exposing epitope assay querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_epitope_assay_by_id(assay_id: str, options: Dict[str, Any] = None,
                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by assay ID.
    
    Args:
        assay_id: The assay ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_id(assay_id, options or {})


def query_epitope_assay_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.query_by(filters, options or {})


def query_epitope_assay_by_assay_group(assay_group: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by assay group.
    
    Args:
        assay_group: The assay group to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_assay_group(assay_group, options or {})


def query_epitope_assay_by_assay_measurement(assay_measurement: str, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by assay measurement.
    
    Args:
        assay_measurement: The assay measurement to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_assay_measurement(assay_measurement, options or {})


def query_epitope_assay_by_assay_measurement_unit(assay_measurement_unit: str, options: Dict[str, Any] = None,
                                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by assay measurement unit.
    
    Args:
        assay_measurement_unit: The assay measurement unit to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_assay_measurement_unit(assay_measurement_unit, options or {})


def query_epitope_assay_by_assay_method(assay_method: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by assay method.
    
    Args:
        assay_method: The assay method to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_assay_method(assay_method, options or {})


def query_epitope_assay_by_assay_result(assay_result: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by assay result.
    
    Args:
        assay_result: The assay result to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_assay_result(assay_result, options or {})


def query_epitope_assay_by_assay_type(assay_type: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by assay type.
    
    Args:
        assay_type: The assay type to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_assay_type(assay_type, options or {})


def query_epitope_assay_by_authors(authors: str, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by authors.
    
    Args:
        authors: The authors to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_authors(authors, options or {})


def query_epitope_assay_by_epitope_id(epitope_id: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by epitope ID.
    
    Args:
        epitope_id: The epitope ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_epitope_id(epitope_id, options or {})


def query_epitope_assay_by_epitope_sequence(epitope_sequence: str, options: Dict[str, Any] = None,
                                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by epitope sequence.
    
    Args:
        epitope_sequence: The epitope sequence to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_epitope_sequence(epitope_sequence, options or {})


def query_epitope_assay_by_epitope_type(epitope_type: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by epitope type.
    
    Args:
        epitope_type: The epitope type to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_epitope_type(epitope_type, options or {})


def query_epitope_assay_by_host_name(host_name: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by host name.
    
    Args:
        host_name: The host name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_host_name(host_name, options or {})


def query_epitope_assay_by_host_taxon_id(host_taxon_id: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by host taxon ID.
    
    Args:
        host_taxon_id: The host taxon ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_host_taxon_id(host_taxon_id, options or {})


def query_epitope_assay_by_mhc_allele(mhc_allele: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by MHC allele.
    
    Args:
        mhc_allele: The MHC allele to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_mhc_allele(mhc_allele, options or {})


def query_epitope_assay_by_mhc_allele_class(mhc_allele_class: str, options: Dict[str, Any] = None,
                                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by MHC allele class.
    
    Args:
        mhc_allele_class: The MHC allele class to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_mhc_allele_class(mhc_allele_class, options or {})


def query_epitope_assay_by_organism(organism: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by organism.
    
    Args:
        organism: The organism to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_organism(organism, options or {})


def query_epitope_assay_by_pdb_id(pdb_id: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by PDB ID.
    
    Args:
        pdb_id: The PDB ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_pdb_id(pdb_id, options or {})


def query_epitope_assay_by_pmid(pmid: str, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by PMID.
    
    Args:
        pmid: The PMID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_pmid(pmid, options or {})


def query_epitope_assay_by_protein_accession(protein_accession: str, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by protein accession.
    
    Args:
        protein_accession: The protein accession to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_protein_accession(protein_accession, options or {})


def query_epitope_assay_by_protein_id(protein_id: str, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by protein ID.
    
    Args:
        protein_id: The protein ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_protein_id(protein_id, options or {})


def query_epitope_assay_by_protein_name(protein_name: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by protein name.
    
    Args:
        protein_name: The protein name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_protein_name(protein_name, options or {})


def query_epitope_assay_by_start(start: int, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by start position.
    
    Args:
        start: The start position to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_start(start, options or {})


def query_epitope_assay_by_end(end: int, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by end position.
    
    Args:
        end: The end position to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_end(end, options or {})


def query_epitope_assay_by_taxon_id(taxon_id: int, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by taxon ID.
    
    Args:
        taxon_id: The taxon ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_taxon_id(taxon_id, options or {})


def query_epitope_assay_by_taxon_lineage_id(taxon_lineage_id: str, options: Dict[str, Any] = None,
                                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by taxon lineage ID.
    
    Args:
        taxon_lineage_id: The taxon lineage ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_taxon_lineage_id(taxon_lineage_id, options or {})


def query_epitope_assay_by_taxon_lineage_name(taxon_lineage_name: str, options: Dict[str, Any] = None,
                                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by taxon lineage name.
    
    Args:
        taxon_lineage_name: The taxon lineage name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_taxon_lineage_name(taxon_lineage_name, options or {})


def query_epitope_assay_by_title(title: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by title.
    
    Args:
        title: The title to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_title(title, options or {})


def query_epitope_assay_by_position_range(min_start: int, max_end: int, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by position range.
    
    Args:
        min_start: Minimum start position
        max_end: Maximum end position
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_position_range(min_start, max_end, options or {})


def query_epitope_assay_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by date inserted range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_date_inserted_range(start_date, end_date, options or {})


def query_epitope_assay_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query epitope assay by date modified range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_by_date_modified_range(start_date, end_date, options or {})


def query_epitope_assay_by_keyword(keyword: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search epitope assay by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.search_by_keyword(keyword, options or {})


def query_epitope_assay_all(options: Dict[str, Any] = None,
                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all epitope assay data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all epitope assay records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.epitope_assay.get_all(options or {})
