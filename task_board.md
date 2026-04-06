# Task Board

## Current status
- The current review build is pushed to GitHub.
- Core loop, score tracking, restart flow, title screen, pause flow, local saves, and packaging guidance are all in place.
- Current focus is tester feedback, packaged-build verification, and issue-driven follow-up.

## In progress
- [ ] Smoke test the packaged Linux build on the main target machine
- [ ] Collect tester feedback on speed and feel

## Ready next
- [ ] Triage and fix any new tester-reported bugs
- [ ] Decide whether issue #7 needs speed retuning or difficulty options
- [ ] Decide whether issue #4 should be part of the next release or deferred
- [ ] Prepare a broader release candidate build if bug intake stays low

## Backlog
- [ ] Add sound effects and basic music
- [ ] Add stronger steampunk visual polish
- [ ] Package a cleaner downloadable build
- [ ] Add alternate board themes or challenge modes

## Done
- [x] Create repository
- [x] Add project planning files
- [x] Define initial game concept as Snake III
- [x] Draft README and planning structure
- [x] Create Python project entry point
- [x] Set up virtual environment instructions
- [x] Implement snake movement system
- [x] Implement pickup spawning
- [x] Implement growth and score tracking
- [x] Implement wall and self-collision detection
- [x] Implement gameplay HUD
- [x] Implement game over state and restart flow
- [x] Ship playable PoC v1
- [x] Add GitHub issue and PR templates
- [x] Add persistent local high score saving
- [x] Add a proper title screen / start state
- [x] Add pause and resume controls
- [x] Complete a release-ready smoke test pass
- [x] Improve restart flow and edge-case handling
- [x] Review movement speed and pacing
- [x] Add gentle score-based speed ramping
- [x] Prepare a lightweight packaging path
- [x] Assemble review notes for the next internal playtest
- [x] Prepare a small changelog for review
- [x] Create a real packaged Linux review build

## Priorities
### High
- Smoke test the packaged Linux build on the main target machine
- Triage tester feedback quickly
- Fix any release-facing bugs found during review

### Medium
- Sound effects
- Better visual identity and decorative polish
- Cleaner packaging and release flow

### Low
- Alternate board themes
- Challenge modes
- Extra visual flourishes

## Suggested next sprint
- [ ] Validate the packaged build on the main target machine
- [ ] Triage every new tester issue within the same day
- [ ] Decide on the next action for issue #7 (retune speed, add simpler options, or defer)
- [ ] Decide on the next action for issue #4 (small visual pass or defer)
- [ ] Prepare a broader release candidate build if no major bugs remain

## Notes
- Keep tasks small and implementation-ready.
- Prioritize making PoC v2 feel complete before adding larger feature scope.
- Record design changes in the relevant markdown files.
