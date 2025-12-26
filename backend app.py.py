backend/app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def alert():
    data = request.json
    lat = data.get('lat')
    lon = data.get('lon')

    return jsonify({
        "message": "Accident detected!",
        "location": f"https://maps.google.com/?q={lat},{lon}"
    })

if __name__ == "__main__":
    app.run(debug=True)