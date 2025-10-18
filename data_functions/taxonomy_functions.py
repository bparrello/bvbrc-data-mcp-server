"""
BV-BRC Taxonomy Functions

This module provides wrapper functions for the BV-BRC Solr API taxonomy resource,
exposing taxonomy querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_taxonomy_by_id(taxon_id: str, options: Dict[str, Any] = None,
                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query taxonomy by taxon ID.
    
    Args:
        taxon_id: The taxon ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of taxonomy records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.taxonomy.get_by_id(taxon_id, options or {})


def query_taxonomy_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query taxonomy by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of taxonomy records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.taxonomy.query_by(filters, options or {})


def query_taxonomy_by_taxon_name(taxon_name: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query taxonomy by taxon name.
    
    Args:
        taxon_name: The taxon name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of taxonomy records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.taxonomy.get_by_taxon_name(taxon_name, options or {})


def query_taxonomy_by_taxon_rank(taxon_rank: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query taxonomy by taxon rank.
    
    Args:
        taxon_rank: The taxon rank to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of taxonomy records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.taxonomy.get_by_taxon_rank(taxon_rank, options or {})


def query_taxonomy_by_lineage(lineage: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query taxonomy by lineage.
    
    Args:
        lineage: The lineage to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of taxonomy records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.taxonomy.get_by_lineage(lineage, options or {})


def query_taxonomy_by_lineage_ids(lineage_ids: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query taxonomy by lineage IDs.
    
    Args:
        lineage_ids: The lineage IDs to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of taxonomy records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.taxonomy.get_by_lineage_ids(lineage_ids, options or {})


def query_taxonomy_by_lineage_names(lineage_names: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query taxonomy by lineage names.
    
    Args:
        lineage_names: The lineage names to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of taxonomy records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.taxonomy.get_by_lineage_names(lineage_names, options or {})


def query_taxonomy_by_parent_id(parent_id: int, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query taxonomy by parent ID.
    
    Args:
        parent_id: The parent ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of taxonomy records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.taxonomy.get_by_parent_id(parent_id, options or {})


def query_taxonomy_by_division(division: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query taxonomy by division.
    
    Args:
        division: The division to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of taxonomy records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.taxonomy.get_by_division(division, options or {})


def query_taxonomy_by_genetic_code(genetic_code: int, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query taxonomy by genetic code.
    
    Args:
        genetic_code: The genetic code to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of taxonomy records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.taxonomy.get_by_genetic_code(genetic_code, options or {})


def query_taxonomy_by_genome_count(genome_count: int, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query taxonomy by genome count.
    
    Args:
        genome_count: The genome count to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of taxonomy records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.taxonomy.get_by_genome_count(genome_count, options or {})


def query_taxonomy_by_core_families(core_families: int, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query taxonomy by core families.
    
    Args:
        core_families: The core families to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of taxonomy records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.taxonomy.get_by_core_families(core_families, options or {})


def query_taxonomy_by_cds_mean(cds_mean: float, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query taxonomy by CDS mean.
    
    Args:
        cds_mean: The CDS mean to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of taxonomy records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.taxonomy.get_by_cds_mean(cds_mean, options or {})


def query_taxonomy_by_genome_length_mean(genome_length_mean: float, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query taxonomy by genome length mean.
    
    Args:
        genome_length_mean: The genome length mean to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of taxonomy records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.taxonomy.get_by_genome_length_mean(genome_length_mean, options or {})


def query_taxonomy_by_cds_mean_range(min_cds_mean: float, max_cds_mean: float, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query taxonomy by CDS mean range.
    
    Args:
        min_cds_mean: Minimum CDS mean
        max_cds_mean: Maximum CDS mean
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of taxonomy records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.taxonomy.get_by_cds_mean_range(min_cds_mean, max_cds_mean, options or {})


def query_taxonomy_by_core_families_range(min_core_families: int, max_core_families: int, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query taxonomy by core families range.
    
    Args:
        min_core_families: Minimum core families
        max_core_families: Maximum core families
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of taxonomy records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.taxonomy.get_by_core_families_range(min_core_families, max_core_families, options or {})


def query_taxonomy_by_genetic_code_range(min_genetic_code: int, max_genetic_code: int, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query taxonomy by genetic code range.
    
    Args:
        min_genetic_code: Minimum genetic code
        max_genetic_code: Maximum genetic code
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of taxonomy records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.taxonomy.get_by_genetic_code_range(min_genetic_code, max_genetic_code, options or {})


def query_taxonomy_by_genome_count_range(min_genome_count: int, max_genome_count: int, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query taxonomy by genome count range.
    
    Args:
        min_genome_count: Minimum genome count
        max_genome_count: Maximum genome count
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of taxonomy records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.taxonomy.get_by_genome_count_range(min_genome_count, max_genome_count, options or {})


def query_taxonomy_by_genome_length_mean_range(min_genome_length_mean: float, max_genome_length_mean: float, options: Dict[str, Any] = None,
                                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query taxonomy by genome length mean range.
    
    Args:
        min_genome_length_mean: Minimum genome length mean
        max_genome_length_mean: Maximum genome length mean
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of taxonomy records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.taxonomy.get_by_genome_length_mean_range(min_genome_length_mean, max_genome_length_mean, options or {})


def query_taxonomy_by_parent_id_range(min_parent_id: int, max_parent_id: int, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query taxonomy by parent ID range.
    
    Args:
        min_parent_id: Minimum parent ID
        max_parent_id: Maximum parent ID
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of taxonomy records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.taxonomy.get_by_parent_id_range(min_parent_id, max_parent_id, options or {})


def query_taxonomy_by_keyword(keyword: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search taxonomy by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of taxonomy records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.taxonomy.search_by_keyword(keyword, options or {})


def query_taxonomy_all(options: Dict[str, Any] = None,
                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all taxonomy data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all taxonomy records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.taxonomy.get_all(options or {})
