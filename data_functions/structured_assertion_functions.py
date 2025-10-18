"""
BV-BRC Structured Assertion Functions

This module provides wrapper functions for the BV-BRC Solr API structured_assertion resource,
exposing structured assertion querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_structured_assertion_by_id(id: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query structured assertion by ID.
    
    Args:
        id: The ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of structured assertion records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.structured_assertion.get_by_id(id, options or {})


def query_structured_assertion_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query structured assertion by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of structured assertion records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.structured_assertion.query_by(filters, options or {})


def query_structured_assertion_by_comment(comment: str, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query structured assertion by comment.
    
    Args:
        comment: The comment to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of structured assertion records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.structured_assertion.get_by_comment(comment, options or {})


def query_structured_assertion_by_evidence_code(evidence_code: str, options: Dict[str, Any] = None,
                                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query structured assertion by evidence code.
    
    Args:
        evidence_code: The evidence code to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of structured assertion records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.structured_assertion.get_by_evidence_code(evidence_code, options or {})


def query_structured_assertion_by_feature_id(feature_id: str, options: Dict[str, Any] = None,
                                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query structured assertion by feature ID.
    
    Args:
        feature_id: The feature ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of structured assertion records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.structured_assertion.get_by_feature_id(feature_id, options or {})


def query_structured_assertion_by_owner(owner: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query structured assertion by owner.
    
    Args:
        owner: The owner to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of structured assertion records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.structured_assertion.get_by_owner(owner, options or {})


def query_structured_assertion_by_patric_id(patric_id: str, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query structured assertion by PATRIC ID.
    
    Args:
        patric_id: The PATRIC ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of structured assertion records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.structured_assertion.get_by_patric_id(patric_id, options or {})


def query_structured_assertion_by_pmid(pmid: str, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query structured assertion by PMID.
    
    Args:
        pmid: The PMID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of structured assertion records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.structured_assertion.get_by_pmid(pmid, options or {})


def query_structured_assertion_by_property(property: str, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query structured assertion by property.
    
    Args:
        property: The property to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of structured assertion records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.structured_assertion.get_by_property(property, options or {})


def query_structured_assertion_by_public_status(is_public: bool, options: Dict[str, Any] = None,
                                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query structured assertion by public status.
    
    Args:
        is_public: The public status to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of structured assertion records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.structured_assertion.get_by_public_status(is_public, options or {})


def query_structured_assertion_by_refseq_locus_tag(refseq_locus_tag: str, options: Dict[str, Any] = None,
                                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query structured assertion by RefSeq locus tag.
    
    Args:
        refseq_locus_tag: The RefSeq locus tag to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of structured assertion records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.structured_assertion.get_by_refseq_locus_tag(refseq_locus_tag, options or {})


def query_structured_assertion_by_score(score: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query structured assertion by score.
    
    Args:
        score: The score to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of structured assertion records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.structured_assertion.get_by_score(score, options or {})


def query_structured_assertion_by_source(source: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query structured assertion by source.
    
    Args:
        source: The source to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of structured assertion records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.structured_assertion.get_by_source(source, options or {})


def query_structured_assertion_by_value(value: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query structured assertion by value.
    
    Args:
        value: The value to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of structured assertion records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.structured_assertion.get_by_value(value, options or {})


def query_structured_assertion_by_user_read(user_read: str, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query structured assertion by user read.
    
    Args:
        user_read: The user read to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of structured assertion records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.structured_assertion.get_by_user_read(user_read, options or {})


def query_structured_assertion_by_user_write(user_write: str, options: Dict[str, Any] = None,
                                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query structured assertion by user write.
    
    Args:
        user_write: The user write to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of structured assertion records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.structured_assertion.get_by_user_write(user_write, options or {})


def query_structured_assertion_by_version(version: int, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query structured assertion by version.
    
    Args:
        version: The version to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of structured assertion records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.structured_assertion.get_by_version(version, options or {})


def query_structured_assertion_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query structured assertion by date inserted range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of structured assertion records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.structured_assertion.get_by_date_inserted_range(start_date, end_date, options or {})


def query_structured_assertion_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query structured assertion by date modified range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of structured assertion records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.structured_assertion.get_by_date_modified_range(start_date, end_date, options or {})


def query_structured_assertion_by_keyword(keyword: str, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search structured assertion by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of structured assertion records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.structured_assertion.search_by_keyword(keyword, options or {})


def query_structured_assertion_all(options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all structured assertion data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all structured assertion records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.structured_assertion.get_all(options or {})
