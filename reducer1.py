#!/usr/bin/env python3

# Reducer 1 - Python script used to populate values and obtain value count

import sys

# Initialize master vehicle_info dictionary
master_info = {}


# Create flush function to print out desired output
def flush():
    """
    Observe each key inside our master_info dictionary we created.
    We will print the make, year and accident_count as result.
    :return: Prints make, year and accident_count to be read with second mapper Python script.
    """
    for key in master_info.keys():
        print(f'{(master_info[key]["make"], master_info[key]["year"])}\t{master_info[key]["accident_count"]}')

# Debug - Ignore
# count = 0
# for line in sys.stdin:
#     line = line.strip()
#     print(line)
#     count += 1
#     if count == 3:
#         break


for line in sys.stdin:
    # Recall that each line has four values.
    # I may need to edit code so that I instead have other three values vs. a values_arr.
    line = line.strip()
    # print(line)
    vin_number, values = line.split('\t')
    # List comprehension to remove unnecessary characters and extract desired values.
    values_list = [val.replace("'", "").replace("(", "").replace(")", "").replace(" ", "") for val in values.split(",")]

    incident_type = values_list[0]
    vehicle_make = values_list[1]
    vehicle_year = values_list[2]

    # Check for whether vin_number is present in dictionary
    if vin_number not in master_info:
        # Use master_info dictionary to keep track of accident_count for each make and year
        master_info[vin_number] = {"make": None, "year": None, "accident_count": 0}

    # Collect the vehicle make and year data from master_info where incident type == "I" to propagate
    if incident_type == "I":
        master_info[vin_number]["make"] = vehicle_make
        master_info[vin_number]["year"] = vehicle_year

    # Increment the count for each incident type == A (accident records)
    if incident_type == "A":
        master_info[vin_number]["accident_count"] += 1

# Output reducer values
flush()