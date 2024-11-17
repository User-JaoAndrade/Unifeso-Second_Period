import pandas as pd
from pandas import DataFrame
import datetime


if __name__ == "__main__":

    # Carregando o CSV
    data_frame = pd.read_csv('atendimentos.csv')
    
    # Convertendo colunas para o tipo datetime
    data_frame['inicio'] = pd.to_datetime(data_frame['inicio']) 
    data_frame['fim'] = pd.to_datetime(data_frame['fim'])