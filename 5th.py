#!/usr/bin/python
# -*- coding: utf8 -*-

'''
Νίκος Κοντόπουλος Π15056 ΣΕΠΤΕΜΒΡΙΟΣ 2016
Άσκηση 5
Γράψτε ένα πρόγραμμα το οποίο χρησιμοποιεί το API του
BreweryDB (http://www.brewerydb.com/developers).
Εμφανίστε στο χρήστη τις μπύρες που είναι καταχωρημές στη βάση
για το είδος μπύρας που ζήτησε ο χρήστης, εμφανίζοντας μόνο τα απαραίτητα πεδία κειμένου.
BreweryDb.search({'type':'beer','q':'unibroue'}
'''

import requests
from brewerydb import *
import brewerydb

DEFAULT_BASE_URI = "http://api.brewerydb.com/v2"
BASE_URI = DEFAULT_BASE_URI
API_KEY = "47f25f72907f1924061a1ee9b57d6f10"

simple_endpoints = ["beers", "breweries", "categories", "events",
                    "featured", "features", "fluidsizes", "glassware",
                    "locations", "guilds", "heartbeat", "ingredients",
                    "search", "search/upc", "socialsites", "styles"]

single_param_endpoints = ["beer", "brewery", "category", "event",
                          "feature", "glass", "guild", "ingredient",
                          "location", "socialsite", "style", "menu"]


#print simple_endpoints
#print single_param_endpoints



class BreweryDb:


    @staticmethod
    def __make_simple_endpoint_fun(name):
        @staticmethod
        def _function(options={"categories"}):
            return BreweryDb._get("/" + name, options)
        return _function

    @staticmethod
    def __make_singlearg_endpoint_fun(name):
        @staticmethod
        def _function(id, options={}):
            return BreweryDb._get("/" + name + "/" + id, options)
        return _function

    @staticmethod
    def _get(request, options):
        options.update({"key" : BreweryDb.API_KEY})
        
        return requests.get(BreweryDb.BASE_URI + request, params=options).json()

    @staticmethod
    def configure(apikey=API_KEY, baseuri=DEFAULT_BASE_URI):
        BreweryDb.API_KEY = apikey
        BreweryDb.BASE_URI = baseuri
        for endpoint in simple_endpoints:
            fun = BreweryDb.__make_simple_endpoint_fun(endpoint)
            setattr(BreweryDb, endpoint.replace('/', '_'), fun)
        for endpoint in single_param_endpoints:
            fun = BreweryDb.__make_singlearg_endpoint_fun(endpoint)
            setattr(BreweryDb, endpoint.replace('/', '_'), fun)
    
    endpoint = "categories"
    def get(request, endpoint):
           endpoint.update({"key" : BreweryDb.API_KEY})
           return request.get(BreweryDb.BASE_URI + request, params=endpoint).json()
print requests.get
