from models.transacao import Transacao

class ControleGastos:


    def __init__(self, usuario):
        self.usuario = usuario

    def registrar_gasto(self, valor, categoria, descricao):
        transacao = Transacao(valor, categoria, descricao, tipo="gasto")
        self.usuario.adicionar_transacao(transacao)

    def registrar_entrada(self, valor, descricao="Mesada"):
  
        transacao = Transacao(valor, "mesada", descricao, tipo="entrada")
        self.usuario.adicionar_transacao(transacao)

    def listar_gastos_por_categoria(self):

        resumo = {}

        for t in self.usuario.transacoes:
            if t.tipo == "gasto":
                resumo[t.categoria] = resumo.get(t.categoria, 0) + t.valor

        return resumo
