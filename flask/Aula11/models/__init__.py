# =============================================================================
# models/__init__.py
# Cenário: C - Figurinhas
# =============================================================================
# Ponto de entrada do pacote `models`.
#
# Responsabilidades:
#   1. Criar a ÚNICA instância do SQLAlchemy (db) usada em todo o projeto.
#      Importar db daqui garante que todos os models compartilhem o mesmo
#      objeto — evitando erros de "tabela criada em contexto diferente".
#   2. Importar todos os models DEPOIS de criar db, para que as classes
#      já encontrem o objeto ao serem carregadas.
#   3. Expor __all__ para deixar claro o que faz parte da API pública
#      deste pacote.
# =============================================================================

from flask_sqlalchemy import SQLAlchemy

# ------------------------------------------------------------------
# Instância global do SQLAlchemy.
# Será "plugada" ao app Flask em app.py via db.init_app(app).
# ------------------------------------------------------------------
db = SQLAlchemy()

# ------------------------------------------------------------------
# Imports dos models — DEVEM vir DEPOIS de criar db, pois cada
# model faz "from . import db" ao ser carregado.
# ------------------------------------------------------------------
from .base import ModeloBase              # noqa: E402 (ordem intencional)
from .colecionador import Colecionador    # noqa: E402
from .figurinha import Figurinha          # noqa: E402
from .oferta import OfertaTroca, ItemOferta  # noqa: E402

# Lista os símbolos exportados quando alguém faz "from models import *"
__all__ = [
    "db",
    "ModeloBase",
    "Colecionador",
    "Figurinha",
    "OfertaTroca",
    "ItemOferta",
]
