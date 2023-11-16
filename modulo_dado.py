# modulo_dado.py
import pygame
import random

class ModuloDado:
    def __init__(self, rect, font, button_text='Roll', button_color=(0, 0, 0), text_color=(255, 255, 255), rectContainer=None):
        """
        Constructor de la clase ModuloDado.

        Parámetros:
            rectContainer (pygame.Rect, opcional): Rectángulo que define la posición y tamaño del contenedor del dado.
        """
        self.rect = rect
        self.font = font
        self.button_text = button_text
        self.button_color = button_color
        self.text_color = text_color
        self.results = [(1, 3), (1, 1), (0, 2), (1, 3), (1, 1), (2, 0)]
        self.current_result = (1, 1)  # Resultado inicial por defecto

        # Configurar el contenedor con un valor predeterminado si no se proporciona
        if rectContainer is None:
            # Alineado a la izquierda del rect y centrado verticalmente, con tamaños 280x300
            container_x = 500
            container_y = 10
            self.rectContainer = pygame.Rect(container_x + 20, container_y, 270, 300)
        else:
            self.rectContainer = rectContainer

    def roll(self):
        """
        Lanza el dado seleccionando un resultado aleatorio de la lista de resultados posibles.

        Retorna:
            tuple: El resultado de la tirada del dado.
        """
        self.current_result = random.choice(self.results)
        return self.current_result

    def draw(self, screen):
        """
        Dibuja el botón del dado en la pantalla, incluyendo el resultado actual.

        Parámetros:
            screen (pygame.Surface): La superficie de Pygame donde se dibujará el botón.
        """
        # Define colors and measurements
        button_color = (255, 200, 200)  # Un color rojo claro para el botón
        border_color = (255, 0, 0)  # Color rojo para el borde
        border_radius = 10  # Radio para las esquinas redondeadas
        top_text_color = (0, 0, 255)  # Color azul para el texto superior
        bottom_text_color = (255, 0, 0)  # Color rojo para el texto inferior
        padding = 5  # Relleno para el borde

        # Primero dibuja el contenedor
        container_color = (200, 200, 200)  # Por ejemplo, gris claro
        pygame.draw.rect(screen, container_color, self.rectContainer, border_radius=border_radius)


        # Dibuja el botón con esquinas redondeadas
        inner_rect = pygame.Rect(self.rect.x + padding, self.rect.y + padding,
                                 self.rect.width - 2 * padding, self.rect.height - 2 * padding)
        pygame.draw.rect(screen, button_color, inner_rect, border_radius=border_radius)
        
        # Ajusta el rectángulo del borde
        border_rect = self.rect.inflate(-2 * padding, -2 * padding)

        # Dibuja el borde
        pygame.draw.rect(screen, border_color, border_rect, border_radius=border_radius, width=2)
        
        # Renderiza el texto del resultado del dado
        result_top = self.font.render(str(self.current_result[0]), True, top_text_color)
        result_bottom = self.font.render(str(self.current_result[1]), True, bottom_text_color)

        # Calcula las posiciones para el texto
        top_text_pos = (self.rect.x + self.rect.width // 2 - result_top.get_width() // 2,
                        self.rect.y + self.rect.height // 4 - result_top.get_height() // 2)
        bottom_text_pos = (self.rect.x + self.rect.width // 2 - result_bottom.get_width() // 2,
                           self.rect.y + 3 * self.rect.height // 4 - result_bottom.get_height() // 2)

        # Dibuja el texto sobre el botón
        screen.blit(result_top, top_text_pos)
        screen.blit(result_bottom, bottom_text_pos)
