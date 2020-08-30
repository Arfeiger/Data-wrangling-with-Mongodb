#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 16:21:43 2020

@author: khalef
"""

'''
Find the time and value of max load for each of the regions
COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
and write the result out in a csv file, using pipe character | as the delimiter.

An example output can be seen in the "example.csv" file.
'''

import xlrd
import os
import csv
from zipfile import ZipFile

datafile = "/home/khalef/Workspace/Data wrangling with Mongodb/Data Extraction Fundamentals/2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"


#def open_zip(datafile):
#   with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
#      myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = []
    
    region_name = ""
    max_value = 0
    time = 0
    load_time = 0
    
    # Iterate through the rows and columns
    for i in range(1,sheet.ncols - 1):
        region_name = sheet.cell_value(0,i)
        for j in range(1,sheet.nrows):
            if max_value <sheet.cell_value(j,i):
                max_value = sheet.cell_value(j,i)
                time = sheet.cell_value(j,0)
         
        # Convert excel date to python tuple
        load_time = xlrd.xldate_as_tuple(time,0)
        load_time = list(load_time)
        
        
        # Save into an array
        load_time.insert(0,region_name)
        load_time.append(max_value)
        data.append(load_time)
        max_value = 0
        
    return data

def save_file(data, filename):

    with open(outfile,"w",newline="") as file :
        writer =csv.writer(file,delimiter ="|")
        writer.writerow(["Station","Year","Month","Day",'Hour','Max Load'])
        writer.writerows(data)

    
def test():
    #open_zip(datafile)
    data = parse_file(datafile)
    
    save_file(data, outfile)

    number_of_rows = 0
    stations = []

    ans = {'FAR_WEST': {'Max Load': '2281.2722140000024',
                        'Year': '2013',
                        'Month': '6',
                        'Day': '26',
                        'Hour': '17'}}
    correct_stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH',
                        'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
    fields = ['Year', 'Month', 'Day', 'Hour', 'Max Load']

    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            station = line['Station']
            if station == 'FAR_WEST':
                for field in fields:
                    # Check if 'Max Load' is within .1 of answer
                    if field == 'Max Load':
                        max_answer = round(float(ans[station][field]), 1)
                        max_line = round(float(line[field]), 1)
                        #assert max_answer == max_line

                    # Otherwise check for equality
                    else:
                        assert ans[station][field] == line[field]

            number_of_rows += 1
            stations.append(station)

        # Output should be 8 lines not including header
        assert number_of_rows == 8

        # Check Station Names
        assert set(stations) == set(correct_stations)

        
if __name__ == "__main__":
    test()
