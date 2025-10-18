"""
BV-BRC Subsystem Functions

This module provides wrapper functions for the BV-BRC Solr API subsystem resource,
exposing subsystem querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_subsystem_by_id(id: str, options: Dict[str, Any] = None,
                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem by ID.
    
    Args:
        id: The ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem.get_by_id(id, options or {})


def query_subsystem_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem.query_by(filters, options or {})


def query_subsystem_by_active(active: str, options: Dict[str, Any] = None,
                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem by active status.
    
    Args:
        active: The active status to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem.get_by_active(active, options or {})


def query_subsystem_by_class(class_name: str, options: Dict[str, Any] = None,
                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem by class.
    
    Args:
        class_name: The class to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem.get_by_class(class_name, options or {})


def query_subsystem_by_feature_id(feature_id: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem by feature ID.
    
    Args:
        feature_id: The feature ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem.get_by_feature_id(feature_id, options or {})


def query_subsystem_by_gene(gene: str, options: Dict[str, Any] = None,
                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem by gene.
    
    Args:
        gene: The gene to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem.get_by_gene(gene, options or {})


def query_subsystem_by_genome_id(genome_id: str, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem by genome ID.
    
    Args:
        genome_id: The genome ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem.get_by_genome_id(genome_id, options or {})


def query_subsystem_by_genome_name(genome_name: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem by genome name.
    
    Args:
        genome_name: The genome name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem.get_by_genome_name(genome_name, options or {})


def query_subsystem_by_owner(owner: str, options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem by owner.
    
    Args:
        owner: The owner to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem.get_by_owner(owner, options or {})


def query_subsystem_by_patric_id(patric_id: str, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem by PATRIC ID.
    
    Args:
        patric_id: The PATRIC ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem.get_by_patric_id(patric_id, options or {})


def query_subsystem_by_product(product: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem by product.
    
    Args:
        product: The product to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem.get_by_product(product, options or {})


def query_subsystem_by_public_status(is_public: bool, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem by public status.
    
    Args:
        is_public: The public status to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem.get_by_public_status(is_public, options or {})


def query_subsystem_by_refseq_locus_tag(refseq_locus_tag: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem by RefSeq locus tag.
    
    Args:
        refseq_locus_tag: The RefSeq locus tag to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem.get_by_refseq_locus_tag(refseq_locus_tag, options or {})


def query_subsystem_by_role_id(role_id: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem by role ID.
    
    Args:
        role_id: The role ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem.get_by_role_id(role_id, options or {})


def query_subsystem_by_role_name(role_name: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem by role name.
    
    Args:
        role_name: The role name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem.get_by_role_name(role_name, options or {})


def query_subsystem_by_subclass(subclass: str, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem by subclass.
    
    Args:
        subclass: The subclass to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem.get_by_subclass(subclass, options or {})


def query_subsystem_by_subsystem_id(subsystem_id: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem by subsystem ID.
    
    Args:
        subsystem_id: The subsystem ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem.get_by_subsystem_id(subsystem_id, options or {})


def query_subsystem_by_subsystem_name(subsystem_name: str, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem by subsystem name.
    
    Args:
        subsystem_name: The subsystem name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem.get_by_subsystem_name(subsystem_name, options or {})


def query_subsystem_by_superclass(superclass: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem by superclass.
    
    Args:
        superclass: The superclass to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem.get_by_superclass(superclass, options or {})


def query_subsystem_by_taxon_id(taxon_id: int, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem by taxon ID.
    
    Args:
        taxon_id: The taxon ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem.get_by_taxon_id(taxon_id, options or {})


def query_subsystem_by_user_read(user_read: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem by user read.
    
    Args:
        user_read: The user read to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem.get_by_user_read(user_read, options or {})


def query_subsystem_by_user_write(user_write: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem by user write.
    
    Args:
        user_write: The user write to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem.get_by_user_write(user_write, options or {})


def query_subsystem_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem by date inserted range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem.get_by_date_inserted_range(start_date, end_date, options or {})


def query_subsystem_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query subsystem by date modified range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem.get_by_date_modified_range(start_date, end_date, options or {})


def query_subsystem_by_keyword(keyword: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search subsystem by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of subsystem records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem.search_by_keyword(keyword, options or {})


def query_subsystem_all(options: Dict[str, Any] = None,
                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all subsystem data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all subsystem records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.subsystem.get_all(options or {})
