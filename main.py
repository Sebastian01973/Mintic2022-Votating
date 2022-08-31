from flask import Flask, request, Response, jsonify
from flask_cors import CORS
import json

from controllers.politicalPartyController import PoliticalPartyController

app = Flask(__name__)
cors = CORS(app)

myControllerPoliticalparty = PoliticalPartyController()

@app.route("/", methods=["GET"])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)

################################################
#           ENDPOINT  DEL PARTIDO              #
################################################

#Metodo para listar todos los partidos 
@app.route("/politicalPartys", methods=['GET'])
def get_political_partys():
    json = myControllerPoliticalparty.index()
    return jsonify(json)

#Metodo para mostrar un partido en especifico
@app.route("/politicalParty/<string:id>", methods=['GET'])
def get_political_party(id):
    json = myControllerPoliticalparty.show(id)
    return jsonify(json)

#Metodo para crear un partido
@app.route("/politicalParty", methods=['POST'])
def create_political_party():
    data = request.get_json()
    json = myControllerPoliticalparty.create(data)
    return jsonify(json)

#Metodo para modificar un partido
@app.route("/politicalParty/<string:id>", methods=['PUT'])
def update_political_party(id):
    data = request.get_json()
    json = myControllerPoliticalparty.update(id,data)
    return jsonify(json)

#Metodo para eliminar un partido
@app.route("/politicalParty/<string:id>", methods=['DELETE'])
def delete_political_party(id):
    json = myControllerPoliticalparty.delete(id)
    return jsonify(json)



if __name__ == "__main__":
    app.run(debug=True, port=4000)


