# config.py

# Window dimensions
WIDTH, HEIGHT = 800, 600

# Graph rectangle dimensions
RECT_GRAFO_X = 10
RECT_GRAFO_Y = 10
RECT_GRAFO_WIDTH = 500
RECT_GRAFO_HEIGHT = 300

# Dice rectangle dimensions
RECT_DADO_WIDTH = 100
RECT_DADO_HEIGHT = 100
RECT_DADO_X = WIDTH - RECT_DADO_WIDTH*2
RECT_DADO_Y = 50 + RECT_GRAFO_Y

# Colors
COLOR_BACKGROUND = (0, 0, 0)
COLOR_TEXT_DEFAULT = (255, 255, 255)
COLOR_HERO = (128, 0, 0)
COLOR_WITCH = (0, 0, 128)
COLOR_KEY = (255, 255, 0)
COLOR_CONTAINER = (200, 200, 200)
COLOR_BUTTON = (255, 200, 200)
COLOR_BORDER = (255, 0, 0)
COLOR_PROGRESS_BAR = (0, 255, 0)  # Color verde para la barra de progreso
COLOR_PROGRESS_BAR_BG = (0, 0, 0)  # Color negro para el fondo de la barra de progreso

# Font size
FONT_SIZE = 24

# GameManager styles and configurations
GAME_MANAGER_FONT_SIZE = 36
GAME_MANAGER_HEROE_COLOR = (0, 128, 0)  # Verde para el Héroe
GAME_MANAGER_BRUJA_COLOR = (128, 0, 0)  # Rojo para la Bruja
GAME_MANAGER_STAT_BAR_WIDTH = 200
GAME_MANAGER_STAT_BAR_HEIGHT = 40
GAME_MANAGER_STAT_TEXT_X = 250
GAME_MANAGER_STAT_BAR_Y = RECT_GRAFO_HEIGHT + 20  # Posición vertical para las barras de estadísticas
GAME_MANAGER_STAT_TEXT_Y_HEROE = RECT_GRAFO_HEIGHT + 60  # Posición vertical para el texto de estadísticas del Héroe
GAME_MANAGER_STAT_TEXT_Y_BRUJA = RECT_GRAFO_HEIGHT + 100  # Posición vertical para el texto de estadísticas de la Bruja
