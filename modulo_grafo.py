import pygame
import networkx as nx
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

class ModuloGrafo:
    def __init__(self, rect, padding=50, node_color=(100, 100, 255), edge_color=(50, 50, 50), node_size=4, graph_file="assets/graph.graphml"):
        self.rect = rect
        self.padding = padding
        self.node_color = node_color
        self.edge_color = edge_color
        self.node_size = node_size
        self.graph = self.cargar_grafo_desde_graphml(graph_file)
        self.posiciones = self.obtener_posiciones(graph_file)

    def cargar_grafo_desde_graphml(self, graph_file):
        grafo = nx.Graph()
        tree = ET.parse(graph_file)
        root = tree.getroot()

        for node in root.findall(".//node"):
            node_id = int(node.get("id"))
            grafo.add_node(node_id)

        for edge in root.findall(".//edge"):
            source = int(edge.get("source"))
            target = int(edge.get("target"))
            grafo.add_edge(source, target)

        return grafo

    def obtener_posiciones(self, graph_file):
        tree = ET.parse(graph_file)
        root = tree.getroot()
        posiciones = {}

        # Obtener coordenadas máximas y mínimas
        min_x, min_y, max_x, max_y = float('inf'), float('inf'), float('-inf'), float('-inf')

        for node in self.graph.nodes:
            node_id = node
            pos_x = float(root.find(f'.//node[@id="{node_id}"]').get("positionX"))
            pos_y = float(root.find(f'.//node[@id="{node_id}"]').get("positionY"))

            # Actualizar coordenadas máximas y mínimas
            min_x = min(min_x, pos_x)
            min_y = min(min_y, pos_y)
            max_x = max(max_x, pos_x)
            max_y = max(max_y, pos_y)

            posiciones[node_id] = (pos_x, pos_y)

        # Calcular los factores de escala
        x_scale = (self.rect.width - 2 * self.padding) / (max_x - min_x) if max_x > min_x else 1
        y_scale = (self.rect.height - 2 * self.padding) / (max_y - min_y) if max_y > min_y else 1

        # Escalar y ajustar las coordenadas
        for node_id, (pos_x, pos_y) in posiciones.items():
            scaled_x = (pos_x - min_x) * x_scale + self.padding + self.rect.x
            scaled_y = (pos_y - min_y) * y_scale + self.padding + self.rect.y
            posiciones[node_id] = (scaled_x, scaled_y)

        return posiciones


    def dibujar_grafo(self, screen):
        posiciones = self.posiciones

        for edge in self.graph.edges():
            start_node = edge[0]
            end_node = edge[1]
            start_pos = posiciones[start_node]
            end_pos = posiciones[end_node]
            pygame.draw.line(screen, self.edge_color, start_pos, end_pos, 1)

        for node, pos in posiciones.items():
            pygame.draw.circle(screen, self.node_color, (int(pos[0]), int(pos[1])), self.node_size)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 0, border_radius=10)
        self.dibujar_grafo(screen)

    def handle_event(self, event):
        pass

    def guardar_grafo_como_png(self, nombre_archivo):
        node_color_hex = "#{:02x}{:02x}{:02x}".format(*self.node_color)
        edge_color_hex = "#{:02x}{:02x}{:02x}".format(*self.edge_color)
        G = nx.DiGraph(self.graph)
        pos = self.posiciones

        nx.draw(G, pos, with_labels=True, node_color=node_color_hex, edge_color=edge_color_hex)
        plt.savefig(nombre_archivo)

# Ejemplo de uso
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    modulo_grafo = ModuloGrafo(pygame.Rect(0, 0, 800, 600))
    
    ejecutando = True
    while ejecutando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False
        
        screen.fill((255, 255, 255))
        modulo_grafo.draw(screen)
        pygame.display.flip()
    
    pygame.quit()
