#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 16:24:43 2020

@author: khalef
"""

import csv
import os

DATADIR = ""
DATAFILE = "/home/khalef/Workspace/Data wrangling with Mongodb/Data Extraction Fundamentals/nrel.csv"


def parse_file(datafile):
    header = ""
    name   = ""
    data   = []
    with open(datafile,'r') as f:
      
        #name = header[1].strip()
        #print(name)
        file_reader = csv.reader(f, delimiter=",", quotechar='"')
        header = next(file_reader) 
        name   = header[1]
        next(file_reader)
        for line in file_reader:
            data.append(line)
    # Do not change the line below
    return (name ,data)
    
  


def test():
    datafile = os.path.join(DATADIR, DATAFILE)
    name,data = parse_file(datafile)
 
    assert str(name) == "MOUNTAIN VIEW MOFFETT FLD NAS"
    assert data[0][1] == "01:00"
    assert data[2][0] == "01/01/2005"
    assert data[2][5] == "2"


if __name__ == "__main__":
    test()
    