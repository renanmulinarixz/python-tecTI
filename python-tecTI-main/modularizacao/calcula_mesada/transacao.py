from datetime import datetime

class Transacao:


    def __init__(self, valor, categoria, descricao, tipo="gasto"):

        self.valor = valor
        self.categoria = categoria
        self.descricao = descricao
        self.tipo = tipo
        self.data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "valor": self.valor,
            "categoria": self.categoria,
            "descricao": self.descricao,
            "tipo": self.tipo,
            "data": self.data
        }
