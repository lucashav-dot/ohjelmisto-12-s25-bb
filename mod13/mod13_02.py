from flask import Flask, jsonify

app = Flask(__name__)

AIRPORT_DATABASE = {
    "EFHK": {
        "Name": "Helsinki Vantaa Airport",
        "Municipality": "Helsinki"
    },
    "EFPO": {
        "Name": "Pori Airport",
        "Municipality": "Pori"
    },
    "EFPR": {
        "Name": "Pärnu Airport",
        "Municipality": "Pärnu"
    },
    "EFKT": {
        "Name": "Kitee Airport",
        "Municipality": "Kitee"
    }
}

@app.route('/kenttä/<icao_code>', methods=['GET'])
def get_airport_info(icao_code):
    icao_code_upper = icao_code.upper()
    airport_info = AIRPORT_DATABASE.get(icao_code_upper)

    if airport_info:
        response_data = {
            "ICAO": icao_code_upper,
            "Name": airport_info["Name"],
            "Municipality": airport_info["Municipality"]
        }
        return jsonify(response_data)
    else:
        return jsonify({"Error": f"Airport with ICAO code '{icao_code_upper}' not found"}), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)