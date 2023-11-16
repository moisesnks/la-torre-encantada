import random
import networkx as nx

class Personajes:
    """
    Clase Personajes para gestionar los personajes del juego y sus movimientos.

    Atributos:
        graph (networkx.Graph): El grafo que representa el juego.
        dado (Dado): Objeto que simula un dado para determinar los movimientos.
        heroe_position (int): Posición actual del héroe en el grafo.
        bruja_position (int): Posición actual de la bruja en el grafo.
        llave_position (int): Posición de la llave en el grafo.
        game_over (bool): Indica si el juego ha terminado.
        heroe_found_key (bool): Indica si el héroe ha encontrado la llave.
        heroe_moves (list): Lista de movimientos del héroe.
        bruja_moves (list): Lista de movimientos de la bruja.
        heroe_wins (int): Contador de victorias del héroe.
        bruja_wins (int): Contador de victorias de la bruja.
    """
    def __init__(self, graph, dado, heroe_initial_position):
        """
        Inicializa los personajes y sus posiciones iniciales.

        Args:
            graph (networkx.Graph): Grafo del juego.
            dado (Dado): Dado para determinar los movimientos.
            heroe_initial_position (int): Posición inicial del héroe en el grafo.
        """
        self.graph = graph
        self.dado = dado
        self.heroe_position = heroe_initial_position
        self.reset_positions(heroe_initial_position)
        self.game_over = False
        self.heroe_found_key = False  # To track if the hero found the key
        self.heroe_moves = []  # List to store hero's movements
        self.bruja_moves = []  # List to store witch's movements
        self.heroe_wins = 0  # Counter for hero's wins
        self.bruja_wins = 0  # Counter for witch's wins
        
    def reset_positions(self, heroe_initial_position):
        """
        Reinicia las posiciones de los personajes y la llave en el grafo.

        Args:
            heroe_initial_position (int): Posición inicial del héroe en el grafo.
        """
        self.heroe_position = heroe_initial_position
        self.bruja_position = 0  # La bruja comienza en el nodo 1
        self.llave_position = random.choice([23, 27, 32])  # Las posiciones son 24, 28 y 33, pero se indexan desde 0

    def mover_heroe(self):
        """
        Mueve al héroe en el grafo basado en el resultado del dado.

        Returns:
            tuple: La posición previa, nueva posición y número de pasos del héroe.
        """
        if self.game_over:
            return self.heroe_position, self.heroe_position, 0

        prev_position = self.heroe_position
        dice_result = self.dado.roll()
        n_pasos = dice_result[1]  # Asumiendo que el segundo elemento es para el movimiento del héroe

        for _ in range(n_pasos):
            adyacentes = list(self.graph.neighbors(self.heroe_position))

            # Eliminar la posición previa de la lista de adyacentes
            adyacentes = [pos for pos in adyacentes if pos != prev_position]

            # Si no hay adyacentes a los que moverse, el juego no debería terminar automáticamente
            # simplemente el héroe no se moverá en esta ronda
            if not adyacentes:
                break

            # Elegir un nuevo nodo adyacente al que moverse, excluyendo el nodo del que proviene
            next_position = random.choice(adyacentes)
            prev_position = self.heroe_position
            self.heroe_position = next_position

            # Comprobar si el héroe ha encontrado la llave solo si está en uno de los nodos válidos
            if self.heroe_position in [23, 27, 32] and self.heroe_position == self.llave_position:
                self.game_over = True
                self.heroe_found_key = True
                self.heroe_wins += 1  # Incrementar el contador de victorias del héroe
                break

            # Agregar el movimiento a la lista de movimientos del héroe
            self.heroe_moves.append(self.heroe_position)

        return prev_position, self.heroe_position, n_pasos

    def mover_bruja(self):
        """
        Mueve a la bruja en el grafo hacia la llave usando el camino más corto.

        Returns:
            tuple: La posición previa, nueva posición y número de pasos de la bruja.
        """
        if self.game_over:
            return self.bruja_position, self.bruja_position, 0

        prev_position = self.bruja_position
        dice_result = self.dado.roll()
        n_pasos = dice_result[0]  # Assuming the first element is for the witch's movement

        shortest_path = nx.dijkstra_path(self.graph, self.bruja_position, self.llave_position)
        steps_taken = 0
        for _ in range(n_pasos):
            if len(shortest_path) > 1:
                self.bruja_position = shortest_path.pop(1)
                steps_taken += 1
                if self.bruja_position == self.llave_position:
                    self.game_over = True
                    self.heroe_found_key = False
                    self.bruja_wins += 1  # Incrementar el contador de victorias de la bruja
                    break

            # Agregar el movimiento a la lista de movimientos de la bruja
            self.bruja_moves.append(self.bruja_position)

        return prev_position, self.bruja_position, steps_taken

    def check_game_over(self):
        """
        Verifica si el juego ha terminado, ya sea porque el héroe encontró la llave o la bruja la alcanzó.

        Returns:
            tuple: Un booleano indicando si el juego terminó y otro si el héroe encontró la llave.
        """
        return self.game_over, self.heroe_found_key
