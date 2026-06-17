# =============================================================================
# models/oferta.py
# Cenário: C - Figurinhas
# =============================================================================
# Define DUAS tabelas relacionadas:
#
#   OfertaTroca  → cabeçalho da oferta (quem quer trocar + observação)
#   ItemOferta   → linhas da oferta (figurinha + tipo: "oferece"/"deseja")
#
# Diagrama de relacionamentos:
#
#   Colecionador ──< OfertaTroca ──< ItemOferta >── Figurinha
#       (1)              (N)             (N)            (1)
#
# Cada OfertaTroca tem:
#   - 1 FK para Colecionador   (quem está negociando)
#   - N itens ItemOferta       (as figurinhas envolvidas)
#
# Cada ItemOferta tem:
#   - 1 FK para OfertaTroca    (a oferta à qual pertence)
#   - 1 FK para Figurinha      (qual figurinha é essa)
#   - tipo: "oferece" ou "deseja"
# =============================================================================

from . import db
from .base import ModeloBase


class OfertaTroca(ModeloBase):
    """Cabeçalho de uma proposta de troca publicada no mural."""

    __tablename__ = "ofertas_troca"

    # ------------------------------------------------------------------
    # FK → colecionadores.id
    # nullable=False → toda oferta DEVE ter um dono
    # ------------------------------------------------------------------
    colecionador_id = db.Column(
        db.Integer,
        db.ForeignKey("colecionadores.id"),  # referencia a PK da outra tabela
        nullable=False,
    )

    # Texto livre opcional (ex.: "só troco por repetidas")
    observacao = db.Column(db.String(255), nullable=True)

    # ------------------------------------------------------------------
    # Relacionamento N:1 → Colecionador
    # back_populates="ofertas" espelha o atributo em Colecionador
    # ------------------------------------------------------------------
    colecionador = db.relationship(
        "Colecionador",
        back_populates="ofertas",
    )

    # ------------------------------------------------------------------
    # Relacionamento 1:N → ItemOferta
    # cascade garante que ao deletar a oferta, os itens também somem
    # ------------------------------------------------------------------
    itens = db.relationship(
        "ItemOferta",
        back_populates="oferta",
        cascade="all, delete-orphan",
    )

    @classmethod
    def listar_com_colecionador(cls):
        """
        Retorna todas as ofertas ordenadas da mais recente para a mais antiga.
        O joinedload pré-carrega o colecionador em UMA query só,
        evitando o problema N+1 (uma query por oferta ao acessar .colecionador).
        """
        return (
            cls.query
            .order_by(cls.data_criacao.desc())
            .all()
        )

    def __repr__(self):
        return f"<OfertaTroca id={self.id} colecionador_id={self.colecionador_id}>"


class ItemOferta(ModeloBase):
    """Linha de uma oferta: qual figurinha e se está sendo oferecida ou desejada."""

    __tablename__ = "itens_oferta"

    # ------------------------------------------------------------------
    # FK → ofertas_troca.id
    # Liga este item à oferta à qual pertence
    # ------------------------------------------------------------------
    oferta_id = db.Column(
        db.Integer,
        db.ForeignKey("ofertas_troca.id"),
        nullable=False,
    )

    # ------------------------------------------------------------------
    # FK → figurinhas.id
    # Indica qual figurinha está envolvida neste item
    # ------------------------------------------------------------------
    figurinha_id = db.Column(
        db.Integer,
        db.ForeignKey("figurinhas.id"),
        nullable=False,
    )

    # "oferece" → o colecionador tem esta figurinha para dar
    # "deseja"  → o colecionador quer receber esta figurinha
    tipo = db.Column(db.String(20), nullable=False)

    # Quantidade de cópias envolvidas (padrão = 1)
    quantidade = db.Column(db.Integer, nullable=False, default=1)

    # ------------------------------------------------------------------
    # Relacionamentos inversos
    # ------------------------------------------------------------------
    # Permite item.oferta para navegar de volta à OfertaTroca
    oferta = db.relationship("OfertaTroca", back_populates="itens")

    # Permite item.figurinha para acessar os dados da figurinha
    figurinha = db.relationship("Figurinha")

    def __repr__(self):
        return (
            f"<ItemOferta oferta={self.oferta_id} "
            f"figurinha={self.figurinha_id} tipo={self.tipo}>"
        )
