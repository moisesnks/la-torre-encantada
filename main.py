# main.py
import pygame
import config
from utils import eliminar_archivos_output, combinar_csvs, prompt_for_iterations, mostrar_menu_opciones
from game_functions import iniciar_juego, reiniciar_juego
from analizador_montecarlo import AnalizadorMonteCarlo
import time

def mostrar_mensaje_opciones(screen, font):
    mensaje = "Presione Esc para salir, S para modo estadístico, o P para menú de propuestas."
    text_surface = font.render(mensaje, True, config.COLOR_TEXT_DEFAULT)
    text_rect = text_surface.get_rect(center=(config.WIDTH // 2, config.HEIGHT - 50))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

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
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                elif event.key == pygame.K_s:
                    analizador = AnalizadorMonteCarlo(archivo_combinado)
                    analizador.analizar_y_graficar()
                elif event.key == pygame.K_p:
                    opcion_elegida = mostrar_menu_opciones(screen, font)
                    if opcion_elegida:
                        reiniciar_juego(screen, font, opcion_elegida, n_iterations)
        
        # Muestra el mensaje de opciones
        mostrar_mensaje_opciones(screen, font)

if __name__ == "__main__":
    main()
