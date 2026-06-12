# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 20:19:08 2023

@author: USER
"""

import csv

# Identify the columns for each table
dim_columns = {
    'gun': ['gun_id', 'gun_stolen', 'gun_type'],
    'participant': ['participant_id', 'participant_age_group', 'participant_gender', 'participant_status', 'participant_type'],
    'date': ['date_id', 'date', 'day', 'month', 'year', 'quarter', 'day_of_week'],
    'incident': ['incident_id'],
    'geography': ['geo_id', 'latitude', 'longitude', 'city', 'state', 'continent']
}

# Populate dimension tables with data from the input CSV row.
def populate_dimension_data(row, dimension_data, dimension_columns, dim_columns):
    for dim_key in dimension_columns:
        dim_set = dimension_data[dim_key]
        # Check if the key is present in the row
        if dim_columns[dim_key][0] in row:
            # Convert 'incident_id' to integer before adding to the set
            if dim_key == 'incident':
                dim_set.add(int(row[dim_columns[dim_key][0]]))
            else:
                # Access columns dynamically
                dim_set.add(tuple(row[column] for column in dim_columns[dim_key]))

#Write a dimension table to a CSV file.
def write_dimension_table(dim_name, dim_set, dim_columns):
    with open(f'{dim_name}_table.csv', 'w', newline='') as dim_csv:
        dim_writer = csv.writer(dim_csv)
        dim_writer.writerow(dim_columns[dim_name])  # Preserve column names
        if dim_name == 'incident':
            dim_writer.writerows([(item,) for item in dim_set])  # Convert each item to a tuple for 'incident'
        else:
            dim_writer.writerows(dim_set)

#Write a fact table to a CSV file
def write_fact_table(fact_table, fact_columns, fact_data):
    with open(fact_table, 'w', newline='') as fact_csv:
        fact_writer = csv.writer(fact_csv)
        fact_writer.writerow(fact_columns)  # Preserve column names
        fact_writer.writerows(fact_data)

def main():
    # Initialize sets for dimension tables
    dimension_data = {
        'gun': set(),
        'participant': set(),
        'date': set(),
        'incident': set(),  
        'geography': set(),
    }

    # Initialize the fact table
    custody = []

    with open('police_final_data.csv', 'r') as original_csv:
        csv_reader = csv.DictReader(original_csv)

        # Identify the columns for the fact table
        custody_columns = ['custody_id', 'date_id', 'participant_id', 'geo_id', 'crime_gravity', 'gun_id', 'incident_id']

        for row in csv_reader:
            # Populate the dimension sets
            populate_dimension_data(row, dimension_data, ['gun', 'participant', 'date', 'incident', 'geography'], dim_columns)

            # Populate the fact table
            fact_row = [row[column] for column in custody_columns]
            custody.append(fact_row)

    # Write dimension tables to separate CSV files
    for dim_name, dim_set in dimension_data.items():
        write_dimension_table(dim_name, dim_set, dim_columns)

    # Write the fact table to a CSV file
    write_fact_table('custody.csv', custody_columns, custody)

if __name__ == "__main__":
    main()



