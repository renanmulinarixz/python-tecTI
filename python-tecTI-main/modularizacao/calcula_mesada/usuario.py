class Usuario:
    def __init__(self, nome, saldo_inicial):
        self.nome = nome
        self.saldo = saldo_inicial
        self.transacoes = []

    def adicionar_transacao(self, transacao):

        if transacao.tipo == "gasto":
            self.saldo -= transacao.valor
        else:
            self.saldo += transacao.valor

        self.transacoes.append(transacao)

    def resumo(self):

        return {
            "nome": self.nome,
            "saldo": self.saldo,
            "total_transacoes": len(self.transacoes)
        }
