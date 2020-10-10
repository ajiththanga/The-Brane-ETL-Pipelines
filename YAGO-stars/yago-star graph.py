# coding: utf-8
'''
	Ajith Thangavelautham
	October 2020
	YAGO/WIKIDATA STARS GRAPH
'''


import requests
url = 'https://yago-knowledge.org/sparql/query'
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import re
import json
import os.path
from qwikidata.sparql  import return_sparql_query_results
import numpy as np
import math


### FUNCTIONS

def create_topic(properties):
    '''
    Returns a duplicate of a dictionary without blank values
            Parameters:
                    properties (dict): Dictionary of topic parameters
            Returns:
                    topic_json_struct (dict): Properties dictionary without blank values
    '''
    topic_json_struct = {}
    for prop, value in properties.items():
        if value != None:
            topic_json_struct[prop] = value
    return topic_json_struct


def create_link(properties):
    return create_topic(properties)


def new_topic_key(topic_key_val):
    '''
    Returns an updated topic key for the current topic, and the topic number for the next topic
            Parameters:
                    topic_key_val (int): Current topic number
    '''
    return 'T' + str(topic_key_val), topic_key_val + 1


def new_link_key(link_key_val):
    return 'L' + str(link_key_val), link_key_val + 1


def find_nth(haystack, needle, n):
    '''
    Find position of the nth needle (string) in haystack (string)
    '''
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start


def format_uri(url):
    '''
    Returns the title of a yago, schema, or wikidata page's url
    '''
    start = url.rfind('/')
    title = url[start+1:]
    
    ## yago link
    if url.startswith('http://y') == True:
        title = title.replace("_", " ")
    #remove Q12345678
        if bool(re.search(r'[Q][1-9]', title)) == True:
            stringToRemove = re.search(r'[Q][1-9]', title).group()
            nRemove = find_nth(title, stringToRemove, 1)
            title = title[:nRemove]

    ## schema link
    if url.startswith('http://s') == True: 
        title = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', title)
        title = re.sub('([a-z0-9])([A-Z])', r'\1 \2', title)

    ## owl link
    elif url.startswith('http://w') == True: 
        start2 = title.rfind('#')
        title = title[start2+1:]
        title = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', title)
        title = re.sub('([a-z0-9])([A-Z])', r'\1 \2', title).title()
        
    title = title.rstrip()

    return title


def get_star_yago_data(star_url):
    '''
    Returns all properties associated with yago object in json format by calling yago sparql API
            Parameters:
                    star_url (string): yago url of a subject with rdf:type 'Star'
            Returns:
                    data (list of dicts): all properties of a yago object using rdf-triple language
    '''
    try:
        # create SPARQL query
        star_value = "{<" + star_url + ">}" 
        query_parts = []
        prefix = """
            PREFIX yago: <http://yago-knowledge.org/resource/>
            PREFIX schema: <http://schema.org/>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            """
        select_where = """CONSTRUCT { ?yago_url ?property ?value .} WHERE { """
        values = """VALUES ?yago_url {0} """.format(star_value)
        query1 = "?yago_url ?property ?value ."
        filter1 = """FILTER ( !isLiteral(?value) || lang(?value) = "" || lang(?value)='en' )"""
        filter2 = """FILTER ( ?property not in ( schema:sameAs ) )"""
        close = """}"""
        query_parts.append(prefix)
        query_parts.append(select_where)
        query_parts.append(values)
        query_parts.append(query1)
        query_parts.append(filter1)
        query_parts.append(filter2)
        query_parts.append(close)
        query = "\n".join(query_parts)

        # request data
        r = requests.get(url, params = {'format': 'json', 'query': query})
        data = r.json()
        data = data['results']['bindings']

    except:
        print("error")
        data = None
        
    return data


def get_definition(value):
    '''
    Returns definition (if it exists) of a yago object by calling yago sparql API
            Parameters:
                    value (string): yago url
            Returns:
                    basic_metadata (list of dicts): definition of a yago object using rdf-triple language
    '''
    try:
        
        value = "{<" + value + ">}"

        query_parts = []
        prefix = """
            PREFIX yago: <http://yago-knowledge.org/resource/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX schema: <http://schema.org/> 
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
            """
        select_where = """SELECT ?yago_url ?definition WHERE {"""
        values = """VALUES ?yago_url {0} """.format(value)
        d_query = "OPTIONAL{?yago_url rdfs:comment ?definition . FILTER(lang(?definition)='en')}."
        close = """
            } LIMIT 1
            """
        query_parts.append(prefix)
        query_parts.append(select_where)
        query_parts.append(values)
        query_parts.append(d_query)
        query_parts.append(close)
        query = "\n".join(query_parts)

        # request data
        r = requests.get(url, params = {'format': 'json', 'query': query})
        basic_metadata = r.json()

    except:
        basic_metadata = None
        pass

    return basic_metadata


def get_wikidata_info(wikidata_search):
    '''
    Returns all properties associated with wikidata object in json format by using qwikidata.sparql module
            Parameters:
                    wikidata_search (string): wikdata url extracted from yago database
            Returns:
                    data (list of dicts): all properties of a yago object using rdf-triple language
    '''
    try:
        query_parts = []

        query1 = """SELECT DISTINCT ?predLink ?objValue ?objValueLabel ?predValueLabel ?quantityAmount ?quantityUnitLabel ?qualPredLabel ?qualObjLabel WHERE {"""
        query2 = """VALUES (?item) {0}""".format(wikidata_search)
        query3 = """?item ?predLink ?statement .""" 
        query4 = """?statement ?ps ?objValue ."""
        query5 = """?predValue wikibase:claim ?predLink."""
        query6 = """?predValue wikibase:statementProperty ?ps."""
        query7 = """OPTIONAL {"""
        query8 = """?statement ?psv ?valuenode ."""
        query9 = """?valuenode wikibase:quantityAmount ?quantityAmount."""
        query10 = """?valuenode wikibase:quantityUnit ?quantityUnit.}"""
        query11 = """OPTIONAL {"""
        query12 = """?statement ?pq ?qualObj ."""
        query13 = """?qualPred wikibase:qualifier ?pq .}"""
        query14 = """SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }}"""

        query_parts.append(query1)
        query_parts.append(query2)
        query_parts.append(query3)
        query_parts.append(query4)
        query_parts.append(query5)
        query_parts.append(query6)
        query_parts.append(query7)
        query_parts.append(query8)
        query_parts.append(query9)
        query_parts.append(query10)
        query_parts.append(query11)
        query_parts.append(query12)
        query_parts.append(query13)
        query_parts.append(query14)
        query_string = "\n".join(query_parts)

        res = return_sparql_query_results(query_string)
        data = res["results"]["bindings"]
        
    except:
        data = None
        pass
    
    return data


def schema_ontology_mapping(data):
    '''
    For each rdf-triple the predicate is searched for in the schema ontology mapping, and categorized as a topic, property or metadata
            Parameters:
                    data (list of dicts): data extracted from yago
            Returns:
                    data (list of dicts): data with new column: 'valueType'
    '''
    for i in data:
        predicate = i['predicate']['value']
        df_pred = df_schema.loc[df_schema['url'] == predicate]
        pred_type = df_pred.iloc[0]['_Type']
        i['predicate']['_Type'] = pred_type
        if pred_type == 'Property':
            pred_valuetype = df_pred.iloc[0]['valueType']
            i['predicate']['valueType'] = pred_valuetype
    
    return data


def get_differences(new_topics, filename, isTopic):
    '''
    Returns a list of topics that haven't been created during previous runs by reading a saved json file
    '''
    topics_to_delete = list()
    topics_to_add = list()
    if(os.path.isfile(filename)):
        print("found ", filename)
        with open(filename, 'r+', encoding='utf-8') as f:
            existing_topics_list = json.load(f)
            existing_topics_dict = dict()
            for topic in existing_topics_list:
                existing_topics_dict[topic['_key']] = topic
            new_topics_dict = dict()
            for topic in new_topics:
                new_topics_dict[topic['_key']] = topic

            for existing_topic_key, topic in existing_topics_dict.items():
                # Completely deleted
                if new_topics_dict.get(existing_topic_key) == None:
                    topics_to_delete.append(topic)
                else:
                    # Row has changed?
                    if topic != new_topics_dict[existing_topic_key]:
                        topics_to_delete.append(topic)

            for new_topic_key, topic in new_topics_dict.items():
                # Brand new topic?
                if existing_topics_dict.get(new_topic_key) == None:
                    topics_to_add.append(topic)
                else:
                    # Row has changed?
                    if topic != existing_topics_dict[new_topic_key]:
                        topics_to_add.append(topic)
    # First time running - will assume all topics need to be added to graph
    else:
        topics_to_add = new_topics

    for topic in topics_to_add:
        if isTopic:
            topic['_id'] = 'topics/' + topic['_key']
        else:
            topic['_id'] = 'links/' + topic['_key']
            topic['_to'] = 'topics/' + topic['_to']

    # Links will use a different format: It will be a dict with key as link's from_, value as list of topics with that from_
    if not isTopic:
        my_new_links = dict()
        for link in topics_to_add:
            from_ = link['_from']
            if my_new_links.get(from_) == None:
                my_new_links[from_] = list()
            link['_from'] = 'topics/' + from_
            my_new_links[from_].append(link)
        return my_new_links, topics_to_delete

    return topics_to_add, topics_to_delete


def format_with_metadata(topics, links):
    '''
    Returns a list of topics and links with metadata properly formatted for the brane
    '''
    new_topics = list()
    new_links = dict()

    for old_topic in topics:
        topic = dict()
        for prop, val in old_topic.items():
            propSet = False
            if prop == '_key':
                continue
            if prop == 'title' or prop == '_type' or prop == 'definition' or prop == '_id' or prop == 'terms' or prop == 'reference' or prop == 'sources':
                topic[prop] = val
                propSet = True
            elif val != '':
                if old_topic['_type'] == 'property':
                    if prop == 'valueType':
                        topic[prop] = val
                        propSet = True
                # Add more if statements if necessary
                if not propSet:
                    if topic.get('metadata') == None:
                        topic['metadata'] = dict()
                    topic['metadata'][prop] = val
                    propSet = True
        new_topics.append(topic)

    # Assume these have been formatted correctly already other than _key
    for from_, old_links in links.items():
        new_links[from_] = list()
        for old_link in old_links:
            link = dict()
            for prop, val in old_link.items():
                propSet = False
                if prop == '_key':
                    continue
                if prop == 'name' or prop == '_id' or prop == 'definition' or prop == '_from' or prop == '_to' or prop == '_type':
                    link[prop] = val
                    propSet = True
                elif val != '':
                    if old_link['_type'] == 'has':
                        if prop == 'value':
                            link[prop] = val
                            propSet = True

                    if not propSet:
                        if link.get('metadata') == None:
                            link['metadata'] = dict()
                        link['metadata'][prop] = val
                        propSet = True
            new_links[from_].append(link)

    return new_topics, new_links


def output_to_file(info, file):
    '''
    Outputs 2 json files for topics and links
            Parameters:
                    info (list): list of topics or links
                    file (string): file name to be saved as
    '''
    with open(file, 'w', encoding='utf-8') as f:
        f.write('[')
        i = 0
        for topic in info:
            f.write(json.dumps(topic, ensure_ascii=False))
            if i != len(info) - 1:
                f.write(",\n")
            else:
                f.write('\n')
            i = i + 1
        f.write(']')


### CODE


### 1. VARIABLE INITIALIZATION

topic_filename = 'star_topics.json'
link_filename = 'star_links.json'

# list of topics and links to be sent to the brane
new_topics = list()
new_links = list()

# dictionaries to save and check existing topics and properties to avoid duplicates
topic_title_to_key = dict()
prop_title_unit_to_key = dict()


### 2. SAVE ONTOLOGY MAPS

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


### 3. CREATE FIRST LAYER OF GRAPH
# root node, star cluster, star type cluster, constellation cluster

# create root node
topic_params = {
    '_key': 'T1', 
    '_type': 'system', 
    'title': 'YAGO STARS', 
    'reference': 'https://yago-knowledge.org/resource/Star', 
    'definition': '', 
    'valueType': '', 
}
new_topics.append(create_topic(topic_params))

# create star type cluster and link to root node
topic_params = {
    '_key': 'T2', 
    '_type': 'cluster', 
    'title': 'Star Types', 
    'reference': '', 
    'definition': '', 
    'valueType': '', 
}
new_topics.append(create_topic(topic_params))

link_params = {
    '_key': 'L1',
    '_type': 'encompasses',
    '_from': 'T1', 
    '_to': 'T2'
}
new_links.append(create_link(link_params))

# create star cluster and link to root node
topic_params = {
    '_key': 'T3', 
    '_type': 'cluster', 
    'title': 'Stars', 
    'reference': '', 
    'definition': '', 
    'valueType': '', 
}
new_topics.append(create_topic(topic_params))

link_params = {
    '_key': 'L2',
    '_type': 'encompasses',
    '_from': 'T1', 
    '_to': 'T3'
}
new_links.append(create_link(link_params))

# create constellation cluster and link to root node
topic_params = {
    '_key': 'T4', 
    '_type': 'cluster', 
    'title': 'Constellations', 
    'reference': '', 
    'definition': '', 
    'valueType': '', 
}
new_topics.append(create_topic(topic_params))

link_params = {
    '_key': 'L3',
    '_type': 'encompasses',
    '_from': 'T1', 
    '_to': 'T4'
}
new_links.append(create_link(link_params))

star_key = 'T5' 
topic_key_val = 6
link_key_val = 4


### 4. GET LIST OF STARS FROM YAGO

star_list = list()

# create SPARQL query
query_parts = []
prefix = """
    PREFIX yago: <http://yago-knowledge.org/resource/>
    PREFIX schema: <http://schema.org/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    """ 
select_where = """SELECT ?star WHERE {"""
query1 = """?star rdf:type yago:Star ."""
close = """}"""
query_parts.append(prefix)
query_parts.append(select_where)
query_parts.append(query1)
query_parts.append(close)
query = "\n".join(query_parts)

# request data
r = requests.get(url, params = {'format': 'json', 'query': query})
data = r.json()
data = data['results']['bindings']
for i in data:
    star_list.append(i['star']['value'])

### 5. LOOP THROUGH LIST OF STARS AND TRANSFORM DATA TO BRANE FORMAT

star_num = 1
for star_url in star_list:
    print(str(star_num) + ": " + star_url)
    star_num += 1
    
    star_data = get_star_yago_data(star_url)
    
    if star_data != None:
        
        star_data = schema_ontology_mapping(star_data)

        # used for creating links
        topics_list = list()
        metadata_list = list()
        property_list = list()

        for star_property in star_data:

            # if type = topic
            # for yago topics, only interested in rdf:type 
            if star_property['predicate']['_Type'] == "Topic":

                # ignore type = Star, Thing, Place. also ignore location topic since only 2/~13k stars have it 
                if star_property['object']['value'] not in ('http://yago-knowledge.org/resource/Star','http://schema.org/Thing', 'http://schema.org/Place', 'http://schema.org/containedInPlace'):

                    topic_ref = star_property['object']['value']
                    topic_title = format_uri(star_property['object']['value'])

                    # if topic already exists, get key
                    if (topic_title_to_key.get(topic_title) != None):
                        topic_key = topic_title_to_key[topic_title]

                    # if topic doesn't exist, create it
                    else:
                        topic_key, topic_key_val = new_topic_key(topic_key_val)
                        topic_params = {
                            '_key': topic_key,
                            '_type': 'cluster',
                            'title': topic_title,
                            'reference': topic_ref,
                            'definition': '', 
                            'valueType': ''
                        }

                        # get definition
                        definition = get_definition(star_property['object']['value'])
                        if 'definition' in definition['results']['bindings'][0]:
                            definition = definition['results']['bindings'][0]['definition']['value']
                            topic_params['definition'] = definition

                        new_topics.append(create_topic(topic_params))
                        topic_title_to_key[topic_title] = topic_key

                    topics_list.append({'_key':topic_key,'title':topic_title})

                    # link to star type cluster
                    link_key, link_key_val = new_link_key(link_key_val)
                    link_params = {
                        '_key': link_key,
                        '_type': 'hasSubclass',
                        '_from': 'T2', 
                        '_to': topic_key
                    }
                    new_links.append(create_link(link_params))

            # if type = metadata, store
            elif star_property['predicate']['_Type'] == "Metadata":
                metadata_dict = {'predicate':format_uri(star_property['predicate']['value']),'object':star_property['object']['value']}
                metadata_list.append(metadata_dict)

            # if type = property, create topic and store
            elif star_property['predicate']['_Type'] == "Property":

                property_value = star_property['object']['value']
                property_title = format_uri(star_property['predicate']['value'])
                property_unit = ''
                prop_title_unit = property_title + '; ' + property_unit

                # if property already exists, get key
                if (prop_title_unit_to_key.get(prop_title_unit) != None):
                    topic_key = prop_title_unit_to_key[prop_title_unit]

                # if property doesn't exist, create it
                else:            
                    topic_key, topic_key_val = new_topic_key(topic_key_val)

                    property_ref = star_property['predicate']['value']
                    property_title = format_uri(star_property['predicate']['value'])
                    property_value = star_property['object']['value']
                    valueType = star_property['predicate']['valueType']

                    topic_params = {
                        '_key': topic_key,
                        '_type': 'property',
                        'title': property_title,
                        'reference': property_ref,
                        'definition': '', 
                        'valueType': valueType,
                        'unit': property_unit
                    }                    
                    new_topics.append(create_topic(topic_params))
                    prop_title_unit_to_key[prop_title_unit] = topic_key

                property_list.append({'_key':topic_key,'title':property_title, 'value':property_value})

        ##### wikidata

        # get wikidata link from yago data
        wikidata_url = "/"
        for star_property in star_data:
            if star_property['predicate']['value'] == 'http://www.w3.org/2002/07/owl#sameAs' and star_property['object']['value'].startswith("http://www.wikidata.org/entity/"):
                wikidata_url = star_property['object']['value']
                break
        start = wikidata_url.rfind('/')
        wikidata_id = wikidata_url[start+1:]  
        wikidata_search = "{(wd:" + wikidata_id + ")}"
        
        # wikidata sparql query
        wikidata_data = get_wikidata_info(wikidata_search)

        if wikidata_data != None:

            wiki_property_list = list()
            wiki_topic_list = list()
            wiki_metadata_list = list()

            for i in wikidata_data:

                predicate = i['predValueLabel']['value']
                df_pred = df_wikidata.loc[df_wikidata['label'] == predicate]
                df_pred = df_pred.replace(r'^\s*$', np.nan, regex=True)
                
                # classify type using ontology mapper
                # check if predicate is topic, property or metadata
                # save relevant data from wikidata and ontology map (use "" values instead of nan)

                # property
                if pd.notnull(df_pred.iloc[0,6]): 

                    qualifier = ""
                    if "qualPredLabel" and "qualObjLabel" in i:
                        qualifier = i['qualObjLabel']['value'] + ": " + i['qualPredLabel']['value']

                    wiki_object = i['objValueLabel']['value']
                    if "quantityAmount" in i:
                        wiki_object = i['quantityAmount']['value']

                    unit = ""
                    if "quantityUnitLabel" in i:
                        unit = i['quantityUnitLabel']['value']

                    prop_reference = ""
                    if "predLink" in i:
                        prop_reference = i['predLink']['value']

                    if type(df_pred.iloc[0,8]) != str and math.isnan(df_pred.iloc[0,8]):
                        terms = ""
                    else:
                        terms = df_pred.iloc[0,8]

                    if type(df_pred.iloc[0,9]) != str and math.isnan(df_pred.iloc[0,9]):
                        desc = ""
                    else:
                        desc = df_pred.iloc[0,9]

                    if type(df_pred.iloc[0,10]) != str and math.isnan(df_pred.iloc[0,10]):
                        valuetype = ""
                    else:
                        valuetype = df_pred.iloc[0,10]

                    property_dict = {
                        'wiki_predicate':predicate,             
                        'wiki_object':wiki_object,
                        'unit':unit,
                        'qualifier':qualifier,
                        'reference':prop_reference,
                        'terms':terms, 
                        'description':desc, 
                        'value type':valuetype}

                    wiki_property_list.append(property_dict)

                # topic
                elif pd.notnull(df_pred.iloc[0,11]):

                    if type(df_pred.iloc[0,13]) != str and math.isnan(df_pred.iloc[0,13]):
                        linktype = ""
                    else:
                        linktype = df_pred.iloc[0,13]

                    if type(df_pred.iloc[0,14]) != str and math.isnan(df_pred.iloc[0,14]):
                        aliases = ""
                    else:
                        aliases = df_pred.iloc[0,14]

                    if type(df_pred.iloc[0,15]) != str and math.isnan(df_pred.iloc[0,15]):
                        desc = ""
                    else:
                        desc = df_pred.iloc[0,15]

                    topic_dict = {
                        'wiki_predicate':predicate, 
                        'wiki_object':i['objValueLabel']['value'],
                        'object_link':i['objValue']['value'],
                        'link type':linktype, 
                        'aliases':aliases, 
                        'description':desc}

                    wiki_topic_list.append(topic_dict)

                # metadata
                elif pd.notnull(df_pred.iloc[0,16]):

                    if type(df_pred.iloc[0,16]) != str and math.isnan(df_pred.iloc[0,16]):
                        mdtype = ""
                    else:
                        mdtype = df_pred.iloc[0,16]

                    if type(df_pred.iloc[0,17]) != str and math.isnan(df_pred.iloc[0,17]):
                        label = ""
                    else:
                        label = df_pred.iloc[0,17]

                    if type(df_pred.iloc[0,18]) != str and math.isnan(df_pred.iloc[0,18]):
                        terms = ""
                    else:
                        terms = df_pred.iloc[0,18]

                    if type(df_pred.iloc[0,19]) != str and math.isnan(df_pred.iloc[0,19]):
                        desc = ""
                    else:
                        desc = df_pred.iloc[0,19]

                    if type(df_pred.iloc[0,20]) != str and math.isnan(df_pred.iloc[0,20]):
                        aliases = ""
                    else:
                        aliases = df_pred.iloc[0,20]

                    if type(df_pred.iloc[0,21]) != str and math.isnan(df_pred.iloc[0,21]):
                        image = ""
                    else:
                        image = df_pred.iloc[0,21]

                    if type(df_pred.iloc[0,22]) != str and math.isnan(df_pred.iloc[0,22]):
                        ref = ""
                    else:
                        ref = df_pred.iloc[0,22]

                    metadata_dict = {
                        'wiki_predicate':predicate, 
                        'wiki_object':i['objValueLabel']['value'],  
                        'metadata type':mdtype, 
                        'label':label, 
                        'terms':terms, 
                        'description':desc, 
                        'image':image, 
                        'reference':ref}

                    wiki_metadata_list.append(metadata_dict)

            # create wikidata property topics

            for wiki_prop in wiki_property_list: 

                property_value = wiki_prop['wiki_object']
                property_title = wiki_prop['wiki_predicate']
                property_unit = wiki_prop['unit']
                prop_title_unit = property_title + '; ' + property_unit

                # if property already exists, get key
                if (prop_title_unit_to_key.get(prop_title_unit) != None):
                    topic_key = prop_title_unit_to_key[prop_title_unit]

                # if topic doesn't exist, create it
                else:
                    topic_key, topic_key_val = new_topic_key(topic_key_val)

                    property_ref = wiki_prop['reference']
                    valueType = wiki_prop['value type']
                    property_desc = wiki_prop['description']
                    property_qual = wiki_prop['qualifier']
                    property_terms = wiki_prop['terms']

                    topic_params = {
                        '_key': topic_key,
                        '_type': 'property',
                        'title': property_title,
                        'reference': property_ref,
                        'definition': property_desc, 
                        'valueType': valueType,
                        'unit': property_unit,
                        'qualifier': property_qual,
                        'terms': property_terms
                    }                    
                    new_topics.append(create_topic(topic_params))
                    prop_title_unit_to_key[prop_title_unit] = topic_key

                property_list.append({'_key':topic_key,'title':property_title, 'value':property_value})

            ## create topic for constellations only and link to constellation cluster
            for wiki_topic in wiki_topic_list:
                if wiki_topic['wiki_predicate'] == 'constellation':

                    topic_ref = wiki_topic['object_link']
                    topic_title = wiki_topic['wiki_object']
                    topic_def = wiki_topic['description']

                    # if topic already exists, get key
                    if (topic_title_to_key.get(topic_title) != None):
                        topic_key = topic_title_to_key[topic_title]

                    # if topic doesn't exist, create it
                    else:
                        topic_key, topic_key_val = new_topic_key(topic_key_val)
                        topic_params = {
                            '_key': topic_key,
                            '_type': 'cluster',
                            'title': topic_title,
                            'reference': topic_ref,
                            'definition': topic_def, 
                            'valueType': ''
                        }
                        new_topics.append(create_topic(topic_params))
                        topic_title_to_key[topic_title] = topic_key

                    topics_list.append({'_key':topic_key,'title':topic_title})

                    # link to type cluster
                    link_key, link_key_val = new_link_key(link_key_val)
                    link_params = {
                        '_key': link_key,
                        '_type': 'hasSubclass',
                        '_from': 'T4', 
                        '_to': topic_key
                    }
                    new_links.append(create_link(link_params))
            
            # save wikidata metadata values
            for wiki_metadata in wiki_metadata_list:
                metadata_dict = {
                    'predicate':wiki_metadata['wiki_predicate'],
                    'object':wiki_metadata['wiki_object']
                }
                metadata_list.append(metadata_dict)

        ##### create star topic
        topic_params = {
            '_key': star_key, 
            '_type': 'star', 
            'title': format_uri(star_url),
            'reference': star_url,
            'definition': '', 
            'valueType': ''
        }
        # add metadata
        for metadata in metadata_list:
            if metadata['predicate'] == 'http://www.w3.org/2000/01/rdf-schema#comment':
                topic_params['definition'] = metadata['object']
            else:
                metadata_title = format_uri(metadata['predicate'])
                if metadata_title in topic_params: # check for duplicate metadata titles
                    topic_params[metadata_title] = topic_params[metadata_title] + '; ' + metadata['object']
                else:
                    topic_params[metadata_title] = metadata['object']

        new_topics.append(create_topic(topic_params))

        # link star to topic clusters (star type, constellation)
        for topic in topics_list:

            link_key, link_key_val = new_link_key(link_key_val)
            link_params = {
                '_key': link_key,
                '_type': 'hasInstance',
                '_from': topic['_key'], 
                '_to': star_key
            }
            new_links.append(create_link(link_params))

        # link star to star cluster
        link_key, link_key_val = new_link_key(link_key_val)
        link_params = {
            '_key': link_key,
            '_type': 'hasInstance',
            '_from': 'T3', 
            '_to': star_key
        }
        new_links.append(create_link(link_params))

        # link property to star
        for star_property in property_list:

            link_key, link_key_val = new_link_key(link_key_val)
            link_params = {
                '_key': link_key,
                '_type': 'has',
                '_from': star_key, 
                '_to': star_property['_key'],
                'name': star_property['title'],
                'value': star_property['value']
            }
            new_links.append(create_link(link_params))

        # update key for next star
        star_key, topic_key_val = new_topic_key(topic_key_val)


### 6. FORMAT TOPICS AND LINKS

topics_to_add, topics_to_delete = get_differences(new_topics, topic_filename, True)
links_to_add, links_to_delete = get_differences(new_links, link_filename, False)
topics_to_add_metadata, links_to_add_metadata = format_with_metadata(topics_to_add, links_to_add)


### 7. OUTPUT JSON FILES

for link in new_links:
    if (link.get('_id') != None):
        # Effectively checking if we added any new links
        link['_from'] = link['_from'][7:]
        link['_to'] = link['_to'][7:]
        link.pop('_id')
for topic in new_topics:
    if (topic.get('_id') != None):
        topic.pop('_id')

print("Outputting to files")
output_to_file(new_topics, topic_filename)
output_to_file(new_links, link_filename)


### 8. PUSH TOPICS AND LINKS TO GRAPH USING TOPICS API

start_url = 'http://topics-api.staging.thebrane.com/yago-stars/'

# Add new topics
if (len(topics_to_add_metadata) != 0):
    print("Adding new topics ", len(topics_to_add_metadata))
    topics_post_url = start_url + 'topics'
    requests.post(topics_post_url, json=topics_to_add_metadata)

# Add new links
if (len(links_to_add_metadata) != 0):
    print("Adding new links ", len(links_to_add_metadata))
    link_post_url = start_url + 'topics'
    headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
    for from_, links in links_to_add_metadata.items():
        url = link_post_url + '/' + from_ + '/links'
        requests.post(url, json=links, headers=headers)