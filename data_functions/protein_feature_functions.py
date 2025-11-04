"""
BV-BRC Protein Feature Functions

This module provides protein feature querying functions for the BV-BRC Solr API.
"""

from typing import Any, Dict, List, Tuple
from .common_functions import create_bvbrc_client


def query_protein_feature_by_id(id: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by ID using cursor-based streaming.
    
    Args:
        id: The ID to query
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for id (use q_expr instead of fq)
    q_expr = f"id:{id}"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by custom filters using cursor-based streaming.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression from the filters dict
    # For multiple filters, we need to combine them with AND logic
    filter_parts = []
    for key, value in filters.items():
        if isinstance(value, str):
            filter_parts.append(f'{key}:"{value}"')
        else:
            filter_parts.append(f"{key}:{value}")
    
    # Combine multiple filters with AND logic
    if len(filter_parts) == 1:
        q_expr = filter_parts[0]
    else:
        q_expr = " AND ".join(f"({part})" for part in filter_parts)
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_aa_sequence_md5(aa_sequence_md5: str, options: Dict[str, Any] = None,
                                             base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by amino acid sequence MD5 using cursor-based streaming.
    
    Args:
        aa_sequence_md5: The amino acid sequence MD5 to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for aa_sequence_md5 (use q_expr instead of fq)
    q_expr = f'aa_sequence_md5:"{aa_sequence_md5}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_classification(classification: str, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by classification using cursor-based streaming.
    
    Args:
        classification: The classification to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for classification (use q_expr instead of fq)
    q_expr = f'classification:"{classification}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_comment(comment: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by comment using cursor-based streaming.
    
    Args:
        comment: The comment to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for comment (use q_expr instead of fq)
    q_expr = f'comment:"{comment}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_description(description: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by description using cursor-based streaming.
    
    Args:
        description: The description to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for description (use q_expr instead of fq)
    q_expr = f'description:"{description}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_e_value(e_value: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by E-value using cursor-based streaming.
    
    Args:
        e_value: The E-value to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for e_value (use q_expr instead of fq)
    q_expr = f'e_value:"{e_value}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_end(end: int, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by end position using cursor-based streaming.
    
    Args:
        end: The end position to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for end (use q_expr instead of fq)
    q_expr = f"end:{end}"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_evidence(evidence: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by evidence using cursor-based streaming.
    
    Args:
        evidence: The evidence to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for evidence (use q_expr instead of fq)
    q_expr = f'evidence:"{evidence}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_feature_id(feature_id: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by feature ID using cursor-based streaming.
    
    Args:
        feature_id: The feature ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for feature_id (use q_expr instead of fq)
    q_expr = f'feature_id:"{feature_id}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_feature_type(feature_type: str, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by feature type using cursor-based streaming.
    
    Args:
        feature_type: The feature type to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for feature_type (use q_expr instead of fq)
    q_expr = f'feature_type:"{feature_type}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_gene(gene: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by gene using cursor-based streaming.
    
    Args:
        gene: The gene to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for gene (use q_expr instead of fq)
    q_expr = f'gene:"{gene}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_genome_id(genome_id: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by genome ID using cursor-based streaming.
    
    Args:
        genome_id: The genome ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for genome_id (use q_expr instead of fq)
    q_expr = f'genome_id:"{genome_id}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_genome_name(genome_name: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by genome name using cursor-based streaming.
    
    Args:
        genome_name: The genome name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for genome_name (use q_expr instead of fq)
    q_expr = f'genome_name:"{genome_name}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_interpro_description(interpro_description: str, options: Dict[str, Any] = None,
                                                  base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by InterPro description using cursor-based streaming.
    
    Args:
        interpro_description: The InterPro description to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for interpro_description (use q_expr instead of fq)
    q_expr = f'interpro_description:"{interpro_description}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_interpro_id(interpro_id: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by InterPro ID using cursor-based streaming.
    
    Args:
        interpro_id: The InterPro ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for interpro_id (use q_expr instead of fq)
    q_expr = f'interpro_id:"{interpro_id}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_length(length: int, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by length using cursor-based streaming.
    
    Args:
        length: The length to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for length (use q_expr instead of fq)
    q_expr = f"length:{length}"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_patric_id(patric_id: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by PATRIC ID using cursor-based streaming.
    
    Args:
        patric_id: The PATRIC ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for patric_id (use q_expr instead of fq)
    q_expr = f'patric_id:"{patric_id}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_product(product: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by product using cursor-based streaming.
    
    Args:
        product: The product to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for product (use q_expr instead of fq)
    q_expr = f'product:"{product}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_publication(publication: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by publication using cursor-based streaming.
    
    Args:
        publication: The publication to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for publication (use q_expr instead of fq)
    q_expr = f'publication:"{publication}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_refseq_locus_tag(refseq_locus_tag: str, options: Dict[str, Any] = None,
                                              base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by RefSeq locus tag using cursor-based streaming.
    
    Args:
        refseq_locus_tag: The RefSeq locus tag to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for refseq_locus_tag (use q_expr instead of fq)
    q_expr = f'refseq_locus_tag:"{refseq_locus_tag}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_score(score: float, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by score using cursor-based streaming.
    
    Args:
        score: The score to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for score (use q_expr instead of fq)
    q_expr = f"score:{score}"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_segment(segment: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by segment using cursor-based streaming.
    
    Args:
        segment: The segment to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for segment (use q_expr instead of fq)
    q_expr = f'segment:"{segment}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_sequence(sequence: str, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by sequence using cursor-based streaming.
    
    Args:
        sequence: The sequence to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for sequence (use q_expr instead of fq)
    q_expr = f'sequence:"{sequence}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_source(source: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by source using cursor-based streaming.
    
    Args:
        source: The source to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for source (use q_expr instead of fq)
    q_expr = f'source:"{source}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_source_id(source_id: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by source ID using cursor-based streaming.
    
    Args:
        source_id: The source ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for source_id (use q_expr instead of fq)
    q_expr = f'source_id:"{source_id}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_start(start: int, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by start position using cursor-based streaming.
    
    Args:
        start: The start position to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for start (use q_expr instead of fq)
    q_expr = f"start:{start}"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_taxon_id(taxon_id: int, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by taxon ID using cursor-based streaming.
    
    Args:
        taxon_id: The taxon ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for taxon_id (use q_expr instead of fq)
    q_expr = f"taxon_id:{taxon_id}"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_score_range(min_score: float, max_score: float, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by score range using cursor-based streaming.
    
    Args:
        min_score: Minimum score
        max_score: Maximum score
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for score range (use q_expr instead of fq)
    q_expr = f"score:[{min_score} TO {max_score}]"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_length_range(min_length: int, max_length: int, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by length range using cursor-based streaming.
    
    Args:
        min_length: Minimum length
        max_length: Maximum length
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for length range (use q_expr instead of fq)
    q_expr = f"length:[{min_length} TO {max_length}]"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_position_range(min_start: int, max_end: int, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by position range using cursor-based streaming.
    
    Args:
        min_start: Minimum start position
        max_end: Maximum end position
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for position range (use q_expr instead of fq)
    q_expr = f"start:[{min_start} TO {max_end}] AND end:[{min_start} TO {max_end}]"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                                base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by date inserted range using cursor-based streaming.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for date_inserted range (use q_expr instead of fq)
    q_expr = f'date_inserted:[{start_date} TO {end_date}]'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                                 base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by date modified range using cursor-based streaming.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for date_modified range (use q_expr instead of fq)
    q_expr = f'date_modified:[{start_date} TO {end_date}]'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_by_keyword(keyword: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query protein feature by keyword using cursor-based streaming.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for keyword search (use q_expr instead of fq)
    q_expr = f'*{keyword}*'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr=q_expr,
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)


def query_protein_feature_all(options: Dict[str, Any] = None,
                             base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query all protein feature data using cursor-based streaming.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of protein feature records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.protein_feature.stream_all_solr(
        rows=options.get("rows", 1000),
        sort=options.get("sort"),
        fields=options.get("select"),
        q_expr="*:*",  # Match all documents
        context_overrides={"base_url": base_url, "headers": headers} if base_url or headers else None
    )
    
    # Collect all results into a list
    results = []
    for doc in pager:
        results.append(doc)
    return results, len(results)