# Arquivos e URLs analisados — A3

## Repositório upstream

Base: https://github.com/2noise/ChatTTS (branch `main`)

### Estratégia de testes (Eixo A)

- https://github.com/2noise/ChatTTS/tree/main/tests
- https://github.com/2noise/ChatTTS/blob/main/tests/testall.sh
- https://github.com/2noise/ChatTTS/blob/main/.github/workflows/unitest.yml

### Scripts de teste existentes (Eixos B e C)

- https://github.com/2noise/ChatTTS/blob/main/tests/%23511.py
- https://github.com/2noise/ChatTTS/blob/main/tests/%23588.py
- https://github.com/2noise/ChatTTS/blob/main/tests/%23655.py

### Módulos críticos (Eixo C)

- https://github.com/2noise/ChatTTS/blob/main/ChatTTS/core.py
- https://github.com/2noise/ChatTTS/blob/main/requirements.txt
- https://github.com/2noise/ChatTTS/releases

### Normalização (Eixo B/C)

- https://github.com/2noise/ChatTTS/blob/main/tools/normalizer.py

## Itens verificados como ausentes no upstream

- `conftest.py`, `pytest.ini`, `fixtures/`, `mock/`
- Arquivos `test_*.py` com nomenclatura padrão
- Relatório de cobertura no CI
- Testes dedicados para emoção, pausas, multi-locutor, download de modelos

## Conexão A1/A2

- A1: métricas de validação de áudio, `cache_dir`, fallback normalizer
- A2: God Object em `core.py`, proposta `PipelineFactory` — alvo dos snippets em `snippets/`
