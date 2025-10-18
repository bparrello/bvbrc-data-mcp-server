"""
BV-BRC Genome Functions

This module provides genome querying functions for the BV-BRC Solr API.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_genome_by_id(genome_id: str, options: Dict[str, Any] = None, 
                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genome by ID.
    
    Args:
        genome_id: The genome ID to query
        options: Optional query options (limit, select, sort, etc.)
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome.get_by_id(genome_id, options or {})


def query_genome_by_taxon_id(taxon_id: int, options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genomes by taxon ID.
    
    Args:
        taxon_id: The taxon ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome.get_by_taxon_id(taxon_id, options or {})


def query_genome_by_genome_name(genome_name: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genomes by genome name.

    Args:
        genome_name: The genome name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome.get_by_genome_name(genome_name, options or {})


def query_genome_by_species(species: str, options: Dict[str, Any] = None,
                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genomes by species.
    
    Args:
        species: The species name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome.get_by_species(species, options or {})


def query_genome_by_genus(genus: str, options: Dict[str, Any] = None,
                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genomes by genus.
    
    Args:
        genus: The genus name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome.get_by_genus(genus, options or {})


def query_genome_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query genomes by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of genome records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.genome.query_by(filters, options or {})
