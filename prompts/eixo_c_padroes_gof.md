# Eixo C — Padrões de Projeto (GoF)

## 1. Criacionais

| Pergunta | Onde olhar |
| :--- | :--- |
| Singleton explícito? | Busca em `ChatTTS/` — não há singleton formal |
| Factory? | `Chat.load()` / `_load` encapsulam criação de GPT, DVAE, Vocos, etc. |
| Risco | Nova instância de `Chat` pode recarregar modelos (memória) |

**Evidência:** `evidencias/eixo_c_load_factory.html`

**Risco:** Médio.

---

## 2. Estruturais

| Padrão | Evidência |
| :--- | :--- |
| **Facade** | Classe `Chat`, método `infer()` esconde GPT/DVAE/Vocos |
| **Adapter** | Parcial — integração vLLM em `model/velocity/` |
| Agentes | Não aplicável — pipeline linear, sem hierarquia multiagente |

**Evidência:** `evidencias/eixo_c_facade_infer.html`

**Risco:** Baixo.

---

## 3. Comportamentais

| Padrão | Evidência |
| :--- | :--- |
| **Chain of Responsibility** | Pipeline texto → refine → código → decode → áudio |
| **Strategy** | Parcial — `RefineTextParams` / `InferCodeParams` (dataclasses), sem algoritmos substituíveis |
| if/else massivo | Condicionais de dispositivo (MPS/NPU/CPU) e flags (`use_vllm`, `stream`) |

**Evidência:** `evidencias/eixo_c_params_strategy.html`

**Risco:** Médio-baixo.
