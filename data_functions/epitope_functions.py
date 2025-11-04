"""
BV-BRC Epitope Functions

This module provides epitope querying functions for the BV-BRC Solr API.
"""

from typing import Any, Dict, List, Tuple
from .common_functions import create_bvbrc_client


def query_epitope_by_id(epitope_id: str, options: Dict[str, Any] = None,
                       base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query epitope by epitope ID using cursor-based streaming.
    
    Args:
        epitope_id: The epitope ID to query
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of epitope records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for epitope_id (use q_expr instead of fq)
    q_expr = f"epitope_id:{epitope_id}"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.epitope.stream_all_solr(
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


def query_epitope_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query epitope by custom filters using cursor-based streaming.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of epitope records, count of results)
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
    
    pager = client.epitope.stream_all_solr(
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


def query_epitope_by_epitope_sequence(epitope_sequence: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query epitope by epitope sequence using cursor-based streaming.
    
    Args:
        epitope_sequence: The epitope sequence to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of epitope records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for epitope_sequence (use q_expr instead of fq)
    q_expr = f'epitope_sequence:"{epitope_sequence}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.epitope.stream_all_solr(
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


def query_epitope_by_epitope_type(epitope_type: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query epitope by epitope type using cursor-based streaming.
    
    Args:
        epitope_type: The epitope type to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of epitope records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for epitope_type (use q_expr instead of fq)
    q_expr = f"epitope_type:{epitope_type}"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.epitope.stream_all_solr(
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


def query_epitope_by_host_name(host_name: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query epitope by host name using cursor-based streaming.
    
    Args:
        host_name: The host name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of epitope records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for host_name (use q_expr instead of fq)
    q_expr = f'host_name:"{host_name}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.epitope.stream_all_solr(
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


def query_epitope_by_organism(organism: str, options: Dict[str, Any] = None,
                              base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query epitope by organism using cursor-based streaming.
    
    Args:
        organism: The organism to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of epitope records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for organism (use q_expr instead of fq)
    q_expr = f'organism:"{organism}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.epitope.stream_all_solr(
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


def query_epitope_by_protein_accession(protein_accession: str, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query epitope by protein accession using cursor-based streaming.
    
    Args:
        protein_accession: The protein accession to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of epitope records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for protein_accession (use q_expr instead of fq)
    q_expr = f"protein_accession:{protein_accession}"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.epitope.stream_all_solr(
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


def query_epitope_by_protein_id(protein_id: str, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query epitope by protein ID using cursor-based streaming.
    
    Args:
        protein_id: The protein ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of epitope records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for protein_id (use q_expr instead of fq)
    q_expr = f"protein_id:{protein_id}"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.epitope.stream_all_solr(
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


def query_epitope_by_protein_name(protein_name: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query epitope by protein name using cursor-based streaming.
    
    Args:
        protein_name: The protein name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of epitope records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for protein_name (use q_expr instead of fq)
    q_expr = f'protein_name:"{protein_name}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.epitope.stream_all_solr(
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


def query_epitope_by_start(start: int, options: Dict[str, Any] = None,
                          base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query epitope by start position using cursor-based streaming.
    
    Args:
        start: The start position to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of epitope records, count of results)
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
    
    pager = client.epitope.stream_all_solr(
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


def query_epitope_by_end(end: int, options: Dict[str, Any] = None,
                        base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query epitope by end position using cursor-based streaming.
    
    Args:
        end: The end position to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of epitope records, count of results)
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
    
    pager = client.epitope.stream_all_solr(
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


def query_epitope_by_taxon_id(taxon_id: int, options: Dict[str, Any] = None,
                             base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query epitope by taxon ID using cursor-based streaming.
    
    Args:
        taxon_id: The taxon ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of epitope records, count of results)
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
    
    pager = client.epitope.stream_all_solr(
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


def query_epitope_by_bcell_assays(bcell_assays: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query epitope by B-cell assays using cursor-based streaming.
    
    Args:
        bcell_assays: The B-cell assays to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of epitope records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for bcell_assays (use q_expr instead of fq)
    q_expr = f"bcell_assays:{bcell_assays}"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.epitope.stream_all_solr(
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


def query_epitope_by_mhc_assays(mhc_assays: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query epitope by MHC assays using cursor-based streaming.
    
    Args:
        mhc_assays: The MHC assays to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of epitope records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for mhc_assays (use q_expr instead of fq)
    q_expr = f"mhc_assays:{mhc_assays}"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.epitope.stream_all_solr(
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


def query_epitope_by_tcell_assays(tcell_assays: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query epitope by T-cell assays using cursor-based streaming.
    
    Args:
        tcell_assays: The T-cell assays to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of epitope records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for tcell_assays (use q_expr instead of fq)
    q_expr = f"tcell_assays:{tcell_assays}"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.epitope.stream_all_solr(
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


def query_epitope_by_total_assays(total_assays: int, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query epitope by total assays using cursor-based streaming.
    
    Args:
        total_assays: The total assays to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of epitope records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for total_assays (use q_expr instead of fq)
    q_expr = f"total_assays:{total_assays}"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.epitope.stream_all_solr(
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


def query_epitope_by_comment(comment: str, options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query epitope by comment using cursor-based streaming.
    
    Args:
        comment: The comment to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of epitope records, count of results)
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
    
    pager = client.epitope.stream_all_solr(
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


def query_epitope_by_assay_result(assay_result: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query epitope by assay result using cursor-based streaming.
    
    Args:
        assay_result: The assay result to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of epitope records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for assay_result (use q_expr instead of fq)
    q_expr = f"assay_result:{assay_result}"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.epitope.stream_all_solr(
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


def query_epitope_by_taxon_lineage_id(taxon_lineage_id: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query epitope by taxon lineage ID using cursor-based streaming.
    
    Args:
        taxon_lineage_id: The taxon lineage ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of epitope records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for taxon_lineage_id (use q_expr instead of fq)
    q_expr = f"taxon_lineage_id:{taxon_lineage_id}"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.epitope.stream_all_solr(
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


def query_epitope_by_taxon_lineage_name(taxon_lineage_name: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query epitope by taxon lineage name using cursor-based streaming.
    
    Args:
        taxon_lineage_name: The taxon lineage name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of epitope records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for taxon_lineage_name (use q_expr instead of fq)
    q_expr = f'taxon_lineage_name:"{taxon_lineage_name}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.epitope.stream_all_solr(
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


def query_epitope_by_position_range(min_start: int, max_end: int, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query epitope by position range using cursor-based streaming.
    
    Args:
        min_start: Minimum start position
        max_end: Maximum end position
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of epitope records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for position range (use q_expr instead of fq)
    q_expr = f"start:[{min_start} TO {max_end}]"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.epitope.stream_all_solr(
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


def query_epitope_by_total_assays_range(min_assays: int, max_assays: int, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query epitope by total assays range using cursor-based streaming.
    
    Args:
        min_assays: Minimum total assays
        max_assays: Maximum total assays
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of epitope records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for total_assays range (use q_expr instead of fq)
    q_expr = f"total_assays:[{min_assays} TO {max_assays}]"
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.epitope.stream_all_solr(
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


def query_epitope_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query epitope by date inserted range using cursor-based streaming.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of epitope records, count of results)
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
    
    pager = client.epitope.stream_all_solr(
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


def query_epitope_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query epitope by date modified range using cursor-based streaming.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of epitope records, count of results)
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
    
    pager = client.epitope.stream_all_solr(
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


def query_epitope_by_keyword(keyword: str, options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query epitope by keyword using cursor-based streaming.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of epitope records, count of results)
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
    
    pager = client.epitope.stream_all_solr(
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


def query_epitope_all(options: Dict[str, Any] = None,
                     base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query all epitope data using cursor-based streaming.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of epitope records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.epitope.stream_all_solr(
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