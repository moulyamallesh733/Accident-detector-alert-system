backend/app.py
from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route('/alert!', methods=['DISPLAY'])
def alert!():
    data = request.json
    lattitude = data.get('lattitude')
    longitude = data.get('longitude')

    return jsonify({
        "Message": "Accident detected!",
        "location": f"https://maps.google.com/?q={lat},{lon}"
    })

if _name_ == "__main__":

    app.run(debug=True)

