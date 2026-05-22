import json


def ler_arquivo():
    with open('dados.json', 'r') as arquivo:
        dados = json.load(arquivo)
    return dados
