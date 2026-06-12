# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 19:59:34 2023

@author: USER
"""

import csv
from geopy.distance import geodesic

#Load coordinate data from a CSV file and create a dictionary with integer parts of coordinates as keys
def load_coordinate_data(file_path):
    coordinate_dict = {}
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            latitude = int(float(row['lat']))  # Use the integer part of latitude
            longitude = int(float(row['lng']))  # Use the integer part of longitude
            city = row['city']
            state = row['state_name']
            coordinate_dict[(latitude, longitude)] = (city, state)
    return coordinate_dict                  # A dictionary with coordinate tuples as keys and corresponding city and state as values.

#Find the nearest city and state based on latitude and longitude.
def find_nearest_city_state(latitude, longitude, coordinate_dict):
    nearest_distance = float('inf')
    nearest_city, nearest_state = None, None

    for (lat, lon), (city, state) in coordinate_dict.items():
        distance = geodesic((latitude, longitude), (lat, lon)).kilometers
        if distance < nearest_distance:
            nearest_distance = distance
            nearest_city, nearest_state = city, state

    return nearest_city, nearest_state  

# Process each row in the input CSV file, enriching it with city, state, and continent information based on coordinates.
def process_and_add_location(input_file_path, output_file_path, coordinate_dict):
    output_data = []

    with open(input_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            latitude = int(float(row['latitude']))  # Use the integer part of latitude
            longitude = int(float(row['longitude']))  # Use the integer part of longitude
            city, state = coordinate_dict.get((latitude, longitude), (None, None))

            if city is None and state is None:
                # If no match is found with integer parts, find the nearest city and state
                city, state = find_nearest_city_state(latitude, longitude, coordinate_dict)

            row['city'] = city
            row['state'] = state
            row['continent'] = 'North America'  # Add the continent column
            output_data.append(row)

    fieldnames = reader.fieldnames + ['city', 'state', 'continent']
    with open(output_file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_data)

def main():
    # Load coordinate data
    coordinate_dict = load_coordinate_data('uscitystate.csv')

    # Process and add location information to the CSV
    process_and_add_location('police_crime_gravity.csv', 'police_data.csv', coordinate_dict)

    # Define the path to the CSV file
    csv_file_path = 'police_data.csv'

    # Open and read the CSV file
    with open(csv_file_path, 'r') as csv_file:
        for line in csv_file:
            # Print each line of the CSV file
            print(line, end='')

if __name__ == "__main__":
    main()
