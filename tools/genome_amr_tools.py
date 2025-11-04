#!/usr/bin/env python3
"""
BV-BRC Genome AMR Tools

This module contains MCP tools for querying genome antimicrobial resistance data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None

from data_functions import (
    query_genome_amr_by_id,
    query_genome_amr_by_filters,
    query_genome_amr_by_antibiotic,
    query_genome_amr_by_computational_method,
    query_genome_amr_by_computational_method_version,
    query_genome_amr_by_evidence,
    query_genome_amr_by_genome_id,
    query_genome_amr_by_genome_name,
    query_genome_amr_by_laboratory_typing_method,
    query_genome_amr_by_laboratory_typing_method_version,
    query_genome_amr_by_laboratory_typing_platform,
    query_genome_amr_by_measurement,
    query_genome_amr_by_measurement_sign,
    query_genome_amr_by_measurement_unit,
    query_genome_amr_by_measurement_value,
    query_genome_amr_by_owner,
    query_genome_amr_by_pmid,
    query_genome_amr_by_public_status,
    query_genome_amr_by_resistant_phenotype,
    query_genome_amr_by_source,
    query_genome_amr_by_taxon_id,
    query_genome_amr_by_testing_standard,
    query_genome_amr_by_testing_standard_year,
    query_genome_amr_by_vendor,
    query_genome_amr_by_date_range,
    query_genome_amr_by_modified_date_range,
    query_genome_amr_by_keyword,
    query_genome_amr_all,
    format_query_result
)

def register_genome_amr_tools(mcp: FastMCP, base_url: str):
    """Register all genome AMR-related MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    
    @mcp.tool()
    def bvbrc_genome_amr_get_by_id(id: str,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by ID.
        
        Args:
            id: The AMR record ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_by_id(id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome AMR by ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_query_by_filters(filters_json: str,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query genome AMR data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
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
            result, count = query_genome_amr_by_filters(filters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome AMR by filters: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_get_by_antibiotic(antibiotic: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by antibiotic.
        
        Args:
            antibiotic: The antibiotic to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_by_antibiotic(antibiotic, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome AMR by antibiotic: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_get_by_computational_method(computational_method: str,
                                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by computational method.
        
        Args:
            computational_method: The computational method to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_by_computational_method(computational_method, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome AMR by computational method: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_get_by_computational_method_version(computational_method_version: str,
                                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by computational method version.
        
        Args:
            computational_method_version: The computational method version to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_by_computational_method_version(computational_method_version, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome AMR by computational method version: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_get_by_evidence(evidence: str,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by evidence.
        
        Args:
            evidence: The evidence to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_by_evidence(evidence, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome AMR by evidence: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_get_by_genome_id(genome_id: str,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by genome ID.
        
        Args:
            genome_id: The genome ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_by_genome_id(genome_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome AMR by genome ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_get_by_genome_name(genome_name: str,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by genome name.
        
        Args:
            genome_name: The genome name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_by_genome_name(genome_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome AMR by genome name: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_get_by_laboratory_typing_method(laboratory_typing_method: str,
                                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by laboratory typing method.
        
        Args:
            laboratory_typing_method: The laboratory typing method to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_by_laboratory_typing_method(laboratory_typing_method, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome AMR by laboratory typing method: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_get_by_laboratory_typing_method_version(laboratory_typing_method_version: str,
                                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by laboratory typing method version.
        
        Args:
            laboratory_typing_method_version: The laboratory typing method version to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_by_laboratory_typing_method_version(laboratory_typing_method_version, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome AMR by laboratory typing method version: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_get_by_laboratory_typing_platform(laboratory_typing_platform: str,
                                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by laboratory typing platform.
        
        Args:
            laboratory_typing_platform: The laboratory typing platform to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_by_laboratory_typing_platform(laboratory_typing_platform, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome AMR by laboratory typing platform: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_get_by_measurement(measurement: str,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by measurement.
        
        Args:
            measurement: The measurement to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_by_measurement(measurement, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome AMR by measurement: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_get_by_measurement_sign(measurement_sign: str,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by measurement sign.
        
        Args:
            measurement_sign: The measurement sign to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_by_measurement_sign(measurement_sign, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome AMR by measurement sign: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_get_by_measurement_unit(measurement_unit: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by measurement unit.
        
        Args:
            measurement_unit: The measurement unit to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_by_measurement_unit(measurement_unit, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome AMR by measurement unit: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_get_by_measurement_value(measurement_value: str,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by measurement value.
        
        Args:
            measurement_value: The measurement value to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_by_measurement_value(measurement_value, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome AMR by measurement value: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_get_by_owner(owner: str,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by owner.
        
        Args:
            owner: The owner to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_by_owner(owner, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome AMR by owner: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_get_by_pmid(pmid: int,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by PMID.
        
        Args:
            pmid: The PMID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_by_pmid(pmid, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome AMR by PMID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_get_by_public_status(is_public: bool,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by public status.
        
        Args:
            is_public: The public status to query (True/False)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_by_public_status(is_public, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome AMR by public status: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_get_by_resistant_phenotype(resistant_phenotype: str,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by resistant phenotype.
        
        Args:
            resistant_phenotype: The resistant phenotype to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_by_resistant_phenotype(resistant_phenotype, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome AMR by resistant phenotype: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_get_by_source(source: str,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by source.
        
        Args:
            source: The source to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_by_source(source, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome AMR by source: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_get_by_taxon_id(taxon_id: int,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_by_taxon_id(taxon_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome AMR by taxon ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_get_by_testing_standard(testing_standard: str,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by testing standard.
        
        Args:
            testing_standard: The testing standard to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_by_testing_standard(testing_standard, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome AMR by testing standard: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_get_by_testing_standard_year(testing_standard_year: int,
                                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by testing standard year.
        
        Args:
            testing_standard_year: The testing standard year to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_by_testing_standard_year(testing_standard_year, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome AMR by testing standard year: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_get_by_vendor(vendor: str,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by vendor.
        
        Args:
            vendor: The vendor to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_by_vendor(vendor, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome AMR by vendor: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_get_by_date_range(start_date: str, end_date: str,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_by_date_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome AMR by date range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_get_by_modified_date_range(start_date: str, end_date: str,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome AMR data by modified date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_by_modified_date_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome AMR by modified date range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_search_by_keyword(keyword: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search genome AMR data by keyword.
        
        Args:
            keyword: The keyword to search for
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_by_keyword(keyword, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error searching genome AMR by keyword: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_amr_get_all(select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all genome AMR data.
        
        Args:
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome AMR data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_amr_all(options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying all genome AMR data: {str(e)}"
            }, indent=2)