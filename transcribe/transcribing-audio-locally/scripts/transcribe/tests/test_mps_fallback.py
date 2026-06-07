import sys
import os
import pytest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from transcribe import _run_with_cpu_fallback


class FakePipeline:
    """Records the device it was moved to via .to()."""
    def __init__(self):
        self.device = None

    def to(self, device):
        self.device = device


def test_mps_failure_retries_on_cpu():
    import torch
    pipeline = FakePipeline()

    def run():
        if pipeline.device.type == "mps":
            raise RuntimeError("mps boom")
        return "ok"

    result = _run_with_cpu_fallback(pipeline, torch.device("mps"), run)

    assert result == "ok"
    assert pipeline.device.type == "cpu"


def test_non_mps_failure_propagates_without_fallback():
    import torch
    pipeline = FakePipeline()
    calls = []

    def run():
        calls.append(pipeline.device.type)
        raise RuntimeError("cpu boom")

    with pytest.raises(RuntimeError, match="cpu boom"):
        _run_with_cpu_fallback(pipeline, torch.device("cpu"), run)

    assert calls == ["cpu"]  # ran once, no retry
