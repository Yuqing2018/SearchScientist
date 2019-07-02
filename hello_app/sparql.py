#!/usr/bin/python
# -*- coding: utf-8 -*-
from SPARQLWrapper import SPARQLWrapper, JSON, XML, N3, RDF
import pandas as pd

pubname = "Machine"
pubtype = 'Film'

query_str1 = '''
SELECT COUNT(?pub) SAMPLE(?pub)
WHERE {
	?res rdf:type dbo:%s ;
	     dct:subject ?o .
	?pub dct:subject ?o .
	FILTER ( REGEX(?res, "%s") && (?pub != ?res) ) .
} 
GROUP BY ?pub
ORDER BY DESC(count(?pub))
LIMIT 15
''' % (pubtype, pubname)

query_str ='''
#Whose birthday is today?
SELECT ?entity ?entityLabel ?genderLabel ?entityImage ?birthPlaceLabel ?entityDescription (YEAR(?date) as ?year)
WHERE {
    BIND(MONTH(NOW()) AS ?nowMonth)
    BIND(DAY(NOW()) AS ?nowDay)
    ?entity wdt:P31 wd:Q5 .# all items that have instance-of with value human.
    ?entity wdt:P106/wdt:P279* wd:Q901 .
     OPTIONAL {?entity wdt:P18 ?entityImage .}   
     OPTIONAL {?entity wdt:P19 ?birthPlace . }
    OPTIONAL {?entity wdt:P21 ?gender .}
    ?entity wdt:P569 ?date .
    FILTER (MONTH(?date) = ?nowMonth && DAY(?date) = ?nowDay)
SERVICE wikibase:label { bd:serviceParam  wikibase:language "[AUTO_LANGUAGE],en". }   
}
'''
def GetScientists():
  sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
  sparql.setQuery(query_str)
  sparql.setReturnFormat(JSON)
  results = sparql.query().convert()
  rs = results['results']['bindings']
  return rs
  # print(type(rs))
  # print(type(rs[0]))
  # # results_df = pd.io.json.json_normalize(results['results']['bindings']) # 'entityImage.value','birthPlace.value',
  # df = rs[['entityLabel.value','genderLabel.value','entityImage.value','birthPlaceLabel.value', 'entityDescription.value','year.value']].head()
  # print(len(df))
  # return df
# GetScientists()
