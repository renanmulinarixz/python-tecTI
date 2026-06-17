# =============================================================================
# app.py
# Cenário: C - Figurinhas
# =============================================================================
# Ponto de entrada da aplicação Flask.
#
# Responsabilidades:
#   1. Criar e configurar o app Flask
#   2. Conectar o SQLAlchemy ao app (db.init_app)
#   3. Registrar o Blueprint do cenário C (/figurinhas)
#   4. Criar as tabelas no banco (db.create_all) na primeira execução
#   5. Iniciar o servidor de desenvolvimento
#
# ATENÇÃO: este arquivo já existia na Aula 11. Os trechos marcados com
# "ADICIONAR" são os únicos que precisam ser inseridos no arquivo original.
# =============================================================================

from flask import Flask

# Importa a instância db e TODOS os models (necessário para create_all)
from models import db, Colecionador, Figurinha, OfertaTroca, ItemOferta  # noqa: F401

# ── ADICIONAR ──────────────────────────────────────────────────────────────
# Importa o Blueprint do cenário C
from controllers.figurinhas_controller import figurinhas_bp
# ──────────────────────────────────────────────────────────────────────────

# ------------------------------------------------------------------------------
# Criação e configuração do app Flask
# ------------------------------------------------------------------------------
app = Flask(
    __name__,
    template_folder="views/templates",  # pasta onde o Flask busca os HTMLs
    static_folder="views/static",       # pasta de CSS/JS/imagens (se houver)
)

# URI do banco de dados SQLite (arquivo local, criado automaticamente)
# Em produção, troque por PostgreSQL: "postgresql://user:pass@host/dbname"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///aula11.db"

# Desabilita o rastreamento de modificações (economiza memória, sem perda)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Chave secreta usada para sessões Flask (sessions, flash messages)
app.config["SECRET_KEY"] = "aula11-figurinhas-secret"

# ------------------------------------------------------------------------------
# Plugar o SQLAlchemy ao app (padrão Application Factory do Flask)
# ------------------------------------------------------------------------------
db.init_app(app)

# ── ADICIONAR ──────────────────────────────────────────────────────────────
# Registrar o Blueprint do cenário C
# Todas as rotas definidas em figurinhas_controller.py ficam disponíveis
# com o prefixo /figurinhas (definido no url_prefix do Blueprint)
app.register_blueprint(figurinhas_bp)
# ──────────────────────────────────────────────────────────────────────────

# ------------------------------------------------------------------------------
# Criação das tabelas no banco (apenas na primeira execução)
# ------------------------------------------------------------------------------
# db.create_all() lê os __tablename__ de todos os models importados acima
# e cria as tabelas que ainda não existem no SQLite.
# NÃO apaga dados existentes — seguro de chamar sempre.
with app.app_context():
    db.create_all()

# ------------------------------------------------------------------------------
# Inicialização do servidor de desenvolvimento
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    # debug=True → recarrega o servidor ao salvar arquivos + exibe erros no browser
    app.run(debug=True)
