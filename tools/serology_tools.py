#!/usr/bin/env python3
"""
BV-BRC Serology Tools

This module contains MCP tools for querying serology data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None

from data_functions import (
    query_serology_by_id,
    query_serology_by_filters,
    query_serology_by_collection_city,
    query_serology_by_collection_country,
    query_serology_by_collection_state,
    query_serology_by_collection_year,
    query_serology_by_host_species,
    query_serology_by_host_type,
    query_serology_by_serotype,
    query_serology_by_strain,
    query_serology_by_test_type,
    query_serology_by_test_result,
    query_serology_by_test_interpretation,
    query_serology_by_test_pathogen,
    query_serology_by_test_antigen,
    query_serology_by_sample_accession,
    query_serology_by_sample_identifier,
    query_serology_by_virus_identifier,
    query_serology_by_project_identifier,
    query_serology_by_contributing_institution,
    query_serology_by_geographic_group,
    query_serology_by_host_common_name,
    query_serology_by_host_health,
    query_serology_by_host_identifier,
    query_serology_by_host_sex,
    query_serology_by_host_age,
    query_serology_by_host_age_group,
    query_serology_by_positive_definition,
    query_serology_by_taxon_lineage_id,
    query_serology_by_collection_date_range,
    query_serology_by_date_inserted_range,
    query_serology_by_date_modified_range,
    query_serology_by_keyword,
    query_serology_all,
    format_query_result
)

def register_serology_tools(mcp: FastMCP, base_url: str):
    """Register all serology-related MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    
    @mcp.tool()
    def bvbrc_serology_get_by_id(id: str,
                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by ID.
        
        Args:
            id: The ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_id(id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_query_by_filters(filters_json: str,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query serology data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
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
            result, count = query_serology_by_filters(filters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by filters: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_collection_city(collection_city: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by collection city.
        
        Args:
            collection_city: The collection city to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_collection_city(collection_city, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by collection city: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_collection_country(collection_country: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by collection country.
        
        Args:
            collection_country: The collection country to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_collection_country(collection_country, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by collection country: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_collection_state(collection_state: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by collection state.
        
        Args:
            collection_state: The collection state to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_collection_state(collection_state, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by collection state: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_collection_year(collection_year: str,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by collection year.
        
        Args:
            collection_year: The collection year to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_collection_year(collection_year, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by collection year: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_host_species(host_species: str,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by host species.
        
        Args:
            host_species: The host species to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_host_species(host_species, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by host species: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_host_type(host_type: str,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by host type.
        
        Args:
            host_type: The host type to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_host_type(host_type, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by host type: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_serotype(serotype: str,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by serotype.
        
        Args:
            serotype: The serotype to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_serotype(serotype, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by serotype: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_strain(strain: str,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by strain.
        
        Args:
            strain: The strain to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_strain(strain, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by strain: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_test_type(test_type: str,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by test type.
        
        Args:
            test_type: The test type to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_test_type(test_type, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by test type: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_test_result(test_result: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by test result.
        
        Args:
            test_result: The test result to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_test_result(test_result, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by test result: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_test_interpretation(test_interpretation: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by test interpretation.
        
        Args:
            test_interpretation: The test interpretation to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_test_interpretation(test_interpretation, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by test interpretation: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_test_pathogen(test_pathogen: str,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by test pathogen.
        
        Args:
            test_pathogen: The test pathogen to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_test_pathogen(test_pathogen, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by test pathogen: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_test_antigen(test_antigen: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by test antigen.
        
        Args:
            test_antigen: The test antigen to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_test_antigen(test_antigen, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by test antigen: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_sample_accession(sample_accession: str,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by sample accession.
        
        Args:
            sample_accession: The sample accession to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_sample_accession(sample_accession, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by sample accession: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_sample_identifier(sample_identifier: str,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by sample identifier.
        
        Args:
            sample_identifier: The sample identifier to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_sample_identifier(sample_identifier, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by sample identifier: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_virus_identifier(virus_identifier: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by virus identifier.
        
        Args:
            virus_identifier: The virus identifier to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_virus_identifier(virus_identifier, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by virus identifier: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_project_identifier(project_identifier: str,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by project identifier.
        
        Args:
            project_identifier: The project identifier to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_project_identifier(project_identifier, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by project identifier: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_contributing_institution(contributing_institution: str,
                                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by contributing institution.
        
        Args:
            contributing_institution: The contributing institution to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_contributing_institution(contributing_institution, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by contributing institution: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_geographic_group(geographic_group: str,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by geographic group.
        
        Args:
            geographic_group: The geographic group to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_geographic_group(geographic_group, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by geographic group: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_host_common_name(host_common_name: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by host common name.
        
        Args:
            host_common_name: The host common name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_host_common_name(host_common_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by host common name: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_host_health(host_health: str,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by host health.
        
        Args:
            host_health: The host health to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_host_health(host_health, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by host health: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_host_identifier(host_identifier: str,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by host identifier.
        
        Args:
            host_identifier: The host identifier to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_host_identifier(host_identifier, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by host identifier: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_host_sex(host_sex: str,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by host sex.
        
        Args:
            host_sex: The host sex to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_host_sex(host_sex, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by host sex: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_host_age(host_age: str,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by host age.
        
        Args:
            host_age: The host age to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_host_age(host_age, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by host age: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_host_age_group(host_age_group: str,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by host age group.
        
        Args:
            host_age_group: The host age group to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_host_age_group(host_age_group, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by host age group: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_positive_definition(positive_definition: str,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by positive definition.
        
        Args:
            positive_definition: The positive definition to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_positive_definition(positive_definition, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by positive definition: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_taxon_lineage_id(taxon_lineage_id: str,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by taxon lineage ID.
        
        Args:
            taxon_lineage_id: The taxon lineage ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_taxon_lineage_id(taxon_lineage_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by taxon lineage ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_collection_date_range(start_date: str, end_date: str,
                                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by collection date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_collection_date_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by collection date range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_date_inserted_range(start_date: str, end_date: str,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_date_inserted_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by date inserted range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_by_date_modified_range(start_date: str, end_date: str,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get serology data by date modified range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_date_modified_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying serology by date modified range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_search_by_keyword(keyword: str,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search serology data by keyword.
        
        Args:
            keyword: The keyword to search for
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_by_keyword(keyword, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error searching serology by keyword: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_serology_get_all(select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all serology data.
        
        Args:
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted serology data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_serology_all(options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying all serology data: {str(e)}"
            }, indent=2)