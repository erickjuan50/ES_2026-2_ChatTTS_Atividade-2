# Eixo B — Anatomia do Código (SOLID e DRY)

Repositório de referência: branch `main` de https://github.com/2noise/ChatTTS

## 1. Teste da Troca (DIP)

ChatTTS é motor TTS local (não cliente de API OpenAI). Trocar o “motor” implica alterar, no mínimo:

- `ChatTTS/core.py` — orquestração e `load` / `infer`
- `ChatTTS/model/gpt.py`, `ChatTTS/model/dvae.py` — arquitetura neural
- `examples/cmd/run.py` ou `examples/web/webui.py` — parâmetros de uso

**Verificar:** imports concretos em `core.py` (`DVAE`, `GPT`, `Tokenizer`, …) sem interface injetável.

**Evidência:** `evidencias/eixo_b_core_imports_dip.html`

**Violação:** Dependency Inversion Principle (dependência de implementações).

---

## 2. God Object

**Classe:** `Chat` em `ChatTTS/core.py` (~25k caracteres no arquivo; maior concentração de responsabilidades).

Responsabilidades misturadas:

- Download e validação de pesos (`download_models`, `sha256_map`)
- Ciclo de vida de modelos (`_load`, `unload`, `has_loaded`)
- Pipeline de inferência (`infer`, `_refine_text`, `_infer_code`, `_decode_to_wavs`)

**Evidência:** `evidencias/eixo_b_core_god_object.html`

**Violação:** Single Responsibility Principle.

---

## 3. DRY

Comparar lógica repetida entre `_refine_text` e `_infer_code` em `core.py` (ambas usam `gen_logits`, tokenização, ramos vLLM vs. geração local).

**Nota:** O relatório da equipe também analisou duplicação em versões com `ChatTTS/infer/api.py`; na branch `main` atual essa pasta não existe — a duplicação está nos métodos privados de `core.py`.

**Evidência:** `evidencias/eixo_b_dry_refine_infer.html`
