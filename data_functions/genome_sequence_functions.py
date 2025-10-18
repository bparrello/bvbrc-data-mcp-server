"""
BV-BRC Genome Sequence Functions

This module provides wrapper functions for the BV-BRC Solr API genome_sequence resource,
exposing genome sequence querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_genome_sequence_by_id(sequence_id: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by sequence ID.
    
    Args:
        sequence_id: The sequence ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_by_id(sequence_id, options or {})


def query_genome_sequence_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.query_by(filters, options or {})


def query_genome_sequence_by_accession(accession: str, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by accession.
    
    Args:
        accession: The accession to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_by_accession(accession, options or {})


def query_genome_sequence_by_chromosome(chromosome: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by chromosome.
    
    Args:
        chromosome: The chromosome to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_by_chromosome(chromosome, options or {})


def query_genome_sequence_by_description(description: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by description.
    
    Args:
        description: The description to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_by_description(description, options or {})


def query_genome_sequence_by_gc_content(gc_content: float, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by GC content.
    
    Args:
        gc_content: The GC content to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_by_gc_content(gc_content, options or {})


def query_genome_sequence_by_genome_id(genome_id: str, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by genome ID.
    
    Args:
        genome_id: The genome ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_by_genome_id(genome_id, options or {})


def query_genome_sequence_by_genome_name(genome_name: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by genome name.
    
    Args:
        genome_name: The genome name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_by_genome_name(genome_name, options or {})


def query_genome_sequence_by_gi(gi: int, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by GI.
    
    Args:
        gi: The GI to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_by_gi(gi, options or {})


def query_genome_sequence_by_length(length: int, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by length.
    
    Args:
        length: The length to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_by_length(length, options or {})


def query_genome_sequence_by_mol_type(mol_type: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by molecule type.
    
    Args:
        mol_type: The molecule type to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_by_mol_type(mol_type, options or {})


def query_genome_sequence_by_owner(owner: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by owner.
    
    Args:
        owner: The owner to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_by_owner(owner, options or {})


def query_genome_sequence_by_p2_sequence_id(p2_sequence_id: int, options: Dict[str, Any] = None,
                                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by P2 sequence ID.
    
    Args:
        p2_sequence_id: The P2 sequence ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_by_p2_sequence_id(p2_sequence_id, options or {})


def query_genome_sequence_by_plasmid(plasmid: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by plasmid.
    
    Args:
        plasmid: The plasmid to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_by_plasmid(plasmid, options or {})


def query_genome_sequence_by_public_status(is_public: bool, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by public status.
    
    Args:
        is_public: The public status to query (True/False)
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_by_public_status(is_public, options or {})


def query_genome_sequence_by_segment(segment: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by segment.
    
    Args:
        segment: The segment to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_by_segment(segment, options or {})


def query_genome_sequence_by_sequence_md5(sequence_md5: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by sequence MD5.
    
    Args:
        sequence_md5: The sequence MD5 to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_by_sequence_md5(sequence_md5, options or {})


def query_genome_sequence_by_sequence_status(sequence_status: str, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by sequence status.
    
    Args:
        sequence_status: The sequence status to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_by_sequence_status(sequence_status, options or {})


def query_genome_sequence_by_sequence_type(sequence_type: str, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by sequence type.
    
    Args:
        sequence_type: The sequence type to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_by_sequence_type(sequence_type, options or {})


def query_genome_sequence_by_taxon_id(taxon_id: int, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by taxon ID.
    
    Args:
        taxon_id: The taxon ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_by_taxon_id(taxon_id, options or {})


def query_genome_sequence_by_topology(topology: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by topology.
    
    Args:
        topology: The topology to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_by_topology(topology, options or {})


def query_genome_sequence_by_version(version: int, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by version.
    
    Args:
        version: The version to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_by_version(version, options or {})


def query_genome_sequence_by_length_range(min_length: int, max_length: int, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by length range.
    
    Args:
        min_length: Minimum length
        max_length: Maximum length
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_by_length_range(min_length, max_length, options or {})


def query_genome_sequence_by_gc_content_range(min_gc_content: float, max_gc_content: float, options: Dict[str, Any] = None,
                                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by GC content range.
    
    Args:
        min_gc_content: Minimum GC content
        max_gc_content: Maximum GC content
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_by_gc_content_range(min_gc_content, max_gc_content, options or {})


def query_genome_sequence_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by date inserted range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_by_date_inserted_range(start_date, end_date, options or {})


def query_genome_sequence_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by date modified range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_by_date_modified_range(start_date, end_date, options or {})


def query_genome_sequence_by_release_date_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome sequence by release date range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_by_release_date_range(start_date, end_date, options or {})


def query_genome_sequence_by_keyword(keyword: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search genome sequence by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.search_by_keyword(keyword, options or {})


def query_genome_sequence_all(options: Dict[str, Any] = None,
                             base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all genome sequence data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all genome sequence records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome_sequence.get_all(options or {})
