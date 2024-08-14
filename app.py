# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

from colorama import Fore, Back, Style, init

import os

response = None

app = Flask(__name__)
CORS(app)
                                                            
dictonary = "User/"

def Warn(message):
    print(Fore.YELLOW + f"[WARNING] {message}")
def Fatal(MSG):
    print(Fore.RED + Back.YELLOW + f"[FATAL ERROR] {MSG}")

@app.route('/process', methods=['POST'])
def process():
    # Global

    global response
    
    # Get JSON data from request
    data = request.json

    client_ip = request.remote_addr
    
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
            response = "Done"
    elif data["MSG"] == "Login":
        if os.path.exists(dictonary + data["Username"]):
            if data["Password"] == jsonify(open(dictonary + data["Username"] + ".json", "r").read()):
                print(data["Username"] + " login in sucsessfully!")
                response = "Done"
            else:
                print(data["Username"] + " got a failed login request!")
                response = "failed"
        else:
            Warn("User " + data["Username"] + " does not exist but got login request!")
    else:
        # Flags IP in file

        open(client_ip + ".txt", "w")
        Fatal(client_ip + " submited an illegal request!!! (FLAGED)")
    
    # Returns a small string response!
    return response

if __name__ == '__main__':
    app.run(debug=True)
