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
- `v0.2.0` established a solid PoC v2 baseline for the Beta sprint.
- Pacing now uses a slower Beta-tuned speed curve, pending tester confirmation.
- Highest-value remaining work before a Beta candidate is packaged-build validation, optional audio, and any final art polish that clearly improves release quality.
- No open blocking UX gaps remain in the current core loop.

## Follow-up candidates
- Smoke test the packaged Linux build on the main target machine.
- Confirm the slower Beta speed curve with testers.
- Use `docs/review_notes.md`, `docs/beta_checklist.md`, and `docs/changelog.md` when preparing the Beta candidate.
