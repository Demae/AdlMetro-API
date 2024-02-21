from flask import Flask, request, Response
import json

app = Flask(__name__)

# Load bus data from JSON file
with open('table.json', 'r') as json_file:
    bus_data = json.load(json_file)

@app.route('/vehicle', methods=['GET'])
def get_bus_info():
    bus_id = request.args.get('id')

    if bus_id in bus_data:
        response_data = {"bus_id": bus_id, "data": bus_data[bus_id]}
        json_response = json.dumps(response_data, indent=4, sort_keys=False)
        return Response(json_response, mimetype='application/json')
    else:
        return jsonify({"error": "Bus ID not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)