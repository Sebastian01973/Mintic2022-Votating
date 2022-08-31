from repositories.politicalPartyRepository import PoliticalPartyRepository
from models.politicalParty import PoliticalParty

class PoliticalPartyController():

    def __init__(self):
        self.politicalPartyRepository = PoliticalPartyRepository()
    
    def index(self):
        return self.politicalPartyRepository.find_all()
    
    def create(self, infoPoliticalParty):
        newPoliticalParty = PoliticalParty(infoPoliticalParty)
        return self.politicalPartyRepository.save(newPoliticalParty)
    
    def show(self, id):
        thePoliticalParty = PoliticalParty(self.politicalPartyRepository.find_by_id(id))
        return thePoliticalParty.__dict__
    
    def update(self, id, infoPoliticalParty):
        currentPoliticalParty = PoliticalParty(self.politicalPartyRepository.find_by_id(id))
        currentPoliticalParty.id = infoPoliticalParty["id"]
        currentPoliticalParty.name = infoPoliticalParty["name"]
        currentPoliticalParty.motto = infoPoliticalParty["motto"]
        return self.politicalPartyRepository.save(currentPoliticalParty)
    
    def delete(self, id):
        return self.politicalPartyRepository.delete(id)


