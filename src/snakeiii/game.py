from __future__ import annotations

import json
import random
from dataclasses import dataclass
from pathlib import Path

import pygame

CELL_SIZE = 24
GRID_WIDTH = 24
GRID_HEIGHT = 18
HUD_HEIGHT = 72
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE + HUD_HEIGHT
FPS = 10
BACKGROUND = (23, 20, 18)
PANEL = (42, 35, 28)
GRID_LINE = (58, 48, 37)
BRASS = (181, 136, 71)
COPPER = (184, 92, 56)
STEAM = (214, 205, 184)
ACCENT = (116, 171, 120)
TEXT = (236, 229, 214)
GAME_OVER = (160, 60, 50)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

KEY_TO_DIRECTION = {
    pygame.K_UP: UP,
    pygame.K_w: UP,
    pygame.K_DOWN: DOWN,
    pygame.K_s: DOWN,
    pygame.K_LEFT: LEFT,
    pygame.K_a: LEFT,
    pygame.K_RIGHT: RIGHT,
    pygame.K_d: RIGHT,
}

SAVE_DIR = Path(__file__).resolve().parents[2] / ".local"
SAVE_FILE = SAVE_DIR / "high_score.json"


@dataclass
class GameState:
    snake: list[tuple[int, int]]
    direction: tuple[int, int]
    next_direction: tuple[int, int]
    food: tuple[int, int]
    score: int
    best_score: int
    game_over: bool
    started: bool


def load_best_score() -> int:
    try:
        data = json.loads(SAVE_FILE.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return 0
    except (json.JSONDecodeError, OSError, TypeError):
        return 0

    value = data.get("best_score", 0)
    return value if isinstance(value, int) and value >= 0 else 0


def save_best_score(best_score: int) -> None:
    SAVE_DIR.mkdir(parents=True, exist_ok=True)
    SAVE_FILE.write_text(json.dumps({"best_score": best_score}, indent=2) + "\n", encoding="utf-8")


def spawn_food(snake: list[tuple[int, int]]) -> tuple[int, int]:
    free_cells = [
        (x, y)
        for x in range(GRID_WIDTH)
        for y in range(GRID_HEIGHT)
        if (x, y) not in snake
    ]
    return random.choice(free_cells)


def reset(best_score: int) -> GameState:
    start_x = GRID_WIDTH // 2
    start_y = GRID_HEIGHT // 2
    snake = [
        (start_x, start_y),
        (start_x - 1, start_y),
        (start_x - 2, start_y),
    ]
    return GameState(
        snake=snake,
        direction=RIGHT,
        next_direction=RIGHT,
        food=spawn_food(snake),
        score=0,
        best_score=best_score,
        game_over=False,
        started=False,
    )


def is_opposite(a: tuple[int, int], b: tuple[int, int]) -> bool:
    return a[0] == -b[0] and a[1] == -b[1]


def update(state: GameState) -> GameState:
    if state.game_over or not state.started:
        return state

    if not is_opposite(state.direction, state.next_direction):
        state.direction = state.next_direction

    head_x, head_y = state.snake[0]
    dx, dy = state.direction
    new_head = (head_x + dx, head_y + dy)

    hit_wall = not (0 <= new_head[0] < GRID_WIDTH and 0 <= new_head[1] < GRID_HEIGHT)
    hit_self = new_head in state.snake[:-1]

    if hit_wall or hit_self:
        state.game_over = True
        previous_best = state.best_score
        state.best_score = max(state.best_score, state.score)
        if state.best_score > previous_best:
            save_best_score(state.best_score)
        return state

    state.snake.insert(0, new_head)

    if new_head == state.food:
        state.score += 1
        previous_best = state.best_score
        state.best_score = max(state.best_score, state.score)
        if state.best_score > previous_best:
            save_best_score(state.best_score)
        if len(state.snake) < GRID_WIDTH * GRID_HEIGHT:
            state.food = spawn_food(state.snake)
    else:
        state.snake.pop()

    return state


def draw_grid(screen: pygame.Surface) -> None:
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            rect = pygame.Rect(x * CELL_SIZE, HUD_HEIGHT + y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, PANEL, rect, border_radius=4)
            pygame.draw.rect(screen, GRID_LINE, rect, 1, border_radius=4)


def draw_snake(screen: pygame.Surface, snake: list[tuple[int, int]]) -> None:
    for index, (x, y) in enumerate(snake):
        inset = 3 if index else 2
        color = ACCENT if index else BRASS
        rect = pygame.Rect(
            x * CELL_SIZE + inset,
            HUD_HEIGHT + y * CELL_SIZE + inset,
            CELL_SIZE - inset * 2,
            CELL_SIZE - inset * 2,
        )
        pygame.draw.rect(screen, color, rect, border_radius=6)
        if index == 0:
            eye_y = rect.y + rect.height // 3
            pygame.draw.circle(screen, BACKGROUND, (rect.x + rect.width // 3, eye_y), 2)
            pygame.draw.circle(screen, BACKGROUND, (rect.x + rect.width * 2 // 3, eye_y), 2)


def draw_food(screen: pygame.Surface, food: tuple[int, int]) -> None:
    x, y = food
    center_x = x * CELL_SIZE + CELL_SIZE // 2
    center_y = HUD_HEIGHT + y * CELL_SIZE + CELL_SIZE // 2
    pygame.draw.circle(screen, COPPER, (center_x, center_y), CELL_SIZE // 3)
    pygame.draw.circle(screen, STEAM, (center_x - 3, center_y - 3), CELL_SIZE // 10)
    pygame.draw.line(screen, ACCENT, (center_x, center_y - 9), (center_x + 4, center_y - 14), 2)


def draw_hud(screen: pygame.Surface, font: pygame.font.Font, state: GameState) -> None:
    panel = pygame.Rect(0, 0, WINDOW_WIDTH, HUD_HEIGHT)
    pygame.draw.rect(screen, PANEL, panel)
    pygame.draw.line(screen, BRASS, (0, HUD_HEIGHT - 1), (WINDOW_WIDTH, HUD_HEIGHT - 1), 2)

    title = font.render("Snake III", True, BRASS)
    score = font.render(f"Score: {state.score}", True, TEXT)
    best = font.render(f"Best: {state.best_score}", True, TEXT)
    if state.started:
        help_label = "Arrows / WASD to move, R to restart, Esc to quit"
    else:
        help_label = "Press Space to start, arrows / WASD to queue direction, Esc to quit"
    help_text = font.render(help_label, True, STEAM)

    screen.blit(title, (16, 10))
    screen.blit(score, (16, 38))
    screen.blit(best, (160, 38))
    screen.blit(help_text, (320, 38))


def draw_overlay(screen: pygame.Surface, title_font: pygame.font.Font, body_font: pygame.font.Font, state: GameState) -> None:
    if not state.game_over and state.started:
        return

    overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
    overlay.fill((10, 10, 10, 150 if not state.started else 130))
    screen.blit(overlay, (0, 0))

    center_x = WINDOW_WIDTH // 2
    center_y = WINDOW_HEIGHT // 2

    if not state.started:
        title = title_font.render("Snake III", True, BRASS)
        subtitle = body_font.render("A cosy clockwork arcade run", True, STEAM)
        prompt = body_font.render("Press Space to start the mechanism", True, TEXT)
        controls = body_font.render("Move with arrows or WASD", True, TEXT)
        best = body_font.render(f"Stored best score: {state.best_score}", True, ACCENT)

        screen.blit(title, title.get_rect(center=(center_x, center_y - 54)))
        screen.blit(subtitle, subtitle.get_rect(center=(center_x, center_y - 18)))
        screen.blit(prompt, prompt.get_rect(center=(center_x, center_y + 26)))
        screen.blit(controls, controls.get_rect(center=(center_x, center_y + 58)))
        screen.blit(best, best.get_rect(center=(center_x, center_y + 96)))
        return

    title = title_font.render("Boiler pressure lost", True, GAME_OVER)
    subtitle = body_font.render("Press R to restart the mechanism", True, TEXT)
    score = body_font.render(f"Final score: {state.score}", True, STEAM)

    screen.blit(title, title.get_rect(center=(center_x, center_y - 20)))
    screen.blit(score, score.get_rect(center=(center_x, center_y + 12)))
    screen.blit(subtitle, subtitle.get_rect(center=(center_x, center_y + 42)))


def main() -> int:
    pygame.init()
    pygame.display.set_caption("Snake III")
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    hud_font = pygame.font.SysFont("arial", 22)
    title_font = pygame.font.SysFont("arial", 34, bold=True)
    body_font = pygame.font.SysFont("arial", 24)

    state = reset(best_score=load_best_score())
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    state = reset(best_score=state.best_score)
                elif event.key == pygame.K_SPACE and not state.started:
                    state.started = True
                elif event.key in KEY_TO_DIRECTION:
                    state.next_direction = KEY_TO_DIRECTION[event.key]
                    if not state.started:
                        state.started = True

        state = update(state)

        screen.fill(BACKGROUND)
        draw_hud(screen, hud_font, state)
        draw_grid(screen)
        draw_food(screen, state.food)
        draw_snake(screen, state.snake)
        draw_overlay(screen, title_font, body_font, state)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    return 0
