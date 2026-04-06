# Project Goal

## Project overview
- Project name: Snake III
- One sentence summary: A cosy steampunk-inspired snake game built in Python for desktop play.
- Problem this project solves: Create a small, approachable game project that is fast to build, fun to play, and easy for the team to extend.
- Target users: Casual gamers, beginner-friendly players, and people who enjoy retro arcade games with modern polish.

## Vision and success
- Long term vision: Turn a simple snake game into a polished little arcade experience with charm, replayability, and room for future feature expansion.
- What success looks like: Players can download and run the game easily, understand it immediately, and want to replay for a better score.
- Current status: PoC v1 is shipped and proves the core gameplay loop. The next focus is usability, persistence, and visual identity.
- Non-goals: Large open worlds, online multiplayer, complex economies, and heavy live-service features.

## Core gameplay or core experience
- Main player experience: Smooth, responsive movement while collecting items, growing longer, and surviving for as long as possible.
- Core loop: Start run, collect mechanical apples or energy pickups, grow longer, avoid collisions, beat your high score, restart.
- Key features: Keyboard controls, clear GUI, score tracking, game over and restart loop, steampunk visual identity.
- Unique selling points: A warm steampunk presentation, cosy tone, and a clean desktop-first implementation instead of a generic clone.

## Scope
- Must have for v1: GUI for the game, a working Snake-like game, score display, restart flow, game over state, and basic visual polish.
- Completed in PoC v1: Playable loop, score tracking, restart flow, game over state, local setup instructions, and initial steampunk presentation.
- Next for PoC v2: Persistent high score saving, title screen, pause state, feel tuning, and stronger visual polish.
- Nice to have: Sound effects, speed ramping, particle effects, alternate boards.
- Out of scope for now: Online multiplayer, account systems, in-game purchases, mobile launch, procedural campaigns.

## Platform and delivery
- Target platform(s): Python on Linux and Windows.
- Input method(s): Keyboard.
- Distribution plan: GitHub releases and source distribution.
- Performance expectations: Instant startup, stable frame rate on normal desktop hardware, low memory usage.

## Art and audio direction
- Visual style: Steampunk with brass, copper, pipes, gauges, and warm mechanical details.
- Audio style: Soft mechanical clicks, clockwork-inspired effects, and cosy background music.
- Mood and tone: Cosy, friendly, lightly whimsical.
- Reference inspirations: Classic 80s snake, modern minimalist arcade games, light steampunk illustration.

## Technical direction
- Engine / framework: Python with Pygame.
- Programming language(s): Python 3.
- Tools and services: GitHub, Git, Pygame, simple art and audio tools.
- Technical constraints: Keep setup simple, avoid unnecessary dependencies, and favor code readability.

## Team and roles
- Team members: Developer team, project owner, and Neo assisting with planning and structure.
- Responsibilities: Define scope clearly, implement in small steps, document decisions, and test often.
- Decision maker: Project owner.
- Communication norms: Short updates, clear tasks, and written decisions inside the repo.

## Development plan
- Milestones: Planning, PoC v1 release, PoC v2 polish pass, MVP candidate, release preparation.
- First prototype goal: A playable snake game with movement, food spawning, growth, collision detection, and scoring.
- Current milestone: PoC v2, focused on persistence, UX flow, visual polish, and release readiness.
- Risks: Scope creep, overdesign too early, inconsistent art direction, and underestimating polish work.
- Dependencies: Python 3, Pygame, local development environment, and GitHub repo workflow.

## Product requirements
- Player stories / user stories: As a player, I want to start the game quickly, control the snake smoothly, understand my score, and restart without friction.
- Acceptance criteria: The game launches locally, accepts keyboard input, spawns pickups, grows the snake, detects collisions, ends runs correctly, and displays score clearly.
- MVP definition: A polished single-player desktop snake game with a steampunk theme and stable core loop.

## Business and project context
- Timeline target: First playable as soon as possible, then iterative polish.
- Budget constraints: Low-cost project using accessible tools and mostly lightweight assets.
- Monetization plan: None for MVP, optional future premium or free release decision later.
- Legal or licensing concerns: Use properly licensed assets, fonts, and audio, or create originals.

## Open questions
- Question 1: Should the snake theme stay purely classic or add steampunk gadgets and power-ups in v1.1?
- Question 2: Should high scores be local-only or prepared for online sharing later?
- Question 3: How much animation polish is worth doing before first release?

## Change log
- 2026-04-06: Initial draft created and aligned to Snake III.
- 2026-04-06: Updated after PoC v1 release with clearer v2 priorities.
