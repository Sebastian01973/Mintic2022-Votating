from repositories.candidateRepository import CandidateRepository
from repositories.politicalPartyRepository import PoliticalPartyRepository

from models.candidate import Candidate
from models.politicalParty import PoliticalParty

class CandidateController():
    #Metodo constructor
    def __init__(self):
        self.candidateRepository = CandidateRepository()
        self.politicalPartyRepository = PoliticalPartyRepository()

    #Metodo muestra todos los candidatos
    def index(self):
        return self.candidateRepository.find_all()
    
    #Metodo para crear un candidato
    def create(self, infoCandidate):
        newCandidate = Candidate(infoCandidate)
        return self.candidateRepository.save(newCandidate)
    
    #Metodo para buscar un solo candidato por el ID
    def show(self, id ):
        thecandidate = Candidate(self.candidateRepository.find_by_id(id))
        return thecandidate.__dict__
    
    #Metodo para actualizar un candidato por el ID
    def update(self, id, infocandidate):
        currentCandidate = Candidate(self.candidateRepository.find_by_id(id))
        currentCandidate.identification = infocandidate["identification"]
        currentCandidate.resolution_number = infocandidate["resolution_number"]
        currentCandidate.name = infocandidate["name"]
        currentCandidate.last_name = infocandidate["last_name"]
        return self.candidateRepository.save(currentCandidate)
    
    #Metodo para eliminar un candidato por el ID
    def delete(self, id):
        return self.candidateRepository.delete(id)
    
    #Metodo para asignarle un partido a un candidato por el ID del partido y del candidato
    def assign_political_party(self, id, id_politicalParty):
        currentcandidate = Candidate(self.candidateRepository.find_by_id(id))
        currentPoliticalParty = PoliticalParty(self.politicalPartyRepository.find_by_id(id_politicalParty))
        currentcandidate.politicalParty = currentPoliticalParty
        return self.candidateRepository.save(currentcandidate)

    
