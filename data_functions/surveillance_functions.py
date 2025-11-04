"""
BV-BRC Surveillance Functions

This module provides surveillance querying functions for the BV-BRC Solr API.
"""

from typing import Any, Dict, List, Tuple
from .common_functions import create_bvbrc_client


def query_surveillance_by_id(id: str, options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query surveillance by ID using cursor-based streaming.
    
    Args:
        id: The ID to query
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
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
    
    pager = client.surveillance.stream_all_solr(
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


def query_surveillance_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query surveillance by custom filters using cursor-based streaming.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
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
    
    pager = client.surveillance.stream_all_solr(
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


def query_surveillance_by_host_species(host_species: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query surveillance by host species using cursor-based streaming.
    
    Args:
        host_species: The host species to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for host_species (use q_expr instead of fq)
    q_expr = f'host_species:"{host_species}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.surveillance.stream_all_solr(
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


def query_surveillance_by_host_common_name(host_common_name: str, options: Dict[str, Any] = None,
                                           base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query surveillance by host common name using cursor-based streaming.
    
    Args:
        host_common_name: The host common name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for host_common_name (use q_expr instead of fq)
    q_expr = f'host_common_name:"{host_common_name}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.surveillance.stream_all_solr(
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


def query_surveillance_by_sample_identifier(sample_identifier: str, options: Dict[str, Any] = None,
                                           base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query surveillance by sample identifier using cursor-based streaming.
    
    Args:
        sample_identifier: The sample identifier to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for sample_identifier (use q_expr instead of fq)
    q_expr = f'sample_identifier:"{sample_identifier}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.surveillance.stream_all_solr(
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


def query_surveillance_by_sample_accession(sample_accession: str, options: Dict[str, Any] = None,
                                           base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query surveillance by sample accession using cursor-based streaming.
    
    Args:
        sample_accession: The sample accession to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for sample_accession (use q_expr instead of fq)
    q_expr = f'sample_accession:"{sample_accession}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.surveillance.stream_all_solr(
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


def query_surveillance_by_collection_country(collection_country: str, options: Dict[str, Any] = None,
                                             base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query surveillance by collection country using cursor-based streaming.
    
    Args:
        collection_country: The collection country to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for collection_country (use q_expr instead of fq)
    q_expr = f'collection_country:"{collection_country}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.surveillance.stream_all_solr(
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


def query_surveillance_by_collection_city(collection_city: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query surveillance by collection city using cursor-based streaming.
    
    Args:
        collection_city: The collection city to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for collection_city (use q_expr instead of fq)
    q_expr = f'collection_city:"{collection_city}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.surveillance.stream_all_solr(
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


def query_surveillance_by_collection_year(collection_year: str, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query surveillance by collection year using cursor-based streaming.
    
    Args:
        collection_year: The collection year to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for collection_year (use q_expr instead of fq)
    q_expr = f'collection_year:"{collection_year}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.surveillance.stream_all_solr(
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


def query_surveillance_by_species(species: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query surveillance by species using cursor-based streaming.
    
    Args:
        species: The species to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for species (use q_expr instead of fq)
    q_expr = f'species:"{species}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.surveillance.stream_all_solr(
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


def query_surveillance_by_strain(strain: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query surveillance by strain using cursor-based streaming.
    
    Args:
        strain: The strain to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for strain (use q_expr instead of fq)
    q_expr = f'strain:"{strain}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.surveillance.stream_all_solr(
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


def query_surveillance_by_subtype(subtype: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query surveillance by subtype using cursor-based streaming.
    
    Args:
        subtype: The subtype to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for subtype (use q_expr instead of fq)
    q_expr = f'subtype:"{subtype}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.surveillance.stream_all_solr(
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


def query_surveillance_by_pathogen_type(pathogen_type: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query surveillance by pathogen type using cursor-based streaming.
    
    Args:
        pathogen_type: The pathogen type to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for pathogen_type (use q_expr instead of fq)
    q_expr = f'pathogen_type:"{pathogen_type}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.surveillance.stream_all_solr(
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


def query_surveillance_by_genome_id(genome_id: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query surveillance by genome ID using cursor-based streaming.
    
    Args:
        genome_id: The genome ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
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
    
    pager = client.surveillance.stream_all_solr(
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


def query_surveillance_by_disease_status(disease_status: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query surveillance by disease status using cursor-based streaming.
    
    Args:
        disease_status: The disease status to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for disease_status (use q_expr instead of fq)
    q_expr = f'disease_status:"{disease_status}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.surveillance.stream_all_solr(
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


def query_surveillance_by_diagnosis(diagnosis: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query surveillance by diagnosis using cursor-based streaming.
    
    Args:
        diagnosis: The diagnosis to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for diagnosis (use q_expr instead of fq)
    q_expr = f'diagnosis:"{diagnosis}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.surveillance.stream_all_solr(
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


def query_surveillance_by_treatment(treatment: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query surveillance by treatment using cursor-based streaming.
    
    Args:
        treatment: The treatment to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for treatment (use q_expr instead of fq)
    q_expr = f'treatment:"{treatment}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.surveillance.stream_all_solr(
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


def query_surveillance_by_hospitalized(hospitalized: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query surveillance by hospitalized status using cursor-based streaming.
    
    Args:
        hospitalized: The hospitalized status to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for hospitalized (use q_expr instead of fq)
    q_expr = f'hospitalized:"{hospitalized}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.surveillance.stream_all_solr(
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


def query_surveillance_by_vaccination_type(vaccination_type: str, options: Dict[str, Any] = None,
                                           base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query surveillance by vaccination type using cursor-based streaming.
    
    Args:
        vaccination_type: The vaccination type to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for vaccination_type (use q_expr instead of fq)
    q_expr = f'vaccination_type:"{vaccination_type}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.surveillance.stream_all_solr(
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


def query_surveillance_by_exposure(exposure: str, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query surveillance by exposure using cursor-based streaming.
    
    Args:
        exposure: The exposure to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for exposure (use q_expr instead of fq)
    q_expr = f'exposure:"{exposure}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.surveillance.stream_all_solr(
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


def query_surveillance_by_pathogen_test_type(pathogen_test_type: str, options: Dict[str, Any] = None,
                                             base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query surveillance by pathogen test type using cursor-based streaming.
    
    Args:
        pathogen_test_type: The pathogen test type to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for pathogen_test_type (use q_expr instead of fq)
    q_expr = f'pathogen_test_type:"{pathogen_test_type}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.surveillance.stream_all_solr(
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


def query_surveillance_by_pathogen_test_result(pathogen_test_result: str, options: Dict[str, Any] = None,
                                               base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query surveillance by pathogen test result using cursor-based streaming.
    
    Args:
        pathogen_test_result: The pathogen test result to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for pathogen_test_result (use q_expr instead of fq)
    q_expr = f'pathogen_test_result:"{pathogen_test_result}"'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.surveillance.stream_all_solr(
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


def query_surveillance_by_collection_date_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                                base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query surveillance by collection date range using cursor-based streaming.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Build query expression for collection_date range (use q_expr instead of fq)
    q_expr = f'collection_date:[{start_date} TO {end_date}]'
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.surveillance.stream_all_solr(
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


def query_surveillance_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                               base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query surveillance by date inserted range using cursor-based streaming.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
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
    
    pager = client.surveillance.stream_all_solr(
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


def query_surveillance_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                              base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query surveillance by date modified range using cursor-based streaming.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
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
    
    pager = client.surveillance.stream_all_solr(
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


def query_surveillance_by_keyword(keyword: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query surveillance by keyword using cursor-based streaming.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
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
    
    pager = client.surveillance.stream_all_solr(
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


def query_surveillance_all(options: Dict[str, Any] = None,
                           base_url: str = None, headers: Dict[str, str] = None) -> Tuple[List[Dict[str, Any]], int]:
    """
    Query all surveillance data using cursor-based streaming.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        Tuple of (list of surveillance records, count of results)
    """
    client = create_bvbrc_client(base_url, headers)
    options = options or {}
    
    # Convert limit to rows for cursor pagination
    rows = options.get("limit", 1000)
    if "limit" in options:
        del options["limit"]
    options["rows"] = rows
    
    pager = client.surveillance.stream_all_solr(
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