# utils.py
import pygame
import pandas as pd
import os
import config

def combinar_csvs(archivos_csv, archivo_combinado):
    dataframes = []
    for i, archivo in enumerate(archivos_csv, start=1):
        if os.path.exists(archivo):
            df = pd.read_csv(archivo)
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

def mostrar_menu_opciones(screen, font):
    opciones = [
        "a) Qué pasa si los dados de la bruja aumentan 1.",
        "b) Qué pasa si los dados del héroe aumentan 1.",
        "c) Propuesta para que el héroe gane más del 50%. (Aumentar 4 al dado del héroe)"
    ]
    opcion_elegida = None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    opcion_elegida = 'a'
                    running = False
                elif event.key == pygame.K_b:
                    opcion_elegida = 'b'
                    running = False
                elif event.key == pygame.K_c:
                    opcion_elegida = 'c'
                    running = False

        screen.fill(config.COLOR_BACKGROUND)
        for i, texto_opcion in enumerate(opciones, start=1):
            text_surface = font.render(texto_opcion, True, config.COLOR_TEXT_DEFAULT)
            screen.blit(text_surface, (50, 50 + 30 * i))
        pygame.display.flip()

    return opcion_elegida

def eliminar_archivos_output():
    # Directorio donde se encuentran los archivos a eliminar
    directorio_output = 'output'

    try:
        # Obtener la lista de archivos en el directorio
        archivos = os.listdir(directorio_output)

        # Recorrer la lista de archivos y eliminar cada uno
        for archivo in archivos:
            ruta_archivo = os.path.join(directorio_output, archivo)
            if os.path.isfile(ruta_archivo):
                os.remove(ruta_archivo)
                print(f"Se ha eliminado el archivo: {ruta_archivo}")

        print("Todos los archivos en la carpeta 'output' han sido eliminados.")
    
    except Exception as e:
        print(f"Error al eliminar archivos: {str(e)}")


def mostrar_mensaje_opciones(screen, font):
    mensaje = "Presione Esc para salir, S para modo estadístico, o P para menú de propuestas."
    text_surface = font.render(mensaje, True, config.COLOR_TEXT_DEFAULT)
    text_rect = text_surface.get_rect(center=(config.WIDTH // 2, config.HEIGHT - 50))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

def esperar_interaccion_usuario():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return 'quit'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    return 'quit'
                elif event.key == pygame.K_s:
                    return 's'
                elif event.key == pygame.K_p:
                    return 'p'