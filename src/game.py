import pygame

from .constants import SCREEN_HEIGHT, SCREEN_WIDTH
from .Scene.Title import TitleScene
from .Scene.Test import TestScene


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Image Viewer - Pygame")
        clock = pygame.time.Clock()

        # 日本語表示に対応したフォントを優先して取得（見つからなければデフォルト）
        jp_font_candidates = [
            "meiryo",
            "ms gothic",
            "msgothic",
            "yu gothic",
            "ms pgothic",
            "ms ui gothic",
            "arial unicode ms",
        ]
        font = pygame.font.SysFont(jp_font_candidates, 24)
        title_font = pygame.font.SysFont(jp_font_candidates, 32)

        self.scene = TitleScene(
            self.screen,
            clock,
            font,
            title_font,
            on_game=self._on_game,
            on_ai=self._on_ai,
        )
        self._clock = clock
        self._font = font
        self._title_font = title_font

    def run(self) -> None:
        self.scene.run()
        pygame.quit()

    def _on_game(self) -> None:
        print("hello game")

    def _on_ai(self) -> None:
        print("hello AI")
        # AIテストシーンに遷移
        scene = TestScene(self.screen, self._clock, self._font, self._title_font)
        scene.run()
