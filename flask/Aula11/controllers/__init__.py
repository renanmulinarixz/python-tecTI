# =============================================================================
# controllers/__init__.py
# Cenário: C - Figurinhas
# =============================================================================
# Ponto de entrada do pacote `controllers`.
#
# Importar o Blueprint aqui (e não direto no app.py) mantém o app.py
# limpo e segue o padrão do projeto MVC da Aula 11.
#
# O app.py importa este pacote e registra o Blueprint via register_blueprint().
# =============================================================================

# Importa o Blueprint criado em figurinhas_controller.py
from .figurinhas_controller import figurinhas_bp  # noqa: F401
