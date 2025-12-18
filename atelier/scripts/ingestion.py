import pandas as pd
import requests
from datetime import datetime


date = datetime.now ().strftime ("%Y-%m-%d")



#		événements : match UBB
url_ubb = 'https://datahub.bordeaux-metropole.fr/api/explore/v2.1/catalog/datasets/met_agenda/records?select=*&where=(keywords_fr%20%3D%20%22UBB%22%20OR%20keywords_fr%20%3D%20%22Rugby%22)'

#		lecture des données 
data_ubb = requests.get (url_ubb).json () ['results']
df_ubb = pd.DataFrame (data_ubb)

#		stockage
df_ubb.to_parquet (f"/data/ingestion/matchs_ubb_{date}.parquet" , index=False)




#		travaux rocade
url_travaux = 'https://datahub.bordeaux-metropole.fr/api/explore/v2.1/catalog/datasets/ci_chantier/records'

# 		lecture des données 
data_travaux = requests.get (url_travaux).json () ['results']
df_travaux = pd.DataFrame (data_travaux)

#		erreur ArrowInvalid geo_shape -> format impossible à convertir
if 'geo_shape' in df_travaux.columns:
    df_travaux ['geo_shape'] = df_travaux ['geo_shape'].astype (str)
if 'geo_point_2d' in df_travaux.columns:
    df_travaux ['geo_point_2d'] = df_travaux ['geo_point_2d'].astype (str)

# 		stockage
df_travaux.to_parquet(f"/data/ingestion/travaux_rocade_{date}.parquet" , index=False)

print ("traitement terminé : fichiers parquet générés")