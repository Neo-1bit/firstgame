# Review Notes

## Build summary
This Beta-sprint baseline focuses on making Snake III feel like a small complete game rather than a raw prototype.

## What changed since v0.1.0
- Added persistent local high score saving
- Added a proper title screen and cleaner start flow
- Added pause and resume support
- Improved HUD clarity and state-specific messaging
- Improved title, pause, and game-over overlays
- Tightened restart behavior for edge cases
- Added gentle score-based speed ramping
- Added smoke-test and packaging documentation

## What to test during review
- Launch flow from title screen
- Starting with `Space`
- Starting directly with movement keys
- General movement feel and readability
- Pause and resume behavior with `P`
- Restart behavior with `R` from all states
- Game over clarity and restart loop
- High score persistence across relaunch
- Whether speed ramping feels good or too aggressive

## Questions for Beta feedback
- Does the game now feel stable and complete enough for a Beta candidate?
- Does the new slower speed curve feel right?
- Does the HUD communicate state clearly enough?
- Is more visual polish needed before the next release?
- Should sound be part of Beta, or wait until after Beta?

## Recommended next moves during Beta
- Validate the packaged build on the target platform
- Confirm the new slower speed curve with testers
- Decide whether to invest in more visual polish before the Beta candidate
