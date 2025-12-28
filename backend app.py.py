backend/app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/alert!', methods=['POST'])
def alert():
    data = request.json
    lattitude = data.get('lattitude')
    longitude = data.get('longitude')

    return jsonify({
        "Message": "Accident detected!",
        "location": f"https://maps.google.com/?q={lat},{lon}"
    })

if __name__ == "__main__":

    app.run(debug=True)
