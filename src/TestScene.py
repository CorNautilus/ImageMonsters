import os
import pygame

from . import assets
from .constants import FPS
from .ui import draw_button, draw_panel, draw_text, fill_background


class TestScene:
    def __init__(self, screen: pygame.Surface, clock: pygame.time.Clock, font: pygame.font.Font, title_font: pygame.font.Font) -> None:
        self.screen = screen
        self.clock = clock
        self.font = font
        self.title_font = title_font

        self.images = self._load_assets_images()
        self.current_index = 0 if self.images else -1

        self.buttons = [
            {"text": "前へ", "rect": pygame.Rect(40, 520, 120, 44)},
            {"text": "次へ", "rect": pygame.Rect(180, 520, 120, 44)},
        ]

    def _load_assets_images(self) -> list[pygame.Surface]:
        loaded: list[pygame.Surface] = []
        assets_dir = os.path.join("assets")
        max_size = (860, 400)  # パネル内に収まるようにする最大サイズ
        if not os.path.isdir(assets_dir):
            return loaded
        for fname in sorted(os.listdir(assets_dir)):
            if fname.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
                path = os.path.join(assets_dir, fname)
                loaded.append(assets.load_image(path, max_size))
        return loaded

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

            fill_background(self.screen)
            self._draw_layout(mouse_pos, mouse_down)

            pygame.display.flip()
            self.clock.tick(FPS)

    def _draw_layout(self, mouse_pos: tuple[int, int], mouse_down: bool) -> None:
        draw_text(self.screen, "assets 内の画像ビューア", (30, 20), self.title_font)

        viewer_panel = pygame.Rect(30, 60, 900, 440)
        draw_panel(self.screen, viewer_panel)

        if self.current_index >= 0 and self.images:
            image = self.images[self.current_index]
            img_rect = image.get_rect(center=viewer_panel.center)
            self.screen.blit(image, img_rect)
            draw_text(
                self.screen,
                f"{self.current_index + 1} / {len(self.images)}",
                (viewer_panel.x + 12, viewer_panel.y + 12),
                self.font,
            )
        else:
            draw_text(self.screen, "assets フォルダに画像がありません", viewer_panel.center, self.font)

        for idx, btn in enumerate(self.buttons):
            clicked = draw_button(
                self.screen,
                btn["rect"],
                btn["text"],
                self.font,
                mouse_pos,
                mouse_down,
            )
            if clicked and self.images:
                if idx == 0:
                    self.current_index = (self.current_index - 1) % len(self.images)
                else:
                    self.current_index = (self.current_index + 1) % len(self.images)
