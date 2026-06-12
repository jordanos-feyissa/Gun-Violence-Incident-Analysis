# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 10:59:24 2023

@author: USER
"""

#POPULATE DATABASE

import csv
import pyodbc 

#connect to the data source 
server = 'servernmae' 
database = 'Group_ID_13_DB'
username = 'Group_ID_13' 
password = 'PASS'
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
cnxn = pyodbc.connect(connectionString)
cursor = cnxn.cursor()


# CSV file paths
csv_files = {
    "date": "date_table.csv",
    "participant": "participant_table.csv",
    "gun": "gun_table.csv",
    "incident": "incident_table.csv",
    "geography": "geography_table.csv",
    "custody": "custody.csv"
}


# Loop through the csv files
for table_name, file_path in csv_files.items():
    with open(file_path, "r") as csv_file:
        csv_lines = csv.reader(csv_file, delimiter=",")

        is_header = True
        sql = None
        data = []

        for row in csv_lines:
            if is_header:
                # Create SQL query based on the header
                columns = ", ".join(row)
                placeholders = ", ".join(["?" for _ in row])
                sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                is_header = False
            else:
                data.append(row)

        if data:
            # Execute SQL query for the batch of rows
            cursor.executemany(sql, data)
            cnxn.commit()

print("Data upload completed.")

# Close the database connection
cursor.close()
cnxn.close()
