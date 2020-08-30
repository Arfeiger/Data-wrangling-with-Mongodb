#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 20:54:11 2020

@author: khalef
"""


from bs4 import BeautifulSoup
html_page = "/home/khalef/Workspace/Data wrangling with Mongodb/Data in more Complex Format/options.html"


def extract_carriers(page):
    data = []
    sel =""
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, "lxml")
    sel = soup.find(attrs ={"name":"CarrierList"})
    
    #print("sel type : ",type(sel))
    #print(sel.attrs)
    carr = sel.find_all("option")
    #print("carr type :",type(carr))
    
    for i in carr:
        if("All" in i["value"]):
           continue
        data.append(i["value"])
   

    return data


def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]
    airport = data["airport"]
    carrier = data["carrier"]

    r = s.post("https://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
               data = (("__EVENTTARGET", ""),
                       ("__EVENTARGUMENT", ""),
                       ("__VIEWSTATE", viewstate),
                       ("__VIEWSTATEGENERATOR",viewstategenerator),
                       ("__EVENTVALIDATION", eventvalidation),
                       ("CarrierList", carrier),
                       ("AirportList", airport),
                       ("Submit", "Submit")))

    return r.text


def test():
    data = extract_carriers(html_page)
    assert len(data) == 16
    assert "FL" in data
    assert "NK" in data

if __name__ == "__main__":
    