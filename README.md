# Patterns of the World

Patterns of the World is an AI multi-agent simulation framework mapping contemporary socio-economic events to deep historical structural dynamics. Powered by Meta Muse models through Baseten and Modal serverless compute, it models actor incentives, explores scenario variations, and automatically backtests its own explanations.

## Status

This repository currently contains the initial scaffold:

- `baseten_test.py` — a minimal smoke test for the Baseten-hosted model.
- `assets/` — reference images for the project.

The multi-agent simulation framework is still under development and is not yet implemented in this repository. This README will be updated as components land.

## Quick start

1. Create a virtual environment and install dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Copy `.env.example` to `.env` and fill in the Baseten values.

3. Run the smoke test:

   ```bash
   python baseten_test.py
   ```

The expected output is a short greeting from the model. The `.env` file is git-ignored and must never be committed.
