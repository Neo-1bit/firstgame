# Packaging

This project uses a lightweight packaging path for internal review builds.

## Recommended tool
- PyInstaller

## One-file local build
Create and activate a virtual environment first, then install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install pyinstaller
```

Build the game:

```bash
pyinstaller --noconfirm --onefile --windowed --name snakeiii src/main.py
```

Output will be created in:
- `dist/snakeiii`

Build artifacts and temporary files:
- `build/`
- `dist/`
- `snakeiii.spec`

## Linux notes
- Build on the same Linux family you plan to test on when possible.
- If the executable fails on another machine, prefer shipping source plus setup instructions until packaging is stabilized.

## Windows notes
- Build on Windows for the most reliable Windows executable.
- Cross-building from Linux is not the recommended path for this project.

## Release prep checklist
- Confirm the game launches from the packaged executable.
- Confirm title screen, pause, restart, quit, and score saving still work.
- Remove old build artifacts before creating a fresh review build.
