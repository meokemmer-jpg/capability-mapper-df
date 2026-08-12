# capability-mapper-df

Generated Dark Factory template.

## Source Gap

- Gap ID: `tmp-heylou-contrarian-missing-capability-map`
- Priority: `medium`
- Source DF: `.tmp_heylou_contrarian`
- Evidence: `/Users/make/Projects/dark-factories/.tmp_heylou_contrarian/config.yaml`
- Reason: DF config does not declare capabilities; need capability mapping support.

## Run

```bash
python src/engine.py
```

## Test

```bash
python -m pytest
```

## GitHub Workflow

The included workflow runs tests on pushes and pull requests.
