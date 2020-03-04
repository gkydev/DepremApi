from flask import Flask, request, jsonify
from resources import split_data
import os
# init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Functions
def is_inlist(request):
    result = False
    with open("sublist.txt","r") as fp:
        lines = fp.readlines()
        fp.close()
    for line in lines:
        if request.json['mail'] == line.strip("\n"):
            result = True
        else:
            pass
    return result
# Add sub 
@app.route("/depremsublist/add",methods=["POST"])
def add_user():
    status = is_inlist(request)
    if status == True:
        return "Mail already in list"
    else:
        with open("sublist.txt","a") as fp:
            fp.write(request.json['mail'])
            fp.write("\n")
            fp.close()
        return "Succesfully added"
# Delete sub 
@app.route("/depremsublist/delete",methods=["POST"])
def delete_user():
    with open("sublist.txt","r") as fp:
        lines = fp.readlines()
        fp.close()
    with open("toreplace.txt","w") as fp:
        for line in lines:
            if line.strip("\n") != request.json['mail']:
                fp.write(line + "\n")
            else:
                pass
        fp.close()
        os.remove("sublist.txt")
        os.rename("toreplace.txt","sublist.txt")
    return "Succesfully deleted"
@app.route("/deprem/api",methods=["GET"])
def return_data():
    with open("lastErtq.txt","r") as fp:
        Ertq = fp.readline()
        fp.close()
    data = split_data(Ertq)
    return jsonify(data)     
# Run Server
if __name__ == '__main__':
    app.run(debug=True)