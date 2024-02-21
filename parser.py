import pandas as pd
import json

field_names = ['id', 'registration', 'chassis', 'vin', 'body', 'body_no', 'body_date', 'seating', 'livery', 'depot']

file_operator_mapping = {
    'csv/torrens.csv': 'Torrens Transit',
    'csv/southlink.csv': 'SouthLink',
    'csv/busways.csv': 'Busways'
}

combined_json_file = 'table.json'

for file_name, operator in file_operator_mapping.items():
    try:
        with open(combined_json_file, 'r') as json_file:
            compiled_data = json.load(json_file)
    except FileNotFoundError:
        compiled_data = {}

    df = pd.read_csv(file_name, header=None)
    df.columns = field_names
    df.set_index('id', inplace=True)
    df['operator'] = operator
    data_dict = df.to_dict(orient='index')
    compiled_data.update(data_dict)

    with open(combined_json_file, 'w') as json_file:
        json.dump(compiled_data, json_file, indent=4)

## for individual files
##    json_file_name = file_name.split('.')[0] + '.json'
##    with open(json_file_name, 'w') as json_file:
##        json.dump(data_dict, json_file, indent=4)