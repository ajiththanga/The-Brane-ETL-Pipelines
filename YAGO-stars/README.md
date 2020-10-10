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
        * Create and store topics/links for star types and properties. Store metadata.<br />
    * Wikidata
        * Get all Wikidata rdf-triples and categorize each as a topic, property, or metadata.
        * Create and store topics/links for constellations and properties. Store metadata.<br />
    * Create star topic with stored metadata. Make the relevant links between the star and the stored topics/properties.
* Format topics and links, output json files, push data to yago-stars graph using topics api.

### FUTURE USE CASES
This script and methodology can be used as a template for projects that require the importing of data from open-source rdf knowledge databases.

#### Ontology Mapping<br />
By using the ontology mapper any data from YAGO or Wikidata can be automatically categorized in order to be dealt with appropriately.<br />

##### EXAMPLES

Saving ontology maps as dataframes to be parsed:
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

Function that maps YAGO data using schema ontology: 
```python
def schema_ontology_mapping(data):
    '''
    For each rdf-triple the predicate is searched for in the schema ontology mapping, and categorized as a topic, property or metadata
            Parameters:
                    data (list of dicts): data extracted from yago
            Returns:
                    data (list of dicts): data with new column: 'valueType'
    '''
```

#### Sparql Querying<br />
Data can be directly imported from open-source knowledge databases using their sparql APIs.<br />

##### EXAMPLES

Function to get all yago properties for a star using YAGO sparql API:
```python
def get_star_yago_data(star_url):
    '''
    Returns all properties associated with yago object in json format by calling yago sparql API
            Parameters:
                    star_url (string): yago url of a subject with rdf:type 'Star'
            Returns:
                    data (list of dicts): all properties of a yago object using rdf-triple language
    '''
```

Function to get all wikidata properties for a star using qwikidata.sparql module:
```python
def get_wikidata_info(wikidata_search):
    '''
    Returns all properties associated with wikidata object in json format by using qwikidata.sparql module
            Parameters:
                    wikidata_search (string): wikdata url extracted from yago database
            Returns:
                    data (list of dicts): all properties of a yago object using rdf-triple language
    '''
```

#### General Graph Creation<br />
The procedure this script follows to import and classify data, and then transform it into topics that are stored for link creation, can be modified and updated as needed.
