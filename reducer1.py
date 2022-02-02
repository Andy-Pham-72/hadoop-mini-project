#!/usr/bin/env python

# reducer 1 is used to populate values and obtain value count

import sys

# Initialize master vehicle info dictionary
master_info = {}


# Create flush function to print out desired output
def flush():
    """
    Print out the make, year and accident_count as result from the "mapper1.py"
    """
    for key in master_info.keys():
        print('(%s,%s)\t%s'% (master_info[key]["make"], master_info[key]["year"], master_info[key]["accident_count"]))

for line in sys.stdin:
    # In the "mapper1.py" we print out vin_number as key and tuple of (incident type, make, and year) as value.
    # Remove any spaces
    line = line.strip()

    # Assign key value pair from the output of mapper1.py into variables
    vin_number, values = line.split('\t')
    # List comprehension to remove unnecessary characters and extract desired values.
    values_list = [val.replace("'", "").replace("(", "").replace(")", "").replace(" ", "") for val in values.split(",")]
    # Assign the values into separated variables
    incident_type = values_list[0]
    car_make      = values_list[1]
    car_year      = values_list[2]

    # Update vin_number into master_info when it changes
    if vin_number not in master_info:
        # Use master_info dictionary to keep track of accident_count for each make and year
        master_info[vin_number] = {"make": None, "year": None, "accident_count": 0}

    # Collect the vehicle make and year data from master_info where incident type == "I" to propagate
    if incident_type == "I":
        master_info[vin_number]["make"] = car_make
        master_info[vin_number]["year"] = car_year

    # Increment the count for each incident type equal A (accident records)
    if incident_type == "A":
        master_info[vin_number]["accident_count"] += 1

# Output reducer values
flush()