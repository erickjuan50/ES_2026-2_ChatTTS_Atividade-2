import pytest
import numpy as np
from unittest.mock import MagicMock


@pytest.fixture
def mock_chat():
    chat = MagicMock()
    chat.infer.return_value = [np.zeros(24000, dtype=np.float32)]
    chat.load.return_value = None
    return chat


def test_generate_audio_from_text_returns_wav_array(mock_chat):
    chat = mock_chat
    chat.load(compile=False, source="local")
    wavs = chat.infer(["Hello world."], skip_refine_text=True)
    assert len(wavs) == 1
    assert wavs[0] is not None
    assert len(wavs[0]) > 0


def test_infer_output_is_float32_array(mock_chat):
    chat = mock_chat
    chat.load()
    wavs = chat.infer(["Test."])
    assert wavs[0].dtype == np.float32


def test_output_audio_file_can_be_written(mock_chat, tmp_path):
    wav = np.zeros(24000, dtype=np.float32)
    out_path = tmp_path / "output.wav"
    import wave

    with wave.open(str(out_path), "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)
        wf.writeframes((wav * 32767).astype(np.int16).tobytes())
    assert out_path.exists()
    assert out_path.stat().st_size > 0
