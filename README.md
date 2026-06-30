# Auditoria de Testes de Software e Plano de Evolução de Qualidade — ChatTTS

**Disciplina:** Engenharia de Software (COMP0503)  
**Atividade:** A3 — Auditoria de Testes e Plano de Evolução de Qualidade  
**Projeto auditado:** [2noise/ChatTTS](https://github.com/2noise/ChatTTS) (repositório upstream; este repositório contém os artefatos da equipe)

**Link para o vídeo de apresentação:** 
https://drive.google.com/file/d/1rw_iGKvXUCag0ene8N5wb_x06BR0d4wd/view?usp=sharing
## Equipe

Carlos Henrico Fontes Cabral, Wanessa Silva Santos, Luiz Felipe da Conceição Souza, Erick Juan Gois Oliveira, João Pedro Brandão Almeida.

| Integrante | Contribuição na A3 |
| :--- | :--- |
| Carlos Henrico Fontes Cabral | Eixo A — Estratégia atual de testes |
| Luiz Felipe da Conceição Souza | Eixo B — Qualidade técnica dos testes |
| João Pedro Brandão Almeida | Eixo C — Lacunas, riscos e falhas potenciais |
| Erick Juan Gois Oliveira | Evidências de CI e scripts de teste |
| Wanessa Silva Santos | Conexão A1/A2 e Eixo D — Plano de evolução |

## Entregáveis neste repositório

| Pasta | Conteúdo |
| :--- | :--- |
| [`evidencias/`](evidencias/) | Prints (HTML) de trechos e links do GitHub — um por item investigado |
| [`resultado/`](resultado/) | Diagnóstico consolidado por eixo (evidência + análise + risco) |
| [`plano_evolucao/`](plano_evolucao/) | Prioridades, critérios de maturidade e workflow CI proposto |
| [`prompts/`](prompts/) | Roteiros de replicação da auditoria (checklists por eixo) |
| [`snippets/`](snippets/) | Exemplos de testes pytest com mocks e golden tests |
| [`artefatos/`](artefatos/) | Links verificáveis, arquivos analisados e log da auditoria |

**Relatório técnico (PDF)** e **apresentação** são entregues no Classroom conforme o enunciado.

---

## Conexão com as Atividades 1 e 2

Na A1 foram identificados gargalos em suporte Ascend NPU, fallback do normalizer, parametrização de `cache_dir` e ausência de métricas de validação de áudio. Na A2, a classe `Chat` em `ChatTTS/core.py` foi classificada como God Object de alto risco arquitetural.

A A3 verifica se a suíte de testes existente oferece isolamento adequado (mocks/fixtures) para viabilizar refatoração do core sem regressões.

---

## Resumo dos achados (A3)

| Eixo | Foco | Classificação de risco (síntese) |
| :--- | :--- | :--- |
| **A** — Estratégia | Estrutura `tests/` ad hoc, CI via `testall.sh` | Alto |
| **B** — Qualidade | Nomenclatura, isolamento, mocks, regras de negócio | Alto / Médio |
| **C** — Lacunas | Funcionalidades críticas sem teste, regressões | Alto / Médio-alto |
| **D** — Evolução | pytest, golden tests, CI com bloqueio | Plano proposto |

Detalhamento: [`resultado/diagnostico_consolidado_a3.md`](resultado/diagnostico_consolidado_a3.md).

---

## Como replicar a auditoria

1. **Eixo A:** Inspecione https://github.com/2noise/ChatTTS/tree/main/tests e `.github/workflows/unitest.yml`.
2. **Eixo B:** Leia `tests/#511.py`, `#655.py` e `testall.sh`; verifique ausência de `conftest.py` e mocks.
3. **Eixo C:** Mapeie funcionalidades em `ChatTTS/core.py` sem teste correspondente; compare com [releases](https://github.com/2noise/ChatTTS/releases).
4. **Eixo D:** Consulte [`plano_evolucao/`](plano_evolucao/) e execute os snippets: `pip install pytest numpy && pytest snippets/ -v`.

Checklists completos: [`prompts/`](prompts/).

---

## Plano de evolução (visão geral)

1. Migrar `testall.sh` para `pytest` com fixtures e `pytest-cov`.
2. Implementar testes de integração Texto → Áudio com golden datasets.
3. Evoluir CI para bloquear merge em falha de testes.

Detalhes: [`plano_evolucao/README.md`](plano_evolucao/README.md).
