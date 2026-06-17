# =============================================================================
# controllers/figurinhas_controller.py
# Cenário: C - Figurinhas
# =============================================================================
# Define o Blueprint "figurinhas" e todas as rotas do cenário C.
#
# Blueprint é o mecanismo do Flask para agrupar rotas relacionadas em
# módulos separados, sem poluir o app.py principal.
#
# Rotas definidas aqui:
#   GET  /figurinhas/                   → lista todas as ofertas (index)
#   GET  /figurinhas/oferta/cadastrar   → exibe formulário de nova oferta
#   POST /figurinhas/oferta/cadastrar   → processa o formulário e salva no banco
# =============================================================================

from flask import Blueprint, redirect, render_template, request, url_for

from models import Colecionador, Figurinha, ItemOferta, OfertaTroca, db

# ------------------------------------------------------------------------------
# Criação do Blueprint
# ------------------------------------------------------------------------------
# "figurinhas"   → nome do Blueprint; usado em url_for('figurinhas.index')
# __name__       → diz ao Flask onde está este módulo (para achar templates)
# url_prefix     → todas as rotas deste Blueprint começam com /figurinhas
# ------------------------------------------------------------------------------
figurinhas_bp = Blueprint("figurinhas", __name__, url_prefix="/figurinhas")


# ==============================================================================
# ROTA 1 — Mural de ofertas (listagem)
# ==============================================================================
@figurinhas_bp.route("/")
def index():
    """
    Exibe o mural com todas as ofertas de troca publicadas.

    Chama listar_com_colecionador() que retorna as ofertas ordenadas
    da mais recente para a mais antiga.
    O template acessa oferta.colecionador.apelido graças ao relationship.
    """
    # Busca todas as ofertas no banco, mais recentes primeiro
    ofertas = OfertaTroca.listar_com_colecionador()

    # Renderiza o template passando a lista de ofertas como variável Jinja2
    return render_template("figurinhas/lista_ofertas.html", ofertas=ofertas)


# ==============================================================================
# ROTA 2 — Cadastrar nova oferta (GET exibe form / POST processa)
# ==============================================================================
@figurinhas_bp.route("/oferta/cadastrar", methods=["GET", "POST"])
def cadastrar_oferta():
    """
    GET:  Exibe o formulário com selects populados (colecionadores e figurinhas).
    POST: Lê os dados do formulário, cria OfertaTroca + dois ItemOferta
          (um "oferece" e um "deseja") e redireciona para o mural.
    """

    # Sempre carregamos as listas para popular os <select> do HTML
    colecionadores = Colecionador.listar()   # ordem: apelido A→Z
    figurinhas = Figurinha.listar()          # ordem: número crescente

    if request.method == "POST":
        # ------------------------------------------------------------------
        # Leitura dos campos enviados pelo formulário (name= no HTML)
        # ------------------------------------------------------------------
        # ID do colecionador selecionado no <select name="colecionador_id">
        colecionador_id = request.form.get("colecionador_id", type=int)

        # ID da figurinha que o colecionador possui e quer dar
        figurinha_oferece_id = request.form.get("figurinha_oferece_id", type=int)

        # ID da figurinha que o colecionador não tem e quer receber
        figurinha_deseja_id = request.form.get("figurinha_deseja_id", type=int)

        # Texto livre opcional (ex.: "só troco por repetidas")
        observacao = request.form.get("observacao", "").strip()

        # ------------------------------------------------------------------
        # Criação dos objetos e persistência no banco
        # ------------------------------------------------------------------

        # 1. Cria o cabeçalho da oferta (OfertaTroca)
        nova_oferta = OfertaTroca(
            colecionador_id=colecionador_id,
            observacao=observacao if observacao else None,
        )
        db.session.add(nova_oferta)

        # 2. flush() envia o INSERT ao banco SEM confirmar (commit),
        #    gerando o nova_oferta.id necessário para as FKs dos itens.
        db.session.flush()

        # 3. Cria o item "oferece" — figurinha que o colecionador TEM
        item_oferece = ItemOferta(
            oferta_id=nova_oferta.id,
            figurinha_id=figurinha_oferece_id,
            tipo="oferece",       # valor fixo definido no enunciado
            quantidade=1,
        )
        db.session.add(item_oferece)

        # 4. Cria o item "deseja" — figurinha que o colecionador QUER
        item_deseja = ItemOferta(
            oferta_id=nova_oferta.id,
            figurinha_id=figurinha_deseja_id,
            tipo="deseja",        # valor fixo definido no enunciado
            quantidade=1,
        )
        db.session.add(item_deseja)

        # 5. commit() confirma TUDO de uma vez (oferta + 2 itens)
        #    Se qualquer INSERT falhar, o banco reverte automaticamente.
        db.session.commit()

        # Redireciona para o mural após cadastro bem-sucedido
        # Padrão PRG (Post/Redirect/Get) → evita reenvio ao atualizar a página
        return redirect(url_for("figurinhas.index"))

    # GET → apenas renderiza o formulário vazio com os selects populados
    return render_template(
        "figurinhas/formulario_oferta.html",
        colecionadores=colecionadores,
        figurinhas=figurinhas,
    )
