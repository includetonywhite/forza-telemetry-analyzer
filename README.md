# Forza Telemetry Analyzer
![CI](https://github.com/includetonywhite/forza-telemetry-analyzer/actions/workflows/ci.yml/badge.svg)

Forza Horizon 6 UDP telemetry. Data path Xbox -> UDP -> parsed 324 byte packet -> store a run in csv. Parser and CSV recorder made. Identification, ET + Shift and live UI not made yet.

## Requirements

- Python 3.13
- [uv](https://docs.astral.sh/uv/)
- Forza Horizon 6 Data Out on UDP 5300 (Xbox on the same network)

## Quick start

```bash
uv sync --all-groups
uv run pytest
uv run python -m forza_telemetry_analyzer.receiver
```

## Current status
- [x] packet parser (synthetic `struct` round-trip only; no Xbox capture in git)
- [ ] Docker
- [x] GitHub Actions
- [ ] vehicle identification from a run
- [ ] ET + shift points
- [ ] live UI

## Non-goals (v1)
* JS framework, ML, Pacejka, turbo transients
* accounts, cloud, mobile

## Development
```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy --strict src tests
uv run pytest
```

## License
unlicensed personal project
