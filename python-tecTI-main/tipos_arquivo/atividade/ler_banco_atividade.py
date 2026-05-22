import pandas as pd
import json

path_csv = 'banco_2.csv'
path_json = 'banco_1.json'

def ler_banco():
    df_csv = pd.read_csv(path_csv)
    with open(path_json, 'r', encoding='utf-8') as f:
        dados_json = json.load(f)

    df_json = pd.DataFrame(dados_json)
    df_final = pd.concat([df_csv, df_json], ignore_index=True)

    return df_final


print(ler_banco())
