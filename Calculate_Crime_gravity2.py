# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 19:19:30 2023

@author: USER
"""

import csv
import json

#load json files
def load_json_dict(json_file_path):       
    with open(json_file_path, 'r') as file:
        return json.load(file)       
    
#Calculate the crime gravity based on the dictionaries and a CSV row.
def calculate_crime_gravity(row, dict_age_group, dict_status, dict_type):
    age_group = dict_age_group.get(row['participant_age_group'])
    status = dict_status.get(row['participant_status'])
    participant_type = dict_type.get(row['participant_type'])
    gravity = age_group * status * participant_type
    return gravity

# Process a CSV file, calculate crime gravity, and write the result to another CSV file.
def process_csv(input_csv_file, output_csv_file, dict_age_group, dict_status, dict_type):
    with open(input_csv_file, 'r') as input_file, open(output_csv_file, 'w', newline='') as output_file:
        csv_reader = csv.DictReader(input_file)
        fieldnames = csv_reader.fieldnames + ['crime_gravity']  # Add new column name
        csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for row in csv_reader:
            # Calculate the crime gravity
            gravity = calculate_crime_gravity(row, dict_age_group, dict_status, dict_type)
            row['crime_gravity'] = gravity
            csv_writer.writerow(row)

def main():
    # Load dictionaries from JSON files
    dict_age_group = load_json_dict('dict_partecipant_age.json')
    dict_status = load_json_dict('dict_partecipant_status.json')
    dict_type = load_json_dict('dict_partecipant_type.json')

    # Input and output CSV file paths
    input_csv_file = 'merged_data.csv'
    output_csv_file = 'police_crime_gravity.csv'

    # Process CSV file and calculate crime gravity
    process_csv(input_csv_file, output_csv_file, dict_age_group, dict_status, dict_type)

    # Define the path to the output file
    csv_file_path = 'police_crime_gravity.csv'

    # Open and read the file
    with open(csv_file_path, 'r') as csv_file:
        for line in csv_file:
            # Print each line 
            print(line, end='')

if __name__ == "__main__":
    main()
