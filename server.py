# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

import os

app = Flask(__name__)
CORS(app)
                                                            
dictonary = "User/"

@app.route('/process', methods=['POST'])
def process():
    # Get JSON data from request
    data = request.json
    
    if data["MSG"] == "Register":
        PLRDATA = {
            "Username" : data["Username"],
            "Password" : data["Password"],
            "Coin" : 15,
            "Admin" : True
        }

        if os.path.exists(dictonary + data["Username"]):
            response = "AE"
        else:
            open(dictonary + data["Username"] + ".json", "w").write(str(PLRDATA))
    # Return a JSON response
    return response

if __name__ == '__main__':
    app.run(debug=True)
