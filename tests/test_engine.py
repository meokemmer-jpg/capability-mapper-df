import importlib.util
import pathlib


def load_engine_module():
    root = pathlib.Path(__file__).resolve().parents[1]
    engine_path = root / "src" / "engine.py"
    spec = importlib.util.spec_from_file_location("engine", engine_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_engine_discovers_at_least_one_gap():
    module = load_engine_module()
    engine = module.DarkFactoryEngine()
    findings = engine.discover()

    assert isinstance(findings, list)
    assert findings
    assert "gap_id" in findings[0]


def test_main_returns_success():
    module = load_engine_module()

    assert module.main() == 0
