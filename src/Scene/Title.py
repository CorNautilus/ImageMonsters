import pygame
from typing import Callable

from ..ui import draw_button, fill_background, draw_text
from ..constants import SCREEN_WIDTH, SCREEN_HEIGHT


class TitleScene:
    def __init__(
        self,
        screen: pygame.Surface,
        clock: pygame.time.Clock,
        font: pygame.font.Font,
        title_font: pygame.font.Font,
        on_game: Callable[[], None],
        on_ai: Callable[[], None],
    ) -> None:
        self.screen = screen
        self.clock = clock
        self.font = font
        self.title_font = title_font
        self.on_game = on_game
        self.on_ai = on_ai

        self.buttons = [
            {"text": "ゲーム", "rect": pygame.Rect(SCREEN_WIDTH // 2 - 160, 260, 140, 54)},
            {"text": "AIテスト", "rect": pygame.Rect(SCREEN_WIDTH // 2 + 20, 260, 140, 54)},
        ]

    def run(self) -> None:
        running = True
        while running:
            mouse_down = False
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_down = True
            running = self._draw(mouse_pos, mouse_down)
            pygame.display.flip()
            self.clock.tick(60)

    def _draw(self, mouse_pos: tuple[int, int], mouse_down: bool) -> bool:
        fill_background(self.screen)
        draw_text(self.screen, "ImageMonsters", (SCREEN_WIDTH // 2 - 100, 120), self.title_font)
        draw_text(self.screen, "シーン選択", (SCREEN_WIDTH // 2 - 60, 180), self.font)

        for idx, btn in enumerate(self.buttons):
            clicked = draw_button(
                self.screen,
                btn["rect"],
                btn["text"],
                self.font,
                mouse_pos,
                mouse_down,
            )
            if clicked:
                if idx == 0:
                    self.on_game()
                else:
                    self.on_ai()
                return False
        return True
