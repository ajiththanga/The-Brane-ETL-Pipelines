## YAGO 4

https://yago-knowledge.org/

YAGO 4 is an RDFS knowledge base. It is a collection of facts, each of which consists of a subject, a predicate, and an object — as in yago:Elvis_Presley rdf:type schema:Person.
YAGO 4 is the latest version of the YAGO knowledge base and contains more than 50 million entities and 2 billion facts.

It is based on Wikidata — the largest public general-purpose knowledge base. YAGO refines the data as follows:
1. All entity identifiers and property identifiers are human-readable.
2. The top-level classes come from schema.org — a standard repertoire of classes and properties maintained by Google and others, combined with bioschemas.org. The lower level classes are a selection of Wikidata classes.
3. The properties come from schema.org.
4. YAGO 4 contains semantic constraints in the form of SHACL. These constraints keep the data clean, and allow for logical reasoning on YAGO.

YAGO puts each entity into at least one class. The classes form a taxonomy, where the higher classes are taken from schema.org (and bioschemas.org), and the lower classes are a selection of classes from Wikidata. The highest class is schema:Thing.

### DATA

#### Direct Download
https://yago-knowledge.org/downloads/yago-4

#### SPARQL
SPARQL is the standardized query language for RDF, the same way SQL is the standardized query language for relational databases.

Basic Syntax:
SELECT * WHERE {
  ?sub ?pred ?obj .
} 
LIMIT 10

This query can be run directly at https://yago-knowledge.org/sparql or through the YAGO API.

##### Accessing YAGO API with Python
```
if (isAwesome){
  return true
}
```

### CURRENT USES
### FUTURE USES
### CONCERNS
