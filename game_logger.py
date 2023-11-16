import os

class GameLogger:
    """
    Clase GameLogger para registrar eventos y datos del juego en un archivo.

    Atributos:
        output_dir (str): Directorio donde se guardará el archivo de registro.
        file_path (str): Ruta completa al archivo de registro.
    """

    def __init__(self, filename):
        """
        Inicializa el GameLogger con un nombre de archivo especificado.

        Args:
            filename (str): Nombre del archivo de registro.
        """
        self.output_dir = os.path.join(os.getcwd(), 'output')
        os.makedirs(self.output_dir, exist_ok=True)  # Crea el directorio si no existe
        self.file_path = os.path.join(self.output_dir, filename)
        self.clear_log()  # Limpia el archivo de registro al inicio

    def log_data(self, iteration, data):
        """
        Registra datos de una iteración del juego en el archivo.

        Args:
            iteration (int): Número de la iteración actual.
            data (list): Lista de datos para registrar. Cada entrada es una tupla con los datos del juego.
        """
        with open(self.file_path, 'a') as f:
            if iteration == 1:
                # Escribe los encabezados del CSV en la primera iteración
                f.write("Iteration;Character;Prev_Position;New_Position;Steps;Result\n")

            for entry in data:
                # Escribe los datos de cada entrada en el archivo
                f.write(f"{iteration};{entry[0]};{entry[1]};{entry[2]};{entry[3]};{entry[4]}\n")

    def clear_log(self):
        """
        Limpia el contenido del archivo de registro, iniciándolo de nuevo.
        """
        with open(self.file_path, 'w') as f:
            f.write("")  # Vacía el contenido del archivo
