# Eixo A — Estratégia Atual de Testes

Repositório: https://github.com/2noise/ChatTTS (branch `main`)

---

## 1. Estrutura e convenção de testes

| Pergunta | Onde verificar |
| :--- | :--- |
| Existe pasta `tests/`? | https://github.com/2noise/ChatTTS/tree/main/tests |
| Convenção `test_*.py`? | Listar arquivos: `#511.py`, `#588.py`, `#655.py`, `testall.sh` |
| Descoberta automática? | Ausência de `pytest.ini`, `conftest.py` |
| Documentação no README? | README principal — seção de testes |

**Evidência:** `evidencias/eixo_a_estrutura_tests.html`

**Risco registrado:** Alto.

**Recomendação:** Diretório `tests/` com `test_*.py` e separação unitário/integração.

---

## 2. Integração com CI/CD

| Fonte | O que buscar |
| :--- | :--- |
| `.github/workflows/unitest.yml` | Trigger em push/PR; etapa `Run Test` |
| `tests/testall.sh` | Loop `for file in tests/*.py` |
| Cobertura / bloqueio | Ausência de `pytest-cov`, `--cov-fail-under` |

**Evidência:** `evidencias/eixo_a_ci_unitest.html`

**Risco:** Alto.

**Recomendação:** Integrar `pytest` com bloqueio de merge.
