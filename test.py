import pandas as pd
import json

# Read the table into a DataFrame with header=None to indicate unnamed columns
df = pd.read_csv('table.csv', header=None)

# Define the custom field names
field_names = ['Bus No.', 'Rego No.', 'Chassis', 'VIN', 'Body', 'Body No.', 'Body Date', 'Seating', 'Livery', 'Depot']  # Adjust as needed

# Rename columns with custom field names
df.columns = field_names

# Set the first column as the index
df.set_index('Bus No.', inplace=True)  # Assuming the first column is the core item

# Convert the DataFrame to a dictionary
data_dict = df.to_dict(orient='index')

# Write the dictionary to a JSON file
with open('table.json', 'w') as json_file:
    json.dump(data_dict, json_file, indent=4)