# gamemanager.py
import pygame
import time
from personajes import Personajes
from game_logger import GameLogger
import config

from statbar import StatBar, StatText  # Importa la clase StatBar

class GameManager:
    """
    Clase que gestiona la lógica principal del juego, incluyendo el bucle principal del juego,
    la visualización de estadísticas y la gestión de eventos.

    Atributos:
        grafo (ModuloGrafo): Objeto que representa el grafo del juego.
        dado (ModuloDado): Objeto que representa el dado del juego.
        display (GameDisplay): Objeto para gestionar la visualización del juego.
        waiting_time (float): Tiempo de espera entre iteraciones del juego.
        n_iterations (int): Número total de iteraciones del juego.
        logger (GameLogger): Objeto para registrar eventos y resultados del juego.
        heroe_win_bar, bruja_win_bar (StatBar): Barras de estadísticas para victorias de héroe y bruja.
        heroe_win_text, bruja_win_text (StatText): Textos de estadísticas para victorias de héroe y bruja.
        heroe_win_percentage, bruja_win_percentage (float): Porcentajes de victoria del héroe y la bruja.
        dado_rect, grafo_rect (pygame.Rect): Rectángulos para representar el dado y el grafo.
        heroe_initial_position (int): Posición inicial del héroe en el grafo.
    """
    def __init__(self, grafo, dado, display, wt, n_iterations, heroe_initial_position):
        """
        Inicializa el GameManager con los componentes del juego, tiempo de espera y número de iteraciones.

        Args:
            grafo (ModuloGrafo): Objeto del grafo del juego.
            dado (ModuloDado): Objeto del dado del juego.
            display (GameDisplay): Objeto para la visualización del juego.
            wt (float): Tiempo de espera entre iteraciones.
            n_iterations (int): Número total de iteraciones a jugar.
            heroe_initial_position (int): Posición inicial del héroe en el grafo.
        """
        self.grafo = grafo
        self.dado = dado
        self.display = display
        self.waiting_time = wt
        self.n_iterations = n_iterations
        self.heroe_initial_position = heroe_initial_position

        # Initialize logger for this game session
        self.logger = None
        self.restart_logger()

        # Create statistics bars and text
        self.heroe_win_bar = StatBar(20, config.RECT_GRAFO_HEIGHT + 20, 20, 200, 100, (0, 128, 0))
        self.bruja_win_bar = StatBar(50, config.RECT_GRAFO_HEIGHT + 20, 20, 200, 100, (128, 0, 0))
        font = pygame.font.Font(None, 36)  # Adjust the font size and type as needed
        self.heroe_win_text = StatText(250, config.RECT_GRAFO_HEIGHT + 20, font, (0, 128, 0))
        self.bruja_win_text = StatText(250, config.RECT_GRAFO_HEIGHT + 60, font, (128, 0, 0))
        self.heroe_win_percentage = 0
        self.bruja_win_percentage = 0

        self.dado_rect = dado.rect
        self.grafo_rect = grafo.rect

    def restart_logger(self):
        """
        Reinicia el logger del juego. Cierra el logger anterior si existe y crea uno nuevo.
        """
        if self.logger:
            self.logger.close()  # Close the previous logger if it exists

        # Set the filename to 'game_log.csv' for CSV logging
        self.logger = GameLogger('game_log.csv')
        self.logger.clear_log()


    def draw_stats(self):
        """
        Dibuja las barras y textos de estadísticas en la pantalla.
        """
        self.heroe_win_bar.draw(self.display.screen)
        self.bruja_win_bar.draw(self.display.screen)
        self.heroe_win_text.draw(self.display.screen)
        self.bruja_win_text.draw(self.display.screen)

    
    def run_game(self, iteration, heroe_wins_history, bruja_wins_history):
        """
        Ejecuta una iteración del juego, actualiza y dibuja las estadísticas.

        Args:
        iteration (int): Número de la iteración actual.
        heroe_wins_history (list): Historial de victorias del héroe.
        bruja_wins_history (list): Historial de victorias de la bruja.
        """
        personajes = Personajes(self.grafo.graph, self.dado, self.heroe_initial_position)
        game_data = []

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.display.clear_screen()
            self.grafo.draw(self.display.screen)
            self.dado.draw(self.display.screen)

            # Draw the positions of the characters and key
            self.display.draw_circle(self.grafo.posiciones[personajes.heroe_position], config.COLOR_HERO, 10)
            self.display.draw_circle(self.grafo.posiciones[personajes.bruja_position], config.COLOR_WITCH, 10)
            self.display.draw_circle(self.grafo.posiciones[personajes.llave_position], config.COLOR_KEY, 8)

            # Display current positions and iteration number
            text_heroe = f"Posición del Héroe: {personajes.heroe_position}"
            text_bruja = f"Posición de la Bruja: {personajes.bruja_position}"
            text_llave = f"Posición de la Llave: {personajes.llave_position}"
            text_iteracion = f"Iteración: {iteration}"
            text_x = self.dado_rect.x - (self.dado_rect.width - 50) / 2
            text_y = self.dado_rect.y + self.dado_rect.height + 10
            text_x, text_y = self.display.draw_info_rectangles([text_heroe, text_bruja, text_llave, text_iteracion], text_x, text_y)

            if not personajes.game_over:
                prev_hero_position, new_hero_position, hero_steps = personajes.mover_heroe()
                game_data.append(('Heroe', prev_hero_position, new_hero_position, hero_steps, 0))

                prev_bruja_position, new_bruja_position, bruja_steps = personajes.mover_bruja()
                game_data.append(('Bruja', prev_bruja_position, new_bruja_position, bruja_steps, 0))

                game_over, heroe_found_key = personajes.check_game_over()
                if game_over:
                    winner = 'Heroe' if heroe_found_key else 'Bruja'
                    prev_winner_position = personajes.heroe_position if heroe_found_key else personajes.bruja_position
                    winner_position = personajes.heroe_position if heroe_found_key else personajes.bruja_position
                    
                    game_data.append((winner, prev_winner_position, winner_position, 0, 1))
                    self.logger.log_data(iteration, game_data)

                    # Append the results of this game to the history here, before exiting the loop
                    heroe_wins_history.append(1 if winner == 'Heroe' else 0)
                    bruja_wins_history.append(0 if winner == 'Heroe' else 1)

                    winner_message = f"{winner} encontro la llave en el nodo {winner_position} y gano el juego {iteration}."
                    self.display.show_end_game_message(winner_message)
                    running = False

            # Update and draw the statistics bars
            heroe_wins = sum(heroe_wins_history)
            bruja_wins = sum(bruja_wins_history)
            total_iterations = self.n_iterations
            heroe_win_percentage = heroe_wins / total_iterations * 100
            bruja_win_percentage = bruja_wins / total_iterations * 100

            self.heroe_win_bar.value = heroe_win_percentage
            self.bruja_win_bar.value = bruja_win_percentage
            self.heroe_win_bar.update_bar()
            self.bruja_win_bar.update_bar()

            self.heroe_win_text.set_text(f"Victorias del Héroe: {heroe_wins} ({heroe_win_percentage:.2f}%)")
            self.bruja_win_text.set_text(f"Victorias de la Bruja: {bruja_wins} ({bruja_win_percentage:.2f}%)")

            self.heroe_win_bar.draw(self.display.screen)
            self.bruja_win_bar.draw(self.display.screen)

            self.display.update_display()
            time.sleep(self.waiting_time)  # Delay to make movements noticeable

