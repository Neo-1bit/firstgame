# Beta Release Notes

## Snake III Beta Candidate

This Beta candidate builds on the `v0.2.0` PoC v2 review release and focuses on turning the project into a stable, tester-friendly desktop game.

## Highlights
- Persistent local high score saving
- Title screen and cleaner start flow
- Pause and resume support
- HUD and overlay polish
- Calmer Beta-tuned speed curve
- Restart-flow and source-run compatibility fixes
- Lightweight packaging path and release documentation
- Beta visual polish pass for stronger board presentation and readability

## Tester-facing notes
- Source run path: `python -m src.main`
- Local save file: `.local/high_score.json`
- Controls:
  - `Space` to start
  - `WASD` or arrow keys to move
  - `P` to pause/resume
  - `R` to restart
  - `Esc` to quit

## Known Beta expectations
- Packaged Linux build should still be smoke tested on the main target machine before tagging the final Beta release.
- Audio remains optional and is not a Beta blocker.

## Beta acceptance summary
The Beta candidate is intended to ship once:
- packaged-build validation passes on the target machine
- no new high-severity bugs are reported
- release notes are finalized and attached to the tag
