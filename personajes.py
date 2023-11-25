import random
import networkx as nx

class Personajes:
    def __init__(self, graph, dado, heroe_initial_position, game_logger):
        self.graph = graph
        self.dado = dado
        self.game_logger = game_logger
        self.heroe_position = heroe_initial_position
        self.bruja_position = 0
        self.llave_position = random.choice([23, 27, 32])
        self.game_over = False
        self.heroe_found_key = False
        self.ultimo_mov_heroe = (None, heroe_initial_position)
        self.ultimo_mov_bruja = (None, 0)
        self.pasos_heroe = 0
        self.pasos_bruja = 0

    def reset_positions(self, heroe_initial_position):
        self.heroe_position = heroe_initial_position
        self.bruja_position = 0
        self.llave_position = random.choice([23, 27, 32])

    def mover_heroe(self, iteration):
        if self.game_over:
            return

        prev_position = self.heroe_position
        dice_result = self.dado.roll()
        self.pasos_heroe = dice_result[1]

        for _ in range(self.pasos_heroe):
            adyacentes = list(self.graph.neighbors(self.heroe_position))
            adyacentes = [pos for pos in adyacentes if pos != prev_position]
            if not adyacentes:
                break

            next_position = random.choice(adyacentes)
            prev_position = self.heroe_position
            self.heroe_position = next_position
            if self.heroe_position == self.llave_position:
                self.game_over = True
                self.heroe_found_key = True
                break

        self.ultimo_mov_heroe = (prev_position, self.heroe_position)
        self.game_logger.log_movement(iteration, "Heroe", prev_position, self.heroe_position, self.pasos_heroe, 0)

    def mover_bruja(self, iteration):
        if self.game_over:
            return

        prev_position = self.bruja_position
        dice_result = self.dado.roll()
        self.pasos_bruja = dice_result[0]
        shortest_path = nx.dijkstra_path(self.graph, self.bruja_position, self.llave_position)
        for _ in range(self.pasos_bruja):
            if len(shortest_path) > 1:
                self.bruja_position = shortest_path.pop(1)
                if self.bruja_position == self.llave_position:
                    self.game_over = True
                    self.heroe_found_key = False
                    break

        self.ultimo_mov_bruja = (prev_position, self.bruja_position)
        self.game_logger.log_movement(iteration, "Bruja", prev_position, self.bruja_position, self.pasos_bruja, 0)

    def check_game_over(self, iteration):
        if self.game_over:
            character = "HEROE" if self.heroe_found_key else "BRUJA"
            prev_position, current_position = self.ultimo_mov_heroe if self.heroe_found_key else self.ultimo_mov_bruja
            n_pasos = self.pasos_heroe if self.heroe_found_key else self.pasos_bruja
            self.game_logger.log_movement(iteration, character, current_position, current_position, 0, 1)
        return self.game_over, self.heroe_found_key
