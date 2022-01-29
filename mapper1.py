#!/usr/bin/env python3

# Mapper Python Script - Will map out vin_number and tuple of ( ).

import sys

for line in sys.stdin:
    line = line.strip()
    data = line.split(',')
    # Print/Map out values as combination of vin_number and tuple
    print(f"{data[2]}\t{(data[1], data[3], data[5])}")
