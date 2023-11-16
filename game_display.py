# game_display.py
import time
import pygame

from config import (
    FONT_SIZE,
    COLOR_BACKGROUND,
    COLOR_TEXT_DEFAULT,
    COLOR_HERO,
    COLOR_WITCH,
    COLOR_KEY,
    COLOR_CONTAINER,
    COLOR_PROGRESS_BAR,
    COLOR_PROGRESS_BAR_BG,
)

class GameDisplay:
    """
    Clase GameDisplay para manejar la visualización de elementos en la pantalla del juego.

    Atributos:
        screen (pygame.Surface): La superficie de Pygame donde se dibujará el juego.
        font (pygame.font.Font): La fuente utilizada para renderizar texto.
        width, height (int): Dimensiones de la pantalla.
        waiting_time (float): Tiempo de espera para la visualización de mensajes.
        progress (float): Progreso actual del juego, representado en porcentaje.
        default_text_color (tuple): Color predeterminado para el texto.
        default_rect_color (tuple): Color predeterminado para los rectángulos.
        default_rect_radius (int): Radio predeterminado para los bordes redondeados de los rectángulos.
    """
    def __init__(self, screen, font, wt, default_text_color=(0, 0, 0), default_rect_color=(255, 255, 255), default_rect_radius=10):
        """
        Inicializa la instancia de GameDisplay.

        Args:
            screen (pygame.Surface): Superficie de Pygame para la pantalla del juego.
            font (pygame.font.Font): Fuente para renderizar texto.
            wt (float): Tiempo de espera para la visualización de mensajes.
            default_text_color (tuple): Color predeterminado del texto.
            default_rect_color (tuple): Color predeterminado de los rectángulos.
            default_rect_radius (int): Radio para los bordes redondeados de los rectángulos.
        """
        self.screen = screen
        self.font = font
        self.width, self.height = self.screen.get_size()
        self.waiting_time = wt
        self.progress = 0.0  # Initialize progress to 0%
        self.default_text_color = default_text_color
        self.default_rect_color = default_rect_color
        self.default_rect_radius = default_rect_radius

    def clear_screen(self):
        """
        Limpia la pantalla rellenándola con un color de fondo.
        """
        self.screen.fill((0, 0, 0))  # Clear the screen

    def update_display(self):
        """
        Actualiza la pantalla para reflejar los cambios realizados.
        """
        pygame.display.flip()

    def show_end_game_message(self, message, text_color=None, rect_color=None):
        """
        Muestra un mensaje de fin de juego en la pantalla.

        Args:
            message (str): Mensaje a mostrar.
            text_color (tuple): Color del texto. Si es None, se usa el color predeterminado.
            rect_color (tuple): Color del rectángulo de fondo. Si es None, se usa el color predeterminado.
        """
        # Set default colors if not provided
        if text_color is None:
            text_color = self.default_text_color
        if rect_color is None:
            rect_color = self.default_rect_color

        # Render the text
        text_surface = self.font.render(message, True, text_color)
        text_rect = text_surface.get_rect()

        # Calculate the dimensions of the rectangle
        rect_width = text_rect.width + 20  # Add some extra space around the text
        rect_height = text_rect.height + 20

        # Posición del rectángulo
        rect_x = 10
        rect_y = 270

        # Draw the rectangle with rounded edges
        pygame.draw.rect(self.screen, rect_color, (rect_x, rect_y, rect_width, rect_height), border_radius=self.default_rect_radius)
        self.screen.blit(text_surface, (rect_x + 10, rect_y + 10))  # Align the text inside the rectangle

        self.update_display()
        time.sleep(self.waiting_time)

    def draw_text(self, text, position, color=(0, 0, 0)):
        """
        Dibuja texto en la pantalla en una posición específica.

        Args:
            text (str): Texto a dibujar.
            position (tuple): Posición (x, y) en la pantalla para el texto.
            color (tuple): Color del texto.
        """
        text_surface = self.font.render(text, True, color)
        self.screen.blit(text_surface, position)

    def draw_circle(self, position, color, radius):
        """
        Dibuja un círculo en la pantalla.

        Args:
            position (tuple): Posición (x, y) en la pantalla para el círculo.
            color (tuple): Color del círculo.
            radius (int): Radio del círculo.
        """
        pygame.draw.circle(self.screen, color, position, radius)

    def draw_progress_bar(self, iteration, total_iterations):
        """
        Dibuja una barra de progreso en la pantalla.

        Args:
            iteration (int): Número de la iteración actual.
            total_iterations (int): Número total de iteraciones.
        """
        # Draw a green progress bar at the bottom of the screen
        bar_width = int(self.width * (iteration / total_iterations))
        progress_bar_height = 20
        progress_bar_x = 0  # Cambiar la posición X a 0 para pegarla a la izquierda
        progress_bar_y = self.height - 30

        pygame.draw.rect(self.screen, COLOR_PROGRESS_BAR_BG, (0, progress_bar_y, self.width, progress_bar_height))
        pygame.draw.rect(self.screen, COLOR_PROGRESS_BAR, (progress_bar_x, progress_bar_y, bar_width, progress_bar_height))
        self.update_display()


    def draw_info_rectangles(self, texts, text_x, text_y):
        """
        Dibuja rectángulos de información en la pantalla para una lista de textos.

        Args:
            texts (list): Lista de textos a mostrar.
            text_x (int): Posición inicial en el eje x.
            text_y (int): Posición inicial en el eje y.

        Returns:
            tuple: Posición x y y actualizada después de dibujar los textos.
        """
        extra_height = 8

        max_text_width = max(self.font.size(text)[0] for text in texts)

        for text in texts:
            text_size = self.font.size(text)
            text_rect_color = self.get_text_rect_color(text)
            pygame.draw.rect(self.screen, text_rect_color, (text_x, text_y, max_text_width, text_size[1] + extra_height))
            self.draw_text(text, (text_x, text_y), COLOR_TEXT_DEFAULT)
            text_y += 20

        return text_x, text_y

    def get_text_rect_color(self, text):
        """
        Obtiene el color del rectángulo de fondo basado en el contenido del texto.

        Args:
            text (str): Texto a evaluar.

        Returns:
            tuple: Color del rectángulo de fondo.
        """
        if "Heroe" in text:
            return COLOR_CONTAINER
        elif "Bruja" in text:
            return COLOR_CONTAINER
        elif "Llave" in text:
            return COLOR_CONTAINER
        else:
            return COLOR_CONTAINER
