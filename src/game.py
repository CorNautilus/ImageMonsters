import pygame

from .constants import SCREEN_HEIGHT, SCREEN_WIDTH
from .TestScene import TestScene


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Image Viewer - Pygame")
        clock = pygame.time.Clock()
        font = pygame.font.SysFont(None, 24)
        title_font = pygame.font.SysFont(None, 32)

        self.scene = TestScene(self.screen, clock, font, title_font)

    def run(self) -> None:
        self.scene.run()
        pygame.quit()
