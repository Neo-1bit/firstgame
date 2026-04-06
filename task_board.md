# Task Board

## Current status
- `v0.2.0` is released as the PoC v2 review build.
- Core loop, score tracking, restart flow, title screen, pause flow, local saves, and packaging guidance are all in place.
- The new sprint goal is to move from PoC to Beta through stability, packaging confidence, and selective polish.

## In progress
- [ ] Smoke test the packaged Linux build on the main target machine
- [ ] Validate the new slower speed curve with testers

## Ready next
- [ ] Triage and fix any new tester-reported bugs
- [ ] Decide whether issue #4 should be part of the Beta scope or deferred
- [ ] Decide whether audio belongs in Beta or after Beta
- [ ] Prepare release notes for the Beta candidate
- [ ] Prepare a Beta release candidate build

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
- [x] Define the Beta release checklist and acceptance bar

## Priorities
### High
- Stable packaged build on the main target machine
- Fast triage of any release-facing bugs
- Clear Beta acceptance checklist

### Medium
- Sound effects if they materially improve Beta feel
- Better visual identity and decorative polish
- Cleaner packaging and release flow

### Low
- Alternate board themes
- Challenge modes
- Extra visual flourishes

## Suggested next sprint
- [ ] Validate the packaged build on the main target machine
- [ ] Confirm the new slower speed curve with testers
- [ ] Triage every new tester issue within the same day
- [ ] Decide on the next action for issue #4 (small visual pass or defer)
- [ ] Decide whether sound belongs in the Beta target
- [ ] Prepare release notes and a Beta release candidate if no major bugs remain

## Notes
- Keep tasks small and implementation-ready.
- Prioritize making PoC v2 feel complete before adding larger feature scope.
- Record design changes in the relevant markdown files.
