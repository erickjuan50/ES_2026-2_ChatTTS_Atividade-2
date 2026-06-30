# Critérios de maturidade de testes

## Critérios de entrada (estado atual — jun/2026)

| Aspecto | Situação |
| :--- | :--- |
| Automação | Scripts `#511.py`, `#588.py`, `#655.py` via `testall.sh` |
| Framework | Sem `pytest`; sem descoberta automática |
| Isolamento | Modelos reais via `chat.load(source="huggingface")` |
| CI | `unitest.yml` executa shell script; sem cobertura |
| Detecção de falhas | Principalmente em produção e issues abertas |

## Critérios de saída (meta — 6 meses)

| Métrica | Meta |
| :--- | :--- |
| Cobertura `core.py` + `model/` | ≥ 60% |
| PRs validados automaticamente | 100% |
| Bloqueio de merge em falha | Ativo |
| Dependência de GPU nos testes unitários | Eliminada (mocks) |
| Golden tests de normalização | ≥ 1 conjunto por idioma (CN, EN) |
| Tempo médio CI (testes unitários) | < 5 min |

## Indicadores de acompanhamento

```
pytest --cov=ChatTTS --cov-report=term-missing
```

Relatório HTML de cobertura publicado como artefato do GitHub Actions a cada merge em `main`.
