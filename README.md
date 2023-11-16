# La Torre Encantada

## Descripción
"La Torre Encantada" es una simulación automatizada desarrollada en Python con Pygame. Este programa permite a los usuarios observar múltiples iteraciones de un juego en el que intervienen un héroe y una bruja, moviéndose de forma autónoma a través de un grafo. El objetivo es estudiar las estadísticas y patrones del juego utilizando el método de Monte Carlo.

## Características
- Simulación automatizada de movimientos de personajes en un grafo.
- Visualización gráfica del juego utilizando Pygame.
- Análisis estadístico de resultados utilizando el método de Monte Carlo.
- Registro de resultados en `output/game_log.csv` para análisis detallados.

Lamento la confusión. Entiendo tus indicaciones. Aquí está la revisión con la imagen incluida:

## El grafo
En este proyecto, hemos utilizado un mapa proporcionado en el juego "La Torre Encantada". Para representar y visualizar este mapa, lo pasamos a través de la herramienta en línea [graphonline.ru](https://graphonline.ru/en/), que nos permitió generar un archivo .graphml.

Gracias a la biblioteca NetworkX en Python, pudimos cargar y mapear las posiciones de este grafo directamente desde el archivo .graphml. Esto nos permitió mostrar el mapa en pantalla utilizando Pygame.

![Visualización del Grafo](assets/graph.png)

Puedes explorar y manipular interactivamente este grafo en Graphonline.ru a través del siguiente enlace:
[Ver Grafo en Graphonline.ru](http://graphonline.ru/es/?graph=DLyXrovLgHQCpIxpZZcst).


## Componentes
El juego consta de varios módulos principales:
- `modulo_grafo.py`: Gestiona la representación gráfica del grafo del juego.
- `modulo_dado.py`: Simula un dado para determinar el número de pasos de los personajes.
- `game_display.py`: Maneja la visualización y la interfaz gráfica del juego.
- `game_manager.py`: Controla la lógica principal y la ejecución del juego.
- `personajes.py`: Define las reglas de movimiento y acciones de los personajes del juego.
- `game_logger.py`: Registra los eventos y resultados del juego para análisis posteriores.
- `montecarlo.py`: Realiza un análisis estadístico de los resultados del juego utilizando simulaciones de Monte Carlo.

## Requisitos
- Python 3.x
- Pygame
- NetworkX
- SciPy

## Instalación
Sigue estos pasos para instalar y ejecutar la simulación:
```
pip install pygame networkx scipy
python main.py
```

## Uso
Después de iniciar la simulación, el programa ejecutará automáticamente un número definido de iteraciones, mostrando las interacciones entre el héroe y la bruja. Las estadísticas y el progreso de cada iteración se visualizan en tiempo real.

## Modo Estadístico
Al finalizar las iteraciones, presiona 'S' para ver un análisis estadístico de las simulaciones, incluyendo probabilidades de victoria y patrones de movimiento, con los resultados almacenados en `output/game_log.csv`.

## Autor
Desarrollado por [moisesnks](https://github.com/moisesnks), Noviembre 2023.


## Contribuciones
Si deseas contribuir a este proyecto, sigue estas pautas:
- Realiza un fork del repositorio.
- Crea una rama para tus características o correcciones.
- Envía un pull request con tus cambios.

## Licencia
Este proyecto está bajo la Licencia MIT. Para más detalles, ver el archivo [LICENSE](LICENSE).
