#!/usr/bin/python3
import requests as req
import json
from os import system
def spiderIndia():
	urls = 'https://api.rootnet.in/covid19-in/stats/latest'
	response = req.get(urls)
	data = json.loads(response.text)
	    
	with open ('GenderWise_StateWise.json','w')	as outfile:
		json.dump(data,outfile,indent=4)


def spiderworld():
     urls = 'https://corona-api.com/countries'
     response = req.get(urls)
	 data = json.loads(response.text)

	 with open ('DistrictCases.json','w') as outfile:
	 	json.dump(data,outfile,indent=4)
