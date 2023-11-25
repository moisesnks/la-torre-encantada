import pygame
import time
import config

class GameDisplay:
    def __init__(self, screen, font, waiting_time, default_text_color=(0, 0, 0), default_rect_color=(255, 255, 255), default_rect_radius=10):
        self.screen = screen
        self.font = font
        self.width, self.height = self.screen.get_size()
        self.waiting_time = waiting_time
        self.default_text_color = default_text_color
        self.default_rect_color = default_rect_color
        self.default_rect_radius = default_rect_radius

    def clear_screen(self):
        self.screen.fill(config.COLOR_BACKGROUND)

    def update_display(self):
        pygame.display.flip()

    def show_end_game_message(self, message, text_color=None, rect_color=None):
        if text_color is None:
            text_color = self.default_text_color
        if rect_color is None:
            rect_color = self.default_rect_color

        text_surface = self.font.render(message, True, text_color)
        text_rect = text_surface.get_rect()

        rect_width = text_rect.width + 20
        rect_height = text_rect.height + 20

        rect_x = 10
        rect_y = 270

        pygame.draw.rect(self.screen, rect_color, (rect_x, rect_y, rect_width, rect_height), border_radius=self.default_rect_radius)
        self.screen.blit(text_surface, (rect_x + 10, rect_y + 10))

        self.update_display()
        time.sleep(self.waiting_time)

    def draw_text(self, text, position, color=(0, 0, 0)):
        text_surface = self.font.render(text, True, color)
        self.screen.blit(text_surface, position)

    def draw_circle(self, position, color, radius):
        pygame.draw.circle(self.screen, color, position, radius)

    def draw_progress_bar(self, iteration, total_iterations):
        bar_width = int(self.width * (iteration / total_iterations))
        progress_bar_height = 20
        progress_bar_x = 0
        progress_bar_y = self.height - 30

        pygame.draw.rect(self.screen, config.COLOR_PROGRESS_BAR_BG, (0, progress_bar_y, self.width, progress_bar_height))
        pygame.draw.rect(self.screen, config.COLOR_PROGRESS_BAR, (progress_bar_x, progress_bar_y, bar_width, progress_bar_height))
        self.update_display()

    def draw_info_rectangles(self, texts, text_x, text_y):
        extra_height = 8
        max_text_width = max(self.font.size(text)[0] for text in texts)

        for text in texts:
            text_size = self.font.size(text)
            text_rect_color = self.get_text_rect_color(text)
            pygame.draw.rect(self.screen, text_rect_color, (text_x, text_y, max_text_width, text_size[1] + extra_height))
            self.draw_text(text, (text_x, text_y), config.COLOR_TEXT_DEFAULT)
            text_y += 20

        return text_x, text_y

    def get_text_rect_color(self, text):
        if "Heroe" in text:
            return config.COLOR_CONTAINER
        elif "Bruja" in text:
            return config.COLOR_CONTAINER
        elif "Llave" in text:
            return config.COLOR_CONTAINER
        else:
            return config.COLOR_CONTAINER
