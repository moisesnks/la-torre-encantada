import pygame
import time
from personajes import Personajes
import config
from statbar import StatBar, StatText
from game_logger import GameLogger

class GameManager:
    def __init__(self, grafo, dado, display, wt, n_iterations, heroe_initial_position, game_logger):
        self.grafo = grafo
        self.dado = dado
        self.display = display
        self.waiting_time = wt
        self.n_iterations = n_iterations
        self.heroe_initial_position = heroe_initial_position
        self.game_logger = game_logger 
        self.init_graphics()

    def init_graphics(self):
        self.init_stats()
        self.dado_rect = self.dado.rect
        self.grafo_rect = self.grafo.rect

    def init_stats(self):
        font = pygame.font.Font(None, config.GAME_MANAGER_FONT_SIZE)
        self.heroe_win_bar = StatBar(20, config.GAME_MANAGER_STAT_BAR_Y, 20, config.GAME_MANAGER_STAT_BAR_WIDTH, config.GAME_MANAGER_STAT_BAR_HEIGHT, config.GAME_MANAGER_HEROE_COLOR)
        self.bruja_win_bar = StatBar(50, config.GAME_MANAGER_STAT_BAR_Y, 20, config.GAME_MANAGER_STAT_BAR_WIDTH, config.GAME_MANAGER_STAT_BAR_HEIGHT, config.GAME_MANAGER_BRUJA_COLOR)
        self.heroe_win_text = StatText(config.GAME_MANAGER_STAT_TEXT_X, config.GAME_MANAGER_STAT_TEXT_Y_HEROE, font, config.GAME_MANAGER_HEROE_COLOR)
        self.bruja_win_text = StatText(config.GAME_MANAGER_STAT_TEXT_X, config.GAME_MANAGER_STAT_TEXT_Y_BRUJA, font, config.GAME_MANAGER_BRUJA_COLOR)

    def run_game(self):
        # Crear la instancia de Personajes una sola vez
        personajes = Personajes(self.grafo.graph, self.dado, self.heroe_initial_position, self.game_logger)

        for iteration in range(self.n_iterations):
            # Resetear el estado del juego para la nueva iteración, excepto los contadores de victorias
            personajes.reset_positions(self.heroe_initial_position)


            if self.game_loop(personajes, iteration):
                break

            self.update_and_draw_statistics(iteration, personajes)


    def game_loop(self, personajes, iteration):
        running = True
        while running:
            if self.process_events():
                return True
            self.update_game_display(personajes, iteration)
            running = self.update_game_state(personajes, iteration)

            # Actualiza y dibuja las estadísticas
            self.update_and_draw_statistics(iteration, personajes)

            # Actualiza la pantalla para reflejar los cambios
            pygame.display.update()

            time.sleep(self.waiting_time)
        return False


    def update_score(self, personajes):
        if personajes.heroe_found_key:
            self.heroe_wins += 1
        else:
            self.bruja_wins += 1

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    def update_game_display(self, personajes, iteration):
        self.display.clear_screen()
        self.grafo.draw(self.display.screen)
        self.dado.draw(self.display.screen)
        self.draw_characters(personajes)
        self.display_info(personajes, iteration)
        self.display.update_display()

    def draw_characters(self, personajes):
        self.display.draw_circle(self.grafo.posiciones[personajes.heroe_position], config.COLOR_HERO, 10)
        self.display.draw_circle(self.grafo.posiciones[personajes.bruja_position], config.COLOR_WITCH, 10)
        self.display.draw_circle(self.grafo.posiciones[personajes.llave_position], config.COLOR_KEY, 8)

    def display_info(self, personajes, iteration):
        info_texts = [
            f"Posición inicial del Héroe: {self.heroe_initial_position}",
            f"Posición del Héroe: {personajes.heroe_position}",
            f"Posición de la Bruja: {personajes.bruja_position}",
            f"Posición de la Llave: {personajes.llave_position}",
            f"Iteración: {iteration + 1}"
        ]
        text_x = config.WIDTH - config.RECT_DADO_WIDTH * 2.5
        text_y = config.RECT_DADO_HEIGHT + config.RECT_DADO_Y + 10
        self.display.draw_info_rectangles(info_texts, text_x, text_y)

    def update_game_state(self, personajes, iteration):
        personajes.mover_heroe(iteration)
        personajes.mover_bruja(iteration)
        game_over, heroe_found_key = personajes.check_game_over(iteration)
        if game_over:
            self.handle_game_over(personajes, heroe_found_key, iteration)
            return False
        return True

    def handle_game_over(self, personajes, heroe_found_key, iteration):
        winner = 'Heroe' if heroe_found_key else 'Bruja'
        winner_position = personajes.heroe_position if heroe_found_key else personajes.bruja_position
        winner_message = f"{winner} encontró la llave en el nodo {winner_position} y ganó el juego {iteration + 1}."
        self.display.show_end_game_message(winner_message)

    def update_stat_bars(self, heroe_win_percentage, bruja_win_percentage):

        self.heroe_win_bar.value = heroe_win_percentage
        self.bruja_win_bar.value = bruja_win_percentage

        self.heroe_win_bar.update_bar()
        self.bruja_win_bar.update_bar()

    def update_stat_texts(self, heroe_wins, bruja_wins, heroe_win_percentage, bruja_win_percentage):
        text_width = 200  # Estimación del ancho del texto
        text_height = config.GAME_MANAGER_FONT_SIZE  # Altura del texto basada en el tamaño de la fuente

        heroe_text_area = pygame.Rect(config.GAME_MANAGER_STAT_TEXT_X, config.GAME_MANAGER_STAT_TEXT_Y_HEROE, text_width, text_height)
        bruja_text_area = pygame.Rect(config.GAME_MANAGER_STAT_TEXT_X, config.GAME_MANAGER_STAT_TEXT_Y_BRUJA, text_width, text_height)

        self.display.screen.fill(config.COLOR_BACKGROUND, heroe_text_area)
        self.display.screen.fill(config.COLOR_BACKGROUND, bruja_text_area)

        self.heroe_win_text.set_text(f"Victorias del Héroe: {heroe_wins} ({heroe_win_percentage:.2f}%)")
        self.bruja_win_text.set_text(f"Victorias de la Bruja: {bruja_wins} ({bruja_win_percentage:.2f}%)")

    def draw_stats(self):
        self.heroe_win_bar.draw(self.display.screen)
        self.bruja_win_bar.draw(self.display.screen)
        self.heroe_win_text.draw(self.display.screen)
        self.bruja_win_text.draw(self.display.screen)

    def update_and_draw_statistics(self, iteration, personajes):
        total_iterations = iteration + 1
        heroe_wins = personajes.get_heroe_wins()
        bruja_wins = personajes.get_bruja_wins()
        heroe_win_percentage = heroe_wins / total_iterations * 100
        bruja_win_percentage = bruja_wins / total_iterations * 100

        self.update_stat_bars(heroe_win_percentage, bruja_win_percentage)
        self.update_stat_texts(heroe_wins, bruja_wins, heroe_win_percentage, bruja_win_percentage)
        self.draw_stats()
