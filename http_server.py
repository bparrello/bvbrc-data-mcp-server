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

from fastmcp import FastMCP

# Import tool modules
from tools import (
    register_genome_tools,
    register_genome_feature_tools,
    register_antibiotics_tools,
    register_bioset_tools,
    register_bioset_result_tools,
    register_enzyme_class_ref_tools,
    register_epitope_assay_tools,
    register_epitope_tools,
    register_experiment_tools,
    register_gene_ontology_ref_tools,
    register_genome_amr_tools,
    register_genome_sequence_tools,
    register_id_ref_tools,
    register_misc_niaid_sgc_tools,
    register_pathway_ref_tools,
    register_pathway_tools,
    register_ppi_tools,
    register_protein_family_ref_tools,
    register_protein_feature_tools,
    register_protein_structure_tools,
    register_sequence_feature_vt_tools,
    register_sequence_feature_tools,
    register_serology_tools,
    register_sp_gene_ref_tools,
    register_sp_gene_tools,
    register_spike_lineage_tools,
    register_spike_variant_tools,
    register_strain_tools,
    register_structured_assertion_tools,
    register_subsystem_ref_tools,
    register_subsystem_tools,
    register_surveillance_tools,
    register_taxonomy_tools,
    register_common_tools
)

# Load configuration
try:
    with open('config.json', 'r') as f:
        config = json.load(f)
except FileNotFoundError:
    print("Warning: config.json not found, using defaults", file=sys.stderr)
    config = {
        "base_url": "https://www.bv-brc.org/bulk-api",
        "mcp_url": "127.0.0.1",
        "port": 8059,
        "default_limit": 1000
    }

# Get configuration values
base_url = config.get("base_url", "https://www.bv-brc.org/bulk-api")
default_limit = config.get("default_limit", 1000)
mcp_url = config.get("mcp_url", "127.0.0.1")
port = config.get("port", 8059)

# Create FastMCP server
mcp = FastMCP("BV-BRC Data MCP Server")

# Register all tools from the modular files
register_genome_tools(mcp, base_url, default_limit)
register_genome_feature_tools(mcp, base_url, default_limit)
register_antibiotics_tools(mcp, base_url, default_limit)
register_bioset_tools(mcp, base_url, default_limit)
register_bioset_result_tools(mcp, base_url, default_limit)
register_enzyme_class_ref_tools(mcp, base_url, default_limit)
register_epitope_assay_tools(mcp, base_url, default_limit)
register_epitope_tools(mcp, base_url, default_limit)
register_experiment_tools(mcp, base_url, default_limit)
register_gene_ontology_ref_tools(mcp, base_url, default_limit)
register_genome_amr_tools(mcp, base_url, default_limit)
register_genome_sequence_tools(mcp, base_url, default_limit)
register_id_ref_tools(mcp, base_url, default_limit)
register_misc_niaid_sgc_tools(mcp, base_url, default_limit)
register_pathway_ref_tools(mcp, base_url, default_limit)
register_pathway_tools(mcp, base_url, default_limit)
register_ppi_tools(mcp, base_url, default_limit)
register_protein_family_ref_tools(mcp, base_url, default_limit)
register_protein_feature_tools(mcp, base_url, default_limit)
register_protein_structure_tools(mcp, base_url, default_limit)
register_sequence_feature_vt_tools(mcp, base_url, default_limit)
register_sequence_feature_tools(mcp, base_url, default_limit)
register_serology_tools(mcp, base_url, default_limit)
register_sp_gene_ref_tools(mcp, base_url, default_limit)
register_sp_gene_tools(mcp, base_url, default_limit)
register_spike_lineage_tools(mcp, base_url, default_limit)
register_spike_variant_tools(mcp, base_url, default_limit)
register_strain_tools(mcp, base_url, default_limit)
register_structured_assertion_tools(mcp, base_url, default_limit)
register_subsystem_ref_tools(mcp, base_url, default_limit)
register_subsystem_tools(mcp, base_url, default_limit)
register_surveillance_tools(mcp, base_url, default_limit)
register_taxonomy_tools(mcp, base_url, default_limit)
register_common_tools(mcp, base_url, default_limit)


def main() -> int:
    """Main entry point for the BV-BRC Data MCP Server."""
    print(f"Starting BV-BRC Data MCP Server...", file=sys.stderr)
    
    try:
        mcp.run(transport="http", host=mcp_url, port=port)
    except KeyboardInterrupt:
        print("Server stopped.", file=sys.stderr)
    except Exception as e:
        print(f"Server error: {e}", file=sys.stderr)
        return 1
    
    return 0


if __name__ == "__main__":
    main()
