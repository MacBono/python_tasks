#!/usr/bin/python3
#           "Directory's structure"
import os
def listing(cat):
    print(cat)
    elements = os.listdir(cat)
    for element in elements:
        full_path = os.path.join(cat, element)
        if os.path.isdir(full_path):
            listing(full_path)
        else:
            print(full_path)

path = './'
listing(path)
