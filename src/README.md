# Source Directory

This folder contains the current Python source code for Snake III.

## Current structure
- `main.py` - application entry point
- `snakeiii/game.py` - main game loop, input handling, rendering, state flow, and save logic
- `snakeiii/__init__.py` - package marker

## Current implementation notes
The current source includes:
- title screen flow
- active gameplay loop
- pause and game-over states
- persistent local high score saving
- HUD and overlay presentation logic
- gentle score-based speed ramping

If the codebase grows, this folder can later split into dedicated gameplay, UI, and utility modules.
