# -*- coding: utf-8 -*-
'''
	Ajith Thangavelautham
	August 2020
	onboarding form to community graph conversion
'''


import re
import requests
import json
import os.path
import sys
import unidecode
url = 'https://yago-knowledge.org/sparql/query'


### FUNCTIONS

# Auto generated list of initial topics and links
class Convert_Clusters():
    
    def __init__(self):
        print("Creating clusters for community graph")
        
    def convert_clusters(self):
        cluster_topics = list()
        cluster_links = list()
        properties = dict()

        final_topic = 0
        final_link = 0
        
        # Create topics
        properties = dict()
        properties['_key'] = ''
        properties['_type'] = ''
        properties['title'] = ''
        properties['reference'] = ''
        properties['definition'] = ''
        properties['valueType'] = ''

        # T1
        properties['_key'] = 'T1'
        properties['_type'] = 'system'
        properties['title'] = 'The Brane Community'
        properties['reference'] = 'thebrane.com'
        properties['definition'] = ''
        properties['valueType'] = ''
        cluster_topics.append(create_topic(properties))
        
        # T2
        properties['_key'] = 'T2'
        properties['_type'] = 'cluster'
        properties['title'] = 'Member'
        properties['reference'] = ''
        properties['definition'] = ''
        properties['valueType'] = ''
        cluster_topics.append(create_topic(properties))
        
        # T3
        properties['_key'] = 'T3'
        properties['_type'] = 'cluster'
        properties['title'] = 'City'
        properties['reference'] = 'https://schema.org/City'
        properties['definition'] = ''
        properties['valueType'] = ''
        cluster_topics.append(create_topic(properties))
        
        # T4
        properties['_key'] = 'T4'
        properties['_type'] = 'cluster'
        properties['title'] = 'Country'
        properties['reference'] = 'https://schema.org/Country'
        properties['definition'] = ''
        properties['valueType'] = ''
        cluster_topics.append(create_topic(properties))
        
        # T5
        properties['_key'] = 'T5'
        properties['_type'] = 'cluster'
        properties['title'] = 'Organisation'
        properties['reference'] = 'https://schema.org/Organization'
        properties['definition'] = ''
        properties['valueType'] = ''
        cluster_topics.append(create_topic(properties))

        # T6
        properties['_key'] = 'T6'
        properties['_type'] = 'cluster'
        properties['title'] = 'Discipline'
        properties['reference'] = 'http://lod.openlinksw.com/describe/?uri=http://yago-knowledge.org/resource/Discipline_(academia)'
        properties['definition'] = ''
        properties['valueType'] = ''
        cluster_topics.append(create_topic(properties))
        
        # T7
        properties['_key'] = 'T7'
        properties['_type'] = 'cluster'
        properties['title'] = 'Occupation'
        properties['reference'] = 'https://schema.org/Occupation'
        properties['definition'] = ''
        properties['valueType'] = ''
        cluster_topics.append(create_topic(properties))
        
        # T8
        properties['_key'] = 'T8'
        properties['_type'] = 'cluster'
        properties['title'] = 'Skill'
        properties['reference'] = ''
        properties['definition'] = ''
        properties['valueType'] = ''
        cluster_topics.append(create_topic(properties))
        
        # T9
        properties['_key'] = 'T9'
        properties['_type'] = 'cluster'
        properties['title'] = 'Project'
        properties['reference'] = ''
        properties['definition'] = ''
        properties['valueType'] = ''
        cluster_topics.append(create_topic(properties))
        
        # T10
        properties['_key'] = 'T10'
        properties['_type'] = 'cluster'
        properties['title'] = 'Educational Organisation'
        properties['reference'] = 'https://schema.org/EducationalOrganization'
        properties['definition'] = ''
        properties['valueType'] = ''
        cluster_topics.append(create_topic(properties))
        
        final_topic = 10
        
        # Create links
        properties = dict()
        properties['_key'] = ''
        properties['_type'] = ''
        properties['name'] = ''
        properties['_from'] = ''
        properties['_to'] = ''
        properties['value'] = ''
        
        # L1
        properties['_key'] = 'L1'
        properties['_type'] = 'encompasses'
        properties['name'] = ''
        properties['_from'] = 'T1'
        properties['_to'] = 'T2'
        properties['value'] = ''
        cluster_links.append(create_link(properties))

        # L2
        properties['_key'] = 'L2'
        properties['_type'] = 'encompasses'
        properties['name'] = ''
        properties['_from'] = 'T1'
        properties['_to'] = 'T3'
        properties['value'] = ''
        cluster_links.append(create_link(properties))
        
        # L3
        properties['_key'] = 'L3'
        properties['_type'] = 'encompasses'
        properties['name'] = ''
        properties['_from'] = 'T1'
        properties['_to'] = 'T4'
        properties['value'] = ''
        cluster_links.append(create_link(properties))
        
        # L4
        properties['_key'] = 'L4'
        properties['_type'] = 'encompasses'
        properties['name'] = ''
        properties['_from'] = 'T1'
        properties['_to'] = 'T5'
        properties['value'] = ''
        cluster_links.append(create_link(properties))
        
        # L5
        properties['_key'] = 'L5'
        properties['_type'] = 'encompasses'
        properties['name'] = ''
        properties['_from'] = 'T1'
        properties['_to'] = 'T6'
        properties['value'] = ''
        cluster_links.append(create_link(properties))
        
        # L6
        properties['_key'] = 'L6'
        properties['_type'] = 'encompasses'
        properties['name'] = ''
        properties['_from'] = 'T1'
        properties['_to'] = 'T7'
        properties['value'] = ''
        cluster_links.append(create_link(properties))
        
        # L7
        properties['_key'] = 'L7'
        properties['_type'] = 'encompasses'
        properties['name'] = ''
        properties['_from'] = 'T1'
        properties['_to'] = 'T8'
        properties['value'] = ''
        cluster_links.append(create_link(properties))
        
        # L8
        properties['_key'] = 'L8'
        properties['_type'] = 'encompasses'
        properties['name'] = ''
        properties['_from'] = 'T1'
        properties['_to'] = 'T9'
        properties['value'] = ''
        cluster_links.append(create_link(properties))
        
        # L9
        properties['_key'] = 'L9'
        properties['_type'] = 'hasSubclass'
        properties['name'] = ''
        properties['_from'] = 'T5'
        properties['_to'] = 'T10'
        properties['value'] = ''
        cluster_links.append(create_link(properties))
        
        final_link = 9

        return cluster_topics, cluster_links, final_topic + 1, final_link + 1


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


def add_new_topics(old_topics, new_topics):
    for topic in new_topics:
        old_topics.append(topic)
    return old_topics


def add_new_links(old_links, new_links):
    for link in new_links:
        old_links.append(link)
    return old_links


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


def get_city_data(city_value):
    '''
    Returns necessary properties for a yago object of type schema:City
            Parameters:
                    city_value (string): yago url (from user api)
            Returns:
                    data (list of dicts): properties of city using rdf-triple language
    '''
    try:
        city_value = "{<" + city_value + ">}"    
        query_parts = []
        prefix = """
            PREFIX yago: <http://yago-knowledge.org/resource/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX schema: <http://schema.org/> 
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
            """
        select_where = """SELECT ?yago_url ?definition ?location ?url WHERE {"""
        values = """VALUES ?yago_url {0} """.format(city_value)
        d_query = "OPTIONAL{?yago_url rdfs:comment ?definition . FILTER(lang(?definition)='en')}."
        l_query = "OPTIONAL{?yago_url schema:containedInPlace ?location .}."
        u_query = "OPTIONAL{?yago_url schema:url ?url.}."
        close = """
            }
            LIMIT 1
            """
        query_parts.append(prefix)
        query_parts.append(select_where)
        query_parts.append(values)
        query_parts.append(d_query)
        query_parts.append(l_query)
        query_parts.append(u_query)
        query_parts.append(close)
        query = "\n".join(query_parts)

        # request data
        r = requests.get(url, params = {'format': 'json', 'query': query})
        city_data = r.json()

    except:
        city_data = None
        pass
    
    return city_data


def get_org_data(org_value):
    '''
    Returns necessary properties for a yago object of type schema:Organisation
            Parameters:
                    org_value (string): yago url (from user api)
            Returns:
                    data (list of dicts): properties of org using rdf-triple language
    '''
    try: 
        org_value = "{<" + org_value + ">}"

        query_parts = []
        prefix = """
            PREFIX yago: <http://yago-knowledge.org/resource/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX schema: <http://schema.org/> 
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
            """
        select_where = """SELECT ?yago_url ?definition ?location ?foundinglocation ?url (group_concat(distinct ?type; separator = "; ") as ?types) WHERE {"""
        values = """VALUES ?yago_url {0} """.format(org_value)
        d_query = "OPTIONAL{?yago_url rdfs:comment ?definition . FILTER(lang(?definition)='en')}."
        l_query = "OPTIONAL{?yago_url schema:containedInPlace ?location .}."
        fl_query = "OPTIONAL{?yago_url schema:foundingLocation ?foundinglocation .}."
        u_query = "OPTIONAL{?yago_url schema:url ?url.}."
        t_query = "OPTIONAL{?yago_url rdf:type ?type.}."
        close = """
            }
            group by ?yago_url ?definition ?location ?foundinglocation ?url
            LIMIT 1
            """
        query_parts.append(prefix)
        query_parts.append(select_where)
        query_parts.append(values)
        query_parts.append(d_query)
        query_parts.append(l_query)
        query_parts.append(fl_query)
        query_parts.append(u_query)
        query_parts.append(t_query)
        query_parts.append(close)
        query = "\n".join(query_parts)

        # request data
        r = requests.get(url, params = {'format': 'json', 'query': query})
        org_data = r.json()
    
    except:
        print("error")
        org_data = None
        pass
    
    return org_data


def get_country_value(value):
    '''
    Returns country that a city is located in (separate yago query in case it times out)
            Parameters:
                    value (string): yago url of city location (from city sparql query)
            Returns:
                   country_value (string): country that city is located
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
        select_where = """SELECT ?yago_url ?country WHERE {"""
        values = """VALUES ?yago_url {0} """.format(value)
        country_query = "?yago_url schema:containedInPlace* ?country ."
        country_filter = "?country rdf:type schema:Country ."
        close = """
            } LIMIT 1
            """
        query_parts.append(prefix)
        query_parts.append(select_where)
        query_parts.append(values)
        query_parts.append(country_query)
        query_parts.append(country_filter)
        query_parts.append(close)
        query = "\n".join(query_parts)

        # request data
        r = requests.get(url, params = {'format': 'json', 'query': query})
        containedinplace_data = r.json()
        country_value = containedinplace_data['results']['bindings'][0]['country']['value']
    
    except:
        country_value = None
        pass
    
    return country_value


def get_basic_metadata(value):
    '''
    Returns definition and url (if exists) of a yago object
            Parameters:
                    value (string): yago url (from user api)
            Returns:
                    basic_metadata (list of dicts): properties of yago object using rdf-triple language
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
        select_where = """SELECT ?yago_url ?definition ?url WHERE {"""
        values = """VALUES ?yago_url {0} """.format(value)
        d_query = "OPTIONAL{?yago_url rdfs:comment ?definition . FILTER(lang(?definition)='en')}."
        u_query = "OPTIONAL{?yago_url schema:url ?url.}."
        close = """
            } LIMIT 1
            """
        query_parts.append(prefix)
        query_parts.append(select_where)
        query_parts.append(values)
        query_parts.append(d_query)
        query_parts.append(u_query)
        query_parts.append(close)
        query = "\n".join(query_parts)

        # request data
        r = requests.get(url, params = {'format': 'json', 'query': query})
        basic_metadata = r.json()

    except:
        basic_metadata = None
        pass

    return basic_metadata


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


### IMPORT DATA
user_data = json.loads(unidecode.unidecode(sys.argv[1]))


### TRANSFORM AND SEND DATA
class Community_Graph():
    
    def __init__(self, base_url, graph_name):
        self.base_url = base_url
        self.graph_name = graph_name
    def convert(self):
        
        topic_filename = "community_topics.json" 
        link_filename = "community_links.json"
        
        # Topics, Links to output at end
        new_topics = list()
        new_links = list()
        
        # save topics and their keys to this dict to avoid duplication
        topic_title_to_key = dict()

        # Find latest topic and link number if script run before (topic and link jsons exist)
        topic_past_data = []
        if(os.path.isfile(topic_filename) and os.path.isfile(link_filename)):
            previous_run = True
            with open(topic_filename, encoding='utf-8') as f:
                topic_past_data = json.load(f)
            topic_num_max = 0
            for i in topic_past_data:
                topic_num = int(i['_key'][1:])
                if int(topic_num) > topic_num_max:
                    topic_num_max = topic_num
            
            with open(link_filename, encoding='utf-8') as f:
                link_past_data = json.load(f)
            link_num_max = 0
            for i in link_past_data:
                link_num = int(i['_key'][1:])
                if int(link_num) > link_num_max:
                    link_num_max = link_num
                    
            topic_key_val = topic_num_max + 1
            link_key_val = link_num_max + 1
        
        # create clusters if first time running (topic and link jsons don't exist)
        else:
            previous_run = False
            cluster_runner = Convert_Clusters()
            cluster_topics, cluster_links, topic_key_val, link_key_val = cluster_runner.convert_clusters()
            new_topics = add_new_topics(new_topics, cluster_topics)
            new_links = add_new_links(new_links, cluster_links)

        ### load, parse, save data from users api
        
        # if user_data isn't empty
        if user_data['user']:

            # Set member key
            member_key, topic_key_val = new_topic_key(topic_key_val)
            
            ### LOCATION
            city_value = user_data['user']['metadata']['Location']
            print(city_value)
            
            # check if city topic already exists from previous run
            past_run_check = next((item for item in topic_past_data if item["reference"] == city_value), None)
            if past_run_check != None and previous_run:
                city_key = past_run_check["_key"]
                city_title = past_run_check["title"]
                print("city found " +  city_key)
            
                # link city and member
                link_key, link_key_val = new_link_key(link_key_val)
                link_params = {
                    '_key': link_key,
                    '_type': 'link',
                    'name': 'is located in',
                    '_from': member_key, 
                    '_to': city_key
                }
                new_links.append(create_link(link_params))
                print(link_params)
            
            # city topic doesn't exist, create it and link
            else:
                print("city not found")
                # city yago api call
                city_data = get_city_data(city_value)
                city_title = ""
                
                if city_data != None:
                    city_results = city_data['results']['bindings'][0]
                    
                    city_title = format_uri(city_results['yago_url']['value'])
                    if city_title != "":
                    
                        # initialize country variables
                        country_key = None
                        country_title = ""
            
                        if 'location' in city_results:
                            country_value = get_country_value(city_value)
            
                            if country_value != None:
            
                                # country yago api call
                                country_data = get_basic_metadata(country_value)
                                country_results = country_data['results']['bindings'][0]
            
                                # check if country topic already exists from previous run
                                past_run_check = next((item for item in topic_past_data if item["reference"] == country_value), None)
                                if past_run_check != None and previous_run:
                                    country_key = past_run_check["_key"]
                                    country_title = past_run_check["title"]
                                    print("country found " + country_key)
                                    country_found = True
            
                                # check if country topic already exists from this run
                                elif (topic_title_to_key.get(country_value) != None):
                                    country_key = topic_title_to_key[country_value]
                                    country_title = format_uri(country_value) 
                                    print("country found " + country_key)
                                    country_found = True
            
                                # country topic doesn't exist, create it
                                else:
                                    country_found = False
                                    country_key, topic_key_val = new_topic_key(topic_key_val)
                                    country_title = format_uri(country_results['yago_url']['value'])
                                    country_ref = country_results['yago_url']['value']
                                    country_def = ""
                                    if 'definition' in country_results:
                                        country_def = country_results['definition']['value']
                                    country_url = ""
                                    if 'url' in country_results:
                                        country_url = country_results['url']['value']
            
                                    topic_params = {
                                        '_key': country_key, 
                                        '_type': 'Country', 
                                        'title': country_title, 
                                        'reference': country_ref, 
                                        'definition': country_def, 
                                        'valueType': '', 
                                        'URL': country_url 
                                    }
                                    new_topics.append(create_topic(topic_params))
                                    topic_title_to_key[country_value] = country_key
                                    print("country created " + country_key)
            
                        # create city topic
                        city_key, topic_key_val = new_topic_key(topic_key_val)
                        city_title = format_uri(city_results['yago_url']['value'])
                        city_ref = city_results['yago_url']['value']
                        city_def = ""
                        if 'definition' in city_results:
                            city_def = city_results['definition']['value']
                        city_loc = ""
                        if 'location' in city_results:
                            city_loc = format_uri(city_results['location']['value'])
                        city_url = ""
                        if 'url' in city_data:
                            city_url = city_results['url']['value']
            
                        topic_params = {
                            '_key': city_key, 
                            '_type': 'City', 
                            'title': city_title, 
                            'reference': city_ref, 
                            'definition': city_def, 
                            'valueType': '', 
                            'location': city_loc, 
                            'country': country_title,
                            'URL': city_url 
                        }
                        new_topics.append(create_topic(topic_params))
                        topic_title_to_key[city_value] = city_key
                        print("city created " + city_key)
            
                        ## links
            
                        #city & city cluster
                        link_key, link_key_val = new_link_key(link_key_val)
                        link_params = {
                            '_key': link_key,
                            '_type': 'hasInstance', 
                            '_from': 'T3', 
                            '_to': city_key
                        }
                        new_links.append(create_link(link_params))
                        print(link_params)
            
                        if country_key != None:
            
                            #city & country
                            link_key, link_key_val = new_link_key(link_key_val)
                            link_params = {
                                '_key': link_key,
                                '_type': 'link',
                                'name': 'is located in',
                                '_from': city_key, 
                                '_to': country_key
                            }
                            new_links.append(create_link(link_params))
                            print(link_params)
            
                            #country & country cluster
                            if not country_found:
                                link_key, link_key_val = new_link_key(link_key_val)
                                link_params = {
                                    '_key': link_key,
                                    '_type': 'hasInstance', 
                                    '_from': 'T4', 
                                    '_to': country_key
                                }
                                new_links.append(create_link(link_params))
                                print(link_params)
            
                        # link city and member
                        link_key, link_key_val = new_link_key(link_key_val)
                        link_params = {
                            '_key': link_key,
                            '_type': 'link',
                            'name': 'is located in',
                            '_from': member_key, 
                            '_to': city_key
                        }
                        new_links.append(create_link(link_params))
                        print(link_params)
                        
                
            ### ORGANISATIONS/INSTITUTIONS
            org_values = []
            org_list = []
            school_list = []
            
            # list of org types to not create clusters for
            orgtype_delete_list = ['http://schema.org/Organization', 'http://schema.org/Place', 'http://schema.org/Thing']
            
            for value in user_data['user']['metadata']['Organisations']:
                org_values.append(value)
                org_title = format_uri(value)
                org_list.append(org_title) 
            
            for value in user_data['user']['metadata']['Institutions']:
                org_values.append(value)
                org_title = format_uri(value)
                school_list.append(org_title)
            
            print(org_values)
            
            for org_value in org_values:
                
                print("org: " + org_value)
            
                # check if org topic already exists from previous run
                past_run_check = next((item for item in topic_past_data if item["reference"] == org_value), None)
                if past_run_check != None and previous_run:
                    org_key = past_run_check["_key"]
                    org_title = past_run_check["title"]
                    print("org found " + org_key)
                    
                    # link org & member
                    link_key, link_key_val = new_link_key(link_key_val)
                    link_params = {
                        '_key': link_key,
                        '_type': 'link',
                        'name': 'is affiliated with',
                        '_from': member_key, 
                        '_to': org_key
                    }
                    new_links.append(create_link(link_params))
                    print(link_params)
            
                # check if org topic already exists from this run
                elif (topic_title_to_key.get(org_value) != None):
                    org_key = topic_title_to_key[org_value]
                    org_title = format_uri(org_value)                    
                    print("org found " + org_key)
                    
                    # link org & member
                    link_key, link_key_val = new_link_key(link_key_val)
                    link_params = {
                        '_key': link_key,
                        '_type': 'link',
                        'name': 'is affiliated with',
                        '_from': member_key, 
                        '_to': org_key
                    }
                    new_links.append(create_link(link_params))
                    print(link_params)
                    
                # org topic doesn't exist, create it and link
                else:
                    print("org not found")
            
                    # org yago api call
                    org_data = get_org_data(org_value)
                    
                    if org_data != None and org_data['results']['bindings'][0]['types']['value'] != '':
                        org_results = org_data['results']['bindings'][0]
            
                        # org type yago api call
                        orgtypes = org_results['types']['value'].split("; ")
                        orgtypes_titles = []
                        orgtypes_keys = []
                        for orgtype_value in orgtypes:
            
                            if orgtype_value not in orgtype_delete_list:
                                print("org type: " + orgtype_value)
                                past_run_check = next((item for item in topic_past_data if item["reference"] == orgtype_value), None)
            
                                if orgtype_value == 'http://schema.org/EducationalOrganization':
                                    orgtype_key = 'T10'
                                    orgtype_title = 'Educational Organization'
                                    print("org type found " + orgtype_key)
            
                                # check if orgtype topic already exists from previous run
                                elif past_run_check != None and previous_run:
                                    orgtype_key = past_run_check["_key"]
                                    orgtype_title = past_run_check["title"]
                                    print("org type found " + orgtype_key)
                                    org_type_found = True
            
                                # check if orgtype topic already exists from this run
                                elif topic_title_to_key.get(orgtype_value) != None:                            
                                    orgtype_key = topic_title_to_key[orgtype_value]
                                    orgtype_title = format_uri(orgtype_value)
                                    print("org type found " + orgtype_key)
                                    org_type_found = True
            
                                else:
                                    print("org type not found")
                                    org_type_found = False
                                    orgtype_key, topic_key_val = new_topic_key(topic_key_val)
                                    orgtype_data = get_basic_metadata(orgtype_value)
                                    orgtype_results = orgtype_data['results']['bindings'][0]
            
                                    # create org type topic
                                    orgtype_title = format_uri(orgtype_results['yago_url']['value'])
                                    orgtype_ref = orgtype_results['yago_url']['value']
                                    orgtype_def = ""
                                    if 'definition' in orgtype_results:
                                        orgtype_def = orgtype_results['definition']['value']
                                    orgtype_url = ""
                                    if 'url' in orgtype_results:
                                        orgtype_url = orgtype_results['url']['value']
            
                                    topic_params = {
                                        '_key': orgtype_key, 
                                        '_type': 'Organisation Type', 
                                        'title': orgtype_title, 
                                        'reference': orgtype_ref, 
                                        'definition': orgtype_def, 
                                        'valueType': '', 
                                        'URL': orgtype_url 
                                    }
                                    new_topics.append(create_topic(topic_params))
                                    topic_title_to_key[orgtype_value] = orgtype_key
                                    print("org type created " + orgtype_key)
            
                                orgtypes_keys.append(orgtype_key)
                                orgtypes_titles.append(orgtype_title)
            
                        # country api call
                        country_key = None
                        country_title = ""
            
                        if 'location' in org_results:
                            org_loc = org_data['results']['bindings'][0]['location']['value']
                            country_value = get_country_value(org_loc)
            
                            if country_value != None:
            
                                country_data = get_basic_metadata(country_value)
                                country_results = country_data['results']['bindings'][0]
            
                                # check if country topic already exists from previous run
                                past_run_check = next((item for item in topic_past_data if item["reference"] == country_value), None)
                                if past_run_check != None and previous_run:
                                    country_key = past_run_check["_key"]
                                    country_title = past_run_check["title"]
                                    print("country found " + country_key)
                                    country_found = True
            
                                # check if country topic already exists from this run
                                elif (topic_title_to_key.get(country_value) != None):
                                    country_key = topic_title_to_key[country_value]
                                    country_title = format_uri(country_value)
                                    print("country found " + country_key)
                                    country_found = True
            
                                else:
                                    print("country not found")
                                    country_found = False
                                    country_key, topic_key_val = new_topic_key(topic_key_val)
                                    country_title = format_uri(country_results['yago_url']['value'])
                                    country_ref = country_results['yago_url']['value']
                                    country_def = ""
                                    if 'definition' in country_results:
                                        country_def = country_results['definition']['value']
                                    country_url = ""
                                    if 'url' in country_results:
                                        country_url = country_results['url']['value']
            
                                    topic_params = {
                                        '_key': country_key, 
                                        '_type': 'Country', 
                                        'title': country_title, 
                                        'reference': country_ref, 
                                        'definition': country_def, 
                                        'valueType': '', 
                                        'URL': country_url 
                                    }
                                    new_topics.append(create_topic(topic_params))
                                    topic_title_to_key[country_value] = country_key
                                    print("country created " + country_key)
            
                        elif 'foundinglocation' in org_results:
                            org_loc = org_data['results']['bindings'][0]['foundinglocation']['value']
                            country_value = get_country_value(org_loc)
                            country_title = ""
            
                            if country_value != None:
            
                                country_data = get_basic_metadata(country_value)
                                country_results = country_data['results']['bindings'][0]
            
                                # check if country topic already exists from previous run
                                past_run_check = next((item for item in topic_past_data if item["reference"] == country_value), None)
                                if past_run_check != None and previous_run:
                                    country_key = past_run_check["_key"]
                                    country_title = past_run_check["title"]
                                    print("country found " + country_key)
                                    country_found = True
            
                                # check if country topic already exists from this run
                                elif (topic_title_to_key.get(country_value) != None):
                                    country_key = topic_title_to_key[country_value]
                                    country_title = format_uri(country_value) 
                                    print("country found " + country_key)
                                    country_found = True
            
                                else:
                                    print("country not found")
                                    country_found = False
                                    country_key, topic_key_val = new_topic_key(topic_key_val)
                                    country_title = format_uri(country_results['yago_url']['value'])
                                    country_ref = country_results['yago_url']['value']
                                    country_def = ""
                                    if 'definition' in country_results:
                                        country_def = country_results['definition']['value']
                                    country_url = ""
                                    if 'url' in country_results:
                                        country_url = country_results['url']['value']
            
                                    topic_params = {
                                        '_key': country_key, 
                                        '_type': 'Country', 
                                        'title': country_title, 
                                        'reference': country_ref, 
                                        'definition': country_def, 
                                        'valueType': '', 
                                        'URL': country_url 
                                    }
                                    new_topics.append(create_topic(topic_params))
                                    topic_title_to_key[country_value] = country_key
                                    print("country created " + country_key)
                        else:
                            print('no country')
            
                        # create org topic
                        org_key, topic_key_val = new_topic_key(topic_key_val)
                        org_title = format_uri(org_results['yago_url']['value'])
                        org_ref = org_results['yago_url']['value']
                        org_def = ""
                        if 'definition' in org_results:
                            org_def = org_results['definition']['value']
                        org_loc = ""
                        if 'location' in org_results:
                            org_loc = format_uri(org_results['location']['value'])
                        elif 'foundinglocation' in org_results:
                            org_loc = format_uri(org_results['foundinglocation']['value'])
                        org_url = ""
                        if 'url' in org_data:
                            org_url = org_results['url']['value']
            
                        topic_params = {
                            '_key': org_key, 
                            '_type': 'Organisation', 
                            'title': org_title, 
                            'reference': org_ref, 
                            'definition': org_def, 
                            'valueType': '',
                            'organisation type': orgtypes_titles,
                            'location': org_loc, 
                            'country': country_title,
                            'URL': org_url
                        }
                        new_topics.append(create_topic(topic_params))
                        topic_title_to_key[org_value] = org_key
                        print("org created " + org_key)
            
                        # links
            
                        #org type to org cluster, org to org type
                        for orgtype_key in orgtypes_keys:
            
                            #org type & org cluster
                            if orgtype_key == 'T10':
                                link_key, link_key_val = new_link_key(link_key_val)
                                link_params = {
                                    '_key': link_key,
                                    '_type': 'hasInstance', 
                                    '_from': orgtype_key, 
                                    '_to': org_key
                                }
                                new_links.append(create_link(link_params))
                                print(link_params)
            
                            else:    
                                if not org_type_found:
                                    link_key, link_key_val = new_link_key(link_key_val)
                                    link_params = {
                                        '_key': link_key,
                                        '_type': 'hasInstance', 
                                        '_from': 'T5', 
                                        '_to': orgtype_key
                                    }
                                    new_links.append(create_link(link_params))
                                    print(link_params)
            
                                #org & org type
                                link_key, link_key_val = new_link_key(link_key_val)
                                link_params = {
                                    '_key': link_key,
                                    '_type': 'hasInstance', 
                                    '_from': orgtype_key, 
                                    '_to': org_key
                                }
                                new_links.append(create_link(link_params))
                                print(link_params)
            
                        if country_key != None:
                            #org & country
                            link_key, link_key_val = new_link_key(link_key_val)
                            link_params = {
                                '_key': link_key,
                                '_type': 'link',
                                'name': 'is located in',
                                '_from': org_key, 
                                '_to': country_key
                            }
                            new_links.append(create_link(link_params))
                            print(link_params)
            
                            if not country_found:
                                #country & country cluster
                                link_key, link_key_val = new_link_key(link_key_val)
                                link_params = {
                                    '_key': link_key,
                                    '_type': 'hasInstance', 
                                    '_from': 'T4', 
                                    '_to': country_key
                                }
                                new_links.append(create_link(link_params))
                                print(link_params)
            
                        #org & member
                        link_key, link_key_val = new_link_key(link_key_val)
                        link_params = {
                            '_key': link_key,
                            '_type': 'link',
                            'name': 'is affiliated with',
                            '_from': member_key, 
                            '_to': org_key
                        }
                        new_links.append(create_link(link_params))
                        print(link_params)
            
            ### DISCIPLINES
            disc_list = []
            for value in user_data['user']['metadata']['Disciplines']:
                disc_title = format_uri(value)
                disc_list.append(disc_title)
            
            print(disc_list)
            
            for disc_value in user_data['user']['metadata']['Disciplines']:
            
                print("disc: " + disc_value)
            
                # check if occ topic already exists from previous run
                past_run_check = next((item for item in topic_past_data if item["reference"] == disc_value), None)
                if past_run_check != None and previous_run:
                    disc_key = past_run_check["_key"]
                    disc_title = past_run_check["title"]
                    print("disc found " + disc_key)
            
                    # link disc & member
                    link_key, link_key_val = new_link_key(link_key_val)
                    link_params = {
                        '_key': link_key,
                        '_type': 'link',
                        'name': 'studies',
                        '_from': member_key, 
                        '_to': disc_key
                    }
                    new_links.append(create_link(link_params))
                    print(link_params)
                    
                # check if disc topic already exists from this run
                elif (topic_title_to_key.get(disc_value) != None):
                    disc_key = topic_title_to_key[disc_value]
                    disc_title = format_uri(disc_value)
                    print("disc found " + disc_key)
                    
                    # link disc & member
                    link_key, link_key_val = new_link_key(link_key_val)
                    link_params = {
                        '_key': link_key,
                        '_type': 'link',
                        'name': 'studies',
                        '_from': member_key, 
                        '_to': disc_key
                    }
                    new_links.append(create_link(link_params))
                    print(link_params)
            
                # disc topic doesn't exist, create it and link
                else:
                    print("disc not found")
                    disc_key, topic_key_val = new_topic_key(topic_key_val)
            
                    # disc api call
                    disc_data = get_basic_metadata(disc_value)
                    
                    if disc_data != None:
                        disc_results = disc_data['results']['bindings'][0]
            
                        # create disc topic
                        disc_title = format_uri(disc_results['yago_url']['value'])
                        disc_ref = disc_results['yago_url']['value']
                        disc_def = ""
                        if 'definition' in disc_results:
                            disc_def = disc_results['definition']['value']
            
                        topic_params = {
                            '_key': disc_key, 
                            '_type': 'Discipline', 
                            'title': disc_title, 
                            'reference': disc_ref, 
                            'definition': disc_def, 
                            'valueType': '', 
                        }
                        new_topics.append(create_topic(topic_params))
                        topic_title_to_key[disc_value] = disc_key
                        print("disc created " + disc_key)
            
                        ## links
                        #disc & disc cluster
                        link_key, link_key_val = new_link_key(link_key_val)
                        link_params = {
                            '_key': link_key,
                            '_type': 'hasInstance', 
                            '_from': 'T6', 
                            '_to': disc_key
                        }
                        new_links.append(create_link(link_params))
                        print(link_params)
            
                        #disc & member
                        link_key, link_key_val = new_link_key(link_key_val)
                        link_params = {
                            '_key': link_key,
                            '_type': 'link',
                            'name': 'studies',
                            '_from': member_key, 
                            '_to': disc_key
                        }
                        new_links.append(create_link(link_params))
                        print(link_params)
            
            ### OCCUPATION
            occ_list = []
            for value in user_data['user']['metadata']['Occupations']:
                occ_title = format_uri(value)
                occ_list.append(occ_title)
            
            print(occ_list)
            
            for occ_value in user_data['user']['metadata']['Occupations']:
            
                print("occ: " + occ_value)    
            
                # check if occ topic already exists from previous run
                past_run_check = next((item for item in topic_past_data if item["reference"] == occ_value), None)
                if past_run_check != None and previous_run:
                    occ_key = past_run_check["_key"]
                    occ_title = past_run_check["title"]
                    print("occ found " + occ_key)
                    
                    # link occ & member
                    link_key, link_key_val = new_link_key(link_key_val)
                    link_params = {
                        '_key': link_key,
                        '_type': 'link',
                        'name': 'practices',
                        '_from': member_key, 
                        '_to': occ_key
                    }
                    new_links.append(create_link(link_params))
                    print(link_params)
            
                # check if occ topic already exists from this run
                elif (topic_title_to_key.get(occ_value) != None):
                    occ_key = topic_title_to_key[occ_value]
                    occ_title = format_uri(occ_value) 
                    print("occ found " + occ_key)
                    
                    # link occ & member
                    link_key, link_key_val = new_link_key(link_key_val)
                    link_params = {
                        '_key': link_key,
                        '_type': 'link',
                        'name': 'practices',
                        '_from': member_key, 
                        '_to': occ_key
                    }
                    new_links.append(create_link(link_params))
                    print(link_params)
            
                # occ topic doesn't exist, create it and link
                else:
                    print("occ not found")
                    occ_key, topic_key_val = new_topic_key(topic_key_val)
            
                    # occ api call
                    occ_data = get_basic_metadata(occ_value)
                    
                    if occ_data != None:
                        occ_results = occ_data['results']['bindings'][0]
            
                        # create occ topic
                        occ_title = format_uri(occ_results['yago_url']['value'])
                        occ_ref = occ_results['yago_url']['value']
                        occ_def = ""
                        if 'definition' in occ_results:
                            occ_def = occ_results['definition']['value']
            
                        topic_params = {
                            '_key': occ_key, 
                            '_type': 'Occupation', 
                            'title': occ_title, 
                            'reference': occ_ref, 
                            'definition': occ_def, 
                            'valueType': '', 
                        }
                        new_topics.append(create_topic(topic_params))
                        topic_title_to_key[occ_value] = occ_key
                        print("occ created " + occ_key)
            
                        ### links
            
                        #occ & occ cluster
                        link_key, link_key_val = new_link_key(link_key_val)
                        link_params = {
                            '_key': link_key,
                            '_type': 'hasInstance', 
                            '_from': 'T7', 
                            '_to': occ_key
                        }
                        new_links.append(create_link(link_params))
                        print(link_params)
            
                        #occ & member
                        link_key, link_key_val = new_link_key(link_key_val)
                        link_params = {
                            '_key': link_key,
                            '_type': 'link',
                            'name': 'practices',
                            '_from': member_key, 
                            '_to': occ_key
                        }
                        new_links.append(create_link(link_params))
                        print(link_params)
            
            ### SKILL
            skill_list = []
            for value in user_data['user']['metadata']['Skills']:
                skill_title = value
                skill_list.append(skill_title)
            
            print(skill_list)
            
            for skill_value in user_data['user']['metadata']['Skills']:
            
                print("skill: " + skill_value) 
            
                # check if skill topic already exists from previous run
                past_run_check = next((item for item in topic_past_data if item["title"] == skill_value), None)
                if past_run_check != None and previous_run:
                    skill_key = past_run_check["_key"]
                    skill_title = past_run_check["title"]
                    print("skill found " + skill_key)
            
                # check if skill topic already exists from this run
                elif (topic_title_to_key.get(skill_value) != None):
                    skill_key = topic_title_to_key[skill_value]
                    skill_title = format_uri(skill_value)
                    print("skill found " + skill_key)
            
                # skill topic doesn't exist, create it and link
                else:
                    print("skill not found")
                    skill_key, topic_key_val = new_topic_key(topic_key_val)
            
                    # create skill topic
                    skill_title = skill_value
                    skill_ref = ""
                    skill_def = ""
            
                    topic_params = {
                        '_key': skill_key, 
                        '_type': 'Skill', 
                        'title': skill_title, 
                        'reference': skill_ref, 
                        'definition': skill_def, 
                        'valueType': '', 
                    }
                    new_topics.append(create_topic(topic_params))
                    topic_title_to_key[skill_value] = skill_key
                    print("skill created " + skill_key)
            
                    ### links
            
                    #skill & skill cluster
                    link_key, link_key_val = new_link_key(link_key_val)
                    link_params = {
                        '_key': link_key,
                        '_type': 'hasInstance', 
                        '_from': 'T8', 
                        '_to': skill_key
                    }
                    new_links.append(create_link(link_params))
                    print(link_params)
            
                #skill & member
                link_key, link_key_val = new_link_key(link_key_val)
                link_params = {
                    '_key': link_key,
                    '_type': 'link',
                    'name': 'specializes in_02',
                    '_from': member_key, 
                    '_to': skill_key
                }
                new_links.append(create_link(link_params))
                print(link_params)
            
            ### COLLEAGUE
            coll_list = []
            for value in user_data['user']['metadata']['Colleagues']:
                coll_title = value
                coll_list.append(coll_title)
            
            print(coll_list)
            
            for coll_value in user_data['user']['metadata']['Colleagues']:
            
                print("coll: " + coll_value)
            
                # check if coll topic already exists from previous run
                past_run_check = next((item for item in topic_past_data if item["title"] == coll_value), None)
                if past_run_check != None and previous_run:
                    coll_key = past_run_check["_key"]
                    coll_title = past_run_check["title"]
                    print("coll found " + coll_key)
            
                # check if coll topic already exists from this run
                elif (topic_title_to_key.get(coll_value) != None):
                    coll_key = topic_title_to_key[coll_value]
                    coll_title = format_uri(coll_value)
                    print("coll found " + coll_key)
            
                # coll topic doesn't exist, create it and link
                else:
                    print("coll not found")
                    coll_key, topic_key_val = new_topic_key(topic_key_val)
            
                    # create coll topic
                    coll_title = coll_value
                    coll_ref = ""
                    coll_def = ""
            
                    topic_params = {
                        '_key': coll_key, 
                        '_type': 'Colleague', 
                        'title': coll_title, 
                        'reference': coll_ref, 
                        'definition': coll_def, 
                        'valueType': '', 
                    }
                    new_topics.append(create_topic(topic_params))
                    topic_title_to_key[coll_value] = coll_key
                    print("coll created " + coll_key)
            
                ### links
            
                #coll & member
                link_key, link_key_val = new_link_key(link_key_val)
                link_params = {
                    '_key': link_key,
                    '_type': 'link',
                    'name': 'knows',
                    '_from': member_key, 
                    '_to': coll_key
                }
                new_links.append(create_link(link_params))
                print(link_params)
            
            ### PROJECT
            proj_list = []
            for value in user_data['user']['metadata']['Projects']:
                proj_title = value["name"]
                proj_list.append(proj_title)  
            
            print(proj_list)
            
            for proj_value in user_data['user']['metadata']['Projects']:
                print(proj_value)
            
                # check if proj topic already exists from previous run
                past_run_check = next((item for item in topic_past_data if item["title"] == proj_value['name']), None)
                if past_run_check != None and previous_run:
                    proj_key = past_run_check["_key"]
                    proj_title = past_run_check["title"]
                    print("proj found " + proj_key)
            
                # check if proj topic already exists from this run
                elif (topic_title_to_key.get(proj_value['name']) != None):
                    proj_key = topic_title_to_key[proj_value['name']]
                    proj_title = format_uri(proj_value['name'])
                    print("proj found " + proj_key)
            
                # proj topic doesn't exist, create it and link
                else:
                    print("proj not found")
                    proj_key, topic_key_val = new_topic_key(topic_key_val)
            
                    # create occ topic
                    proj_title = proj_value['name']
                    proj_ref = ""
                    proj_def = proj_value["description"]
            
                    topic_params = {
                        '_key': proj_key, 
                        '_type': 'Project', 
                        'title': proj_title, 
                        'reference': proj_ref, 
                        'definition': proj_def, 
                        'valueType': '', 
                    }
                    new_topics.append(create_topic(topic_params))
                    topic_title_to_key[proj_value['name']] = proj_key
                    print("proj created " + proj_key)
            
                    ### links
            
                    #project & project cluster
                    link_key, link_key_val = new_link_key(link_key_val)
                    link_params = {
                        '_key': link_key,
                        '_type': 'hasInstance', 
                        '_from': 'T9', 
                        '_to': proj_key
                    }
                    new_links.append(create_link(link_params))
                    print(link_params)
            
                #project & member
                link_key, link_key_val = new_link_key(link_key_val)
                link_params = {
                    '_key': link_key,
                    '_type': 'link',
                    'name': 'works on',
                    '_from': member_key, 
                    '_to': proj_key
                }
                new_links.append(create_link(link_params))
                print(link_params)
            
            ### MEMBER
            username = user_data['user']['first_name'] + " " + user_data['user']['last_name']
            topic_params = {
                '_key': member_key, 
                '_type': 'Member', 
                'title': username, 
                'reference': '', 
                'definition': '', 
                'valueType': '', 
                'location': city_title, 
                'organisation': org_list, 
                'educational organisation': school_list,
                'occupation': occ_list,
                'discipline': disc_list,
                'skill': skill_list,
                'project': proj_list,
                'colleague': coll_list
            }
            new_topics.append(create_topic(topic_params))
            topic_title_to_key[username] = member_key
            print("member created: " + member_key)
            
            # link Member to Member cluster
            link_key, link_key_val = new_link_key(link_key_val)
            link_params = {
                '_key': link_key,
                '_type': 'hasInstance', 
                '_from': 'T2', 
                '_to': member_key
            }
            new_links.append(create_link(link_params))
            print(link_params)
            
        else:
            print("no new user data")
        
        ### format all topics and links
        topics_to_add, topics_to_delete = get_differences(new_topics, topic_filename, True)
        links_to_add, links_to_delete = get_differences(new_links, link_filename, False)
        topics_to_add_metadata, links_to_add_metadata = format_with_metadata(topics_to_add, links_to_add)
        
        ### output to files
        if previous_run == True:
            
            for topic in new_topics:
                topic_past_data.append(topic)
            save_topics = topic_past_data
            
            for link in new_links:
                link_past_data.append(link)
            save_links = link_past_data            
        
        else:
            save_topics = new_topics
            save_links = new_links
            
        for link in save_links:
            if (link.get('_id') != None):
                # Effectively checking if we added any new links
                link['_from'] = link['_from'][7:]
                link['_to'] = link['_to'][7:]
                link.pop('_id')
        for topic in save_topics:
            if (topic.get('_id') != None):
                topic.pop('_id')
        print("Outputting to files")
        output_to_file(save_topics, topic_filename)
        output_to_file(save_links, link_filename)
  
        ### add/delete requests
        
        if (self.base_url != '' and self.graph_name != ''):
            if self.base_url[-1] == '/':
                start_url = self.base_url + self.graph_name + '/'
            else:
                start_url = self.base_url +'/' + self.graph_name +'/'
        else:
            print("URL NOT SET IN ENVIRONMENT VAR")
            start_url = 'http://topics-api.staging.thebrane.com/the-brane-community-graph/'
    
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

base_url = 'http://topics-api.staging.thebrane.com/'
community_graph_instance = Community_Graph(base_url, 'the-brane-community-graph')
community_graph_instance.convert()
