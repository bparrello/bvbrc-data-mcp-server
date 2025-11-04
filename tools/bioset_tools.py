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


def register_bioset_tools(mcp: FastMCP, base_url: str):
    """Register all bioset-related MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    

    
    @mcp.tool()
    def bvbrc_bioset_get_by_id(bioset_id: str, 
                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by bioset ID.
        
        Args:
            bioset_id: The bioset ID to query (e.g., "bs12345")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_by_id(bioset_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset by ID: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_bioset_query_by_filters(filters_json: str,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query bioset data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria (e.g., '{"bioset_name": "RNA-seq", "organism": "Escherichia coli"}')
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        try:
            filters = json.loads(filters_json)
        except json.JSONDecodeError as e:
            return json.dumps({
                "error": f"Error parsing filters JSON: {str(e)}"
            }, indent=2)
        
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_by_filters(filters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset by filters: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_bioset_get_by_name(bioset_name: str,
                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by bioset name.
        
        Args:
            bioset_name: The bioset name to query (e.g., "RNA-seq")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_by_name(bioset_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset by name: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_bioset_get_by_type(bioset_type: str,
                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by bioset type.
        
        Args:
            bioset_type: The bioset type to query (e.g., "RNA-seq")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_by_type(bioset_type, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset by type: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_bioset_get_by_exp_id(exp_id: str,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by experiment ID.
        
        Args:
            exp_id: The experiment ID to query (e.g., "exp12345")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_by_exp_id(exp_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset by experiment ID: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_bioset_get_by_exp_name(exp_name: str,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by experiment name.
        
        Args:
            exp_name: The experiment name to query (e.g., "RNA-seq experiment")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_by_exp_name(exp_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset by experiment name: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_bioset_get_by_exp_type(exp_type: str,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by experiment type.
        
        Args:
            exp_type: The experiment type to query (e.g., "RNA-seq")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_by_exp_type(exp_type, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset by experiment type: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_bioset_get_by_organism(organism: str,
                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by organism.
        
        Args:
            organism: The organism to query (e.g., "Escherichia coli")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_by_organism(organism, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset by organism: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_bioset_get_by_strain(strain: str,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by strain.
        
        Args:
            strain: The strain to query (e.g., "K-12")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_by_strain(strain, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset by strain: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_bioset_get_by_taxon_id(taxon_id: int,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query (e.g., 562)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_by_taxon_id(taxon_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset by taxon ID: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_bioset_get_by_entity_type(entity_type: str,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by entity type.
        
        Args:
            entity_type: The entity type to query (e.g., "gene")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_by_entity_type(entity_type, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset by entity type: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_bioset_get_by_result_type(result_type: str,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by result type.
        
        Args:
            result_type: The result type to query (e.g., "differential_expression")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_by_result_type(result_type, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset by result type: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_bioset_get_by_analysis_method(analysis_method: str,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by analysis method.
        
        Args:
            analysis_method: The analysis method to query (e.g., "DESeq2")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_by_analysis_method(analysis_method, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset by analysis method: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_bioset_get_by_analysis_group_1(analysis_group_1: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by analysis group 1.
        
        Args:
            analysis_group_1: The analysis group 1 to query (e.g., "control")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_by_analysis_group_1(analysis_group_1, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset by analysis group 1: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_bioset_get_by_analysis_group_2(analysis_group_2: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by analysis group 2.
        
        Args:
            analysis_group_2: The analysis group 2 to query (e.g., "treatment")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_by_analysis_group_2(analysis_group_2, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset by analysis group 2: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_bioset_get_by_treatment_type(treatment_type: str,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by treatment type.
        
        Args:
            treatment_type: The treatment type to query (e.g., "antibiotic")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_by_treatment_type(treatment_type, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset by treatment type: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_bioset_get_by_treatment_name(treatment_name: str,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by treatment name.
        
        Args:
            treatment_name: The treatment name to query (e.g., "ampicillin")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_by_treatment_name(treatment_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset by treatment name: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_bioset_get_by_study_name(study_name: str,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by study name.
        
        Args:
            study_name: The study name to query (e.g., "Antibiotic resistance study")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_by_study_name(study_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset by study name: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_bioset_get_by_study_pi(study_pi: str,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by study PI.
        
        Args:
            study_pi: The study PI to query (e.g., "Dr. Smith")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_by_study_pi(study_pi, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset by study PI: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_bioset_get_by_study_institution(study_institution: str,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by study institution.
        
        Args:
            study_institution: The study institution to query (e.g., "University of California")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_by_study_institution(study_institution, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset by study institution: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_bioset_get_by_genome_id(genome_id: str,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by genome ID.
        
        Args:
            genome_id: The genome ID to query (e.g., "208964.12")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_by_genome_id(genome_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset by genome ID: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_bioset_get_by_date_range(start_date: str, end_date: str,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_by_date_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset by date range: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_bioset_get_by_modified_date_range(start_date: str, end_date: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get bioset data by modified date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_by_modified_date_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying bioset by modified date range: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_bioset_search_by_keyword(keyword: str,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search bioset data by keyword.
        
        Args:
            keyword: The keyword to search for (e.g., "RNA-seq")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_by_keyword(keyword, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error searching bioset by keyword: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_bioset_get_all(select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all bioset data.
        
        Args:
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted bioset data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_bioset_all(options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying all biosets: {str(e)}"
            }, indent=2)
