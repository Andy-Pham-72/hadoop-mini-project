#!/usr/bin/env python

<<<<<<< HEAD
# mapper1 will map out vin_number and tuple of (incident type, make, and year).
=======
# Mapper Python Script - Will map out vin_number and tuple of ( ).
>>>>>>> 39de5cd20d0b594253e195f4af9ad4cf1887e88f

import sys

for line in sys.stdin:
    # Remove any spaces
    line = line.strip()
    # Split by ","
    data = line.split(',')
<<<<<<< HEAD
    # Print the combination of vin_number as key and value as incident type, make, and year
    print('%s\t(%s,%s,%s)'% (data[2],data[1],data[3],data[5]))
=======
    # Print/Map out values as combination of vin_number and tuple
    print(f"{data[2]}\t{(data[1], data[3], data[5])}")
>>>>>>> 39de5cd20d0b594253e195f4af9ad4cf1887e88f
