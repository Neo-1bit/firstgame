# Release Checklist

## Smoke test scope
- [x] Game launches from `python -m src.main`
- [x] Title screen appears before the first run starts
- [x] `Space` starts a run from the title screen
- [x] Direction keys can launch a run directly from the title screen
- [x] Movement keys steer during gameplay
- [x] `P` pauses and resumes during an active run
- [x] Movement input is ignored while paused
- [x] `R` restarts cleanly from idle, running, paused, or game-over states
- [x] Wall collision triggers game over cleanly
- [x] Self collision logic remains intact in code path
- [x] `Esc` quits the game cleanly
- [x] Best score persists across launches via `.local/high_score.json`

## Release readiness notes
- Current build is suitable for the next internal review.
- Highest-value remaining work before a wider release is feel tuning, packaging, and optional audio.
- No open blocking UX gaps remain in the current core loop.

## Follow-up candidates
- Review pacing and decide whether speed ramping is needed before release.
- Add a lightweight packaging path for Linux and Windows.
- Add sound effects if presentation needs a stronger sense of feedback.
