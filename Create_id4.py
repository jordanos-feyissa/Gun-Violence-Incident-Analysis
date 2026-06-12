# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 20:12:17 2023

@author: USER
"""

import csv

#Load data from the input CSV file.
def load_data(input_file):
    with open(input_file, 'r') as input_csv:
        reader = csv.DictReader(input_csv)
        return list(reader)
    
#Generate  the participant ID based on participant attributes.
def generate_participant_id(participant_id_map, row):
    participant_age_group = row['participant_age_group']
    participant_gender = row['participant_gender']
    participant_status = row['participant_status']
    participant_type = row['participant_type']

    participant_key = (
        participant_age_group,
        participant_gender,
        participant_status,
        participant_type
    )

    if participant_key in participant_id_map:
        return participant_id_map[participant_key]
    else:
        participant_id = f'P{len(participant_id_map) + 1}'
        participant_id_map[participant_key] = participant_id
        return participant_id

#Generate the geo ID based on latitude and longitude.
def generate_geo_id(generated_geo_ids, row):
    latitude = row['latitude']
    longitude = row['longitude']
    geo_key = (latitude, longitude)

    if geo_key in generated_geo_ids:
        return generated_geo_ids[geo_key]
    else:
        geo_id = 'US' + str(len(generated_geo_ids) + 1)
        generated_geo_ids[geo_key] = geo_id
        return geo_id
    
#Generate or retrieve the gun ID based on gun attributes.
def generate_gun_id(generated_gun_ids, row):
    gun_stolen = row['gun_stolen']
    gun_type = row['gun_type']
    gun_key = (gun_stolen, gun_type)

    if gun_key in generated_gun_ids:
        return generated_gun_ids[gun_key]
    else:
        gun_id = 'G' + str(len(generated_gun_ids) + 1)
        generated_gun_ids[gun_key] = gun_id
        return gun_id

#Add new columns ('participant_id', 'geo_id', 'gun_id') to the data.
def add_new_columns(data, participant_id_map, generated_geo_ids, generated_gun_ids):
    new_data = []

    for row in data:
        participant_id = generate_participant_id(participant_id_map, row)
        geo_id = generate_geo_id(generated_geo_ids, row)
        gun_id = generate_gun_id(generated_gun_ids, row)

        new_row = dict(row)
        new_row.update({
            'participant_id': participant_id,
            'geo_id': geo_id,
            'gun_id': gun_id
        })

        new_data.append(new_row)

    return new_data

#Write the data with new columns to the output CSV file.
def write_data(output_file, data):
    with open(output_file, 'w', newline='') as output_csv:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def main():
    # Define the input and output file names
    input_file = 'police_data.csv'
    output_file = 'police_final_data.csv'

    # Load data from the input CSV file
    data = load_data(input_file)

    # Create dictionaries to store generated IDs
    participant_id_map = {}
    generated_geo_ids = {}
    generated_gun_ids = {}

    # Add new columns to the data
    new_data = add_new_columns(data, participant_id_map, generated_geo_ids, generated_gun_ids)

    # Write the data with new columns to the output CSV file
    write_data(output_file, new_data)

    # Define the path to the CSV file
    csv_file_path = 'police_final_data.csv'

    # Open and read the CSV file
    with open(csv_file_path, 'r') as csv_file:
        for line in csv_file:
            # Print each line of the CSV file
            print(line, end='')

if __name__ == "__main__":
    main()
