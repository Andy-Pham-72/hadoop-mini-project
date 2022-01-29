#!/usr/bin/env python3


import sys

# Initialize accident count dictionary to keep track
acc_count_info = {}


# Flush out reducer key and values with function
def flush():
    """
    Output of function is to return combination of make and year as key and count as value.
    :return:
    """
    for key in acc_count_info.keys():
        print(f'{key}\t{acc_count_info[key]}')


for line in sys.stdin:
    line = line.strip()
    make_year, acc_count = line.split('\t')
    # Remove unnecessary characters.
    acc_count = int(acc_count.replace("'", "").replace("(", "").replace(")", ""))
    # If key from mapper2.py is not present in the dictionary, create a new entry.
    if make_year not in acc_count_info:
        acc_count_info[make_year] = 0
    acc_count_info[make_year] += acc_count

flush()