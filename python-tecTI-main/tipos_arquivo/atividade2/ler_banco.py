import pandas as pd
import json

path = 'dados.csv'

def ler_banco():
    df = pd.read_csv(path)
    with open('populacao.json', 'r', encoding='utf-8') as f:
        populacao = json.load(f)
    df['populacao'] = df['cidade'].map(populacao)

    return df

    
print(ler_banco())
