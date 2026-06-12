# -*- coding: utf-8 -*-

"""
Created on Sat Nov  4 14:46:50 2023

@author: USER

"""
import csv

#convert XML to CSV
def convert_xml_to_csv(xml_file_path, csv_file_path):
    import xml.etree.ElementTree as ET
    import datetime

    # Parse XML data
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Create CSV file and write header
    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['date_id', 'date', 'day', 'month', 'year', 'quarter', 'day_of_week'])

        # Iterate through XML data and write to CSV
        for row in root.findall('row'):
            date_id = row.find('date_pk').text
            full_date_time = row.find('date').text
            date_parts = full_date_time.split()[0] # Extract only the date part from the full date-time value
            year, month, day = date_parts.split('-')
            date_element = datetime.datetime(int(year), int(month), int(day))
            quarter = "Q"+ str(((date_element.month - 1) // 3) + 1) #Calculate the quarter of the year based on the month
            day_of_week = date_element.strftime('%A')    #Get the day of the week in string format
            csv_writer.writerow([date_id, full_date_time, day, month, year, quarter, day_of_week])

# merge CSV files and remove date_fk column
def merge_and_remove_column(primary_csv, secondary_csv, merge_key_primary, merge_key_secondary, output_csv):
    with open(primary_csv, 'r') as first_file:
        first_reader = csv.DictReader(first_file)
        first_data = list(first_reader)

    with open(secondary_csv, 'r') as second_file:
        second_reader = csv.DictReader(second_file)
        second_data = list(second_reader)

    # Create dictionary for second CSV based on merge key(date_fk)
    second_data_dict = {row[merge_key_secondary]: row for row in second_data}

    merged_data = []

    # Merge data from second CSV into first CSV based on merge key(date_fk)
    for row in first_data:
        merge_value = row[merge_key_primary]
        if merge_value in second_data_dict:
            second_row = second_data_dict[merge_value]
            row.update(second_row)

        # Remove date_fk from the merged data
        if merge_key_primary in row:
            del row[merge_key_primary]

        merged_data.append(row)

    # Write merged data to new CSV
    fieldnames = merged_data[0].keys()
    with open(output_csv, 'w', newline='') as merged_file:
        writer = csv.DictWriter(merged_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(merged_data)

# Convert XML to CSV
convert_xml_to_csv('dates.xml', 'date.csv')

# Merge and remove date_fk column
merge_and_remove_column('Police.csv', 'date.csv', 'date_fk', 'date_id', 'merged_data.csv')
