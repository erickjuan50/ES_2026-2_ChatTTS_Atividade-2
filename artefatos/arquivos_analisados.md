# Arquivos e URLs analisados — A2

## Repositório upstream

Base: https://github.com/2noise/ChatTTS (branch `main`)

### Gestão (Eixo A)

- https://github.com/2noise/ChatTTS/issues/704
- https://github.com/2noise/ChatTTS/releases
- https://github.com/2noise/ChatTTS/graphs/contributors
- https://github.com/2noise/ChatTTS/blob/main/README.md

### Código e arquitetura (Eixos B e C)

- https://github.com/2noise/ChatTTS/blob/main/ChatTTS/core.py
- https://github.com/2noise/ChatTTS/blob/main/ChatTTS/model/gpt.py
- https://github.com/2noise/ChatTTS/blob/main/ChatTTS/model/dvae.py
- https://github.com/2noise/ChatTTS/blob/main/ChatTTS/model/tokenizer.py
- https://github.com/2noise/ChatTTS/blob/main/ChatTTS/model/__init__.py
- https://github.com/2noise/ChatTTS/blob/main/ChatTTS/norm.py

### CI (Eixo A.3)

- https://github.com/2noise/ChatTTS/blob/main/.github/workflows/unitest.yml
- https://github.com/2noise/ChatTTS/blob/main/tests/testall.sh
- https://github.com/2noise/ChatTTS/blob/main/tests/%23655.py

### Exemplos (contexto DIP)

- https://github.com/2noise/ChatTTS/tree/main/examples

## Nota sobre `ChatTTS/infer/api.py`

O relatório PDF da equipe referencia `ChatTTS/infer/api.py` para duplicação DRY. Na branch `main` atual essa pasta **não existe**; a lógica equivalente está nos métodos `_refine_text` e `_infer_code` de `core.py`. A auditoria deste repositório usa o código vigente no GitHub.
