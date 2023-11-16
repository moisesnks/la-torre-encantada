# modulo_grafo.py
import pygame
import networkx as nx
from grafo import grafo  # Asegúrate de que 'grafo' sea un diccionario accesible
import matplotlib.pyplot as plt
class ModuloGrafo:
    """
    Clase ModuloGrafo para representar y dibujar un grafo en una interfaz gráfica utilizando Pygame.

    Atributos:
        rect (pygame.Rect): Rectángulo que define el área en la que se dibujará el grafo.
        padding (int): Espaciado alrededor del grafo dentro del rectángulo.
        node_color (tuple): Color de los nodos del grafo en formato RGB.
        edge_color (tuple): Color de las aristas del grafo en formato RGB.
        node_size (int): Tamaño de los nodos del grafo.
        posiciones (dict): Diccionario que mapea nodos a posiciones en la pantalla.
        graph (networkx.DiGraph): Objeto de grafo de NetworkX basado en el diccionario 'grafo'.
    """
    def __init__(self, rect, padding=50, node_color=(100, 100, 255), edge_color=(50, 50, 50), node_size=4):
        """
        Inicializa el módulo del grafo con el área de dibujo, estilo y configuración.

        Args:
            rect (pygame.Rect): Rectángulo para el área de dibujo del grafo.
            padding (int): Espaciado alrededor del grafo.
            node_color (tuple): Color RGB de los nodos.
            edge_color (tuple): Color RGB de las aristas.
            node_size (int): Tamaño de los nodos.
        """
        self.rect = rect
        self.padding = padding
        self.node_color = node_color
        self.edge_color = edge_color
        self.node_size = node_size
        self.posiciones = self.obtener_posiciones(grafo)
        self.graph = nx.DiGraph(grafo)

    def obtener_posiciones(self, grafo):
        """
        Calcula las posiciones de los nodos del grafo para su visualización.

        Args:
            grafo (dict): Diccionario que representa el grafo.

        Returns:
            dict: Diccionario de posiciones de nodos.
        """
        G = nx.DiGraph(grafo)
        pos = nx.kamada_kawai_layout(G, scale=1)  # scale parameter ensures coordinates are normalized
        scaled_pos = {}
        
        # Get range of positions to find the scale factors
        xs = [x for x, y in pos.values()]
        ys = [y for x, y in pos.values()]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        
        # Calculate scale factors
        x_scale = (self.rect.width - 2 * self.padding) / (max_x - min_x) if max_x > min_x else 1
        y_scale = (self.rect.height - 2 * self.padding) / (max_y - min_y) if max_y > min_y else 1
        
        for node, (x, y) in pos.items():
            # Translate and scale the graph to fit the rect
            scaled_x = (x - min_x) * x_scale + self.padding + self.rect.x
            scaled_y = (y - min_y) * y_scale + self.padding + self.rect.y
            
            scaled_pos[node] = (scaled_x, scaled_y)
        
        return scaled_pos

    def dibujar_grafo(self, screen):
        """
        Dibuja el grafo en una pantalla dada.

        Args:
            screen (pygame.Surface): La superficie de Pygame donde se dibujará el grafo.
        """
        G = nx.DiGraph(grafo)
        for nodo1, nodo2 in G.edges():
            pygame.draw.line(screen, self.edge_color, self.posiciones[nodo1], self.posiciones[nodo2], 1)
        for nodo, (x, y) in self.posiciones.items():
            pygame.draw.circle(screen, self.node_color, (int(x), int(y)), self.node_size)

    def draw(self, screen):
        """
        Dibuja el fondo y el grafo en la pantalla.

        Args:
            screen (pygame.Surface): La superficie de Pygame para el dibujo.
        """
        # Dibujar un fondo blanco en el área del grafo
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 0, border_radius=10)
        

        # Dibujar el grafo
        self.dibujar_grafo(screen)


    def handle_event(self, event):
        """
        Maneja eventos relacionados con el grafo. Método para futuras extensiones.

        Args:
            event (pygame.event.Event): Evento de Pygame para procesar.
        """
        # Aquí se podría manejar cualquier evento si fuera necesario.
        pass

    def guardar_grafo_como_png(self, nombre_archivo):
        """
        Guarda el grafo como un archivo PNG.

        Args:
            nombre_archivo (str): El nombre del archivo donde se guardará el grafo.
        """
        # Convertir colores RGB a formato hexadecimal
        node_color_hex = "#{:02x}{:02x}{:02x}".format(*self.node_color)
        edge_color_hex = "#{:02x}{:02x}{:02x}".format(*self.edge_color)

        # Crear un objeto de grafo de NetworkX
        G = nx.DiGraph(grafo)

        # Generar posiciones para los nodos
        pos = nx.kamada_kawai_layout(G)

        # Dibujar nodos y aristas
        nx.draw(G, pos, with_labels=True, node_color=node_color_hex, edge_color=edge_color_hex)

        # Guardar la figura
        plt.savefig(nombre_archivo)

# Ejemplo de uso
if __name__ == "__main__":
    modulo_grafo = ModuloGrafo(pygame.Rect(0, 0, 800, 600))
    modulo_grafo.guardar_grafo_como_png("networkx.png")
