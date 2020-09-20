#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 15:11:48 2020

@author: khalef
"""



from bs4 import BeautifulSoup
html_page = "/home/khalef/Workspace/Data wrangling with Mongodb/Data in more Complex Format/options.html"


def extract_airports(page):
    data = []
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, "lxml")
        
    sele = soup.find(attrs ={"id":"AirportList"})
    
    options = sele.find_all("option")
       
    for air in options :
       if("All" in air["value"]):
           continue
       data.append(air["value"])
       
    return data


def test():
    data = extract_airports(html_page)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

if __name__ == "__main__":
    test()