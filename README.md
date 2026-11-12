# JobTracker API

API for tracking job applications and interviews in the tech sector.

## Status

🚧 Em desenvolvimento — Fase 2 (modelagem)

## Decisões técnicas

- **uv** — lockfile + reprodutibilidade; separa dev-deps; rápido; compatível com pip.
- **Layout flat** — app, não lib; `src/` não paga o custo agora; reversível.
- **Ruff** — unifica lint + format + isort em uma ferramenta; menos superfície.
- **`package = false`** — app (Tipo B), não lib; evita rebuild/stale import; CI mais rápido.

## Como rodar

Em breve (Fase 2).

## Requisitos

- Python 3.14+