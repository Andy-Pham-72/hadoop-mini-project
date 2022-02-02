#!/usr/bin/env python

# mapper1 will map out vin_number and tuple of (incident type, make, and year).

import sys

for line in sys.stdin:
    # Remove any spaces
    line = line.strip()
    # Split by ","
    data = line.split(',')
    # Print the combination of vin_number as key and value as incident type, make, and year
    print('%s\t(%s,%s,%s)'% (data[2],data[1],data[3],data[5]))
