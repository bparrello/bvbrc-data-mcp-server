"""
BV-BRC Experiment Functions

This module provides wrapper functions for the BV-BRC Solr API experiment resource,
exposing experiment querying capabilities through a simplified interface.
"""

from typing import Any, Dict, List
from .common_functions import create_bvbrc_client


def query_experiment_by_id(exp_id: str, options: Dict[str, Any] = None,
                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by experiment ID.
    
    Args:
        exp_id: The experiment ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_id(exp_id, options or {})


def query_experiment_by_filters(filters: Dict[str, Any], options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by custom filters.
    
    Args:
        filters: Dictionary of filter criteria
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.query_by(filters, options or {})


def query_experiment_by_additional_data(additional_data: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by additional data.
    
    Args:
        additional_data: The additional data to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_additional_data(additional_data, options or {})


def query_experiment_by_additional_metadata(additional_metadata: str, options: Dict[str, Any] = None,
                                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by additional metadata.
    
    Args:
        additional_metadata: The additional metadata to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_additional_metadata(additional_metadata, options or {})


def query_experiment_by_biosets(biosets: int, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by biosets.
    
    Args:
        biosets: The biosets to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_biosets(biosets, options or {})


def query_experiment_by_detection_instrument(detection_instrument: str, options: Dict[str, Any] = None,
                                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by detection instrument.
    
    Args:
        detection_instrument: The detection instrument to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_detection_instrument(detection_instrument, options or {})


def query_experiment_by_doi(doi: str, options: Dict[str, Any] = None,
                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by DOI.
    
    Args:
        doi: The DOI to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_doi(doi, options or {})


def query_experiment_by_exp_description(exp_description: str, options: Dict[str, Any] = None,
                                       base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by experiment description.
    
    Args:
        exp_description: The experiment description to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_exp_description(exp_description, options or {})


def query_experiment_by_exp_name(exp_name: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by experiment name.
    
    Args:
        exp_name: The experiment name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_exp_name(exp_name, options or {})


def query_experiment_by_exp_poc(exp_poc: str, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by experiment point of contact.
    
    Args:
        exp_poc: The experiment point of contact to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_exp_poc(exp_poc, options or {})


def query_experiment_by_exp_protocol(exp_protocol: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by experiment protocol.
    
    Args:
        exp_protocol: The experiment protocol to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_exp_protocol(exp_protocol, options or {})


def query_experiment_by_exp_title(exp_title: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by experiment title.
    
    Args:
        exp_title: The experiment title to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_exp_title(exp_title, options or {})


def query_experiment_by_exp_type(exp_type: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by experiment type.
    
    Args:
        exp_type: The experiment type to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_exp_type(exp_type, options or {})


def query_experiment_by_experimenters(experimenters: str, options: Dict[str, Any] = None,
                                     base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by experimenters.
    
    Args:
        experimenters: The experimenters to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_experimenters(experimenters, options or {})


def query_experiment_by_genome_id(genome_id: str, options: Dict[str, Any] = None,
                                  base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by genome ID.
    
    Args:
        genome_id: The genome ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_genome_id(genome_id, options or {})


def query_experiment_by_measurement_technique(measurement_technique: str, options: Dict[str, Any] = None,
                                              base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by measurement technique.
    
    Args:
        measurement_technique: The measurement technique to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_measurement_technique(measurement_technique, options or {})


def query_experiment_by_organism(organism: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by organism.
    
    Args:
        organism: The organism to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_organism(organism, options or {})


def query_experiment_by_pmid(pmid: str, options: Dict[str, Any] = None,
                            base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by PMID.
    
    Args:
        pmid: The PMID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_pmid(pmid, options or {})


def query_experiment_by_public_identifier(public_identifier: str, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by public identifier.
    
    Args:
        public_identifier: The public identifier to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_public_identifier(public_identifier, options or {})


def query_experiment_by_public_repository(public_repository: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by public repository.
    
    Args:
        public_repository: The public repository to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_public_repository(public_repository, options or {})


def query_experiment_by_samples(samples: int, options: Dict[str, Any] = None,
                                base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by samples.
    
    Args:
        samples: The samples to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_samples(samples, options or {})


def query_experiment_by_strain(strain: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by strain.
    
    Args:
        strain: The strain to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_strain(strain, options or {})


def query_experiment_by_study_description(study_description: str, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by study description.
    
    Args:
        study_description: The study description to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_study_description(study_description, options or {})


def query_experiment_by_study_institution(study_institution: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by study institution.
    
    Args:
        study_institution: The study institution to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_study_institution(study_institution, options or {})


def query_experiment_by_study_name(study_name: str, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by study name.
    
    Args:
        study_name: The study name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_study_name(study_name, options or {})


def query_experiment_by_study_pi(study_pi: str, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by study principal investigator.
    
    Args:
        study_pi: The study principal investigator to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_study_pi(study_pi, options or {})


def query_experiment_by_study_title(study_title: str, options: Dict[str, Any] = None,
                                   base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by study title.
    
    Args:
        study_title: The study title to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_study_title(study_title, options or {})


def query_experiment_by_taxon_id(taxon_id: int, options: Dict[str, Any] = None,
                                 base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by taxon ID.
    
    Args:
        taxon_id: The taxon ID to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_taxon_id(taxon_id, options or {})


def query_experiment_by_taxon_lineage_ids(taxon_lineage_ids: str, options: Dict[str, Any] = None,
                                         base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by taxon lineage IDs.
    
    Args:
        taxon_lineage_ids: The taxon lineage IDs to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_taxon_lineage_ids(taxon_lineage_ids, options or {})


def query_experiment_by_treatment_amount(treatment_amount: str, options: Dict[str, Any] = None,
                                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by treatment amount.
    
    Args:
        treatment_amount: The treatment amount to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_treatment_amount(treatment_amount, options or {})


def query_experiment_by_treatment_duration(treatment_duration: str, options: Dict[str, Any] = None,
                                          base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by treatment duration.
    
    Args:
        treatment_duration: The treatment duration to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_treatment_duration(treatment_duration, options or {})


def query_experiment_by_treatment_name(treatment_name: str, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by treatment name.
    
    Args:
        treatment_name: The treatment name to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_treatment_name(treatment_name, options or {})


def query_experiment_by_treatment_type(treatment_type: str, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by treatment type.
    
    Args:
        treatment_type: The treatment type to query
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_treatment_type(treatment_type, options or {})


def query_experiment_by_date_inserted_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by date inserted range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_date_inserted_range(start_date, end_date, options or {})


def query_experiment_by_date_modified_range(start_date: str, end_date: str, options: Dict[str, Any] = None,
                                           base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by date modified range.
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_date_modified_range(start_date, end_date, options or {})


def query_experiment_by_biosets_range(min_biosets: int, max_biosets: int, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by biosets range.
    
    Args:
        min_biosets: Minimum biosets
        max_biosets: Maximum biosets
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_biosets_range(min_biosets, max_biosets, options or {})


def query_experiment_by_samples_range(min_samples: int, max_samples: int, options: Dict[str, Any] = None,
                                      base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Query experiment by samples range.
    
    Args:
        min_samples: Minimum samples
        max_samples: Maximum samples
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_by_samples_range(min_samples, max_samples, options or {})


def query_experiment_by_keyword(keyword: str, options: Dict[str, Any] = None,
                               base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Search experiment by keyword.
    
    Args:
        keyword: The keyword to search for
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.search_by_keyword(keyword, options or {})


def query_experiment_all(options: Dict[str, Any] = None,
                        base_url: str = None, headers: Dict[str, str] = None) -> List[Dict[str, Any]]:
    """
    Get all experiment data.
    
    Args:
        options: Optional query options
        base_url: Optional base URL override
        headers: Optional headers override
        
    Returns:
        List of all experiment records
    """
    client = create_bvbrc_client(base_url, headers)
    return client.experiment.get_all(options or {})
