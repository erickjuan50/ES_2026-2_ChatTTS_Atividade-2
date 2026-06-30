# Eixo B — Qualidade Técnica dos Testes

---

## 1. Nomenclatura e comportamento observável

| Verificação | Referência upstream |
| :--- | :--- |
| Arquivos descritivos | Ausentes: `test_inference.py`, `test_speaker_generation.py` |
| Funções `test_*` | Scripts executados como `python tests/#511.py` |
| README documenta suíte | Não |

**Evidência:** `evidencias/eixo_b_nomenclatura_tests.html` · **Risco:** Alto

---

## 2. Isolamento, independência e reprodutibilidade

| Verificação | Referência |
| :--- | :--- |
| Carregamento de modelos | `tests/#511.py` linha 18: `chat.load(source="huggingface")` |
| Dependências | `requirements.txt`: torch, transformers, numpy |
| Seed fixa | Parcial em `#655.py` (`manual_seed=12345`) |
| Container/Docker | Ausente |

**Evidência:** `evidencias/eixo_b_isolamento_ambiente.html` · **Risco:** Alto

---

## 3. Mocks, stubs e fixtures

| Verificação | Resultado |
| :--- | :--- |
| `fixtures/`, `mock/`, `conftest.py` | Não encontrados |
| Uso de `unittest.mock` | Não nos scripts existentes |

**Evidência:** `evidencias/eixo_b_ausencia_mocks.html` · **Risco:** Alto

---

## 4. Validação de regras de negócio

| Fluxo | Cobertura |
| :--- | :--- |
| Geração de voz | Parcial — `#511.py` verifica `wav is not None` |
| Emoção / pausas / locutor | Ausente |
| Normalização | Parcial — `#655.py` compara string exata |

**Evidência:** `evidencias/eixo_b_regras_negocio.html` · **Risco:** Alto

---

## 5. Redundância e fragilidade

| Fator | Impacto |
| :--- | :--- |
| GPU / CUDA / PyTorch | Resultados variáveis entre ambientes |
| `testall.sh` | Executa todos os scripts sequencialmente |
| Aleatoriedade do modelo | `sample_random_speaker()` em `#511.py` |

**Evidência:** `evidencias/eixo_b_fragilidade.html` · **Risco:** Médio
