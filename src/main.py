try:
    from snakeiii.game import main
except ModuleNotFoundError:
    from src.snakeiii.game import main


if __name__ == "__main__":
    raise SystemExit(main())
