import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generate as g  # noqa: E402


def test_spec_arg_refreshes_snapshot(tmp_path, monkeypatch):
    incoming = tmp_path / "fresh.json"
    incoming.write_text(json.dumps({"openapi": "3.1.0", "paths": {}}))
    snapshot = tmp_path / "openapi.json"
    monkeypatch.setattr(g, "SPEC", snapshot)

    args = g.parse_args(["--spec", str(incoming)])
    resolved = g.resolve_spec(args)

    assert resolved == snapshot
    assert json.loads(snapshot.read_text())["openapi"] == "3.1.0"


def test_no_patch_spec_symbol():
    # The vestigial patcher is removed entirely.
    assert not hasattr(g, "patch_spec")
