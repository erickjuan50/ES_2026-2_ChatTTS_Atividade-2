# Diagnóstico consolidado — A3 Auditoria de Testes ChatTTS

Formato por item: **Evidência** → **Diagnóstico** → **Risco** → **Recomendação**

Repositório analisado: https://github.com/2noise/ChatTTS (branch `main`)

---

## Eixo A — Estratégia Atual de Testes

### A.1 Estrutura e convenção de testes

| Campo | Conteúdo |
| :--- | :--- |
| **Evidência** | Pasta `tests/` com `#511.py`, `#588.py`, `#655.py` e `testall.sh` — `evidencias/eixo_a_estrutura_tests.html` |
| **Diagnóstico** | Existe diretório de testes, porém sem convenção `test_*.py` nem organização por tipo (unitário/integração). Scripts ad hoc nomeados por issue impedem descoberta automática por `pytest`. |
| **Risco** | **Alto** |
| **Recomendação** | Estruturar `tests/` com `test_*.py` e separação unitário/integração. |

### A.2 Integração com CI/CD

| Campo | Conteúdo |
| :--- | :--- |
| **Evidência** | `.github/workflows/unitest.yml` executa `tests/testall.sh` — `evidencias/eixo_a_ci_unitest.html` |
| **Diagnóstico** | CI instala dependências e executa scripts via shell. Não há cobertura, relatório estruturado nem validação assertiva de regras de negócio. Mudanças em `core.py` podem integrar sem barreira robusta. |
| **Risco** | **Alto** |
| **Recomendação** | Integrar `pytest` ao pipeline com bloqueio de merge. |

---

## Eixo B — Qualidade Técnica dos Testes

### B.1 Nomenclatura e comportamento observável

| Campo | Conteúdo |
| :--- | :--- |
| **Evidência** | Ausência de `test_inference.py`, `test_speaker_generation.py`, `test_text_normalization.py` — `evidencias/eixo_b_nomenclatura_tests.html` |
| **Diagnóstico** | Workflow de Unit Test existe, mas a suíte não está documentada no README nem nomeada por comportamento. |
| **Risco** | **Alto** |
| **Recomendação** | Adotar `def test_generate_audio_from_text()` e arquivos descritivos. |

### B.2 Isolamento, independência e reprodutibilidade

| Campo | Conteúdo |
| :--- | :--- |
| **Evidência** | `tests/#511.py` — `chat.load(source="huggingface")` + inferência real — `evidencias/eixo_b_isolamento_ambiente.html` |
| **Diagnóstico** | Testes dependem de GPU/CPU, PyTorch, Transformers e download de pesos. Geração probabilística sem seed global fixa. |
| **Risco** | **Alto** |
| **Recomendação** | Seeds fixas, Docker, dados padronizados, testes independentes de GPU. |

### B.3 Mocks, stubs e fixtures

| Campo | Conteúdo |
| :--- | :--- |
| **Evidência** | Ausência de `fixtures/`, `conftest.py`, `mock/` — `evidencias/eixo_b_ausencia_mocks.html` |
| **Diagnóstico** | Modelos reais carregados em runtime. Maior tempo de execução, custo computacional e instabilidade entre ambientes. |
| **Risco** | **Alto** |
| **Recomendação** | Mocks para carregamento de modelos, fixtures de áudio e dados sintéticos. |

### B.4 Validação de regras de negócio

| Campo | Conteúdo |
| :--- | :--- |
| **Evidência** | Releases com correções de inferência e normalização — `evidencias/eixo_b_regras_negocio.html` |
| **Diagnóstico** | Fluxos centrais (voz, emoção, pausas, locutor) sem cobertura robusta. Bugs chegam a versões públicas. |
| **Risco** | **Alto** |
| **Recomendação** | Testes para geração de áudio, estabilidade do locutor, pausas e qualidade de saída. |

### B.5 Redundância e fragilidade

| Campo | Conteúdo |
| :--- | :--- |
| **Evidência** | `testall.sh` + `requirements.txt` — `evidencias/eixo_b_fragilidade.html` |
| **Diagnóstico** | Poucos testes para avaliar redundância; alta fragilidade por dependência de ambiente e bibliotecas voláteis. |
| **Risco** | **Médio** |
| **Recomendação** | Separar testes unitários, integração e IA. |

---

## Eixo C — Lacunas, Riscos e Falhas Potenciais

### C.1 Funcionalidades críticas sem testes

| Campo | Conteúdo |
| :--- | :--- |
| **Evidência** | Mapeamento funcional — `evidencias/eixo_c_funcionalidades_sem_testes.html` |
| **Diagnóstico** | Inferência, emoção, pausas, multi-locutor, download e compatibilidade GPU/CPU sem testes dedicados. |
| **Risco** | **Alto** |
| **Recomendação** | Testes automatizados para geração de áudio, speaker e normalização. |

### C.2 Módulos de maior risco

| Campo | Conteúdo |
| :--- | :--- |
| **Evidência** | `ChatTTS/core.py`, normalizadores, `requirements.txt` — `evidencias/eixo_c_modulos_risco.html` |
| **Diagnóstico** | Inferência e normalização concentram dívida técnica e complexidade. |
| **Risco** | **Alto** |
| **Recomendação** | Testes de regressão antes de alterações em `core.py`. |

### C.3 Dependências externas sem isolamento

| Campo | Conteúdo |
| :--- | :--- |
| **Evidência** | `requirements.txt` — `evidencias/eixo_c_dependencias_externas.html` |
| **Diagnóstico** | PyTorch, Transformers, Hugging Face sem mocks ou ambientes simulados. |
| **Risco** | **Alto** |
| **Recomendação** | Camadas de abstração e mocks das dependências. |

### C.4 Proteção contra regressões

| Campo | Conteúdo |
| :--- | :--- |
| **Evidência** | CI parcial + histórico de releases — `evidencias/eixo_c_regressoes.html` |
| **Diagnóstico** | Proteção limitada; sem golden tests nem validação de qualidade de áudio. |
| **Risco** | **Alto** |
| **Recomendação** | Golden tests, integração end-to-end, métricas automáticas de áudio. |

### C.5 Detecção de bugs severos

| Campo | Conteúdo |
| :--- | :--- |
| **Evidência** | Síntese da suíte — `evidencias/eixo_c_deteccao_bugs.html` |
| **Diagnóstico** | Resposta parcial: CI detecta falhas pontuais, mas falhas em inferência/qualidade podem passar despercebidas. |
| **Risco** | **Médio-alto** |
| **Recomendação** | Ampliar cobertura, integração completa e métricas de validação. |

---

## Síntese para o Plano de Evolução (Eixo D)

Prioridades: (1) migração para `pytest` com fixtures e cobertura; (2) testes de integração Texto→GPT→Vocoder→Áudio com golden datasets; (3) CI com bloqueio de merge.

Detalhamento: [`plano_evolucao/`](../plano_evolucao/) e [`snippets/`](../snippets/).
