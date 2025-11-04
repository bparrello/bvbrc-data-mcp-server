#!/usr/bin/env python3
"""
BV-BRC Experiment Tools

This module contains MCP tools for querying experiment data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None

from data_functions import (
    query_experiment_by_id,
    query_experiment_by_filters,
    query_experiment_by_exp_name,
    query_experiment_by_exp_type,
    query_experiment_by_exp_description,
    query_experiment_by_exp_title,
    query_experiment_by_organism,
    query_experiment_by_strain,
    query_experiment_by_genome_id,
    query_experiment_by_taxon_id,
    query_experiment_by_study_name,
    query_experiment_by_study_title,
    query_experiment_by_study_pi,
    query_experiment_by_study_institution,
    query_experiment_by_experimenters,
    query_experiment_by_measurement_technique,
    query_experiment_by_detection_instrument,
    query_experiment_by_pmid,
    query_experiment_by_doi,
    query_experiment_by_public_identifier,
    query_experiment_by_public_repository,
    query_experiment_by_biosets,
    query_experiment_by_samples,
    query_experiment_by_treatment_name,
    query_experiment_by_treatment_type,
    query_experiment_by_treatment_amount,
    query_experiment_by_treatment_duration,
    query_experiment_by_date_inserted_range,
    query_experiment_by_date_modified_range,
    query_experiment_by_biosets_range,
    query_experiment_by_samples_range,
    query_experiment_by_keyword,
    query_experiment_all,
    format_query_result
)

def register_experiment_tools(mcp: FastMCP, base_url: str):
    """Register all experiment-related MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    
    @mcp.tool()
    def bvbrc_experiment_get_by_id(exp_id: str,
                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by experiment ID.
        
        Args:
            exp_id: The experiment ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_id(exp_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_query_by_filters(filters_json: str,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query experiment data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        try:
            filters = json.loads(filters_json)
        except json.JSONDecodeError as e:
            return f"Error parsing filters JSON: {str(e)}"
        
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_filters(filters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by filters: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_exp_name(exp_name: str,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by experiment name.
        
        Args:
            exp_name: The experiment name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_exp_name(exp_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by experiment name: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_exp_type(exp_type: str,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by experiment type.
        
        Args:
            exp_type: The experiment type to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_exp_type(exp_type, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by experiment type: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_exp_description(exp_description: str,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by experiment description.
        
        Args:
            exp_description: The experiment description to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_exp_description(exp_description, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by experiment description: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_exp_title(exp_title: str,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by experiment title.
        
        Args:
            exp_title: The experiment title to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_exp_title(exp_title, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by experiment title: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_organism(organism: str,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by organism.
        
        Args:
            organism: The organism to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_organism(organism, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by organism: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_strain(strain: str,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by strain.
        
        Args:
            strain: The strain to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_strain(strain, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by strain: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_genome_id(genome_id: str,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by genome ID.
        
        Args:
            genome_id: The genome ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_genome_id(genome_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by genome ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_taxon_id(taxon_id: int,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_taxon_id(taxon_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by taxon ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_study_name(study_name: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by study name.
        
        Args:
            study_name: The study name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_study_name(study_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by study name: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_study_title(study_title: str,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by study title.
        
        Args:
            study_title: The study title to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_study_title(study_title, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by study title: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_study_pi(study_pi: str,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by study principal investigator.
        
        Args:
            study_pi: The study principal investigator to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_study_pi(study_pi, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by study principal investigator: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_study_institution(study_institution: str,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by study institution.
        
        Args:
            study_institution: The study institution to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_study_institution(study_institution, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by study institution: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_experimenters(experimenters: str,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by experimenters.
        
        Args:
            experimenters: The experimenters to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_experimenters(experimenters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by experimenters: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_measurement_technique(measurement_technique: str,
                                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by measurement technique.
        
        Args:
            measurement_technique: The measurement technique to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_measurement_technique(measurement_technique, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by measurement technique: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_detection_instrument(detection_instrument: str,
                                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by detection instrument.
        
        Args:
            detection_instrument: The detection instrument to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_detection_instrument(detection_instrument, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by detection instrument: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_pmid(pmid: str,
                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by PMID.
        
        Args:
            pmid: The PMID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_pmid(pmid, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by PMID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_doi(doi: str,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by DOI.
        
        Args:
            doi: The DOI to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_doi(doi, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by DOI: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_public_identifier(public_identifier: str,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by public identifier.
        
        Args:
            public_identifier: The public identifier to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_public_identifier(public_identifier, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by public identifier: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_public_repository(public_repository: str,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by public repository.
        
        Args:
            public_repository: The public repository to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_public_repository(public_repository, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by public repository: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_biosets(biosets: int,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by biosets.
        
        Args:
            biosets: The biosets to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_biosets(biosets, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by biosets: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_samples(samples: int,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by samples.
        
        Args:
            samples: The samples to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_samples(samples, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by samples: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_treatment_name(treatment_name: str,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by treatment name.
        
        Args:
            treatment_name: The treatment name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_treatment_name(treatment_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by treatment name: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_treatment_type(treatment_type: str,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by treatment type.
        
        Args:
            treatment_type: The treatment type to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_treatment_type(treatment_type, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by treatment type: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_treatment_amount(treatment_amount: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by treatment amount.
        
        Args:
            treatment_amount: The treatment amount to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_treatment_amount(treatment_amount, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by treatment amount: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_treatment_duration(treatment_duration: str,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by treatment duration.
        
        Args:
            treatment_duration: The treatment duration to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_treatment_duration(treatment_duration, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by treatment duration: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_biosets_range(min_biosets: int, max_biosets: int,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by biosets range.
        
        Args:
            min_biosets: Minimum biosets
            max_biosets: Maximum biosets
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_biosets_range(min_biosets, max_biosets, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by biosets range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_samples_range(min_samples: int, max_samples: int,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by samples range.
        
        Args:
            min_samples: Minimum samples
            max_samples: Maximum samples
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_samples_range(min_samples, max_samples, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by samples range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_date_inserted_range(start_date: str, end_date: str,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_date_inserted_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by date inserted range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_by_date_modified_range(start_date: str, end_date: str,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by date modified range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_date_modified_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying experiment by date modified range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_search_by_keyword(keyword: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search experiment data by keyword.
        
        Args:
            keyword: The keyword to search for
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_by_keyword(keyword, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error searching experiment by keyword: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_experiment_get_all(select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all experiment data.
        
        Args:
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_experiment_all(options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying all experiment data: {str(e)}"
            }, indent=2)