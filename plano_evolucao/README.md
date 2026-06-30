# Plano de Evolução da Qualidade — ChatTTS

Proposta derivada do Eixo D da auditoria A3. Artefatos de implementação em [`../snippets/`](../snippets/).

---

## 1. Top 3 prioridades

| # | Prioridade | Ação |
| :--- | :--- | :--- |
| 1 | Infraestrutura de testes | Migrar `testall.sh` para `pytest` com `fixtures` e `pytest-cov` |
| 2 | Testes de integração de fluxo | Validar cadeia Texto → GPT → Vocoder → Áudio com golden datasets sintéticos |
| 3 | CI/CD com bloqueio | Evoluir `unitest.yml` para executar `pytest` em todo PR com merge bloqueado |

---

## 2. Camadas de foco

| Camada | Escopo |
| :--- | :--- |
| **Unidade** | `PipelineFactory` (proposta A2): verificar instância Local vs. Cloud com mocks, sem carregar pesos |
| **Integração** | Orquestração de `core.py`: inferência com textos curtos, validação de formato de saída |
| **Regressão** | Golden tests com entradas/saídas de referência para normalização e tokenizer |

---

## 3. Implantação gradual

Regra do escoteiro: toda nova funcionalidade exige teste unitário correspondente. Legado coberto conforme manutenção.

---

## 4. Ferramentas

- `pytest` + `pytest-cov` + GitHub Actions
- Fixtures para isolar modelos (`conftest.py`)
- Dados sintéticos em `tests/fixtures/`

---

## 5. Critérios de sucesso

| Tipo | Critério |
| :--- | :--- |
| **Entrada** | Scripts ad hoc, execução manual, ambiente acoplado ao desenvolvedor, detecção por produção |
| **Saída** | ≥60% cobertura em `core.py` e `model/` em 6 meses; 100% dos PRs validados; mocks/containers; regressões detectadas antes de `main` |

Detalhamento: [`criterios_maturidade.md`](criterios_maturidade.md)

Workflow proposto: [`ci_pytest_exemplo.yml`](ci_pytest_exemplo.yml)
