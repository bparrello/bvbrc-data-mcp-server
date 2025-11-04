"""
BV-BRC Taxonomy Functions

This module provides taxonomy querying functions for the BV-BRC Solr API.
"""

from typing import Any, Dict, List, Tuple
from .common_functions import create_bvbrc_client


def query_taxonomy_by_id(taxon_id: str, options: Dict[str, Any] = None,
                         base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query taxonomy by taxon ID using cursor-based streaming.
    
    Args:
        taxon_id: The taxon ID to query
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of taxonomy records, count of results)
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
    
    pager = client.taxonomy.stream_all_solr(
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


def query_taxonomy_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query taxonomy by custom filters using cursor-based streaming.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of taxonomy records, count of results)
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
    
    pager = client.taxonomy.stream_all_solr(
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


def query_taxonomy_by_taxon_name(taxon_name: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query taxonomy by taxon name using cursor-based streaming.
    
    Args:
        taxon_name: The taxon name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of taxonomy records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for taxon_name (use q_expr instead of fq)
    q_expr = f'taxon_name:"{taxon_name}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.taxonomy.stream_all_solr(
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


def query_taxonomy_by_taxon_rank(taxon_rank: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query taxonomy by taxon rank using cursor-based streaming.
    
    Args:
        taxon_rank: The taxon rank to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of taxonomy records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for taxon_rank (use q_expr instead of fq)
    q_expr = f'taxon_rank:"{taxon_rank}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.taxonomy.stream_all_solr(
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


def query_taxonomy_by_lineage(lineage: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query taxonomy by lineage using cursor-based streaming.
    
    Args:
        lineage: The lineage to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of taxonomy records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for lineage (use q_expr instead of fq)
    q_expr = f'lineage:"{lineage}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.taxonomy.stream_all_solr(
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


def query_taxonomy_by_lineage_ids(lineage_ids: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query taxonomy by lineage IDs using cursor-based streaming.
    
    Args:
        lineage_ids: The lineage IDs to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of taxonomy records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for lineage_ids (use q_expr instead of fq)
    q_expr = f'lineage_ids:"{lineage_ids}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.taxonomy.stream_all_solr(
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


def query_taxonomy_by_lineage_names(lineage_names: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query taxonomy by lineage names using cursor-based streaming.
    
    Args:
        lineage_names: The lineage names to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of taxonomy records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for lineage_names (use q_expr instead of fq)
    q_expr = f'lineage_names:"{lineage_names}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.taxonomy.stream_all_solr(
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


def query_taxonomy_by_parent_id(parent_id: int, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query taxonomy by parent ID using cursor-based streaming.
    
    Args:
        parent_id: The parent ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of taxonomy records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for parent_id (use q_expr instead of fq)
    q_expr = f"parent_id:{parent_id}"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.taxonomy.stream_all_solr(
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


def query_taxonomy_by_division(division: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query taxonomy by division using cursor-based streaming.
    
    Args:
        division: The division to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of taxonomy records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for division (use q_expr instead of fq)
    q_expr = f'division:"{division}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.taxonomy.stream_all_solr(
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


def query_taxonomy_by_genetic_code(genetic_code: int, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query taxonomy by genetic code using cursor-based streaming.
    
    Args:
        genetic_code: The genetic code to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of taxonomy records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for genetic_code (use q_expr instead of fq)
    q_expr = f"genetic_code:{genetic_code}"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.taxonomy.stream_all_solr(
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


def query_taxonomy_by_genome_count(genome_count: int, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query taxonomy by genome count using cursor-based streaming.
    
    Args:
        genome_count: The genome count to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of taxonomy records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for genome_count (use q_expr instead of fq)
    q_expr = f"genome_count:{genome_count}"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.taxonomy.stream_all_solr(
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


def query_taxonomy_by_core_families(core_families: int, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query taxonomy by core families using cursor-based streaming.
    
    Args:
        core_families: The core families to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of taxonomy records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for core_families (use q_expr instead of fq)
    q_expr = f"core_families:{core_families}"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.taxonomy.stream_all_solr(
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


def query_taxonomy_by_cds_mean(cds_mean: float, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query taxonomy by CDS mean using cursor-based streaming.
    
    Args:
        cds_mean: The CDS mean to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of taxonomy records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for cds_mean (use q_expr instead of fq)
    q_expr = f"cds_mean:{cds_mean}"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.taxonomy.stream_all_solr(
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


def query_taxonomy_by_genome_length_mean(genome_length_mean: float, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query taxonomy by genome length mean using cursor-based streaming.
    
    Args:
        genome_length_mean: The genome length mean to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of taxonomy records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for genome_length_mean (use q_expr instead of fq)
    q_expr = f"genome_length_mean:{genome_length_mean}"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.taxonomy.stream_all_solr(
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


def query_taxonomy_by_cds_mean_range(min_cds_mean: float, max_cds_mean: float, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query taxonomy by CDS mean range using cursor-based streaming.
    
    Args:
        min_cds_mean: Minimum CDS mean
        max_cds_mean: Maximum CDS mean
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of taxonomy records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for cds_mean range (use q_expr instead of fq)
    q_expr = f"cds_mean:[{min_cds_mean} TO {max_cds_mean}]"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.taxonomy.stream_all_solr(
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


def query_taxonomy_by_core_families_range(min_core_families: int, max_core_families: int, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query taxonomy by core families range using cursor-based streaming.
    
    Args:
        min_core_families: Minimum core families
        max_core_families: Maximum core families
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of taxonomy records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for core_families range (use q_expr instead of fq)
    q_expr = f"core_families:[{min_core_families} TO {max_core_families}]"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.taxonomy.stream_all_solr(
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


def query_taxonomy_by_genetic_code_range(min_genetic_code: int, max_genetic_code: int, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query taxonomy by genetic code range using cursor-based streaming.
    
    Args:
        min_genetic_code: Minimum genetic code
        max_genetic_code: Maximum genetic code
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of taxonomy records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for genetic_code range (use q_expr instead of fq)
    q_expr = f"genetic_code:[{min_genetic_code} TO {max_genetic_code}]"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.taxonomy.stream_all_solr(
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


def query_taxonomy_by_genome_count_range(min_genome_count: int, max_genome_count: int, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query taxonomy by genome count range using cursor-based streaming.
    
    Args:
        min_genome_count: Minimum genome count
        max_genome_count: Maximum genome count
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of taxonomy records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for genome_count range (use q_expr instead of fq)
    q_expr = f"genome_count:[{min_genome_count} TO {max_genome_count}]"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.taxonomy.stream_all_solr(
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


def query_taxonomy_by_genome_length_mean_range(min_genome_length_mean: float, max_genome_length_mean: float, options: Dict[str, Any] = None,
                                               base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query taxonomy by genome length mean range using cursor-based streaming.
    
    Args:
        min_genome_length_mean: Minimum genome length mean
        max_genome_length_mean: Maximum genome length mean
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of taxonomy records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for genome_length_mean range (use q_expr instead of fq)
    q_expr = f"genome_length_mean:[{min_genome_length_mean} TO {max_genome_length_mean}]"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.taxonomy.stream_all_solr(
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


def query_taxonomy_by_parent_id_range(min_parent_id: int, max_parent_id: int, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query taxonomy by parent ID range using cursor-based streaming.
    
    Args:
        min_parent_id: Minimum parent ID
        max_parent_id: Maximum parent ID
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of taxonomy records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for parent_id range (use q_expr instead of fq)
    q_expr = f"parent_id:[{min_parent_id} TO {max_parent_id}]"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.taxonomy.stream_all_solr(
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


def query_taxonomy_by_keyword(keyword: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query taxonomy by keyword using cursor-based streaming.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of taxonomy records, count of results)
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
    
    pager = client.taxonomy.stream_all_solr(
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


def query_taxonomy_all(options: Dict[str, Any] = None,
                       base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query all taxonomy data using cursor-based streaming.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of taxonomy records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.taxonomy.stream_all_solr(
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