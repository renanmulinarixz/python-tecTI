import json

def salvar_dados(usuario, caminho="dados/dados.json"):

    dados = {
        "nome": usuario.nome,
        "saldo": usuario.saldo,
        "transacoes": [t.to_dict() for t in usuario.transacoes]
    }

    with open(caminho, "w") as f:
        json.dump(dados, f, indent=4)


def carregar_dados(caminho="dados/dados.json"):

    try:
        with open(caminho, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None
