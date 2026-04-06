# Tech Stack

## Technical goals
- Development speed: Fast iteration with a simple local setup.
- Maintainability: Clear Python project structure and readable code.
- Performance target: Smooth gameplay at a stable frame rate on ordinary desktop hardware.
- Deployment target: Easy local run during development, later packaged for Linux and Windows.

## Core stack
- Engine / framework: Pygame.
- Language: Python 3.12 or close stable Python 3 version available in the environment.
- Rendering approach: 2D desktop window rendering with a fixed board grid.
- Physics approach: Grid-based logic, no heavy physics engine.
- UI approach: Lightweight in-game menus and HUD built directly in Pygame.

## Tooling
- Version control: Git and GitHub.
- Project management: Markdown planning files in the repo.
- Art tools: Lightweight pixel or illustration tools, depending on asset style.
- Audio tools: Simple royalty-free sourcing or basic editing tools.
- Build tools: Python virtual environment, pip, and a lightweight PyInstaller packaging path for review builds.
- Testing tools: Manual playtesting first, optional pytest for logic modules later.

## Repository standards
- Branching strategy: Start simple on main while the team is tiny, move to feature branches if parallel work increases.
- Commit style: Small commits with clear action-oriented messages.
- Code review expectations: Review gameplay logic, file structure, and user-facing behavior before merging larger changes.
- Definition of done: Code runs locally, docs updated if needed, and no obvious regression in the core loop.

## Architecture notes
- Project structure: `src/` for code, `assets/` for media, `docs/` for supporting documentation.
- Main modules: Entry point, game loop, input, board state, snake movement, pickups, scoring, UI overlays, and local save handling.
- Data flow: Main loop updates input, updates game state, then renders frame.
- State management: Simple in-code state flow for title, playing, paused, and game over states.
- Asset pipeline: Keep source assets organized and use optimized runtime assets as needed.

## Platforms
- Primary platform: Linux desktop.
- Secondary platform(s): Windows desktop.
- Input support: Keyboard, with arrow keys and WASD.
- Resolution / performance notes: Start with a fixed window size and scale cleanly if needed later.

## Services and integrations
- Analytics: None.
- Cloud saves: None.
- Backend needs: None.
- Third-party SDKs: Avoid unless there is a clear reason.

## Security and reliability
- Secrets handling: No secrets should live in the repo.
- Backup strategy: GitHub as primary remote backup plus local commits.
- Dependency update approach: Keep dependencies minimal and pin versions when the build stabilizes.
- Error logging: Console logging during development, lightweight file logging only if needed later.

## Open decisions
- Decision 1: Exact Python version to standardize for the team.
- Decision 2: Whether to include packaged builds directly in the next broader tester release.
- Decision 3: Whether to add audio before the next wider release.

## Change log
- 2026-04-06: Initial Snake III technical stack draft created.
- 2026-04-06: Updated after PoC v2 review push to reflect implemented UI flow, local saves, and packaging path.
