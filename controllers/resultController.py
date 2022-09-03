from repositories.repositoryInterface import RepositoryInterface
from repositories.resultRepository import ResultRepository
from repositories.boardRepository import BoardRepository
from repositories.candidateRepository import CandidateRepository

from models.result import Result
from models.board import Board
from models.candidate import Candidate

class ResultController():
    # Metodo Constructor
    def __init__(self):
        self.resultRepository = ResultRepository()
        self.boardRepository = BoardRepository()
        self.candidateRepository = CandidateRepository()
    
    #Funcion que devuleve todos los resultados
    def index(self):
        return self.resultRepository.find_all()
    
    #Funcion para asignar una mesa y candidato al resultado
    def create(self, infoResult,id_board,id_candidate):
        newResult = Result(infoResult)
        theBoard = Board(self.boardRepository.find_by_id(id_board))
        theCandidate = Candidate(self.candidateRepository.find_by_id(id_candidate))
        newResult.board = theBoard
        newResult.candidate = theCandidate
        return self.resultRepository.save(newResult)

    #Funcion que devuelve un solo resultado segun el ID
    def show(self, id):
        theResult = Result(self.resultRepository.find_by_id(id))
        return theResult.__dict__
    
    #Funcion para actualizar el resultado de la mesa y candidato
    def update(self, id, infoResult, id_board, id_candidate):
        theResult = Result(self.resultRepository.find_by_id(id))
        theResult.id = infoResult["id"]
        theResult.board_number = infoResult["board_number"]
        theResult.id_candidate = infoResult["id_candidate"]
        theBoard = Board(self.boardRepository.find_by_id(id_board))
        theCandidate = Candidate(self.candidateRepository.find_by_id(id_candidate))
        theResult.board = theBoard
        theResult.candidate = theCandidate
        return self.resultRepository.save(theResult)
    
    #Eliminar un resultado
    def delete(self, id):
        return self.resultRepository.delete(id)
    
    #Obtener todos los candidatos inscritos en una mesa
    def get_list_candidate_signUp_board(self,id_board):
        return self.resultRepository.get_list_candidate_signUp_board(id_board)
    
    #Obtener las mesas en las que esta inscrito un candidato
    def get_list_board_signUp_candidate(self,id_candidate):
        return self.resultRepository.get_list_board_signUp_candidate(id_candidate)
    
    #Obtener el candidato con mayor cédula
    def get_new_identification(self):
        return self.resultRepository.get_new_identification()
    
    #Metodo para encontrar la mesa y el partido
    def findBy_board_and_party(self, id_board, id_party):
        return self.resultRepository.findBy_board_and_party(id_board,id_party)
    
    
    







    
