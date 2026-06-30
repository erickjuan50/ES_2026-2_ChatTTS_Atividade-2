# Eixo D — Plano de Evolução da Qualidade

---

## 1. Top 3 prioridades

1. **Infraestrutura:** migrar `testall.sh` → `pytest` + `pytest-cov`
2. **Integração:** fluxo Texto → GPT → Vocoder → Áudio com golden datasets
3. **CI/CD:** bloqueio de merge em falha de testes

---

## 2. Camadas de foco

| Camada | Alvo | Técnica |
| :--- | :--- | :--- |
| Unidade | `PipelineFactory` | Mocks sem carregar pesos |
| Integração | `core.py` / `infer()` | Textos curtos, validação de saída |
| Regressão | Normalização | Golden tests parametrizados |

Snippets: [`../snippets/`](../snippets/)

---

## 3. Implantação gradual

Regra do escoteiro: teste unitário obrigatório por nova funcionalidade.

---

## 4. Automação e critérios de sucesso

| Ferramenta | Uso |
| :--- | :--- |
| `pytest` | Descoberta e execução |
| `pytest-cov` | Cobertura ≥60% em 6 meses |
| GitHub Actions | 100% dos PRs validados |

Workflow proposto: [`../plano_evolucao/ci_pytest_exemplo.yml`](../plano_evolucao/ci_pytest_exemplo.yml)

Critérios detalhados: [`../plano_evolucao/criterios_maturidade.md`](../plano_evolucao/criterios_maturidade.md)
