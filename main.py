# main.py
import pygame
import config
from utils import eliminar_archivos_output, combinar_csvs, prompt_for_iterations, mostrar_menu_opciones, mostrar_mensaje_opciones, esperar_interaccion_usuario
from game_functions import iniciar_juego, reiniciar_juego
from analizador_montecarlo import AnalizadorMonteCarlo
import time

def main():
    pygame.init()
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    pygame.display.set_caption("La Torre Encantada")
    font = pygame.font.Font(None, config.FONT_SIZE)

    n_iterations = prompt_for_iterations(screen, font)
    archivos_csv = []

    eliminar_archivos_output()

    for heroe_initial_position in [1, 2, 3]:
        csv_filename = f'output/game_log_{heroe_initial_position}.csv'
        archivos_csv.append(csv_filename)
        iniciar_juego(screen, font, heroe_initial_position, n_iterations, csv_filename)
        time.sleep(1)

    archivo_combinado = 'output/game_log_combinado.csv'
    combinar_csvs(archivos_csv, archivo_combinado)

    opcion_elegida = None

    time.sleep(1)
    
    # Muestra el mensaje de opciones una vez antes de entrar al bucle principal
    mostrar_mensaje_opciones(screen, font)

    while True:
        opcion_elegida = esperar_interaccion_usuario()
        
        if opcion_elegida == 'quit':
            return  # Salir del programa
        elif opcion_elegida == 's':
            analizador = AnalizadorMonteCarlo(archivo_combinado)
            analizador.analizar_y_graficar()
        elif opcion_elegida == 'p':
            opcion_elegida = mostrar_menu_opciones(screen, font)
            if opcion_elegida:
                reiniciar_juego(screen, font, opcion_elegida, n_iterations)

if __name__ == "__main__":
    main()
