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
_default_limit = None

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


def register_experiment_tools(mcp: FastMCP, base_url: str, default_limit: int):
    """Register all experiment-related MCP tools with the Flask app."""
    global _base_url, _default_limit
    _base_url = base_url
    _default_limit = default_limit
    

    
    @mcp.tool()
    def bvbrc_experiment_get_by_id(exp_id: str, limit: int = _default_limit,
                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by experiment ID.
        
        Args:
            exp_id: The experiment ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_id(exp_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by ID: {str(e)}"


    @mcp.tool()
    def bvbrc_experiment_query_by_filters(filters_json: str, limit: int = _default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query experiment data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        try:
            filters = json.loads(filters_json)
        except json.JSONDecodeError as e:
            return f"Error parsing filters JSON: {str(e)}"
        
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_filters(filters, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by filters: {str(e)}"


    @mcp.tool()
    def bvbrc_experiment_get_by_exp_name(exp_name: str, limit: int = _default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by experiment name.
        
        Args:
            exp_name: The experiment name to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_exp_name(exp_name, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by experiment name: {str(e)}"


    @mcp.tool()
    def bvbrc_experiment_get_by_exp_type(exp_type: str, limit: int = _default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by experiment type.
        
        Args:
            exp_type: The experiment type to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_exp_type(exp_type, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by experiment type: {str(e)}"


    @mcp.tool()
    def bvbrc_experiment_get_by_organism(organism: str, limit: int = _default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by organism.
        
        Args:
            organism: The organism to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_organism(organism, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by organism: {str(e)}"


    @mcp.tool()
    def bvbrc_experiment_get_by_strain(strain: str, limit: int = _default_limit,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by strain.
        
        Args:
            strain: The strain to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_strain(strain, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by strain: {str(e)}"


    @mcp.tool()
    def bvbrc_experiment_get_by_genome_id(genome_id: str, limit: int = _default_limit,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by genome ID.
        
        Args:
            genome_id: The genome ID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_genome_id(genome_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by genome ID: {str(e)}"


    @mcp.tool()
    def bvbrc_experiment_get_by_study_name(study_name: str, limit: int = _default_limit,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by study name.
        
        Args:
            study_name: The study name to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_study_name(study_name, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by study name: {str(e)}"


    @mcp.tool()
    def bvbrc_experiment_get_by_study_pi(study_pi: str, limit: int = _default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by study principal investigator.
        
        Args:
            study_pi: The study principal investigator to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_study_pi(study_pi, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by study principal investigator: {str(e)}"


    @mcp.tool()
    def bvbrc_experiment_get_by_pmid(pmid: str, limit: int = _default_limit,
                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by PMID.
        
        Args:
            pmid: The PMID to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_pmid(pmid, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by PMID: {str(e)}"


    @mcp.tool()
    def bvbrc_experiment_get_by_doi(doi: str, limit: int = _default_limit,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by DOI.
        
        Args:
            doi: The DOI to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_doi(doi, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by DOI: {str(e)}"


    @mcp.tool()
    def bvbrc_experiment_get_by_treatment_name(treatment_name: str, limit: int = _default_limit,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by treatment name.
        
        Args:
            treatment_name: The treatment name to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_treatment_name(treatment_name, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by treatment name: {str(e)}"


    @mcp.tool()
    def bvbrc_experiment_get_by_treatment_type(treatment_type: str, limit: int = _default_limit,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by treatment type.
        
        Args:
            treatment_type: The treatment type to query
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_treatment_type(treatment_type, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by treatment type: {str(e)}"


    @mcp.tool()
    def bvbrc_experiment_get_by_biosets_range(min_biosets: int, max_biosets: int, limit: int = _default_limit,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by biosets range.
        
        Args:
            min_biosets: Minimum biosets
            max_biosets: Maximum biosets
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_biosets_range(min_biosets, max_biosets, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by biosets range: {str(e)}"


    @mcp.tool()
    def bvbrc_experiment_get_by_samples_range(min_samples: int, max_samples: int, limit: int = _default_limit,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by samples range.
        
        Args:
            min_samples: Minimum samples
            max_samples: Maximum samples
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_samples_range(min_samples, max_samples, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by samples range: {str(e)}"


    @mcp.tool()
    def bvbrc_experiment_get_by_date_inserted_range(start_date: str, end_date: str, limit: int = _default_limit,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get experiment data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_date_inserted_range(start_date, end_date, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying experiment by date inserted range: {str(e)}"


    @mcp.tool()
    def bvbrc_experiment_search_by_keyword(keyword: str, limit: int = _default_limit,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search experiment data by keyword.
        
        Args:
            keyword: The keyword to search for
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_by_keyword(keyword, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching experiment by keyword: {str(e)}"


    @mcp.tool()
    def bvbrc_experiment_get_all(limit: int = _default_limit,
                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all experiment data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted experiment data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_experiment_all(options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all experiment data: {str(e)}"
