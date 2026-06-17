# =============================================================================
# models/colecionador.py
# Cenário: C - Figurinhas
# =============================================================================
# Define a tabela `colecionadores` — representa a pessoa que participa
# do mural de trocas.
#
# Relacionamento:
#   Colecionador ──< OfertaTroca   (um colecionador pode ter várias ofertas)
#   O lado "um" declara relationship(); o lado "muitos" declara a FK.
# =============================================================================

from . import db          # instância SQLAlchemy compartilhada
from .base import ModeloBase  # traz id + data_criacao automaticamente


class Colecionador(ModeloBase):
    """Representa um participante do mural de trocas de figurinhas."""

    # Nome da tabela no banco de dados SQLite/PostgreSQL
    __tablename__ = "colecionadores"

    # Apelido usado no mural (ex.: "Zeca_SP") — obrigatório, até 60 chars
    apelido = db.Column(db.String(60), nullable=False)

    # Cidade do colecionador — exibida na lista para facilitar trocas locais
    cidade = db.Column(db.String(80), nullable=False)

    # ------------------------------------------------------------------
    # Relacionamento 1-N com OfertaTroca
    # ------------------------------------------------------------------
    # back_populates="colecionador" → cria o atributo inverso em OfertaTroca,
    # permitindo oferta.colecionador sem query extra (lazy join).
    # cascade="all, delete-orphan" → ao deletar um Colecionador, suas
    # ofertas também são deletadas automaticamente.
    # ------------------------------------------------------------------
    ofertas = db.relationship(
        "OfertaTroca",
        back_populates="colecionador",
        cascade="all, delete-orphan",
    )

    @classmethod
    def listar(cls):
        """Retorna todos os colecionadores ordenados alfabeticamente pelo apelido."""
        return cls.query.order_by(cls.apelido).all()

    def __repr__(self):
        # Representação útil no terminal/debug: <Colecionador Zeca_SP>
        return f"<Colecionador {self.apelido}>"
