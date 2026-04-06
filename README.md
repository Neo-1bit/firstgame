# Snake III

A cosy steampunk snake game built in Python.

## Overview
`Snake III` is a modern take on the classic snake formula. The goal is to build a small, polished desktop game with a friendly steampunk presentation, smooth controls, and enough charm to feel handcrafted rather than generic.

## Vision
The project starts with a clean, fun single-player snake game for Linux and Windows, then leaves room for later additions like power-ups, special boards, score challenges, and visual polish.

## Current goals
- Move the project from PoC review build to Beta readiness
- Stabilize the packaged build and tester experience
- Address the highest-value quality and polish gaps
- Keep the code simple and maintainable while preparing the next release

## Project documents
- `project_goal.md` - project vision, scope, and success criteria
- `game_design.md` - gameplay systems, mechanics, and player experience
- `task_board.md` - current tasks, priorities, and progress tracking
- `tech_stack.md` - technical choices, tools, and architecture notes

## Repository structure
- `src/` - game source code
- `assets/` - images, sounds, fonts, and art source files
- `docs/` - setup, packaging, review, and release documentation

## Getting started
1. Review `project_goal.md`
2. Review `game_design.md`
3. Check `tech_stack.md`
4. Use `task_board.md` to drive work

## Installation and run
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m src.main
```

If `venv` is missing on Debian or Ubuntu, install it with:

```bash
sudo apt install -y python3.12-venv python3-pip
```

For more setup notes, see `docs/setup.md`.

For packaging notes, see `docs/packaging.md`.
For review guidance, see `docs/review_notes.md` and `docs/changelog.md`.

## Save data
- Best score is saved locally in `.local/high_score.json`
- Save data is created automatically after setting a score

## Controls
- `Space` to start from the title screen
- Arrow keys or `WASD` to move
- `P` to pause or resume during a run
- `R` to restart
- `Esc` to quit

## MVP target
A playable desktop game where the player controls a snake, collects items, grows longer, avoids collisions, and can restart easily after game over.

## Status
`v0.2.0` is out as the PoC v2 review build. The next sprint is aimed at Beta readiness: stable tester experience, packaged-build confidence, selective polish, and issue-driven quality improvements toward the next release.
