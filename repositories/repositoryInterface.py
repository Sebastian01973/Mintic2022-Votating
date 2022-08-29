from bson import DBRef
from bson.objectid import ObjectId
from typing import List,get_origin,get_args,Generic,TypeVar
import json
import database.database as dbase

T = TypeVar('T')

class RepositoryInterface(Generic[T]):
    def __init__(self):
        self.db = dbase.datadabe_connection()
        theClass = get_args(self.__orig_bases__[0])
        self.collection = theClass[0].__name__.lower()


