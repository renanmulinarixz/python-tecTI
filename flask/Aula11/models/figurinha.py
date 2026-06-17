# =============================================================================
# models/figurinha.py
# Cenário: C - Figurinhas
# =============================================================================
# Define a tabela `figurinhas` — representa cada carta/figurinha do álbum
# da Copa do Mundo.
#
# Esta tabela é referenciada por ItemOferta (via FK figurinha_id),
# que registra quais figurinhas estão sendo oferecidas ou desejadas
# em cada oferta de troca.
# =============================================================================

from . import db
from .base import ModeloBase


class Figurinha(ModeloBase):
    """Representa uma figurinha do álbum da Copa do Mundo."""

    __tablename__ = "figurinhas"

    # Número da figurinha no álbum (ex.: 42) — facilita identificação
    numero = db.Column(db.Integer, nullable=False)

    # Nome do jogador estampado na figurinha (ex.: "Vinicius Jr.")
    nome_jogador = db.Column(db.String(100), nullable=False)

    # Seleção/time representado (ex.: "Brasil", "Argentina")
    time = db.Column(db.String(80), nullable=False)

    @classmethod
    def listar(cls):
        """Retorna todas as figurinhas ordenadas pelo número no álbum."""
        return cls.query.order_by(cls.numero).all()

    def __repr__(self):
        # Ex.: <Figurinha #10 - Vinicius Jr. (Brasil)>
        return f"<Figurinha #{self.numero} - {self.nome_jogador} ({self.time})>"
