import pytest
from unittest.mock import MagicMock, patch


@pytest.fixture
def mock_logger():
    logger = MagicMock()
    logger.warning = MagicMock()
    return logger


@pytest.fixture
def mock_pipeline():
    pipeline = MagicMock()
    pipeline.refine_text.return_value = ["refined text"]
    pipeline.synthesize.return_value = [MagicMock()]
    return pipeline


@pytest.fixture
def sample_texts():
    return ["Hello world.", "Test sentence for TTS."]
