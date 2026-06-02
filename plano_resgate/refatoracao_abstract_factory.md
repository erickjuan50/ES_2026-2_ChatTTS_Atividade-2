# Refatoração conceitual — Abstract Factory

## Gargalo identificado

| Item | Detalhe |
| :--- | :--- |
| **Local** | `ChatTTS/core.py`, classe `Chat` |
| **Sintoma** | Download de pesos, alocação GPU/CPU e orquestração `infer()` no mesmo módulo |
| **Anti-padrão** | God Object |
| **Princípio violado** | OCP/SOLID — novo vocoder ou backend exige editar o núcleo |

## Arquitetura atual (resumo)

```
Chat (core.py)
 ├── download_models() / _load()
 ├── gpt, dvae, decoder, vocos, tokenizer (concretos)
 └── infer() → _refine_text → _infer_code → _decode_to_wavs
```

## Proposta — Abstract Factory

Separar **montagem** de **inferência**. O `Chat` recebe uma fábrica que entrega um pipeline pronto.

```python
# Exemplo conceitual — não faz parte do upstream ChatTTS
from abc import ABC, abstractmethod
from typing import Protocol

class InferencePipeline(Protocol):
    def refine_text(self, text: list[str], params) -> list[str]: ...
    def synthesize(self, text: list[str], params) -> list: ...

class PipelineFactory(ABC):
    @abstractmethod
    def create_pipeline(self) -> InferencePipeline: ...

class LocalWeightsFactory(PipelineFactory):
    """Pesos locais + sha256 — cenário atual do ChatTTS."""
    def create_pipeline(self) -> InferencePipeline:
        ...

class HuggingFaceSnapshotFactory(PipelineFactory):
    """Carregamento via snapshot_download — cenário HF."""
    def create_pipeline(self) -> InferencePipeline:
        ...

class Chat:
    def __init__(self, factory: PipelineFactory):
        self._factory = factory
        self._pipeline = None

    def load(self, **kwargs) -> bool:
        self._pipeline = self._factory.create_pipeline()
        return self._pipeline.warmup(**kwargs)

    def infer(self, text, **kwargs):
        return self._pipeline.synthesize(text, **kwargs)
```

## Impacto esperado

- `Chat` deixa de instanciar `GPT`, `DVAE`, `Vocos` diretamente.
- Novos ambientes (teste leve vs. produção) = nova fábrica, sem alterar `infer()`.
- Testes unitários podem injetar pipeline mock.

## Evidência do problema (upstream)

https://github.com/2noise/ChatTTS/blob/main/ChatTTS/core.py — métodos `load`, `_load`, `infer`.

Diagramas: [`diagrama_arquitetura_atual.mmd`](diagrama_arquitetura_atual.mmd), [`diagrama_arquitetura_proposta.mmd`](diagrama_arquitetura_proposta.mmd).
