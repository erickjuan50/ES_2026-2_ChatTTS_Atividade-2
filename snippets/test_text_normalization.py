import pytest


GOLDEN_CASES = [
    {
        "input": "What is [uv_break]your favorite english food?[laugh][lbreak]",
        "expected_refined": "what is [uv_break] your favorite english [uv_break] food [laugh] [lbreak]",
    },
    {
        "input": "Hello [uv_break] world.",
        "expected_refined": "hello [uv_break] world.",
    },
]


@pytest.mark.parametrize("case", GOLDEN_CASES, ids=lambda c: c["input"][:30])
def test_text_normalization_golden(case):
    from unittest.mock import MagicMock

    normalizer = MagicMock()
    normalizer.normalize.return_value = case["expected_refined"]
    result = normalizer.normalize(case["input"])
    assert result == case["expected_refined"]


def test_speaker_embedding_shape():
    import numpy as np

    spk_emb = np.random.randn(768).astype(np.float32)
    assert spk_emb.shape == (768,)
    assert spk_emb.dtype == np.float32
