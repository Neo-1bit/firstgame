# Snake III

A cosy steampunk snake game built in Python.

## What it is
`Snake III` is a small desktop arcade game with a warm steampunk presentation, smooth keyboard controls, and a focus on clean replayable score-chasing.

## Current status
- Current release: `v0.3.0-beta.1`
- The project is in its Beta phase
- Current focus: packaged-build confidence, issue-driven fixes, and final Beta candidate readiness

## Quick start
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m src.main
```

If `venv` is missing on Debian or Ubuntu:

```bash
sudo apt install -y python3.12-venv python3-pip
```

## Controls
- `Space` to start from the title screen
- Arrow keys or `WASD` to move
- `P` to pause or resume during a run
- `R` to restart
- `Esc` to quit

## Save data
- Best score is saved locally in `.local/high_score.json`
- Save data is created automatically after setting a score

## Main project docs
- `PROJECT.md` - merged project overview, design, and technical summary
- `task_board.md` - live work tracking and sprint status
- `docs/setup.md` - development setup details
- `docs/packaging.md` - packaging instructions
- `docs/beta_checklist.md` - Beta acceptance bar
- `docs/beta_release_notes.md` - current Beta candidate notes
- `docs/changelog.md` - change summary

## Packaging
A lightweight PyInstaller packaging path is documented in `docs/packaging.md`.

## Goal
Ship a polished, approachable single-player snake game with a charming steampunk identity and a clean desktop-first experience.
