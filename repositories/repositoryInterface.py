from bson import DBRef
from bson.objectid import ObjectId
from typing import List,get_origin,get_args,Generic,TypeVar
import json
import database.database as dbase

# Variable para el tipo de dato generico
T = TypeVar('T')

class RepositoryInterface(Generic[T]):
    #constructor de la clase
    def __init__(self):
        self.db = dbase.datadabe_connection()
        theClass = get_args(self.__orig_bases__[0])
        self.collection = theClass[0].__name__.lower()
    
    # Trae el valor buscado
    def get_values_DBRef_from_list(self, theList):
        newList = []
        thecollection = self.db[theList[0].collection]
        for item in theList:
            value = thecollection.find_one({"_id": ObjectId(item.id)})
            value["_id"] = value["_id"].__str__()
            newList.append(value)
        return newList

    #Trae el valor buscado 
    def get_values_DBRef(self,x):
        keys = x.keys()
        for k in keys:
            if isinstance(x[k],DBRef):
                theCollection = self.db[x[k].collection]
                value = theCollection.find_one({"_id": ObjectId(x[k].id)})
                value["_id"] = value["_id"].__str__()
                x[k] = value
                x[k] = self.get_values_DBRef(x[k])
            elif isinstance(x[k],list) and len(x[k]) > 0:
                x[k] = self.get_values_DBRef_from_list(x[k])
            elif isinstance(x[k], dict):
                x[k] = self.get_values_DBRef(x[k])
        return x
    
    #Busca la coleccion
    def find_by_dd(self, id):
        theCollection = self.db[self.collection]
        x = theCollection.find_one({"_id": ObjectId(id)})
        x = self.get_values_DBRef(x)
        if x == None:
            x = {}
        else:
            x["_id"] = x["_id"].__str__()
        return x
    
    # De una lista y devuelve una lista
    def format_list(self, x):
        newList = []
        for item in x:
            if isinstance(item, ObjectId):
                newList.append(item.__str__())
        if len(newList) == 0:
            newList = x
        return x
        
    # Transforma el objeto ID
    


