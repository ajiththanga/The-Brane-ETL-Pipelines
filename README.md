~ Forked from The Brane. Two ETL pipelines I built for them using Python and SPARQL to integrate the RDFS knowledge database, *Yago*, into their existing data infrastructure. ~ 

## YAGO 4

https://yago-knowledge.org/<br /> 

YAGO 4 is an RDFS knowledge base. It is a collection of facts, each of which consists of a subject, a predicate, and an object — as in yago:Elvis_Presley rdf:type schema:Person.<br /> 
YAGO 4 is the latest version of the YAGO knowledge base and contains more than 50 million entities and 2 billion facts.<br /> 

It is based on Wikidata — the largest public general-purpose knowledge base. YAGO refines the data as follows:<br /> 
1. All entity identifiers and property identifiers are human-readable.<br /> 
2. The top-level classes come from schema.org — a standard repertoire of classes and properties maintained by Google and others, combined with bioschemas.org. The lower level classes are a selection of Wikidata classes.<br /> 
3. The properties come from schema.org.<br /> 
4. YAGO 4 contains semantic constraints in the form of SHACL. These constraints keep the data clean, and allow for logical reasoning on YAGO.<br /> 

YAGO puts each entity into at least one class. The classes form a taxonomy, where the higher classes are taken from schema.org (and bioschemas.org), and the lower classes are a selection of classes from Wikidata. The highest class is schema:Thing.<br /> 

### DATA

#### Direct Download
https://yago-knowledge.org/downloads/yago-4 <br /> 

#### SPARQL
SPARQL is the standardized query language for RDF, the same way SQL is the standardized query language for relational databases.<br /> 

**Basic Syntax:**<br /> 
SELECT * WHERE {<br /> 
  ?sub ?pred ?obj .<br /> 
} <br /> 
LIMIT 10<br /> 

This query can be run directly at https://yago-knowledge.org/sparql or through the YAGO API.<br /> 

##### Accessing YAGO API with Python
```
# recreating same query as above in Python

import requests
import json
url = 'https://yago-knowledge.org/sparql/query'

query_parts = list()
select_where = "SELECT * WHERE {"
query = "?sub ?pred ?obj ."
close = "} LIMIT 10"
query_parts.append(select_where)
query_parts.append(query)
query_parts.append(close)
query = "\n".join(query_parts)

# request data and return it in json format
r = requests.get(url, params = {'format': 'json', 'query': query})
yago_data = r.json()
```

```
# a real example: get definition and location of Toronto, ON

import requests
import json
url = 'https://yago-knowledge.org/sparql/query'
city_value = "<http://yago-knowledge.org/resource/yago:Toronto>"

query_parts = list()
prefix = """
          PREFIX yago: <http://yago-knowledge.org/resource/>
          PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
          PREFIX schema: <http://schema.org/> 
          PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
         """
select_where = """SELECT ?yago_url ?definition ?location ?url WHERE {"""

# set variable yago_url to be city_value        
values = """VALUES ?yago_url {0}""".format(city_value)

# use optional, in case the property doesn’t exist
# filter for English comments        
def_query = "OPTIONAL{?yago_url rdfs:comment ?definition . FILTER(lang(?definition)='en')}."
loc_query = "OPTIONAL{?yago_url schema:containedInPlace ?location .}."
close = "} LIMIT 1"

query_parts.append(select_where)
query_parts.append(def_query)
query_parts.append(loc_query)
query_parts.append(close)
query = "\n".join(query_parts)

# request data and return it in json format
r = requests.get(url, params = {'format': 'json', 'query': query})
yago_data = r.json()
```

These examples use 'SELECT' queries which return variable bindings. Using 'CONSTRUCT' queries instead return an RDF graph.<br />  

### CURRENT USES
* Community Graph:<br />
    * YAGO data is used to populate the user onboarding form on the fly and saved to the users api.
    * Properties for all saved data are extracted from YAGO, transformed into topics and links, and added to the community graph.<br />
* YAGO Stars:<br />
    * This script is an example of how to automate the creation of graphs using YAGO data.
    * An ontology mapper classifies YAGO data as a a topic, a property or metadata, and transforms it correspondingly.<br />
    
### POTENTIAL USES
* Creating new graphs from scratch:<br />
    * Search for term in YAGO (T1).
    * Get properties for T1 from YAGO and create graph.
    * Click on linked topic (T2).
    * Get properties for T2 from YAGO and add to graph.
    * Repeat steps 3 and 4.<br />
* Enriching existing graphs:<br />
    * Add data from YAGO for selected topic(s).<br />
* An example for tackling other knowledge databases:<br />
    * The same process can be applied to other databases such as dbpedia and wikidata.
    * The YAGO stars graph already applies this logic to Wikidata, extracting properties to enrich the data using a Wikidata-specific ontology mapper.<br />

### CONCERNS
* API timeout for complex/rapid queries.<br />
* Long loading times for graph data.<br />
