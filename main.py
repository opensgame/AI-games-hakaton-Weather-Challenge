import pandas as pd
import numpy as np


df = pd.read_csv("train_data/2019_06/B00202A_2019_06.csv", delimiter=';', usecols=[0, 1, 2, 3], header=None,
                 names=['station_id', 'param_code', 'timestamp', 'value'],
                 dtype={'station_id': str, 'param_code': str, 'timestamp': str, 'value': str})
print(df['value'].dtype)

df['value'] = df['value'].apply(lambda x: float(str(x).replace(",", ".")))

df = df.astype({'station_id': str, 'param_code': str, 'timestamp': str, 'value': float}).dtypes

df_opady = pd.read_csv("train_data/2019_06/B00608S_2019_06.csv", delimiter=';', usecols=[0, 1, 2, 4], header=None,
                       names=['station_id', 'param_code', 'timestamp', 'value'],
                       dtype={'station_id': str, 'param_code': str, 'timestamp': str, 'value': str})
print(df_opady['value'].dtype)

df_opady['value'] = df_opady['value'].apply(lambda x: float(str(x).replace(",", ".")))

df_opady = df_opady.astype({'station_id': str, 'param_code': str, 'timestamp': str, 'value': float}).dtypes

print(df.head())


corr = df_opady.corr(method='kendall')
print(corr[1:6])


def getStationList(stationList):
    df = pd.read_csv("train_data/2019_06/B00202A_2019_06.csv", delimiter=';', usecols=[0, 1, 2, 3], header=None,
                     names=['station_id', 'param_code', 'timestamp', 'value'],
                     dtype={'station_id': str, 'param_code': str, 'timestamp': str, 'value': str})
    dfs = []
    for val in stationList:
        dfs.append(df[df.station_id.apply(str).str.contains(val)])
        dfs.append(df[df.station_id.apply(str).str.contains(val)])
    return dfs

# getStationList(['254140010', '249200930'])
