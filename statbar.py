# statbar.py
import pygame
from pygame.sprite import Sprite

# Class to represent real-time statistics bars
class StatBar(Sprite):
    """
    Clase para representar barras de estadísticas en tiempo real en juegos con Pygame.

    Atributos:
        max_value (int): El valor máximo que la barra puede representar.
        value (int): El valor actual de la barra.
        color (tuple): Color de la barra en formato RGB.
        image (pygame.Surface): Superficie de Pygame para la barra.
        rect (pygame.Rect): Rectángulo que define la posición y dimensiones de la barra.
    """
    def __init__(self, x, y, width, height, max_value, color):
        """
        Inicializa la barra de estadísticas con la posición, tamaño, valor máximo y color.

        Args:
            x (int): Posición en el eje X.
            y (int): Posición en el eje Y.
            width (int): Ancho de la barra.
            height (int): Altura de la barra.
            max_value (int): Valor máximo representable por la barra.
            color (tuple): Color de la barra en formato RGB.
        """
        super().__init__()
        self.max_value = max_value
        self.value = 0
        self.color = color
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 255))  # White background
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update_bar(self):
        """
        Actualiza la longitud de la barra en función de los valores actual y máximo.
        """
        # Calcula la altura de la barra como una fracción del alto total del rectángulo
        bar_height = int(self.value / 100 * self.rect.height)  # Se asume que self.value es un porcentaje

        # Limpia la barra actual (para evitar el sobre dibujado)
        self.image.fill((255, 255, 255))  # Fondo blanco (o el color de fondo deseado)

        # Dibuja la nueva barra
        pygame.draw.rect(self.image, self.color, (0, self.rect.height - bar_height, self.rect.width, bar_height))

    def draw(self, screen):
        """
        Dibuja la barra en una pantalla dada.

        Args:
            screen (pygame.Surface): La superficie de Pygame donde se dibujará la barra.
        """
        self.update_bar()
        screen.blit(self.image, self.rect)


# Class to represent statistics text
class StatText(Sprite):
    """
    Clase para representar texto de estadísticas en juegos con Pygame.

    Atributos:
        font (pygame.font.Font): Fuente del texto.
        text_color (tuple): Color del texto en formato RGB.
        text (str): El texto a mostrar.
        image (pygame.Surface): Superficie de Pygame para el texto.
        rect (pygame.Rect): Rectángulo que define la posición y dimensiones del texto.
        x (int): Posición en el eje X.
        y (int): Posición en el eje Y.
    """
    def __init__(self, x, y, font, text_color):
        """
        Inicializa el objeto de texto de estadísticas con la posición, fuente y color del texto.

        Args:
            x (int): Posición en el eje X.
            y (int): Posición en el eje Y.
            font (pygame.font.Font): Fuente del texto.
            text_color (tuple): Color del texto en formato RGB.
        """
        super().__init__()
        self.font = font
        self.text_color = text_color
        self.text = ""
        self.image = None
        self.rect = None
        self.x = x
        self.y = y

    def set_text(self, text):
        """
        Establece el texto a mostrar.

        Args:
            text (str): El texto a mostrar.
        """
        self.text = text
        self.image = self.font.render(self.text, True, self.text_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        """
        Dibuja el texto en una pantalla dada.

        Args:
            screen (pygame.Surface): La superficie de Pygame donde se dibujará el texto.
        """
        screen.blit(self.image, self.rect)
