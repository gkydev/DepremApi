from flask import Flask, request, jsonify
from resources import split_data
import os, sys, requests, time
from bs4 import BeautifulSoup as bs
# init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
#Ertq Grabber Function 
def get_lastErtq():
    try:
        source = requests.get("http://www.koeri.boun.edu.tr/scripts/lst0.asp")
        soup = bs(source.text,'html.parser')
        depremler = soup.find("pre")
        cleaned = depremler.text.strip("<pre>").strip("</pre>")
        splitted = cleaned.split("\n")
        final = splitted[7].replace("Ý","i")
        return final
    except Exception as e:
        print("Error: " + str(e))
        return False
@app.route("/deprem/api",methods=["GET"])
def return_ertq():
    Ertq = get_lastErtq()
    if Ertq == False:
        while Ertq == False:
            Ertq = get_lastErtq()
    data =  split_data(Ertq)
    return jsonify(data)     
# Run Server
if __name__ == '__main__':
    app.run(debug=True)