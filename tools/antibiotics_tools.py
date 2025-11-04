#!/usr/bin/env python3
"""
BV-BRC Antibiotics Tools

This module contains MCP tools for querying antibiotic data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None

from data_functions import (
    query_antibiotics_by_pubchem_cid,
    query_antibiotics_by_filters,
    query_antibiotics_by_keyword,
    query_antibiotics_by_name,
    query_antibiotics_by_cas_id,
    query_antibiotics_by_molecular_formula,
    query_antibiotics_by_atc_classification,
    query_antibiotics_by_mechanism_of_action,
    query_antibiotics_by_pharmacological_class,
    query_antibiotics_by_synonym,
    query_antibiotics_by_molecular_weight_range,
    query_antibiotics_by_date_range,
    query_antibiotics_all,
    format_query_result
)


def register_antibiotics_tools(mcp: FastMCP, base_url: str):
    """Register all antibiotics-related MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    

    
    @mcp.tool()
    def bvbrc_antibiotics_get_by_pubchem_cid(pubchem_cid: str,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get antibiotic data by PubChem CID.
        
        Args:
            pubchem_cid: The PubChem CID to query (e.g., "2244")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted antibiotic data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_antibiotics_by_pubchem_cid(pubchem_cid, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying antibiotics by PubChem CID: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_antibiotics_query_by_filters(filters_json: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query antibiotic data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria (e.g., '{"antibiotic_name": "penicillin", "mechanism_of_action": "cell wall synthesis inhibitor"}')
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted antibiotic data
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
            result, count = query_antibiotics_by_filters(filters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying antibiotics by filters: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_antibiotics_search_by_keyword(keyword: str,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search antibiotic data by keyword.
        
        Args:
            keyword: The keyword to search for (e.g., "penicillin")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted antibiotic data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_antibiotics_by_keyword(keyword, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error searching antibiotics by keyword: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_antibiotics_get_by_name(antibiotic_name: str,
                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get antibiotic data by antibiotic name.
        
        Args:
            antibiotic_name: The antibiotic name to query (e.g., "penicillin")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted antibiotic data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_antibiotics_by_name(antibiotic_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying antibiotics by name: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_antibiotics_get_by_cas_id(cas_id: str,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get antibiotic data by CAS ID.
        
        Args:
            cas_id: The CAS ID to query (e.g., "61-33-6")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted antibiotic data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_antibiotics_by_cas_id(cas_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying antibiotics by CAS ID: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_antibiotics_get_by_molecular_formula(molecular_formula: str,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get antibiotic data by molecular formula.
        
        Args:
            molecular_formula: The molecular formula to query (e.g., "C16H18N2O4S")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted antibiotic data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_antibiotics_by_molecular_formula(molecular_formula, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying antibiotics by molecular formula: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_antibiotics_get_by_atc_classification(atc_classification: str,
                                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get antibiotic data by ATC classification.
        
        Args:
            atc_classification: The ATC classification to query (e.g., "J01CA04")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted antibiotic data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_antibiotics_by_atc_classification(atc_classification, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying antibiotics by ATC classification: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_antibiotics_get_by_mechanism_of_action(mechanism_of_action: str,
                                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get antibiotic data by mechanism of action.
        
        Args:
            mechanism_of_action: The mechanism of action to query (e.g., "cell wall synthesis inhibitor")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted antibiotic data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_antibiotics_by_mechanism_of_action(mechanism_of_action, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying antibiotics by mechanism of action: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_antibiotics_get_by_pharmacological_class(pharmacological_class: str,
                                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get antibiotic data by pharmacological class.
        
        Args:
            pharmacological_class: The pharmacological class to query (e.g., "beta-lactam")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted antibiotic data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_antibiotics_by_pharmacological_class(pharmacological_class, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying antibiotics by pharmacological class: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_antibiotics_get_by_synonym(synonym: str,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get antibiotic data by synonym.
        
        Args:
            synonym: The synonym to query (e.g., "benzylpenicillin")
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted antibiotic data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_antibiotics_by_synonym(synonym, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying antibiotics by synonym: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_antibiotics_get_by_molecular_weight_range(min_weight: float, max_weight: float,
                                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get antibiotic data by molecular weight range.
        
        Args:
            min_weight: Minimum molecular weight
            max_weight: Maximum molecular weight
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted antibiotic data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_antibiotics_by_molecular_weight_range(min_weight, max_weight, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying antibiotics by molecular weight range: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_antibiotics_get_by_date_range(start_date: str, end_date: str,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get antibiotic data by date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted antibiotic data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_antibiotics_by_date_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying antibiotics by date range: {str(e)}"
            }, indent=2)


    @mcp.tool()
    def bvbrc_antibiotics_get_all(select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all antibiotic data.
        
        Args:
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted antibiotic data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_antibiotics_all(options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying all antibiotics: {str(e)}"
            }, indent=2)
