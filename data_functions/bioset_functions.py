"""
BV-BRC Bioset Functions

This module provides bioset querying functions for the BV-BRC Solr API.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_bioset_by_id(bioset_id: str, options: Dict[str, Any] = None, 
                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query bioset by ID.
    
    Args:
        bioset_id: The bioset ID to query
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of bioset records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset.get_by_id(bioset_id, options or {})


def query_bioset_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query bioset by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of bioset records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset.query_by(filters, options or {})


def query_bioset_by_name(bioset_name: str, options: Dict[str, Any] = None,
                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query bioset by bioset name.
    
    Args:
        bioset_name: The bioset name to query
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of bioset records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset.get_by_bioset_name(bioset_name, options or {})


def query_bioset_by_type(bioset_type: str, options: Dict[str, Any] = None,
                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query bioset by bioset type.
    
    Args:
        bioset_type: The bioset type to query
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of bioset records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset.get_by_bioset_type(bioset_type, options or {})


def query_bioset_by_exp_id(exp_id: str, options: Dict[str, Any] = None,
                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query bioset by experiment ID.
    
    Args:
        exp_id: The experiment ID to query
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of bioset records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset.get_by_exp_id(exp_id, options or {})


def query_bioset_by_exp_name(exp_name: str, options: Dict[str, Any] = None,
                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query bioset by experiment name.
    
    Args:
        exp_name: The experiment name to query
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of bioset records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset.get_by_exp_name(exp_name, options or {})


def query_bioset_by_exp_type(exp_type: str, options: Dict[str, Any] = None,
                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query bioset by experiment type.
    
    Args:
        exp_type: The experiment type to query
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of bioset records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset.get_by_exp_type(exp_type, options or {})


def query_bioset_by_organism(organism: str, options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query bioset by organism.
    
    Args:
        organism: The organism to query
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of bioset records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset.get_by_organism(organism, options or {})


def query_bioset_by_strain(strain: str, options: Dict[str, Any] = None,
                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query bioset by strain.
    
    Args:
        strain: The strain to query
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of bioset records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset.get_by_strain(strain, options or {})


def query_bioset_by_taxon_id(taxon_id: int, options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query bioset by taxon ID.
    
    Args:
        taxon_id: The taxon ID to query
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of bioset records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset.get_by_taxon_id(taxon_id, options or {})


def query_bioset_by_entity_type(entity_type: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query bioset by entity type.
    
    Args:
        entity_type: The entity type to query
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of bioset records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset.get_by_entity_type(entity_type, options or {})


def query_bioset_by_result_type(result_type: str, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query bioset by result type.
    
    Args:
        result_type: The result type to query
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of bioset records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset.get_by_result_type(result_type, options or {})


def query_bioset_by_analysis_method(analysis_method: str, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query bioset by analysis method.
    
    Args:
        analysis_method: The analysis method to query
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of bioset records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset.get_by_analysis_method(analysis_method, options or {})


def query_bioset_by_analysis_group_1(analysis_group_1: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query bioset by analysis group 1.
    
    Args:
        analysis_group_1: The analysis group 1 to query
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of bioset records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset.get_by_analysis_group_1(analysis_group_1, options or {})


def query_bioset_by_analysis_group_2(analysis_group_2: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query bioset by analysis group 2.
    
    Args:
        analysis_group_2: The analysis group 2 to query
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of bioset records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset.get_by_analysis_group_2(analysis_group_2, options or {})


def query_bioset_by_treatment_type(treatment_type: str, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query bioset by treatment type.
    
    Args:
        treatment_type: The treatment type to query
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of bioset records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset.get_by_treatment_type(treatment_type, options or {})


def query_bioset_by_treatment_name(treatment_name: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query bioset by treatment name.
    
    Args:
        treatment_name: The treatment name to query
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of bioset records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset.get_by_treatment_name(treatment_name, options or {})


def query_bioset_by_study_name(study_name: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query bioset by study name.
    
    Args:
        study_name: The study name to query
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of bioset records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset.get_by_study_name(study_name, options or {})


def query_bioset_by_study_pi(study_pi: str, options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query bioset by study PI.
    
    Args:
        study_pi: The study PI to query
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of bioset records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset.get_by_study_pi(study_pi, options or {})


def query_bioset_by_study_institution(study_institution: str, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query bioset by study institution.
    
    Args:
        study_institution: The study institution to query
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of bioset records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset.get_by_study_institution(study_institution, options or {})


def query_bioset_by_genome_id(genome_id: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query bioset by genome ID.
    
    Args:
        genome_id: The genome ID to query
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of bioset records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset.get_by_genome_id(genome_id, options or {})


def query_bioset_by_date_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query bioset by date range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of bioset records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset.get_by_date_range(start_date, end_date, options or {})


def query_bioset_by_modified_date_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query bioset by modified date range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of bioset records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset.get_by_modified_date_range(start_date, end_date, options or {})


def query_bioset_by_keyword(keyword: str, options: Dict[str, Any] = None,
                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query bioset by keyword search.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of bioset records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset.search_by_keyword(keyword, options or {})


def query_bioset_all(options: Dict[str, Any] = None,
                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query all bioset records.
    
    Args:
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of bioset records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.bioset.get_all(options or {})
