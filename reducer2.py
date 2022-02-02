#!/usr/bin/env python


import sys

# Initialize accident count dictionary to keep track
accident_count_info = {}


# Flush out reducer key and values with function
def flush():
    """
    Print out the combination of make and year as key and count as value.
    """
    for key in accident_count_info.keys():
        print("%s\t%s"%(key,accident_count_info[key]))

for line in sys.stdin:
    line = line.strip()
    make_year, accident_count = line.split('\t')
    # Remove unnecessary characters.
    accident_count = int(accident_count.replace("'", "").replace("(", "").replace(")", ""))
    # If key from mapper2.py is not present in the dictionary, create a new entry.
    if make_year not in accident_count_info:
        accident_count_info[make_year] = 0
    accident_count_info[make_year] += accident_count

flush()