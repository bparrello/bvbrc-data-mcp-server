#!/usr/bin/env python3
"""
BV-BRC Genome Sequence Tools

This module contains MCP tools for querying genome sequence data from BV-BRC.
"""

import json
from typing import Optional

from fastmcp import FastMCP
# Global variables to store configuration
_base_url = None

from data_functions import (
    query_genome_sequence_by_id,
    query_genome_sequence_by_filters,
    query_genome_sequence_by_accession,
    query_genome_sequence_by_chromosome,
    query_genome_sequence_by_description,
    query_genome_sequence_by_gc_content,
    query_genome_sequence_by_genome_id,
    query_genome_sequence_by_genome_name,
    query_genome_sequence_by_gi,
    query_genome_sequence_by_length,
    query_genome_sequence_by_mol_type,
    query_genome_sequence_by_owner,
    query_genome_sequence_by_p2_sequence_id,
    query_genome_sequence_by_plasmid,
    query_genome_sequence_by_public_status,
    query_genome_sequence_by_segment,
    query_genome_sequence_by_sequence_md5,
    query_genome_sequence_by_sequence_status,
    query_genome_sequence_by_sequence_type,
    query_genome_sequence_by_taxon_id,
    query_genome_sequence_by_topology,
    query_genome_sequence_by_version,
    query_genome_sequence_by_length_range,
    query_genome_sequence_by_gc_content_range,
    query_genome_sequence_by_date_inserted_range,
    query_genome_sequence_by_date_modified_range,
    query_genome_sequence_by_release_date_range,
    query_genome_sequence_by_keyword,
    query_genome_sequence_all,
    format_query_result
)

def register_genome_sequence_tools(mcp: FastMCP, base_url: str):
    """Register all genome sequence-related MCP tools with the Flask app."""
    global _base_url
    _base_url = base_url
    
    @mcp.tool()
    def bvbrc_genome_sequence_get_by_id(sequence_id: str,
                                       select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by sequence ID.
        
        Args:
            sequence_id: The sequence ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_id(sequence_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_query_by_filters(filters_json: str,
                                              select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Query genome sequence data by custom filters.
        
        Args:
            filters_json: JSON string of filter criteria
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
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
            result, count = query_genome_sequence_by_filters(filters, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by filters: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_get_by_accession(accession: str,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by accession.
        
        Args:
            accession: The accession to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_accession(accession, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by accession: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_get_by_chromosome(chromosome: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by chromosome.
        
        Args:
            chromosome: The chromosome to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_chromosome(chromosome, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by chromosome: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_get_by_description(description: str,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by description.
        
        Args:
            description: The description to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_description(description, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by description: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_get_by_gc_content(gc_content: float,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by GC content.
        
        Args:
            gc_content: The GC content to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_gc_content(gc_content, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by GC content: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_get_by_genome_id(genome_id: str,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by genome ID.
        
        Args:
            genome_id: The genome ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_genome_id(genome_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by genome ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_get_by_genome_name(genome_name: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by genome name.
        
        Args:
            genome_name: The genome name to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_genome_name(genome_name, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by genome name: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_get_by_gi(gi: int,
                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by GI.
        
        Args:
            gi: The GI to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_gi(gi, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by GI: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_get_by_length(length: int,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by length.
        
        Args:
            length: The length to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_length(length, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by length: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_get_by_mol_type(mol_type: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by molecule type.
        
        Args:
            mol_type: The molecule type to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_mol_type(mol_type, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by molecule type: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_get_by_owner(owner: str,
                                          select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by owner.
        
        Args:
            owner: The owner to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_owner(owner, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by owner: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_get_by_p2_sequence_id(p2_sequence_id: int,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by P2 sequence ID.
        
        Args:
            p2_sequence_id: The P2 sequence ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_p2_sequence_id(p2_sequence_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by P2 sequence ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_get_by_plasmid(plasmid: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by plasmid.
        
        Args:
            plasmid: The plasmid to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_plasmid(plasmid, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by plasmid: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_get_by_public_status(is_public: bool,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by public status.
        
        Args:
            is_public: The public status to query (True/False)
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_public_status(is_public, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by public status: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_get_by_segment(segment: str,
                                            select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by segment.
        
        Args:
            segment: The segment to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_segment(segment, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by segment: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_get_by_sequence_md5(sequence_md5: str,
                                                select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by sequence MD5.
        
        Args:
            sequence_md5: The sequence MD5 to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_sequence_md5(sequence_md5, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by sequence MD5: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_get_by_sequence_status(sequence_status: str,
                                                   select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by sequence status.
        
        Args:
            sequence_status: The sequence status to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_sequence_status(sequence_status, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by sequence status: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_get_by_sequence_type(sequence_type: str,
                                                 select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by sequence type.
        
        Args:
            sequence_type: The sequence type to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_sequence_type(sequence_type, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by sequence type: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_get_by_taxon_id(taxon_id: int,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by taxon ID.
        
        Args:
            taxon_id: The taxon ID to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_taxon_id(taxon_id, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by taxon ID: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_get_by_topology(topology: str,
                                             select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by topology.
        
        Args:
            topology: The topology to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_topology(topology, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by topology: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_get_by_version(version: int,
                                           select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by version.
        
        Args:
            version: The version to query
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_version(version, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by version: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_get_by_length_range(min_length: int, max_length: int,
                                                  select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by length range.
        
        Args:
            min_length: Minimum length
            max_length: Maximum length
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_length_range(min_length, max_length, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by length range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_get_by_gc_content_range(min_gc_content: float, max_gc_content: float,
                                                     select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by GC content range.
        
        Args:
            min_gc_content: Minimum GC content
            max_gc_content: Maximum GC content
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_gc_content_range(min_gc_content, max_gc_content, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by GC content range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_get_by_date_inserted_range(start_date: str, end_date: str,
                                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by date inserted range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_date_inserted_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by date inserted range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_get_by_date_modified_range(start_date: str, end_date: str,
                                                         select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by date modified range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_date_modified_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by date modified range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_get_by_release_date_range(start_date: str, end_date: str,
                                                        select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get genome sequence data by release date range.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_release_date_range(start_date, end_date, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying genome sequence by release date range: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_search_by_keyword(keyword: str,
                                               select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Search genome sequence data by keyword.
        
        Args:
            keyword: The keyword to search for
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_by_keyword(keyword, options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error searching genome sequence by keyword: {str(e)}"
            }, indent=2)

    @mcp.tool()
    def bvbrc_genome_sequence_get_all(select: Optional[str] = None, sort: Optional[str] = None) -> str:
        """
        Get all genome sequence data.
        
        Args:
            select: Comma-separated list of fields to select (optional)
            sort: Field to sort by (optional)
        
        Returns:
            Formatted genome sequence data
        """
        options = {}
        if select:
            options["select"] = select.split(",")
        if sort:
            options["sort"] = sort
        
        try:
            result, count = query_genome_sequence_all(options, _base_url)
            return json.dumps({
                "count": count,
                "results": result
            }, indent=2)
        except Exception as e:
            return json.dumps({
                "error": f"Error querying all genome sequence data: {str(e)}"
            }, indent=2)