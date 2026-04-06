# PROJECT

## Overview
- Project name: Snake III
- Summary: A cosy steampunk-inspired snake game built in Python for desktop play.
- Genre: Arcade, casual, retro-inspired desktop game.
- Audience: Casual players, retro fans, and beginner gamers.

## Vision
Snake III aims to turn a simple snake game into a polished little arcade experience with charm, replayability, and a warm handcrafted feel.

## Current status
- `v0.2.0` established the PoC v2 review baseline.
- `v0.3.0-beta.1` is the current Beta release.
- The project now includes persistent highscores, title flow, pause support, HUD and overlay polish, calmer Beta speed tuning, packaging guidance, and Beta release documentation.

## Core experience
- Start a run quickly
- Control the snake smoothly with keyboard input
- Collect pickups to grow and score
- Avoid walls and self-collision
- Restart cleanly and chase a better score

## Game pillars
1. Responsive and readable gameplay
2. Small scope with polished presentation
3. A cosy steampunk identity that gives the project personality

## Implemented systems
- Grid-based movement with queued direction changes
- Pickup spawning and score tracking
- Wall and self-collision detection
- Title, playing, paused, and game-over flow
- Persistent local high score saving in `.local/high_score.json`
- HUD and overlay presentation
- Gentle Beta-tuned speed curve

## Current Beta scope
### In scope
- Stability fixes
- Packaged-build validation
- Speed and feel tuning
- Small visual improvements that clearly help readability or release quality
- Release notes and tester guidance

### Out of scope unless bug-driven
- Major new modes or challenge systems
- Large settings-menu expansion
- Broad content expansion
- Theme variants

## Visual and audio direction
- Visual style: brass, copper, pipes, gauges, and warm mechanical details
- Mood: cosy, friendly, lightly whimsical
- Audio direction: soft mechanical clicks and calm arcade ambience
- Audio status: optional for Beta, not Beta-blocking

## Technical notes
- Language: Python 3
- Framework: Pygame
- Target platforms: Linux and Windows
- Packaging path: lightweight PyInstaller flow documented in `docs/packaging.md`
- Runtime source entrypoint: `python -m src.main`

## Beta success bar
A Beta candidate is ready when:
- packaged Linux build passes smoke testing on the target machine
- no high-severity startup or gameplay bugs remain
- current speed curve is accepted by testers
- remaining open issues are non-blocking or explicitly deferred
- release notes are ready for the next tag

## Main docs
- `README.md` - user-facing overview and run instructions
- `PROJECT.md` - merged project vision, design, and technical summary
- `task_board.md` - live planning and sprint tracking
- `docs/` - setup, packaging, Beta checklist, release notes, and changelog
