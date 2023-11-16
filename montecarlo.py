import matplotlib.pyplot as plt
import csv
from collections import defaultdict

class AnalizadorMonteCarlo:
    """
    Clase AnalizadorMonteCarlo para analizar los resultados de simulaciones de Monte Carlo
    de un archivo CSV y visualizar las estadísticas de victorias y visitas a nodos.
    """
    
    def __init__(self, nombre_archivo):
        """
        Inicializa el analizador con el nombre del archivo CSV.
        """
        self.nombre_archivo = nombre_archivo
        self.datos = self.leer_datos_csv()
        self.total_iteraciones = self.contar_iteraciones()

    def leer_datos_csv(self):
        """
        Lee los datos desde un archivo CSV y los devuelve como una lista de diccionarios.
        """
        datos = []
        with open(self.nombre_archivo, 'r') as archivo:
            lector = csv.DictReader(archivo, delimiter=';')
            for fila in lector:
                datos.append(fila)
        return datos

    def contar_iteraciones(self):
        """
        Cuenta el total de iteraciones que resultaron en una victoria.
        """
        return len([fila for fila in self.datos if int(fila['Result']) == 1])

    def victorias_montecarlo(self, personaje):
        """
        Calcula el número de victorias para un personaje específico.
        """
        victorias_personaje = sum(1 for fila in self.datos if fila['Character'] == personaje and int(fila['Result']) == 1)
        return victorias_personaje

    def calcular_visitas_nodos(self, personaje):
        """
        Calcula las visitas a cada nodo por un personaje específico y devuelve los 5 nodos más visitados.
        """
        conteo_nodos = defaultdict(int)
        for fila in self.datos:
            if fila['Character'] == personaje and int(fila['Steps']) != 0 and int(fila['Result']) == 0:
                conteo_nodos[fila['New_Position']] += 1
        return sorted(conteo_nodos.items(), key=lambda x: x[1], reverse=True)[:5]


    def graficar_nodos_top(self, personaje):
        """
        Crea un gráfico de barras para los 5 nodos más visitados por un personaje específico.
        """
        nodos_top = self.calcular_visitas_nodos(personaje)
        nodos, visitas = zip(*nodos_top)

        plt.figure(figsize=(8, 6))
        plt.bar(range(len(nodos)), visitas, tick_label=nodos, color='verde' if personaje == 'Heroe' else 'morado')
        plt.xlabel('Nodos')
        plt.ylabel('Visitas')
        plt.title(f'Top 5 Nodos Visitados por el {personaje}')
        plt.show()

    def analizar_y_graficar(self):
        """
        Ejecuta el análisis y muestra las gráficas resultantes.
        """
        
        fig, axs = plt.subplots(1, 3, figsize=(18, 6))
        
        # Gráfico circular de probabilidades de victoria
        self.graficar_probabilidades_victoria_en_subplot(axs[0])
        
        # Gráficos de barras de nodos más visitados
        self.graficar_nodos_top_en_subplot('Heroe', axs[1])
        self.graficar_nodos_top_en_subplot('Bruja', axs[2])

        plt.tight_layout()
        plt.show()

    def graficar_probabilidades_victoria_en_subplot(self, ax):
        """
        Crea un gráfico circular en un subplot dado para las probabilidades de victoria.
        """
        victorias_heroe = self.victorias_montecarlo('Heroe')
        victorias_bruja = self.victorias_montecarlo('Bruja')

        etiquetas = ['Héroe', 'Bruja']
        tamanos = [victorias_heroe, victorias_bruja]
        colores = ['red', 'blue']

        ax.pie(tamanos, labels=etiquetas, colors=colores, autopct='%1.1f%%', startangle=140)
        ax.set_title('Probabilidad de Victoria')
        ax.axis('equal')  # Asegura que el gráfico circular sea un círculo

    def graficar_nodos_top_en_subplot(self, personaje, ax):
        """
        Crea un gráfico de barras en un subplot dado para los nodos más visitados.
        """
        nodos_top = self.calcular_visitas_nodos(personaje)
        nodos, visitas = zip(*nodos_top)

        ax.bar(range(len(nodos)), visitas, tick_label=nodos, color='green' if personaje == 'Heroe' else 'purple')
        ax.set_xlabel('Nodos')
        ax.set_ylabel('Visitas')
        ax.set_title(f'Top 5 Nodos Visitados por el {personaje}')


# Uso de ejemplo:
if __name__ == "__main__":
    analizador = AnalizadorMonteCarlo('output/game_log.csv')
    analizador.analizar_y_graficar()
