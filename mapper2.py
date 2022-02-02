#!/usr/bin/env python

import sys

for line in sys.stdin:
    # Remove any spaces
    line = line.strip()
    # Assign key value from output of reducer1.py into variables
    key, value = line.split("\t")
    print("%s\t%s"%(key, value))