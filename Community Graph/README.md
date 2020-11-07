## COMMUNITY GRAPH SCRIPT

A python script that creates a graph using information about members of the brane community.<br /> 
The script is triggered whenever a new user completes the onboarding form. This data is saved to the users api.<br /> 
Relevant data is extracted from YAGO using their SPARQL API and transformed to the brane format.<br />
These topics and links are then sent to the community graph, adding the new user's information.<br />


### CODE OVERVIEW

* Import new user data from users api.
* If first time running, create root node and first layer. If not, set the latest topic and link number as the starting point.
* Set user key.
* LOCATION:<br />
    * Create city topic (if it doesn't exist).
    * Create country topic (if it doesn't exist).
    * Link city, country, and user.<br />
* ORGANISATIONS:<br />
    * Create organisation topic (if it doesn't exist).
    * Create organisation type(s) topic (if it doesn't exist).
    * Create country topic (if it doesn't exist).
    * Link organisation, organisation type, country and user.<br />
* DISCIPLINE/OCCUPATION/SKILL/COLLEAGUE/PROJECT:<br />
    * Create topic (if it doesn't exist).
    * Link object and user.<br />
* Create user topic.
* Format topics and links, output json files, push data to community graph using topics api.


### NEXT STEPS

* Add skills database (e.g. DBpedia)
* Link Project and Project Keyword
* How to handle colleagues who aren't members of the brane community
* Further modularize and simplify code
