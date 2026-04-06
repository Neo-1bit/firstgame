# Beta Checklist

## Beta acceptance bar
A build is Beta-ready when all of the following are true:

- [ ] The game launches reliably from source with `python -m src.main`
- [ ] The packaged Linux build is smoke tested on the main target machine
- [x] Title, play, pause, restart, game over, and quit flows all behave cleanly
- [x] Best score saving works across relaunches
- [x] No open high-severity gameplay or startup bugs remain
- [x] Current speed curve is confirmed acceptable by testers
- [x] Remaining open issues are either Beta-scoped, clearly deferred, or non-blocking polish
- [ ] Release notes are ready for the next Beta-tagged build

## Beta scope guidance
### In scope
- Stability fixes
- Packaged build validation
- Speed and feel tuning
- Small visual or audio improvements only if they materially improve Beta quality
- Clear release notes and tester guidance

### Out of scope unless a tester bug demands it
- Major new game modes
- Settings menu expansion
- Challenge systems
- Theme variants
- Broad content expansion

## Current likely blockers
- Packaged Linux build still needs real target-machine smoke testing
- Release notes still need to be prepared for the Beta-tagged build

## Scope decision notes
- Audio is optional for Beta, not a Beta blocker.
- Only include audio before Beta if it can be added with very low risk and clearly improves release quality.

## Exit condition
When the checklist above is satisfied, prepare a Beta release candidate and tag it rather than continuing indefinite polish.
