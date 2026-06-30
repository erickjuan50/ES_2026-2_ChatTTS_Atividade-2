# Eixo C — Lacunas, Riscos e Falhas Potenciais

Conexão com auditorias anteriores: requisitos A1 (Ascend NPU, fallback normalizer, `cache_dir`) e God Object em `core.py` (A2).

---

## 1. Funcionalidades críticas sem testes

| Funcionalidade | Risco associado |
| :--- | :--- |
| Inferência de voz | Geração incorreta de áudio |
| Controle de emoção | Perda de expressividade |
| Controle de pausas | Fala artificial |
| Seleção de locutor | Inconsistência de voz |
| Geração multi-locutor | Troca indevida de falantes |
| Download de modelos | Falhas de inicialização |
| Compatibilidade GPU/CPU | Erros em produção |

**Evidência:** `evidencias/eixo_c_funcionalidades_sem_testes.html` · **Risco:** Alto

---

## 2. Módulos de maior risco

| Módulo | Motivo |
| :--- | :--- |
| `ChatTTS/core.py` | Orquestração de inferência (~750 linhas) |
| `tools/normalizer.py` | Correções recorrentes em releases |
| `requirements.txt` | Dependências voláteis (NumPy 2, Transformers) |

**Evidência:** `evidencias/eixo_c_modulos_risco.html` · **Risco:** Alto

---

## 3. Dependências externas sem isolamento

- PyTorch, Transformers, Hugging Face, modelos pré-treinados
- `chat.load(source="huggingface")` em testes existentes

**Evidência:** `evidencias/eixo_c_dependencias_externas.html` · **Risco:** Alto

---

## 4. Proteção contra regressões

| Aspecto | Status |
| :--- | :--- |
| CI em push/PR | Presente |
| Scripts por issue | 3 arquivos |
| Golden tests | Ausente |
| Validação de áudio | Ausente |
| Regressões em releases | Documentadas |

**Evidência:** `evidencias/eixo_c_regressoes.html` · **Risco:** Alto

---

## 5. Detecção de bugs severos

Resposta esperada: **parcial**.

**Evidência:** `evidencias/eixo_c_deteccao_bugs.html` · **Risco:** Médio-alto
