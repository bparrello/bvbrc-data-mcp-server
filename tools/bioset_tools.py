#!/usr/bin/env python3
"""
BV-BRC Bioset Tools

This module contains MCP tools for querying bioset data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None
_default_limit = None

from data_functions import (
    query_bioset_by_id,
    query_bioset_by_filters,
    query_bioset_by_name,
    query_bioset_by_type,
    query_bioset_by_exp_id,
    query_bioset_by_exp_name,
    query_bioset_by_exp_type,
    query_bioset_by_organism,
    query_bioset_by_strain,
    query_bioset_by_taxon_id,
    query_bioset_by_entity_type,
    query_bioset_by_result_type,
    query_bioset_by_analysis_method,
    query_bioset_by_analysis_group_1,
    query_bioset_by_analysis_group_2,
    query_bioset_by_treatment_type,
    query_bioset_by_treatment_name,
    query_bioset_by_study_name,
    query_bioset_by_study_pi,
    query_bioset_by_study_institution,
    query_bioset_by_genome_id,
    query_bioset_by_date_range,
    query_bioset_by_modified_date_range,
    query_bioset_by_keyword,
    query_bioset_all,
    format_query_result
)


def register_bioset_tools(mcp: FastMCP, base_url: str, default_limit: int):
    """Register all bioset-related MCP tools with the Flask app."""
    global _base_url, _default_limit
    _base_url = base_url
    _default_limit = default_limit
    

    
    @mcp.tool()
    def bvbrc_bioset_get_by_id(bioset_id: str, limit: int = _default_limit, 
                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by bioset ID.
        
        Args:
            bioset_id: The bioset ID to query (e.g., "bs12345")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_bioset_by_id(bioset_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying bioset by ID: {str(e)}"


    @mcp.tool()
    def bvbrc_bioset_query_by_filters(filters_json: str, limit: int = _default_limit,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query bioset data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria (e.g., '{"bioset_name": "RNA-seq", "organism": "Escherichia coli"}')
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
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
            result = query_bioset_by_filters(filters, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying bioset by filters: {str(e)}"


    @mcp.tool()
    def bvbrc_bioset_get_by_name(bioset_name: str, limit: int = _default_limit,
                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by bioset name.
        
        Args:
            bioset_name: The bioset name to query (e.g., "RNA-seq")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_bioset_by_name(bioset_name, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying bioset by name: {str(e)}"


    @mcp.tool()
    def bvbrc_bioset_get_by_type(bioset_type: str, limit: int = _default_limit,
                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by bioset type.
        
        Args:
            bioset_type: The bioset type to query (e.g., "RNA-seq")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_bioset_by_type(bioset_type, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying bioset by type: {str(e)}"


    @mcp.tool()
    def bvbrc_bioset_get_by_exp_id(exp_id: str, limit: int = _default_limit,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by experiment ID.
        
        Args:
            exp_id: The experiment ID to query (e.g., "exp12345")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_bioset_by_exp_id(exp_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying bioset by experiment ID: {str(e)}"


    @mcp.tool()
    def bvbrc_bioset_get_by_exp_name(exp_name: str, limit: int = _default_limit,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by experiment name.
        
        Args:
            exp_name: The experiment name to query (e.g., "RNA-seq experiment")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_bioset_by_exp_name(exp_name, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying bioset by experiment name: {str(e)}"


    @mcp.tool()
    def bvbrc_bioset_get_by_exp_type(exp_type: str, limit: int = _default_limit,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by experiment type.
        
        Args:
            exp_type: The experiment type to query (e.g., "RNA-seq")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_bioset_by_exp_type(exp_type, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying bioset by experiment type: {str(e)}"


    @mcp.tool()
    def bvbrc_bioset_get_by_organism(organism: str, limit: int = _default_limit,
                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by organism.
        
        Args:
            organism: The organism to query (e.g., "Escherichia coli")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_bioset_by_organism(organism, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying bioset by organism: {str(e)}"


    @mcp.tool()
    def bvbrc_bioset_get_by_strain(strain: str, limit: int = _default_limit,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by strain.
        
        Args:
            strain: The strain to query (e.g., "K-12")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_bioset_by_strain(strain, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying bioset by strain: {str(e)}"


    @mcp.tool()
    def bvbrc_bioset_get_by_taxon_id(taxon_id: int, limit: int = _default_limit,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query (e.g., 562)
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_bioset_by_taxon_id(taxon_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying bioset by taxon ID: {str(e)}"


    @mcp.tool()
    def bvbrc_bioset_get_by_entity_type(entity_type: str, limit: int = _default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by entity type.
        
        Args:
            entity_type: The entity type to query (e.g., "gene")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_bioset_by_entity_type(entity_type, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying bioset by entity type: {str(e)}"


    @mcp.tool()
    def bvbrc_bioset_get_by_result_type(result_type: str, limit: int = _default_limit,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by result type.
        
        Args:
            result_type: The result type to query (e.g., "differential_expression")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_bioset_by_result_type(result_type, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying bioset by result type: {str(e)}"


    @mcp.tool()
    def bvbrc_bioset_get_by_analysis_method(analysis_method: str, limit: int = _default_limit,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by analysis method.
        
        Args:
            analysis_method: The analysis method to query (e.g., "DESeq2")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_bioset_by_analysis_method(analysis_method, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying bioset by analysis method: {str(e)}"


    @mcp.tool()
    def bvbrc_bioset_get_by_analysis_group_1(analysis_group_1: str, limit: int = _default_limit,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by analysis group 1.
        
        Args:
            analysis_group_1: The analysis group 1 to query (e.g., "control")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_bioset_by_analysis_group_1(analysis_group_1, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying bioset by analysis group 1: {str(e)}"


    @mcp.tool()
    def bvbrc_bioset_get_by_analysis_group_2(analysis_group_2: str, limit: int = _default_limit,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by analysis group 2.
        
        Args:
            analysis_group_2: The analysis group 2 to query (e.g., "treatment")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_bioset_by_analysis_group_2(analysis_group_2, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying bioset by analysis group 2: {str(e)}"


    @mcp.tool()
    def bvbrc_bioset_get_by_treatment_type(treatment_type: str, limit: int = _default_limit,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by treatment type.
        
        Args:
            treatment_type: The treatment type to query (e.g., "antibiotic")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_bioset_by_treatment_type(treatment_type, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying bioset by treatment type: {str(e)}"


    @mcp.tool()
    def bvbrc_bioset_get_by_treatment_name(treatment_name: str, limit: int = _default_limit,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by treatment name.
        
        Args:
            treatment_name: The treatment name to query (e.g., "ampicillin")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_bioset_by_treatment_name(treatment_name, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying bioset by treatment name: {str(e)}"


    @mcp.tool()
    def bvbrc_bioset_get_by_study_name(study_name: str, limit: int = _default_limit,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by study name.
        
        Args:
            study_name: The study name to query (e.g., "Antibiotic resistance study")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_bioset_by_study_name(study_name, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying bioset by study name: {str(e)}"


    @mcp.tool()
    def bvbrc_bioset_get_by_study_pi(study_pi: str, limit: int = _default_limit,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by study PI.
        
        Args:
            study_pi: The study PI to query (e.g., "Dr. Smith")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_bioset_by_study_pi(study_pi, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying bioset by study PI: {str(e)}"


    @mcp.tool()
    def bvbrc_bioset_get_by_study_institution(study_institution: str, limit: int = _default_limit,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by study institution.
        
        Args:
            study_institution: The study institution to query (e.g., "University of California")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_bioset_by_study_institution(study_institution, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying bioset by study institution: {str(e)}"


    @mcp.tool()
    def bvbrc_bioset_get_by_genome_id(genome_id: str, limit: int = _default_limit,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by genome ID.
        
        Args:
            genome_id: The genome ID to query (e.g., "208964.12")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_bioset_by_genome_id(genome_id, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying bioset by genome ID: {str(e)}"


    @mcp.tool()
    def bvbrc_bioset_get_by_date_range(start_date: str, end_date: str, limit: int = _default_limit,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_bioset_by_date_range(start_date, end_date, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying bioset by date range: {str(e)}"


    @mcp.tool()
    def bvbrc_bioset_get_by_modified_date_range(start_date: str, end_date: str, limit: int = _default_limit,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by modified date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_bioset_by_modified_date_range(start_date, end_date, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying bioset by modified date range: {str(e)}"


    @mcp.tool()
    def bvbrc_bioset_search_by_keyword(keyword: str, limit: int = _default_limit,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search bioset data by keyword.
        
        Args:
            keyword: The keyword to search for (e.g., "RNA-seq")
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_bioset_by_keyword(keyword, options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error searching bioset by keyword: {str(e)}"


    @mcp.tool()
    def bvbrc_bioset_get_all(limit: int = _default_limit,
                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all bioset data.
        
        Args:
            limit: Maximum number of results to return (default: 1000)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {"limit": limit}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result = query_bioset_all(options, _base_url)
            return format_query_result(result)
        except Exception as e:
            return f"Error querying all biosets: {str(e)}"
