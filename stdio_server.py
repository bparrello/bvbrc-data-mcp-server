#!/usr/bin/env python3
"""
BV-BRC Data MCP Server (STDIO Version)

This MCP server provides access to BV-BRC (Bacterial and Viral Bioinformatics Resource Center) 
data through the bvbrc-solr-python-api module. It exposes genome and genome feature data 
querying capabilities through MCP tools using FastMCP via stdio communication.
"""

import os
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

# Load configuration from environment variables
base_url = os.getenv("BVBRC_BASE_URL", "https://www.bv-brc.org/api-bulk")
default_limit = int(os.getenv("BVBRC_DEFAULT_LIMIT", "1000"))

# Create FastMCP server
mcp = FastMCP("BV-BRC Data MCP Server (STDIO)")

# Register all tools from the modular files
register_common_tools(mcp, base_url)
register_antibiotics_tools(mcp, base_url)
register_bioset_tools(mcp, base_url)
register_bioset_result_tools(mcp, base_url)
register_enzyme_class_ref_tools(mcp, base_url)
register_epitope_assay_tools(mcp, base_url)
register_epitope_tools(mcp, base_url)
register_experiment_tools(mcp, base_url)
register_gene_ontology_ref_tools(mcp, base_url)
register_genome_tools(mcp, base_url)
register_genome_feature_tools(mcp, base_url)
register_genome_amr_tools(mcp, base_url)
register_genome_sequence_tools(mcp, base_url)
register_id_ref_tools(mcp, base_url)
register_misc_niaid_sgc_tools(mcp, base_url)
register_pathway_ref_tools(mcp, base_url)
register_pathway_tools(mcp, base_url)
register_ppi_tools(mcp, base_url)
register_protein_family_ref_tools(mcp, base_url)
register_protein_feature_tools(mcp, base_url)
register_protein_structure_tools(mcp, base_url)
register_sequence_feature_vt_tools(mcp, base_url)
register_sequence_feature_tools(mcp, base_url)
register_serology_tools(mcp, base_url)
register_sp_gene_ref_tools(mcp, base_url)
register_spike_lineage_tools(mcp, base_url)
register_spike_variant_tools(mcp, base_url)
register_sp_gene_tools(mcp, base_url)
register_strain_tools(mcp, base_url)
register_structured_assertion_tools(mcp, base_url)
register_subsystem_ref_tools(mcp, base_url)
register_subsystem_tools(mcp, base_url)
register_surveillance_tools(mcp, base_url)
register_taxonomy_tools(mcp, base_url)


def main() -> int:
    """Main entry point for the BV-BRC Data MCP Server (STDIO version)."""
    print("Starting BV-BRC Data MCP Server (STDIO)...", file=sys.stderr)
    
    try:
        # Run in stdio mode (no host/port parameters)
        mcp.run()
    except KeyboardInterrupt:
        print("Server stopped.", file=sys.stderr)
    except Exception as e:
        print(f"Server error: {e}", file=sys.stderr)
        return 1
    
    return 0


if __name__ == "__main__":
    main()
