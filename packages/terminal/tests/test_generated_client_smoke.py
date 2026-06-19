import importlib
from pathlib import Path

GEN = Path(__file__).resolve().parent.parent / "src" / "apt_terminal" / "generated"


def test_generated_dir_exists():
    assert (GEN / "client.py").exists(), "run scripts/generate.py first"


def test_generated_client_imports():
    mod = importlib.import_module("apt_terminal.generated.client")
    assert hasattr(mod, "Client") or hasattr(mod, "AuthenticatedClient")
