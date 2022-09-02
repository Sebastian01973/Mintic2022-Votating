from repositories.repositoryInterface import RepositoryInterface
from models.result import Result
from bson import ObjectId

class ResultRepository(RepositoryInterface[Result]):

    #Obtener los candidatos inscritos en una mesa
    def get_list_candidate_signUp_board(self,id_mesa):
        theQuery = {"board.$id": ObjectId((id_mesa))}
        return self.query(theQuery)
    
     #listado de mesas en las que un candidato esta inscrito
    def get_list_board_signUp_candidate(self,id_candidate):
        theQuery = {"candidate.$id": ObjectId((id_candidate))}
        return self.query(theQuery)
    
    #Devuelve el numero de cédula mayor
    def get_new_identification(self):
        query1 = {
            "$group":{
                "_id":"$candidate",
                "max":{
                    "$max": "$identification"
                },
                "doc":{"$first":"$$ROOT"
                }
            }
        }
        pipeline = [query1]
        return self.query_aggregation(pipeline)
    

    #Metodo para encontrar la mesa y el partido
    def findBy_board_and_party(self, id_board, id_party):
        query1 = {
            "$match": {
                "board.$id": ObjectId(id_board)
            }
        }
        query2 = {
            "$match": {
                "politicalparty.$id": ObjectId(id_party)
            }
        }
        pipeline = [query1, query2]
        return self.query_aggregation(pipeline)

    

