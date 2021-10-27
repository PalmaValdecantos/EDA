import pandas as pd
import numpy as np

#Funcion añadir columna de año
def columna_date(pasar_date):
    date = []
    columna =pd.Series(np.arange(1,51))
    for i in columna:
        date.append(pasar_date)
    return date
columna_date(2019)

# Funcion bailabilidad por genero
def genero_bailable(tabla):  
    resultado = tabla[['genre','danceability']].groupby(["genre"]).mean().sort_values(by=['danceability'], ascending=False)
    return resultado