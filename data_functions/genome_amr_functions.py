"""
BV-BRC Genome AMR Functions

This module provides genome AMR querying functions for the BV-BRC Solr API.
"""

from typing import Any, Dict, List, Tuple
from .common_functions import create_bvbrc_client


def query_genome_amr_by_id(id: str, options: Dict[str, Any] = None,
                          base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by ID using cursor-based streaming.
    
    Args:
        id: The AMR record ID to query
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
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
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by custom filters using cursor-based streaming.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
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
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_by_antibiotic(antibiotic: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by antibiotic using cursor-based streaming.
    
    Args:
        antibiotic: The antibiotic to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for antibiotic (use q_expr instead of fq)
    q_expr = f'antibiotic:"{antibiotic}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_by_computational_method(computational_method: str, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by computational method using cursor-based streaming.
    
    Args:
        computational_method: The computational method to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for computational_method (use q_expr instead of fq)
    q_expr = f'computational_method:"{computational_method}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_by_computational_method_version(computational_method_version: str, options: Dict[str, Any] = None,
                                                     base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by computational method version using cursor-based streaming.
    
    Args:
        computational_method_version: The computational method version to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for computational_method_version (use q_expr instead of fq)
    q_expr = f'computational_method_version:"{computational_method_version}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_by_evidence(evidence: str, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by evidence using cursor-based streaming.
    
    Args:
        evidence: The evidence to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
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
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_by_genome_id(genome_id: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by genome ID using cursor-based streaming.
    
    Args:
        genome_id: The genome ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for genome_id (use q_expr instead of fq)
    q_expr = f"genome_id:{genome_id}"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_by_genome_name(genome_name: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by genome name using cursor-based streaming.
    
    Args:
        genome_name: The genome name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
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
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_by_laboratory_typing_method(laboratory_typing_method: str, options: Dict[str, Any] = None,
                                                 base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by laboratory typing method using cursor-based streaming.
    
    Args:
        laboratory_typing_method: The laboratory typing method to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for laboratory_typing_method (use q_expr instead of fq)
    q_expr = f'laboratory_typing_method:"{laboratory_typing_method}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_by_laboratory_typing_method_version(laboratory_typing_method_version: str, options: Dict[str, Any] = None,
                                                         base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by laboratory typing method version using cursor-based streaming.
    
    Args:
        laboratory_typing_method_version: The laboratory typing method version to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for laboratory_typing_method_version (use q_expr instead of fq)
    q_expr = f'laboratory_typing_method_version:"{laboratory_typing_method_version}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_by_laboratory_typing_platform(laboratory_typing_platform: str, options: Dict[str, Any] = None,
                                                   base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by laboratory typing platform using cursor-based streaming.
    
    Args:
        laboratory_typing_platform: The laboratory typing platform to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for laboratory_typing_platform (use q_expr instead of fq)
    q_expr = f'laboratory_typing_platform:"{laboratory_typing_platform}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_by_measurement(measurement: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by measurement using cursor-based streaming.
    
    Args:
        measurement: The measurement to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for measurement (use q_expr instead of fq)
    q_expr = f'measurement:"{measurement}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_by_measurement_sign(measurement_sign: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by measurement sign using cursor-based streaming.
    
    Args:
        measurement_sign: The measurement sign to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for measurement_sign (use q_expr instead of fq)
    q_expr = f'measurement_sign:"{measurement_sign}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_by_measurement_unit(measurement_unit: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by measurement unit using cursor-based streaming.
    
    Args:
        measurement_unit: The measurement unit to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for measurement_unit (use q_expr instead of fq)
    q_expr = f'measurement_unit:"{measurement_unit}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_by_measurement_value(measurement_value: str, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by measurement value using cursor-based streaming.
    
    Args:
        measurement_value: The measurement value to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for measurement_value (use q_expr instead of fq)
    q_expr = f'measurement_value:"{measurement_value}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_by_owner(owner: str, options: Dict[str, Any] = None,
                             base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by owner using cursor-based streaming.
    
    Args:
        owner: The owner to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for owner (use q_expr instead of fq)
    q_expr = f'owner:"{owner}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_by_pmid(pmid: int, options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by PMID using cursor-based streaming.
    
    Args:
        pmid: The PMID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for pmid (use q_expr instead of fq)
    q_expr = f"pmid:{pmid}"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_by_public_status(is_public: bool, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by public status using cursor-based streaming.
    
    Args:
        is_public: The public status to query (True/False)
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for is_public (use q_expr instead of fq)
    q_expr = f"is_public:{str(is_public).lower()}"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_by_resistant_phenotype(resistant_phenotype: str, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by resistant phenotype using cursor-based streaming.
    
    Args:
        resistant_phenotype: The resistant phenotype to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for resistant_phenotype (use q_expr instead of fq)
    q_expr = f'resistant_phenotype:"{resistant_phenotype}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_by_source(source: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by source using cursor-based streaming.
    
    Args:
        source: The source to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
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
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_by_taxon_id(taxon_id: int, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by taxon ID using cursor-based streaming.
    
    Args:
        taxon_id: The taxon ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
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
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_by_testing_standard(testing_standard: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by testing standard using cursor-based streaming.
    
    Args:
        testing_standard: The testing standard to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for testing_standard (use q_expr instead of fq)
    q_expr = f'testing_standard:"{testing_standard}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_by_testing_standard_year(testing_standard_year: int, options: Dict[str, Any] = None,
                                              base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by testing standard year using cursor-based streaming.
    
    Args:
        testing_standard_year: The testing standard year to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for testing_standard_year (use q_expr instead of fq)
    q_expr = f"testing_standard_year:{testing_standard_year}"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_by_vendor(vendor: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by vendor using cursor-based streaming.
    
    Args:
        vendor: The vendor to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for vendor (use q_expr instead of fq)
    q_expr = f'vendor:"{vendor}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_by_date_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by date range using cursor-based streaming.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for date range (use q_expr instead of fq)
    q_expr = f'date:[{start_date} TO {end_date}]'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_by_modified_date_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by modified date range using cursor-based streaming.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for modified date range (use q_expr instead of fq)
    q_expr = f'date_modified:[{start_date} TO {end_date}]'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_by_keyword(keyword: str, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query genome AMR by keyword using cursor-based streaming.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
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
    
    pager = client.genome_amr.stream_all_solr(
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


def query_genome_amr_all(options: Dict[str, Any] = None,
                        base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query all genome AMR data using cursor-based streaming.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of genome AMR records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.genome_amr.stream_all_solr(
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