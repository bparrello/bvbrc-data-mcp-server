#!/usr/bin/env python3
"""
BV-BRC Data MCP Server

This MCP server provides access to BV-BRC (Bacterial and Viral Bioinformatics Resource Center) 
data through the bvbrc-solr-python-api module. It exposes genome and genome feature data 
querying capabilities through MCP tools using FastMCP.
"""

import json
import sys
from typing import Any, Dict, List, Optional

from data_functions import (
    query_genome_by_id,
    query_genome_by_species,
    query_genome_by_genome_name,
    query_genome_feature_by_genome_id,
    query_genome_feature_by_id,
    query_genome_feature_by_filters,
    query_genome_amr_by_filters,
    query_antibiotics_by_filters,
    query_sp_gene_by_filters,
    format_query_result
)

def main() -> int:
    _base_url = "https://www.bv-brc.org/api"

    try:
        print("Starting test.")
        
        # Example test query for SP gene by filters
        options = {"limit": 1000}

        filter_spec = { "genome_id": "1313.34299" }

        result = query_sp_gene_by_filters(filter_spec, options, _base_url)
        print(format_query_result(result))

    except Exception as e:
        print(f"Test error: {e}", file=sys.stderr)
        return 1
    
    return 0


if __name__ == "__main__":
    main()

