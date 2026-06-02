# Diagnóstico consolidado — A2 Auditoria Forense ChatTTS

Formato por item: **Evidência** → **Diagnóstico** → **Risco**

Repositório analisado: https://github.com/2noise/ChatTTS (branch `main`)

---

## Eixo A — O Pulso da Gestão (GPR)

### A.1 Arqueologia de Issues — #704

| Campo | Conteúdo |
| :--- | :--- |
| **Evidência** | [Issue #704](https://github.com/2noise/ChatTTS/issues/704); print `evidencias/eixo_a_issue_704.html` |
| **Diagnóstico** | Funcionalidade avançada (load customizado + embeddings `.pt`). Aberta por LivinLuo1993 (20/08/2024). Escopo evoluiu de falha em `chat.load()` para inconsistência na identidade vocal no pipeline. Documentação rica na issue, mas rastreabilidade fraca para PR/milestone; labels `documentation` e `stale`. |
| **Risco** | **Alto** |

### A.2 Gestão de riscos ocultos

| Campo | Conteúdo |
| :--- | :--- |
| **Evidência** | README (avisos TransformerEngine/FlashAttention-2); [releases](https://github.com/2noise/ChatTTS/releases); ausência de `SECURITY.md`; `evidencias/eixo_a_readme_riscos_dependencias.html` |
| **Diagnóstico** | Dívida técnica visível em avisos e histórico de correções (inferência, Transformers, streaming). Poucos TODO/FIXME no código; risco concentrado em dependências voláteis (PyTorch, HF). Sem fallback/circuit breaker formal. |
| **Risco** | **Médio-alto** |

### A.3 Ritmo de entrega e code review

| Campo | Conteúdo |
| :--- | :--- |
| **Evidência** | [Contributors](https://github.com/2noise/ChatTTS/graphs/contributors); PRs; `unitest.yml` — `evidencias/eixo_a_ci_unitest.html` |
| **Diagnóstico** | Cadência semi-regular com picos perto de releases. CI reduz risco, mas revisão humana nem sempre documentada nos PRs. |
| **Risco** | **Médio** |

---

## Eixo B — Anatomia do Código (SOLID e DRY)

### B.1 Teste da troca (DIP)

| Campo | Conteúdo |
| :--- | :--- |
| **Evidência** | `ChatTTS/core.py` imports de `DVAE`, `GPT`, … — `evidencias/eixo_b_core_imports_dip.html` |
| **Diagnóstico** | ChatTTS é o motor TTS, não um cliente de API. Troca de backend exige alterar `core.py`, `model/gpt.py`, `model/dvae.py` e exemplos. Classe `Chat` depende de implementações concretas. |
| **Risco** | **Alto** (acoplamento estrutural) |

### B.2 God Object

| Campo | Conteúdo |
| :--- | :--- |
| **Evidência** | `ChatTTS/core.py` — `evidencias/eixo_b_core_god_object.html` |
| **Diagnóstico** | `Chat` agrega download/I/O, `_load` de redes neurais e orquestração `infer`. Violação do SRP e do OCP para novos vocoders/backends. |
| **Risco** | **Alto** |

### B.3 DRY

| Campo | Conteúdo |
| :--- | :--- |
| **Evidência** | `_refine_text` e `_infer_code` em `core.py` — `evidencias/eixo_b_dry_refine_infer.html` |
| **Diagnóstico** | Loops de geração, `gen_logits`, ramos vLLM e `gpt.generate` repetidos entre refinamento textual e inferência de código. |
| **Risco** | **Alto** (manutenção) |

---

## Eixo C — Padrões de Projeto (GoF)

### C.1 Criacionais

| Campo | Conteúdo |
| :--- | :--- |
| **Evidência** | `chat.load()` / `_load` — `evidencias/eixo_c_load_factory.html` |
| **Diagnóstico** | Sem Singleton; Factory Method informal via `load`. Múltiplas instâncias de `Chat` podem recarregar modelos. |
| **Risco** | **Médio** |

### C.2 Estruturais

| Campo | Conteúdo |
| :--- | :--- |
| **Evidência** | `infer()` — `evidencias/eixo_c_facade_infer.html` |
| **Diagnóstico** | **Facade** predominante; módulos em `ChatTTS/model/`. Sem arquitetura multiagente. |
| **Risco** | **Baixo** |

### C.3 Comportamentais

| Campo | Conteúdo |
| :--- | :--- |
| **Evidência** | `RefineTextParams`, `InferCodeParams` — `evidencias/eixo_c_params_strategy.html` |
| **Diagnóstico** | Pipeline sequencial (Chain); Strategy apenas por parametrização, não por algoritmos substituíveis (continuidade da A1). |
| **Risco** | **Médio-baixo** |

---

## Síntese para o Plano de Resgate

Principais riscos arquiteturais: acoplamento em `core.py`, validação de saída de áudio não isolada (herança A1), extensão de vocoders/backends difícil.

Proposta da equipe: Abstract Factory para montagem de pipeline + três ações GPR (nível G MPS.BR) em [`plano_resgate/`](../plano_resgate/).
