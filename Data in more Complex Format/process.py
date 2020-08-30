#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 15:58:25 2020

@author: khalef
"""


from bs4 import BeautifulSoup
from zipfile import ZipFile
import os

datadir = "/home/khalef/Workspace/Data wrangling with Mongodb/Data in more Complex Format/Data Elements_files"


#def open_zip(datadir):
 #   with ZipFile('{0}.zip'.format(datadir), 'r') as myzip:
  #      myzip.extractall()


def process_all(datadir):
    files = os.listdir(datadir)
    return files


def process_file(f):
    """
    This function extracts data from the file given as the function argument in
    a list of dictionaries. This is example of the data structure you should
    return:

    data = [{"courier": "FL",
             "airport": "ATL",
             "year": 2012,
             "month": 12,
             "flights": {"domestic": 100,
                         "international": 100}
            },
            {"courier": "..."}
    ]


    Note - year, month, and the flight data should be integers.
    You should skip the rows that contain the TOTAL data for a year.
    """
    data = []
    info = {}
    info["courier"], info["airport"] = f[:6].split("-")
   
    # Note: create a new dictionary for each entry in the output data list.
    # If you use the info dictionary defined here each element in the list 
    # will be a reference to the same info dictionary.
    with open("{}/{}".format(datadir, f), "r") as html:

        soup = BeautifulSoup(html,"lxml")

    data_tr  = soup.find("table",attrs = {"class":"dataTDRight"}) 
    
    data_td  =  data_tr.find_all("tr")
    
 
    for i  in data_td :
        
        row = i.find_all("td")
        
        year     = row[0].string.strip()
        month    = row[1].string.strip()
        domestic = row[2].string.strip()
        international = row[3].string.strip()
                
        try:
            
           info["year"]  = int(str(year))
           info["month"] = int(str(month).replace(",", "")) 
           info["flights"] = {"domestic": int(str(domestic).replace(",", "")),"international":int(str(international).replace(",", ""))}
           data.append(info)
           
        except ValueError  as err :
            #print(" error: {0}".format(err))
            pass

    return data
    
def test():
    print("Running a simple test...")
    #open_zip(datadir)
    files = process_all(datadir)
    print(files)
    data = []
    # Test will loop over three data files.
    for f in files:
        data += process_file(f)
        
    #assert len(data) == 399  # Total number of rows
    
    #print("data : ")
    #print(data[-1]["flights"])
    
    for entry in data[:3]:
        assert type(entry["year"]) == int
        assert type(entry["month"]) == int
        assert type(entry["flights"]["domestic"]) == int
        assert len(entry["airport"]) == 3
        assert len(entry["courier"]) == 2
    assert data[0]["courier"] == 'FL'
    assert data[0]["month"] == 12
    assert data[-1]["airport"] == "ATL"
    assert data[-1]["flights"] == {'international': 108289, 'domestic': 701425}
    
    print ("... success!")

if __name__ == "__main__":
    test()