# Game Design

## High concept
- Game title: Snake III
- Genre: Arcade, casual, retro-inspired desktop game.
- Elevator pitch: A cosy steampunk reimagining of Snake, where players guide a mechanical serpent through a polished arcade experience.
- Intended audience: Casual players, retro fans, and beginner gamers.

## Player fantasy
- What the player should feel: In control, relaxed, focused, and just a little proud when surviving tight turns.
- What makes the experience satisfying: Clean movement, visible growth, rising tension, and the reward of beating a previous score.
- Current build status: The core loop now includes a title screen, pause state, persistent best score saving, HUD polish, and gentle speed ramping. Beta-phase feedback should focus on stability, feel, presentation, and release value.
- Why players will come back: Short sessions, easy restarts, mastery through repetition, persistent best score, and future room for modifiers or challenge modes.

## Core gameplay loop
1. Start a run and guide the mechanical snake around the board.
2. Collect pickups to grow longer and increase score.
3. Avoid walls and self-collision, then restart and try to beat the last run.

## Game pillars
- Pillar 1: Responsive and readable gameplay.
- Pillar 2: Small scope with polished presentation.
- Pillar 3: A cosy steampunk identity that gives the project personality.

## Core mechanics
- Movement: Grid-based directional movement controlled by keyboard.
- Interaction: Collect pickups, avoid obstacles, and navigate increasing space pressure.
- Combat / challenge: No direct combat, challenge comes from positioning, speed, and self-management.
- Progression: Score increases during a run, with local persistent high score tracking already implemented.
- Rewards: Score growth, survival time, visual feedback, and completion satisfaction.

## Systems
- Player systems: Input handling, movement queue, snake body growth, collision detection.
- Enemy / obstacle systems: Walls by default, optional future hazards.
- Economy / resources: Score as the main tracked resource.
- Level or world systems: Single contained arena for MVP, with room for alternate boards later.
- Save / progression systems: Local high score storage is implemented in `.local/high_score.json`. Future work could expand this into richer local stats or challenge tracking.

## Game modes
- Main mode: Classic endless score attack.
- Secondary modes: Potential timed mode, obstacle mode, or challenge mode later.
- Multiplayer / single-player notes: Single-player only for MVP.

## Level and content design
- Setting: A brass-and-copper mechanical playfield with a clean readable grid.
- Level structure: One compact arena designed for quick sessions.
- Difficulty curve: Starts calm, becomes tenser as the snake grows and optional speed increases.
- Content types: Pickups, UI states, menus, and possible later hazards.

## UX and controls
- Input scheme: Arrow keys or WASD.
- HUD / UI needs: Score display, high score area, title screen, pause state, and game over message.
- Current PoC status: Gameplay HUD, title screen, pause flow, game over state, and restart loop all exist in the current build.
- Accessibility considerations: High-contrast mode later, readable fonts, clear game state prompts, and simple controls.

## Art and audio notes
- Art direction: Soft steampunk visuals with readable shapes, warm metal colors, and subtle decorative details.
- Animation needs: Snake movement, pickup feedback, simple transitions, and a satisfying game over state.
- Music direction: Light looping background music with a calm arcade feel.
- Sound effect direction: Mechanical ticks, soft collection sounds, and gentle failure feedback.

## Narrative
- Story premise: A clockwork serpent moves through a tiny mechanical world collecting energy cores.
- Worldbuilding notes: The setting should feel playful and compact, more like a crafted toybox than a deep lore universe.
- Characters: The snake is the main character through motion and style.
- Dialogue needs: None required for MVP.

## Monetization and retention
- Monetization approach: None for MVP.
- Replayability hooks: Score chasing, better control mastery, and future modifiers.
- Progression hooks: High score improvement and optional unlockable cosmetic touches later.

## Risks and unknowns
- Risk 1: Overcomplicating the first version instead of shipping a strong classic core.
- Risk 2: Making the art direction too ambitious for a small initial release.
- Risk 3: Adding systems before controls and feel are solid.

## Prototype goals
- What the first playable must prove: That the controls feel good, the loop is fun, and the game is stable enough to build on.
- PoC v1 result: Core loop validated, local run path documented, and release published.
- PoC v2 goal: Make the experience feel like a small complete game rather than just a functional prototype.
- Current Beta-sprint baseline: The project is now in a tester-friendly state with cleaner UX flow, packaged-build guidance, and smoke-tested core interactions.
- How success will be measured: Quick local setup, smooth play, no major bugs in the core loop, and positive team reaction to the feel.

## Change log
- 2026-04-06: Initial Snake III design draft created.
- 2026-04-06: Updated after PoC v1 to clarify UX and replay priorities for PoC v2.
- 2026-04-06: Updated after PoC v2 review push to reflect implemented systems and current review goals.
- 2026-04-06: Updated for Beta sprint kickoff and release-candidate evaluation.
