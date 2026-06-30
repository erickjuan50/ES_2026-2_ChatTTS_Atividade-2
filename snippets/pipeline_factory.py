from abc import ABC, abstractmethod
from typing import Protocol
from unittest.mock import MagicMock


class InferencePipeline(Protocol):
    def refine_text(self, text: list[str], params) -> list[str]: ...
    def synthesize(self, text: list[str], params) -> list: ...


class PipelineFactory(ABC):
    @abstractmethod
    def create_pipeline(self) -> InferencePipeline: ...


class LocalWeightsFactory(PipelineFactory):
    def create_pipeline(self) -> InferencePipeline:
        pipeline = MagicMock()
        pipeline.refine_text.return_value = ["local refined"]
        pipeline.synthesize.return_value = [b"\x00" * 1024]
        return pipeline


class HuggingFaceSnapshotFactory(PipelineFactory):
    def create_pipeline(self) -> InferencePipeline:
        pipeline = MagicMock()
        pipeline.refine_text.return_value = ["hf refined"]
        pipeline.synthesize.return_value = [b"\x00" * 2048]
        return pipeline


class Chat:
    def __init__(self, factory: PipelineFactory):
        self._factory = factory
        self._pipeline = None

    def load(self):
        self._pipeline = self._factory.create_pipeline()

    def infer(self, text: list[str], params=None):
        if self._pipeline is None:
            raise RuntimeError("not loaded")
        refined = self._pipeline.refine_text(text, params)
        return self._pipeline.synthesize(refined, params)
