import pygame

from .constants import SCREEN_HEIGHT, SCREEN_WIDTH
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

        self.scene = TestScene(self.screen, clock, font, title_font)

    def run(self) -> None:
        self.scene.run()
        pygame.quit()
