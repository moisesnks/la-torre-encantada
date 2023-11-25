import pygame
import os
import config
from modulo_grafo import ModuloGrafo
from modulo_dado import ModuloDado
from game_display import GameDisplay
from game_manager import GameManager
from game_logger import GameLogger
import time
import pandas as pd

import pygame
from montecarlo import AnalizadorMonteCarlo
from game_display import GameDisplay
from game_manager import GameManager


def combinar_csvs(archivos_csv, archivo_combinado):
    dataframes = []
    for i, archivo in enumerate(archivos_csv, start=1):
        df = pd.read_csv(archivo)
        # Agrega un identificador único a la columna de iteración
        df['Iteration'] = f"{i}." + df['Iteration'].astype(str)
        dataframes.append(df)
    df_combinado = pd.concat(dataframes, ignore_index=True)
    df_combinado.to_csv(archivo_combinado, index=False)



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
    pygame.init()
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    pygame.display.set_caption("La Torre Encantada")
    font = pygame.font.Font(None, config.FONT_SIZE)

    n_iterations = prompt_for_iterations(screen, font)

    archivos_csv = []

    for heroe_initial_position in [1, 2, 3]:
        time.sleep(1)
        grafo = ModuloGrafo(pygame.Rect(config.RECT_GRAFO_X, config.RECT_GRAFO_Y, config.RECT_GRAFO_WIDTH, config.RECT_GRAFO_HEIGHT))
        dado = ModuloDado(pygame.Rect(config.RECT_DADO_X, config.RECT_DADO_Y, config.RECT_DADO_WIDTH, config.RECT_DADO_HEIGHT), font)
        display = GameDisplay(screen, font, 3 / (n_iterations * 100))

        # Genera un nombre de archivo CSV único basado en la posición inicial del héroe
        csv_filename = f'output/game_log_{heroe_initial_position}.csv'
        archivos_csv.append(csv_filename)


        # Comprueba si el archivo ya existe y, en ese caso, lo elimina para crear uno nuevo
        if os.path.exists(csv_filename):
            os.remove(csv_filename)

        # Crea una instancia de GameLogger para la posición inicial del héroe
        game_logger = GameLogger(csv_filename)

        # Utiliza n_iterations como argumento en lugar de self.n_iterations
        game_manager = GameManager(grafo, dado, display, 0.001, n_iterations, heroe_initial_position + 4, game_logger)

        game_manager.run_game()  # Ejecuta el juego con las iteraciones actualizadas
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
                elif event.key == pygame.K_s:
                    archivo_combinado = 'output/game_log_combinado.csv'
                    combinar_csvs(archivos_csv, archivo_combinado)
                    
                    analizador = AnalizadorMonteCarlo(archivo_combinado)
                    analizador.analizar_y_graficar()

                    screen.blit(text_surface, text_rect)
                    pygame.display.flip()

if __name__ == "__main__":
    main()