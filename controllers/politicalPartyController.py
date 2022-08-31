from repositories.politicalPartyRepository import PoliticalPartyRepository
from models.politicalParty import PoliticalParty

class PoliticalPartyController():
    #Metodo Contructor
    def __init__(self):
        self.politicalPartyRepository = PoliticalPartyRepository()
    
    #Metodo muestra todos los partidos
    def index(self):
        return self.politicalPartyRepository.find_all()
    
    #Metodo para crear un partido
    def create(self, infoPoliticalParty):
        newPoliticalParty = PoliticalParty(infoPoliticalParty)
        return self.politicalPartyRepository.save(newPoliticalParty)
    
    #Metodo para buscar un solo partido por el ID
    def show(self, id):
        thePoliticalParty = PoliticalParty(self.politicalPartyRepository.find_by_id(id))
        return thePoliticalParty.__dict__
    
    #Metodo para actualizar un partido por el ID
    def update(self, id, infoPoliticalParty):
        currentPoliticalParty = PoliticalParty(self.politicalPartyRepository.find_by_id(id))
        currentPoliticalParty.id = infoPoliticalParty["id"]
        currentPoliticalParty.name = infoPoliticalParty["name"]
        currentPoliticalParty.motto = infoPoliticalParty["motto"]
        return self.politicalPartyRepository.save(currentPoliticalParty)
    
    #Metodo para eliminar un partido por el ID
    def delete(self, id):
        return self.politicalPartyRepository.delete(id)


