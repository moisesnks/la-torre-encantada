import csv

class GameLogger:
    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Escribir el encabezado del archivo CSV
            writer.writerow(["Iteration", "Character", "Prev_Position", "New_Position", "Steps", "Result"])

    def log_movement(self, iteration, character, prev_position, new_position, steps, result=0):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            # Escribir los datos de cada movimiento
            writer.writerow([iteration, character, prev_position, new_position, steps, result])
