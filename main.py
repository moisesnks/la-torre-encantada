import pygame
import config
from modulo_grafo import ModuloGrafo
from modulo_dado import ModuloDado
from game_display import GameDisplay
from game_manager import GameManager

import pygame
from montecarlo import AnalizadorMonteCarlo
from game_display import GameDisplay
from game_manager import GameManager

def prompt_for_iterations(screen, font):
    """
    Solicita al usuario el número de iteraciones del juego.

    Args:
        screen (pygame.Surface): Superficie de Pygame donde se mostrará el prompt.
        font (pygame.font.Font): Fuente para renderizar el texto.

    Returns:
        int: Número de iteraciones ingresado por el usuario.
    """
    running = True
    input_string = ''
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    input_string = input_string[:-1]
                else:
                    input_string += event.unicode

        screen.fill(config.COLOR_BACKGROUND)
        prompt_text = "Ingrese el número de iteraciones y presione ENTER:"
        text_surface = font.render(prompt_text, True, config.COLOR_TEXT_DEFAULT)
        screen.blit(text_surface, (50, 50))
        input_surface = font.render(input_string, True, config.COLOR_TEXT_DEFAULT)
        screen.blit(input_surface, (50, 100))
        pygame.display.flip()

    try:
        return int(input_string)
    except ValueError:
        return 1

def main():
    """
    Función principal que inicia y ejecuta el juego.
    """
    pygame.init()
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    pygame.display.set_caption("La Torre Encantada")
    font = pygame.font.Font(None, config.FONT_SIZE)

    n_iterations = prompt_for_iterations(screen, font)

    grafo = ModuloGrafo(pygame.Rect(config.RECT_GRAFO_X, config.RECT_GRAFO_Y, config.RECT_GRAFO_WIDTH, config.RECT_GRAFO_HEIGHT))
    dado = ModuloDado(pygame.Rect(config.RECT_DADO_X, config.RECT_DADO_Y, config.RECT_DADO_WIDTH, config.RECT_DADO_HEIGHT), font)
    display = GameDisplay(screen, font, 1 / (n_iterations * 100))

    game_manager = GameManager(grafo, dado, display, 1 / (n_iterations), n_iterations)

    heroe_wins_history = []  # Lista para el seguimiento de las victorias del héroe
    bruja_wins_history = []  # Lista para el seguimiento de las victorias de la bruja

    for iteration in range(1, n_iterations + 1):
        game_manager.run_game(iteration, heroe_wins_history, bruja_wins_history)
        
        # Dibuja las estadísticas en cada iteración
        game_manager.draw_stats()

    text_to_display = "Juego terminado. Presiona 'Esc' para salir o 'S' para modo estadístico."
    text_surface = font.render(text_to_display, True, config.COLOR_TEXT_DEFAULT)
    text_rect = text_surface.get_rect(center=(config.WIDTH // 2, config.HEIGHT - 50))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

    waiting_for_exit = True
    while waiting_for_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                elif event.key == pygame.K_s:  # Listening for 'S' key for stat mode
                    analizador = AnalizadorMonteCarlo('output/game_log.csv')
                    analizador.analizar_y_graficar()

if __name__ == "__main__":
    main()
