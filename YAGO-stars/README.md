## YAGO/WIKIDATA STARS GRAPH

A python script that creates a graph of all stars stored in YAGO (~14,000).<br />
Stars are categorized by star type (YAGO) and constellation (Wikidata).<br />
Relevant properties from YAGO and Wikidata are also included.<br />

### MOTIVATION

Testing the creation of data pipelines from open-source knowledge databases (YAGO, Wikidata, etc.) to the brane,<br /> 
and using ontology mappers to automate the categorization of rdf-triples as topics, properties, or metadata.<br />

### CODE OVERVIEW

* Read and save Schema (YAGO) and Wikidata ontology maps.
* Create first layer of graph (root node, star cluster, star type cluster, constellation cluster).
* Get list of all stars using YAGO sparql API.
* For each star:<br />
    * YAGO
        * Get all YAGO rdf-triples and categorize each as a topic, property, or metadata. 
        * Create topics and links for star types and properties. Store metadata.<br />
    * Wikidata
        * Get all Wikidata rdf-triples and categorize each as a topic, property, or metadata.
        * Create topics and links for constellations and properties. Store metadata.<br />
    * Create star topic and make the relevant links.
* Format topics and links, output json files, push data to yago-stars graph using topics api.

### FUTURE USE CASES
This script and methodology can be used as a template for projects that require the importing of data from open-source rdf knowledge databases.

* Ontology Mapping
By using the ontology mapper any data from YAGO or Wikidata can be automatically categorized in order to be dealt with appropriately.<br />
Saving ontology maps:

```python
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# schema
sheet = client.open("Ontology mappings for YAGO Resources").worksheet('Property Schema Datatypes')
# Extract and save as pandas df
list_of_hashes = sheet.get_all_records()
df_schema = pd.DataFrame(list_of_hashes)

# wikidata
sheet = client.open("Ontology mappings for YAGO Resources").worksheet('Wikidata Property Datatypes')
# Extract and save as pandas df
list_of_hashes = sheet.get_all_records()
df_wikidata = pd.DataFrame(list_of_hashes)
```
