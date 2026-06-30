import pytest
from pipeline_factory import (
    Chat,
    LocalWeightsFactory,
    HuggingFaceSnapshotFactory,
)


def test_local_factory_creates_pipeline_without_heavy_load():
    chat = Chat(LocalWeightsFactory())
    chat.load()
    result = chat.infer(["sample text"])
    assert result is not None
    assert len(result) == 1


def test_huggingface_factory_returns_distinct_pipeline():
    local = Chat(LocalWeightsFactory())
    hf = Chat(HuggingFaceSnapshotFactory())
    local.load()
    hf.load()
    local_out = local.infer(["text"])
    hf_out = hf.infer(["text"])
    assert len(local_out[0]) != len(hf_out[0])


def test_infer_raises_when_not_loaded():
    chat = Chat(LocalWeightsFactory())
    with pytest.raises(RuntimeError, match="not loaded"):
        chat.infer(["text"])
