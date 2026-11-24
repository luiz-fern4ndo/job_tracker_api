# JobTracker API

API for tracking job applications and interviews in the tech sector.

## Status

🚧 Em desenvolvimento — Fase 6 (CRUD de Application e testes)

## Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/) — framework web
- [SQLAlchemy 2.0](https://www.sqlalchemy.org/) — ORM
- [Pydantic v2](https://docs.pydantic.dev/) — validação de dados
- [Pytest](https://docs.pytest.org/) — testes
- [SQLite](https://www.sqlite.org/) — banco de dados (dev)
- [uv](https://docs.astral.sh/uv/) — gerenciador de dependências
- [Ruff](https://docs.astral.sh/ruff/) — lint e formatação

## Endpoints

### Applications
- `POST /applications/` — cria uma candidatura
- `GET /applications/` — lista todas as candidaturas
- `GET /applications/{id}` — busca candidatura por ID
- `PATCH /applications/{id}` — atualiza parcialmente uma candidatura
- `DELETE /applications/{id}` — deleta uma candidatura

*(Endpoints de Interview em desenvolvimento)*

## Como rodar

```bash
# Instalar dependências
uv sync

# Rodar a API
uv run uvicorn main:app --reload

# Acessar o Swagger
# http://127.0.0.1:8000/docs

# Rodar os testes
uv run pytest