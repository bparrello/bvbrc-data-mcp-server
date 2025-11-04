#!/usr/bin/env python3
"""
BV-BRC Protein-Protein Interaction Tools

This module contains MCP tools for querying protein-protein interaction data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None

from data_functions import (
    query_ppi_by_id,
    query_ppi_by_filters,
    query_ppi_by_category,
    query_ppi_by_detection_method,
    query_ppi_by_domain_a,
    query_ppi_by_domain_b,
    query_ppi_by_evidence,
    query_ppi_by_feature_id_a,
    query_ppi_by_feature_id_b,
    query_ppi_by_gene_a,
    query_ppi_by_gene_b,
    query_ppi_by_genome_id_a,
    query_ppi_by_genome_id_b,
    query_ppi_by_genome_name_a,
    query_ppi_by_genome_name_b,
    query_ppi_by_interaction_type,
    query_ppi_by_interactor_a,
    query_ppi_by_interactor_b,
    query_ppi_by_pmid,
    query_ppi_by_source_db,
    query_ppi_by_source_id,
    query_ppi_by_taxon_id_a,
    query_ppi_by_taxon_id_b,
    query_ppi_by_date_inserted_range,
    query_ppi_by_date_modified_range,
    query_ppi_by_keyword,
    query_ppi_all,
    format_query_result
)

def register_ppi_tools(mcp: FastMCP, base_url: str):
    """Register all protein-protein interaction-related MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    
    @mcp.tool()
    def bvbrc_ppi_get_by_id(id: str,
                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by ID.
        
        Args:
            id: The ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_ppi_by_id(id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein-protein interaction by ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_ppi_query_by_filters(filters_json: str,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query protein-protein interaction data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
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
            result, count = query_ppi_by_filters(filters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein-protein interaction by filters: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_ppi_get_by_category(category: str,
                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by category.
        
        Args:
            category: The category to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_ppi_by_category(category, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein-protein interaction by category: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_ppi_get_by_detection_method(detection_method: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by detection method.
        
        Args:
            detection_method: The detection method to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_ppi_by_detection_method(detection_method, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein-protein interaction by detection method: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_ppi_get_by_domain_a(domain_a: str,
                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by domain A.
        
        Args:
            domain_a: The domain A to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_ppi_by_domain_a(domain_a, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein-protein interaction by domain A: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_ppi_get_by_domain_b(domain_b: str,
                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by domain B.
        
        Args:
            domain_b: The domain B to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_ppi_by_domain_b(domain_b, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein-protein interaction by domain B: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_ppi_get_by_evidence(evidence: str,
                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by evidence.
        
        Args:
            evidence: The evidence to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_ppi_by_evidence(evidence, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein-protein interaction by evidence: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_ppi_get_by_feature_id_a(feature_id_a: str,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by feature ID A.
        
        Args:
            feature_id_a: The feature ID A to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_ppi_by_feature_id_a(feature_id_a, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein-protein interaction by feature ID A: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_ppi_get_by_feature_id_b(feature_id_b: str,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by feature ID B.
        
        Args:
            feature_id_b: The feature ID B to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_ppi_by_feature_id_b(feature_id_b, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein-protein interaction by feature ID B: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_ppi_get_by_gene_a(gene_a: str,
                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by gene A.
        
        Args:
            gene_a: The gene A to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_ppi_by_gene_a(gene_a, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein-protein interaction by gene A: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_ppi_get_by_gene_b(gene_b: str,
                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by gene B.
        
        Args:
            gene_b: The gene B to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_ppi_by_gene_b(gene_b, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein-protein interaction by gene B: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_ppi_get_by_genome_id_a(genome_id_a: str,
                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by genome ID A.
        
        Args:
            genome_id_a: The genome ID A to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_ppi_by_genome_id_a(genome_id_a, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein-protein interaction by genome ID A: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_ppi_get_by_genome_id_b(genome_id_b: str,
                                    select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by genome ID B.
        
        Args:
            genome_id_b: The genome ID B to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_ppi_by_genome_id_b(genome_id_b, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein-protein interaction by genome ID B: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_ppi_get_by_genome_name_a(genome_name_a: str,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by genome name A.
        
        Args:
            genome_name_a: The genome name A to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_ppi_by_genome_name_a(genome_name_a, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein-protein interaction by genome name A: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_ppi_get_by_genome_name_b(genome_name_b: str,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by genome name B.
        
        Args:
            genome_name_b: The genome name B to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_ppi_by_genome_name_b(genome_name_b, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein-protein interaction by genome name B: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_ppi_get_by_interaction_type(interaction_type: str,
                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by interaction type.
        
        Args:
            interaction_type: The interaction type to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_ppi_by_interaction_type(interaction_type, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein-protein interaction by interaction type: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_ppi_get_by_interactor_a(interactor_a: str,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by interactor A.
        
        Args:
            interactor_a: The interactor A to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_ppi_by_interactor_a(interactor_a, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein-protein interaction by interactor A: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_ppi_get_by_interactor_b(interactor_b: str,
                                      select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by interactor B.
        
        Args:
            interactor_b: The interactor B to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_ppi_by_interactor_b(interactor_b, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein-protein interaction by interactor B: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_ppi_get_by_pmid(pmid: str,
                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by PMID.
        
        Args:
            pmid: The PMID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_ppi_by_pmid(pmid, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein-protein interaction by PMID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_ppi_get_by_source_db(source_db: str,
                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by source database.
        
        Args:
            source_db: The source database to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_ppi_by_source_db(source_db, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein-protein interaction by source database: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_ppi_get_by_source_id(source_id: str,
                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by source ID.
        
        Args:
            source_id: The source ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_ppi_by_source_id(source_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein-protein interaction by source ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_ppi_get_by_taxon_id_a(taxon_id_a: int,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by taxon ID A.
        
        Args:
            taxon_id_a: The taxon ID A to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_ppi_by_taxon_id_a(taxon_id_a, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein-protein interaction by taxon ID A: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_ppi_get_by_taxon_id_b(taxon_id_b: int,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by taxon ID B.
        
        Args:
            taxon_id_b: The taxon ID B to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_ppi_by_taxon_id_b(taxon_id_b, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein-protein interaction by taxon ID B: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_ppi_get_by_date_inserted_range(start_date: str, end_date: str,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_ppi_by_date_inserted_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein-protein interaction by date inserted range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_ppi_get_by_date_modified_range(start_date: str, end_date: str,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get protein-protein interaction data by date modified range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_ppi_by_date_modified_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying protein-protein interaction by date modified range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_ppi_search_by_keyword(keyword: str,
                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search protein-protein interaction data by keyword.
        
        Args:
            keyword: The keyword to search for
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_ppi_by_keyword(keyword, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error searching protein-protein interaction by keyword: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_ppi_get_all(select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all protein-protein interaction data.
        
        Args:
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted protein-protein interaction data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_ppi_all(options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying all protein-protein interaction data: {str(e)}"
            }, indent=2)