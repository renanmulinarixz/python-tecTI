from ler_banco import ler_banco

dados = ler_banco()

def calcular_media_coluna(distancia_km):
    if dados is not None and distancia_km in dados.columns:
        media = dados[distancia_km].mean()
        return media
    else:
        print(f"Coluna '{distancia_km}' não encontrada ou dados não disponíveis.")
        return None
    

def cidade_mais_proxima():
    if dados is not None and 'distancia_km' in dados.columns:
        cidade_proxima = dados.loc[dados['distancia_km'].idxmin()]['cidade']
        return cidade_proxima
    else:
        print("Coluna 'Distancia_km' não encontrada ou dados não disponíveis.")
        return None


def media_populacao():
    if dados is not None and 'populacao' in dados.columns:
        media = dados['populacao'].mean()
        return media
    else:
        print("Coluna 'populacao' não encontrada ou dados não disponíveis.")
        return None


print("Média da coluna 'Distancia_km':", calcular_media_coluna('Distancia_km'))
print("Cidade mais próxima:", cidade_mais_proxima())
print("Média da população:", media_populacao())



