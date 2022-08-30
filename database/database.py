from pymongo import  MongoClient
import json,certifi

ca = certifi.where()

def load_config_file():
    with open('database/config.json') as f:
        data = json.load(f)
    return data

def datadabe_connection():
    dataConfig = load_config_file()
    try:
        #Conection to Atlas
        client = MongoClient(dataConfig['MONGO_URI_SERVER'], tlsCAFile=ca)
        #Conection local
        #client = MongoClient(dataConfig['MONGO_URI_LOCAL'], dataConfig['MONGO_PORT'])
        db = client['proyecto_ciclo4']
    except ConnectionError:
        print("Error conection to DB")
    return db