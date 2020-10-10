# YAGO/WIKIDATA STARS GRAPH

A python script that creates a graph of all stars stored in YAGO (~14,000).<br />
Stars are categorized by star type (YAGO) and constellation (Wikidata).<br />
Relevant properties from YAGO and Wikidata are also included.<br />

~IMAGE~

## MOTIVATION

Testing the creation of data pipelines from open-source knowledge databases (YAGO, Wikidata, etc.) to the brane,<br /> 
and using ontology mappers to automate the categorization of rdf-triples as topics, properties, or metadata.<br />

## CODE OVERVIEW

* Read and save Schema (YAGO) and Wikidata ontology maps.
* Create first layer of graph (root node, star cluster, star type cluster, constellation cluster).
* Get list of all stars using YAGO sparql API.
* For each star:<br />
    * **YAGO**
        * Get all YAGO rdf-triples and categorize each as a topic, property, or metadata. 
        * Create topics and links for star types and properties. Store metadata.<br />
    * **Wikidata**
        * Get all Wikidata rdf-triples and categorize each as a topic, property, or metadata.
        * Create topics and links for constellations and properties. Store metadata.<br />
    * **Create star topic and make the relevant links.**
* Format topics and links, output json files, push data to yago-stars graph using topics api.
