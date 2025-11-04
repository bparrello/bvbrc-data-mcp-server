"""
BV-BRC MCP Tools

This module contains all MCP tool registration functions for the BV-BRC data server.
"""

from .genome_tools import register_genome_tools
from .genome_feature_tools import register_genome_feature_tools
from .antibiotics_tools import register_antibiotics_tools
from .bioset_tools import register_bioset_tools
from .bioset_result_tools import register_bioset_result_tools
from .enzyme_class_ref_tools import register_enzyme_class_ref_tools
from .epitope_assay_tools import register_epitope_assay_tools
from .epitope_tools import register_epitope_tools
from .experiment_tools import register_experiment_tools
from .gene_ontology_ref_tools import register_gene_ontology_ref_tools
from .genome_amr_tools import register_genome_amr_tools
from .genome_sequence_tools import register_genome_sequence_tools
from .id_ref_tools import register_id_ref_tools
from .misc_niaid_sgc_tools import register_misc_niaid_sgc_tools
from .pathway_ref_tools import register_pathway_ref_tools
from .pathway_tools import register_pathway_tools
from .ppi_tools import register_ppi_tools
from .protein_family_ref_tools import register_protein_family_ref_tools
from .protein_feature_tools import register_protein_feature_tools
from .protein_structure_tools import register_protein_structure_tools
from .sequence_feature_vt_tools import register_sequence_feature_vt_tools
from .sequence_feature_tools import register_sequence_feature_tools
from .serology_tools import register_serology_tools
from .sp_gene_ref_tools import register_sp_gene_ref_tools
from .sp_gene_tools import register_sp_gene_tools
from .spike_lineage_tools import register_spike_lineage_tools
from .spike_variant_tools import register_spike_variant_tools
from .strain_tools import register_strain_tools
from .structured_assertion_tools import register_structured_assertion_tools
from .subsystem_ref_tools import register_subsystem_ref_tools
from .subsystem_tools import register_subsystem_tools
from .surveillance_tools import register_surveillance_tools
from .taxonomy_tools import register_taxonomy_tools
from .common_tools import register_common_tools

__all__ = [
    'register_genome_tools',
    'register_genome_feature_tools',
    'register_antibiotics_tools',
    'register_bioset_tools',
    'register_bioset_result_tools',
    'register_enzyme_class_ref_tools',
    'register_epitope_assay_tools',
    'register_epitope_tools',
    'register_experiment_tools',
    'register_gene_ontology_ref_tools',
    'register_genome_amr_tools',
    'register_genome_sequence_tools',
    'register_id_ref_tools',
    'register_misc_niaid_sgc_tools',
    'register_pathway_ref_tools',
    'register_pathway_tools',
    'register_ppi_tools',
    'register_protein_family_ref_tools',
    'register_protein_feature_tools',
    'register_protein_structure_tools',
    'register_sequence_feature_vt_tools',
    'register_sequence_feature_tools',
    'register_serology_tools',
    'register_sp_gene_ref_tools',
    'register_sp_gene_tools',
    'register_spike_lineage_tools',
    'register_spike_variant_tools',
    'register_strain_tools',
    'register_structured_assertion_tools',
    'register_subsystem_ref_tools',
    'register_subsystem_tools',
    'register_surveillance_tools',
    'register_taxonomy_tools',
    'register_common_tools'
]
