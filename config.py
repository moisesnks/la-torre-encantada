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
RECT_DADO_X = RECT_GRAFO_WIDTH + (WIDTH - RECT_GRAFO_WIDTH) / 2 - RECT_DADO_WIDTH / 2
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
