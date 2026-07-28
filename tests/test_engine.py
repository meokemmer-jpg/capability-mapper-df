from pathlib import Path

from src.engine import run


def test_engine_writes_report(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    source = tmp_path / "dfs"
    source.mkdir()
    log = tmp_path / "spawned-dfs-log.jsonl"

    assert run(source, log) == 0
    assert (tmp_path / "artifacts" / "report.json").exists()
    assert log.exists()
    assert 'capability-mapper-df' in log.read_text(encoding="utf-8")
