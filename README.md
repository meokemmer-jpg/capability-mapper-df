# capability-mapper-df

Auto-spawned Dark Factory template.

## Capability

`capability-mapper`

## Gap

__pycache__ lacks discoverable capability metadata

Evidence:

```text
missing: /Users/make/Projects/dark-factories/__pycache__/capabilities.yaml, /Users/make/Projects/dark-factories/__pycache__/capabilities.yml, /Users/make/Projects/dark-factories/__pycache__/capabilities.json, /Users/make/Projects/dark-factories/__pycache__/README.md
```

## Run

```bash
python src/engine.py --source-dir ~/Projects/dark-factories --log-path ./spawned-dfs-log.jsonl
```

## Test

```bash
python -m pytest
```
