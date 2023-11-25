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
        # Contadores de victoria
        self.heroe_wins = 0
        self.bruja_wins = 0

    def reset_positions(self, heroe_initial_position):
        self.heroe_position = heroe_initial_position
        self.bruja_position = 0
        self.llave_position = random.choice([23, 27, 32])

    def mover_heroe(self, iteration):
        if self.game_over:
            return

        dice_result = self.dado.roll()
        self.pasos_heroe = dice_result[1]

        movimientos = [self.heroe_position]

        for _ in range(self.pasos_heroe):
            prev_position = self.heroe_position
            adyacentes = list(self.graph.neighbors(self.heroe_position))
            adyacentes = [pos for pos in adyacentes if pos != prev_position]
            if not adyacentes:
                break  # No hay movimientos posibles desde la posición actual

            next_position = random.choice(adyacentes)
            prev_position = self.heroe_position  # Actualizar la posición previa antes de mover al héroe
            self.heroe_position = next_position
            movimientos.append(self.heroe_position)

            if self.heroe_position == self.llave_position:
                self.game_over = True
                self.heroe_found_key = True
                break

        secuencia_movimientos = ' -> '.join(map(str, movimientos))
        info_movimiento = f"Iteración: {iteration}, Pasos dados: {self.pasos_heroe}, Movimientos: {secuencia_movimientos}"
        print(info_movimiento)

        self.ultimo_mov_heroe = (movimientos[-2], self.heroe_position) if len(movimientos) > 1 else (self.heroe_position, self.heroe_position)
        self.game_logger.log_movement(iteration, "Heroe", self.ultimo_mov_heroe[0], self.heroe_position, self.pasos_heroe, 0)

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

    def reset_positions(self, heroe_initial_position):
        self.heroe_position = heroe_initial_position
        self.bruja_position = 0  # O cualquier posición inicial que desees para la bruja
        self.llave_position = random.choice([23, 27, 32])  # Selecciona una nueva posición para la llave
        self.game_over = False
        self.heroe_found_key = False


    def check_game_over(self, iteration):
        if self.game_over:
            character = "Heroe" if self.heroe_found_key else "Bruja"
            prev_position, current_position = self.ultimo_mov_heroe if self.heroe_found_key else self.ultimo_mov_bruja
            n_pasos = self.pasos_heroe if self.heroe_found_key else self.pasos_bruja
            self.game_logger.log_movement(iteration, character, current_position, current_position, 0, 1)
            
            # Actualiza los contadores de victorias
            if self.heroe_found_key:
                self.heroe_wins += 1
            else:
                self.bruja_wins += 1
            
        return self.game_over, self.heroe_found_key
    
    # Métodos getter para las victorias
    def get_heroe_wins(self):
        return self.heroe_wins

    def get_bruja_wins(self):
        return self.bruja_wins
