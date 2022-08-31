from repositories.boardRepository import BoardRepository
from models.board import Board

class BoardController():
    #Metodo constructor
    def __init__(self):
        self.boardRepository = BoardRepository()

    #Metodo muestra todos las mesas
    def index(self):
        return self.boardRepository.find_all()
    
    #Metodo para crear una mesa
    def create(self, infoBoard):
        newBoard = Board(infoBoard)
        return self.boardRepository.save(newBoard)
    
    #Metodo para buscar una mesa por el ID
    def show(self, id):
        theBoard = Board(self.boardRepository.find_by_id(id))
        return theBoard.__dict__
    
    #Metodo para actualizar una mesa por el ID
    def update(self, id, infoBoard):
        currentBoard = Board(self.boardRepository.find_by_id(id))
        currentBoard.number = infoBoard["number"]
        currentBoard.number_registrants = infoBoard["number_registrants"]
        return self.boardRepository.save(currentBoard)
    
    #Metodo para eliminar una mesa por el ID
    def delete(self, id):
        return self.boardRepository.delete(id)
    