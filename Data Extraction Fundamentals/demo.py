#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 15:04:20 2020

@author: khalef
"""


def f123():
    yield 1
    yield 2
    yield 3

for item in f123():
    print (item)
    print(item)