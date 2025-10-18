"""
BV-BRC Protein Structure Functions

This module provides wrapper functions for the BV-BRC Solr API protein_structure resource,
exposing protein structure querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_protein_structure_by_id(pdb_id: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein structure by PDB ID.
    
    Args:
        pdb_id: The PDB ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.get_by_id(pdb_id, options or {})


def query_protein_structure_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein structure by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.query_by(filters, options or {})


def query_protein_structure_by_feature_id(feature_id: str, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein structure by feature ID.
    
    Args:
        feature_id: The feature ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.get_by_feature_id(feature_id, options or {})


def query_protein_structure_by_genome_id(genome_id: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein structure by genome ID.
    
    Args:
        genome_id: The genome ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.get_by_genome_id(genome_id, options or {})


def query_protein_structure_by_patric_id(patric_id: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein structure by PATRIC ID.
    
    Args:
        patric_id: The PATRIC ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.get_by_patric_id(patric_id, options or {})


def query_protein_structure_by_organism_name(organism_name: str, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein structure by organism name.
    
    Args:
        organism_name: The organism name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.get_by_organism_name(organism_name, options or {})


def query_protein_structure_by_title(title: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein structure by title.
    
    Args:
        title: The title to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.get_by_title(title, options or {})


def query_protein_structure_by_resolution(resolution: str, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein structure by resolution.
    
    Args:
        resolution: The resolution to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.get_by_resolution(resolution, options or {})


def query_protein_structure_by_institution(institution: str, options: Dict[str, Any] = None,
                                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein structure by institution.
    
    Args:
        institution: The institution to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.get_by_institution(institution, options or {})


def query_protein_structure_by_file_path(file_path: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein structure by file path.
    
    Args:
        file_path: The file path to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.get_by_file_path(file_path, options or {})


def query_protein_structure_by_author(author: str, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein structure by author.
    
    Args:
        author: The author to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.get_by_author(author, options or {})


def query_protein_structure_by_method(method: str, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein structure by method.
    
    Args:
        method: The method to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.get_by_method(method, options or {})


def query_protein_structure_by_gene(gene: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein structure by gene.
    
    Args:
        gene: The gene to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.get_by_gene(gene, options or {})


def query_protein_structure_by_product(product: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein structure by product.
    
    Args:
        product: The product to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.get_by_product(product, options or {})


def query_protein_structure_by_sequence(sequence: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein structure by sequence.
    
    Args:
        sequence: The sequence to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.get_by_sequence(sequence, options or {})


def query_protein_structure_by_sequence_md5(sequence_md5: str, options: Dict[str, Any] = None,
                                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein structure by sequence MD5.
    
    Args:
        sequence_md5: The sequence MD5 to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.get_by_sequence_md5(sequence_md5, options or {})


def query_protein_structure_by_uniprotkb_accession(uniprotkb_accession: str, options: Dict[str, Any] = None,
                                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein structure by UniProtKB accession.
    
    Args:
        uniprotkb_accession: The UniProtKB accession to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.get_by_uniprotkb_accession(uniprotkb_accession, options or {})


def query_protein_structure_by_pmid(pmid: str, options: Dict[str, Any] = None,
                                    base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein structure by PMID.
    
    Args:
        pmid: The PMID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.get_by_pmid(pmid, options or {})


def query_protein_structure_by_taxon_id(taxon_id: int, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein structure by taxon ID.
    
    Args:
        taxon_id: The taxon ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.get_by_taxon_id(taxon_id, options or {})


def query_protein_structure_by_taxon_lineage_id(taxon_lineage_id: str, options: Dict[str, Any] = None,
                                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein structure by taxon lineage ID.
    
    Args:
        taxon_lineage_id: The taxon lineage ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.get_by_taxon_lineage_id(taxon_lineage_id, options or {})


def query_protein_structure_by_taxon_lineage_name(taxon_lineage_name: str, options: Dict[str, Any] = None,
                                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein structure by taxon lineage name.
    
    Args:
        taxon_lineage_name: The taxon lineage name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.get_by_taxon_lineage_name(taxon_lineage_name, options or {})


def query_protein_structure_by_alignment(alignment: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein structure by alignment.
    
    Args:
        alignment: The alignment to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.get_by_alignment(alignment, options or {})


def query_protein_structure_by_release_date_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein structure by release date range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.get_by_release_date_range(start_date, end_date, options or {})


def query_protein_structure_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein structure by date inserted range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.get_by_date_inserted_range(start_date, end_date, options or {})


def query_protein_structure_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query protein structure by date modified range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.get_by_date_modified_range(start_date, end_date, options or {})


def query_protein_structure_by_keyword(keyword: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search protein structure by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.search_by_keyword(keyword, options or {})


def query_protein_structure_all(options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all protein structure data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all protein structure records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.protein_structure.get_all(options or {})
