import requests
import json


with open("config.json", "r") as f:
    config = json.load(f)

call_url = "http://127.0.0.1:8059/mcp/tools/call"
list_url = "http://127.0.0.1:8059/mcp/tools/list"

if True:
    print('********* listing tools *********')

    url = list_url

    response = requests.get(url)

    print(response.json())

if False:
    print('********* calling tool: bvbrc_genome_get_by_id *********')

    params = {
        "genome_id": "208964.12",
        "limit": 5,
        "select": "genome_id,genome_name,organism_name,species,genus"
    }

    response = requests.post(call_url, json={"jsonrpc": "2.0", "id": 1, "name": "bvbrc_genome_get_by_id", "params": params})
    print(response.json())

if False:
    print('********* calling tool: bvbrc_genome_get_by_species *********')

    params = {
        "species": "coli",
        "limit": 3,
        "select": "genome_id,genome_name,organism_name,species,genus"
    }

    response = requests.post(call_url, json={"jsonrpc": "2.0", "id": 1, "name": "bvbrc_genome_get_by_species", "params": params})
    print(response.json())

if False:
    print('********* calling tool: bvbrc_genome_get_by_genus *********')

    params = {
        "genus": "Escherichia",
        "limit": 3,
        "select": "genome_id,genome_name,organism_name,species,genus"
    }

    response = requests.post(call_url, json={"jsonrpc": "2.0", "id": 1, "name": "bvbrc_genome_get_by_genus", "params": params})
    print(response.json())

if False:
    print('********* calling tool: bvbrc_genome_query_by_filters *********')

    params = {
        "filters_json": '{"genus": "Escherichia", "species": "coli"}',
        "limit": 3,
        "select": "genome_id,genome_name,organism_name,species,genus"
    }

    response = requests.post(call_url, json={"jsonrpc": "2.0", "id": 1, "name": "bvbrc_genome_query_by_filters", "params": params})
    print(response.json())

if False:
    print('********* calling tool: bvbrc_genome_feature_get_by_genome_id *********')

    params = {
        "genome_id": "208964.12",
        "limit": 5,
        "select": "feature_id,gene,product,feature_type,genome_id"
    }

    response = requests.post(call_url, json={"jsonrpc": "2.0", "id": 1, "name": "bvbrc_genome_feature_get_by_genome_id", "params": params})
    print(response.json())

if False:
    print('********* calling tool: bvbrc_genome_feature_get_by_gene *********')

    params = {
        "gene_name": "lacZ",
        "limit": 5,
        "select": "feature_id,gene,product,feature_type,genome_id"
    }

    response = requests.post(call_url, json={"jsonrpc": "2.0", "id": 1, "name": "bvbrc_genome_feature_get_by_gene", "params": params})
    print(response.json())

if False:
    print('********* calling tool: bvbrc_genome_feature_get_by_product *********')

    params = {
        "product_name": "beta-galactosidase",
        "limit": 5,
        "select": "feature_id,gene,product,feature_type,genome_id"
    }

    response = requests.post(call_url, json={"jsonrpc": "2.0", "id": 1, "name": "bvbrc_genome_feature_get_by_product", "params": params})
    print(response.json())

if False:
    print('********* calling tool: bvbrc_genome_feature_query_by_filters *********')

    params = {
        "filters_json": '{"genome_id": "208964.12", "feature_type": "CDS"}',
        "limit": 5,
        "select": "feature_id,gene,product,feature_type,genome_id"
    }

    response = requests.post(call_url, json={"jsonrpc": "2.0", "id": 1, "name": "bvbrc_genome_feature_query_by_filters", "params": params})
    print(response.json())

if False:
    print('********* calling tool: bvbrc_query_direct *********')

    params = {
        "core": "genome",
        "filter_str": "eq(genome_id,208964.12)",
        "limit": 3,
        "select": "genome_id,genome_name,organism_name,species,genus"
    }

    response = requests.post(call_url, json={"jsonrpc": "2.0", "id": 1, "name": "bvbrc_query_direct", "params": params})
    print(response.json())