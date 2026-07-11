from pathlib import Path

from src.engine import Engine


def test_engine_generates_discovery_report(tmp_path: Path) -> None:
    source_df = tmp_path / "source-df"
    source_df.mkdir()

    result = Engine(tmp_path / "artifacts").run(
        source_df,
        {"gap_type": "missing-capabilities-config", "missing_capability": "capability-mapper"},
    )

    assert result.status == "completed"
    assert result.capability == "capability-mapper"
    assert len(result.artifacts) == 1
    assert Path(result.artifacts[0]).exists()
