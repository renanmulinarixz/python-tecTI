# =============================================================================
# models/base.py
# Cenário: C - Figurinhas
# =============================================================================
# Este arquivo define a classe base que TODOS os modelos herdam.
# Ela já entrega automaticamente:
#   - id          → chave primária autoincrementada
#   - data_criacao → timestamp de inserção, preenchido pelo banco
#
# Ao herdar ModeloBase, qualquer model ganha esses campos sem precisar
# redeclará-los — mantendo o código DRY (Don't Repeat Yourself).
# =============================================================================

from datetime import datetime

from . import db  # importa a instância SQLAlchemy criada em models/__init__.py


class ModeloBase(db.Model):
    """Classe abstrata compartilhada por todos os models do projeto."""

    # abstract = True → SQLAlchemy NÃO cria tabela para esta classe;
    # ela serve só como "molde" para as subclasses.
    __abstract__ = True

    # Chave primária: inteiro, gerado automaticamente a cada INSERT
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Data/hora de criação: preenchida uma única vez, no momento do INSERT.
    # server_default usa a função NOW() do banco → independe do fuso do Python.
    data_criacao = db.Column(
        db.DateTime,
        default=datetime.utcnow,   # fallback Python caso o banco não suporte
        nullable=False,
    )
