from flask import Flask, request, Response, jsonify
from flask_cors import CORS
import json

from controllers.politicalPartyController import PoliticalPartyController
from controllers.candidateController import CandidateController

app = Flask(__name__)
cors = CORS(app)

myControllerPoliticalparty = PoliticalPartyController()
myControllercandidate = CandidateController()

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


################################################
#           ENDPOINT  DEL PARTIDO              #
################################################

#Metodo para listar todos los candidatos 
@app.route("/candidates", methods = ['GET'])
def get_candidates():
    json = myControllercandidate.index()
    return jsonify(json)

#Metodo para mostrar un candidato en especifico
@app.route("/candidates/<string:id_candidate>", methods=['GET'])
def get_candidate(id_candidate):
    json = myControllercandidate.show(id_candidate)
    return jsonify(json)

#Metodo para crear un candidato
@app.route("/candidates", methods=['POST'])
def create_candidate():
    data = request.get_json()
    json = myControllercandidate.create(data)
    return jsonify(json)

#Metodo para modificar un candidato
@app.route("/candidates/<string:id_candidate>", methods=['PUT'])
def update_candidate(id_candidate):
    data = request.get_json()
    json = myControllercandidate.update(id_candidate, data)
    return jsonify(json)

#Metodo para eliminar un candidato
@app.route("/candidates/<string:id_candidate>", methods=['DELETE'])
def delete_candidate(id_candidate):
    json = myControllercandidate.delete(id_candidate)
    return jsonify(json)

#Metodo para asignarle un partido al candidato
@app.route("/candidates/<string:id_candidate>/politicalParty/<string:id_politicalParty>", methods=['PUT'])
def assign_party_to_candidate(id_candidate,id_politicalParty):
    json = myControllercandidate.assign_political_party(id_candidate,id_politicalParty)
    return jsonify(json)

if __name__ == "__main__":
    app.run(debug=True, port=4000)


