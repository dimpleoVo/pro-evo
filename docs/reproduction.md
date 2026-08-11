# Reproduction

Use Python 3.10+ and pytest. From the repository root run `python -m pytest -q` and `python examples/evidence-replay/run.py`. Both operations are deterministic and offline. They neither read private paths nor make Provider calls. The Replay verifies the numbers reported in the README from the immutable public JSON projection.
