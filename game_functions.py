# game_functions.py
from modulo_grafo import ModuloGrafo
from modulo_dado import ModuloDado
from game_display import GameDisplay
from game_manager import GameManager
from game_logger import GameLogger
import pygame
import config
import time
from utils import eliminar_archivos_output, combinar_csvs
def iniciar_juego(screen, font, heroe_initial_position, n_iterations, csv_filename, dado=None):
    grafo = ModuloGrafo(pygame.Rect(config.RECT_GRAFO_X, config.RECT_GRAFO_Y, config.RECT_GRAFO_WIDTH, config.RECT_GRAFO_HEIGHT))
    if dado is None:
        dado = ModuloDado(pygame.Rect(config.RECT_DADO_X, config.RECT_DADO_Y, config.RECT_DADO_WIDTH, config.RECT_DADO_HEIGHT), pygame.font.Font(None, config.FONT_SIZE))
    display = GameDisplay(screen, font, 3 / (n_iterations * 100))
    game_logger = GameLogger(csv_filename)
    game_manager = GameManager(grafo, dado, display, 0.001, n_iterations, heroe_initial_position + 4, game_logger)
    game_manager.run_game()


def reiniciar_juego(screen, font, opcion_elegida, n_iterations):
    eliminar_archivos_output()
    archivos_csv = []
    for heroe_initial_position in [1, 2, 3]:
        csv_filename = f'output/game_log_{heroe_initial_position}.csv'
        archivos_csv.append(csv_filename)

        dado = ModuloDado(pygame.Rect(config.RECT_DADO_X, config.RECT_DADO_Y, config.RECT_DADO_WIDTH, config.RECT_DADO_HEIGHT), font)
        # Ajusta el dado según la opción elegida
        if opcion_elegida == 'a':
            dado.cargar_dado_bruja(1)
        elif opcion_elegida == 'b':
            dado.cargar_dado_heroe(1)
        elif opcion_elegida == 'c':
            dado.cargar_dado_heroe(4)

        iniciar_juego(screen, font, heroe_initial_position, n_iterations, csv_filename, dado)
        time.sleep(1)

    archivo_combinado = 'output/game_log_combinado.csv'
    combinar_csvs(archivos_csv, archivo_combinado)
    time.sleep(1)
