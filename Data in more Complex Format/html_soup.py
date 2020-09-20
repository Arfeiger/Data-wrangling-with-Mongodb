#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 16:57:35 2020

@author: khalef
"""


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Please note that the function 'make_request' is provided for your reference only.
# You will not be able to to actually use it from within the Udacity web UI.
# Your task is to process the HTML using BeautifulSoup, extract the hidden
# form field values for "__EVENTVALIDATION" and "__VIEWSTATE" and set the appropriate
# values in the data dictionary.
# All your changes should be in the 'extract_data' function
from bs4 import BeautifulSoup
import requests
import json

html_page = "/home/khalef/Workspace/Data wrangling with Mongodb/Data in more Complex Format/Data_elements.html"


def extract_data(page):
    data = {"eventvalidation": "","viewstate": ""}
    soup = 0
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html,"html.parser")
    data["viewstate"]       = soup.find(attrs={"id":"__VIEWSTATE"})["value"]
    data["eventvalidation"] = soup.find(attrs={"id":"__EVENTVALIDATION"})["value"]
    
    
   
    
    return data


def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]

    r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                    data={'AirportList': "BOS",
                          'CarrierList': "VX",
                          'Submit': 'Submit',
                          "__EVENTTARGET": "",
                          "__EVENTARGUMENT": "",
                          "__EVENTVALIDATION": eventvalidation,
                          "__VIEWSTATE": viewstate
                    })

    return r.text


def test():
    data = extract_data(html_page)
    assert data["eventvalidation"] != ""
    assert data["eventvalidation"].startswith("/wEWjAkCoIj1ng0")
    assert data["viewstate"].startswith("/wEPDwUKLTI")
    text = make_request(data)
    
    print(type(text))
    
test()