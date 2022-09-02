from flask import Flask, request, Response, jsonify
from flask_cors import CORS
import json
from controllers.boardController import BoardController

from controllers.politicalPartyController import PoliticalPartyController
from controllers.candidateController import CandidateController
from controllers.boardController import BoardController
from controllers.resultController import ResultController

app = Flask(__name__)
cors = CORS(app)

myControllerPoliticalparty = PoliticalPartyController()
myControllercandidate = CandidateController()
myControllerBoard = BoardController()
myControllerResult = ResultController()

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

################################################
#           ENDPOINT  DE LA MESA               #
################################################

#Metodo para listar todos las mesas 
@app.route("/boards",methods=['GET'])
def get_boards():
    json = myControllerBoard.index()
    return jsonify(json)

#Metodo para crear una mesa 
@app.route("/boards",methods=['POST'])
def create_board():
    data = request.get_json()
    json = myControllerBoard.create(data)
    return jsonify(json)

#Metodo para buscar una mesa por el ID
@app.route("/boards/<string:id>",methods=['GET'])
def get_board(id):
    json = myControllerBoard.show(id)
    return jsonify(json)

#Metodo para actualizar una mesa por el ID
@app.route("/boards/<string:id>",methods=['PUT'])
def update_board(id):
    data = request.get_json()
    json = myControllerBoard.update(id,data)
    return jsonify(json)

#Metodo para eliminar una mesa por el ID
@app.route("/boards/<string:id>",methods=['DELETE'])
def delete_board(id):
    json = myControllerBoard.delete(id)
    return jsonify(json)

#####################################################
##            ENDPOINTS DE RESULTADOS              ##
#####################################################

#OBTENER TODOS LOS RESULTADOS  
@app.route("/results", methods=['GET'])
def get_results():
    json = myControllerResult.index()
    return jsonify(json)

#OBTENER UN RESULTADO EN ESPECIFICO
@app.route("/results/<string:id>", methods=['GET'])
def get_result(id):
    json = myControllerResult.show(id)
    return jsonify(json)

#agregar un resultado en una mesa
@app.route("/results/board/<string:id_board>/candidate/<string:id_candidate>", methods=['POST'])
def create_result(id_board,id_candidate):
    data = request.get_json()
    json = myControllerResult.create(data,id_board,id_candidate)
    return jsonify(json)

#actualizar un resultado
@app.route("/results/<string:id_result>/board/<string:id_board>/candidate/<string:id_candidate>",methods=['PUT'])
def update_result(id_result,id_board,id_candidate):
    data = request.get_json()
    json = myControllerResult.update(id_result,data,id_board,id_candidate)
    return jsonify(json)

#Eliminar un resultado
@app.route("/results/<string:id>", methods=['DELETE'])
def delete_result(id):
    json = myControllerResult.delete(id)
    return jsonify(json)

################################################
#         ENDPOINT  DE LOS REPORTES            #
################################################

#Inscritos total en una mesa
@app.route("/reports/boards/<string:id_board>",methods=['GET'])
def sign_up_boards(id_board):
    json = myControllerResult.get_list_candidate_signUp_board(id_board)
    return jsonify(json)

#Obtener las mesas en las que esta inscrito un candidato
@app.route("/reports/candidate/<string:id_candidate>",methods=['GET'])
def sign_up_boards_candidate(id_candidate):
    json = myControllerResult.get_list_board_signUp_candidate(id_candidate)
    return jsonify(json)

#Devuelve el numero de cédula mayor
@app.route("/reports/newIdentification",methods=['GET'])
def get_new_identification():
    json = myControllerResult.get_new_identification()
    return jsonify(json)


#####################################################
##                     EJECUTABLE                  ##
#####################################################
if __name__ == "__main__":
    app.run(debug=True, port=4000)


