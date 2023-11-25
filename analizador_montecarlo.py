import pandas as pd
import matplotlib.pyplot as plt

class AnalizadorMonteCarlo:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
        self.datos = None

    def cargar_datos(self):
        """Carga los datos del archivo CSV en un DataFrame."""
        self.datos = pd.read_csv(self.archivo_csv)

    def analizar_exito_heroe(self):
        """Analiza el número de casos de éxito del héroe desde distintas casillas."""
        exitos_heroe = self.datos[(self.datos['Character'] == 'Heroe') & (self.datos['Result'] == 1)]
        frecuencia_exito = exitos_heroe['Prev_Position'].value_counts()
        return frecuencia_exito

    def analizar_exito_bruja(self):
        """Analiza el número de casos de éxito de la bruja desde distintas casillas."""
        exitos_bruja = self.datos[(self.datos['Character'] == 'Bruja') & (self.datos['Result'] == 1)]
        frecuencia_exito = exitos_bruja['Prev_Position'].value_counts()
        return frecuencia_exito

    def turnos_max_min_heroe(self):
        """Calcula los turnos máximo y mínimo para que el héroe encontró la llave."""
        juegos_heroe = self.datos[self.datos['Character'] == 'Heroe'].groupby('Iteration').size()
        max_turnos = juegos_heroe.max()
        min_turnos = juegos_heroe.min()
        return max_turnos, min_turnos

    def turnos_max_min_bruja(self):
        """Calcula los turnos máximo y mínimo para que la bruja llegó a la llave."""
        juegos_bruja = self.datos[self.datos['Character'] == 'Bruja'].groupby('Iteration').size()
        max_turnos = juegos_bruja.max()
        min_turnos = juegos_bruja.min()
        return max_turnos, min_turnos

    def visualizar_resultados(self, frecuencia_exito_heroe, frecuencia_exito_bruja, turnos_heroe, turnos_bruja):
        """Visualiza los resultados del análisis."""
        plt.figure(figsize=(12, 6))

        plt.subplot(2, 2, 1)
        frecuencia_exito_heroe.plot(kind='bar')
        plt.title("Éxito del Héroe por Casilla")

        plt.subplot(2, 2, 2)
        frecuencia_exito_bruja.plot(kind='bar')
        plt.title("Éxito de la Bruja por Casilla")

        plt.subplot(2, 2, 3)
        plt.bar(['Máximo', 'Mínimo'], turnos_heroe)
        plt.title("Turnos Máximo y Mínimo - Héroe")

        plt.subplot(2, 2, 4)
        plt.bar(['Máximo', 'Mínimo'], turnos_bruja)
        plt.title("Turnos Máximo y Mínimo - Bruja")

        plt.tight_layout()
        plt.show()

    def analizar_y_graficar(self):
        """Método integral para realizar el análisis y la visualización."""
        self.cargar_datos()
        frecuencia_exito_heroe = self.analizar_exito_heroe()
        frecuencia_exito_bruja = self.analizar_exito_bruja()
        turnos_heroe = self.turnos_max_min_heroe()
        turnos_bruja = self.turnos_max_min_bruja()
        self.visualizar_resultados(frecuencia_exito_heroe, frecuencia_exito_bruja, turnos_heroe, turnos_bruja)

