from pymongo import MongoClient
import pandas as pd



df_uruguaio = pd.read_csv("DadosCSV/Uruguaio/campeonato_uruguaio.csv", encoding="UTF-8")
df_uruguaio_2 = pd.read_csv("DadosCSV/Uruguaio/campeonato_uruguaio_2.csv", encoding="UTF-8")


client = MongoClient('localhost', 27017)
db = client['mineracao_expulsoes']
collection = db['partidas']

collection.insert_many(df_uruguaio.to_dict('records'))
collection.insert_many(df_uruguaio_2.to_dict('records'))

#print(client)