#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 16:22:21 2020

@author: khalef
"""





#!/usr/bin/env python
# -*- coding: utf-8 -*-
# So, the problem is that the gigantic file is actually not a valid XML, because
# it has several root elements, and XML declarations.
# It is, a matter of fact, a collection of a lot of concatenated XML documents.
# So, one solution would be to split the file into separate documents,
# so that you can process the resulting files as valid XML documents.

import xml.etree.ElementTree as ET
import time

PATENTS = "/home/khalef/Workspace/Data wrangling with Mongodb/Data in more Complex Format/patent.data"


def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()

def files():
    n = 0
    while True:
        n += 1
        yield open("data-{}".format(n),"w")


def split_file(filename):
    """
    Split the input file into separate files, each containing a single patent.
    As a hint - each patent declaration starts with the same line that was
    causing the error found in the previous exercises.
    
    The new files should be saved with filename in the following format:
    "{}-{}".format(filename, n) where n is a counter, starting from 0.
    """
    
    
#tree = ElementTree.ElementTree()
#root = ElementTree.Element("root")
#a = ElementTree.Element("a")
#a.text = "1"
#root.append(a)
#tree._setroot(root)
#tree.write("sample.xml" 

    
    find_counter  = 0
    check_counter = 0 
    tree_file = files()
    #outfile = next(tree_file)
   
    
    with open(filename,mode ="r") as file :
        
        for line in file :
          
            if line.startswith("<?xml"):
                outfile = next(tree_file)
            outfile.write(line)
                
                
                
           

                
                
             

def test():
    split_file(PATENTS)
    for n in range(4):
        try:
            fname = "{}-{}".format(PATENTS, n)
            f = open(fname, "r")
            if not f.readline().startswith("<?xml"):
                print ("You have not split the file {} in the correct boundary!".format(fname))
            f.close()
        except:
            print ("Could not find file {}. Check if the filename is correct!".format(fname))


test()
