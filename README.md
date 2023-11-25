# La Torre Encantada

## Descripción
"La Torre Encantada" es una simulación automatizada desarrollada en Python con Pygame. Este programa permite a los usuarios observar múltiples iteraciones de un juego en el que intervienen un héroe y una bruja, moviéndose de forma autónoma a través de un grafo. El objetivo es estudiar las estadísticas y patrones del juego utilizando el método de Monte Carlo.

## Características
- **Simulación Automatizada**: Simula automáticamente los movimientos de los personajes en un grafo.
- **Visualización Gráfica**: Utiliza Pygame para mostrar una visualización gráfica del juego.
- **Análisis Estadístico**: Realiza un análisis estadístico de los resultados utilizando el método de Monte Carlo.
- **Registro de Resultados**: Registra los resultados en `output/game_log.csv` para análisis detallados.

## Instalación
Asegúrate de tener instalados los siguientes requisitos:

- Python 3.x
- Pygame
- NetworkX

Puedes instalar las dependencias usando pip:

```bash
pip install pygame networkx
```
## El grafo
En este proyecto, hemos utilizado un mapa proporcionado en el juego "La Torre Encantada". Para representar y visualizar este mapa, lo pasamos a través de la herramienta en línea [graphonline.ru](https://graphonline.ru/en/), que nos permitió generar un archivo .graphml.

Gracias a la biblioteca NetworkX en Python, pudimos cargar y mapear las posiciones de este grafo directamente desde el archivo .graphml. Esto nos permitió mostrar el mapa en pantalla utilizando Pygame.

![Visualización del Grafo](assets/graph.png)

Puedes explorar y manipular interactivamente este grafo en Graphonline.ru a través del siguiente enlace:
[Ver Grafo en Graphonline.ru](http://graphonline.ru/es/?graph=DLyXrovLgHQCpIxpZZcst).

## Uso
Para ejecutar la simulación, simplemente ejecuta el siguiente comando:

```bash
python main.py
```

## Ejecutando el archivo
Una vez ejecutado el archivo, tendrá que definir cuántas iteraciones querrá simular, si simula entre [10-1] iteraciones podrá visualizar gráficamente cómo se mueve el héroe y la bruja, ya que el waiting-time para que se pueda visualizar está seteado en 0.6 segundos, sino, (si agrega un valor mayor) su waiting-time es de 1 milisegundo.

## Movimiento de la Bruja
- La bruja conoce la ubicación de la llave desde el principio del juego.
- La bruja utiliza la ruta más corta para llegar a la llave antes que el héroe, utilizando algoritmos de grafos para optimizar su ruta.

## Movimiento del Héroe
1. El héroe se moverá un número de casillas igual al número rojo que arroje el dado en cada turno.
2. Si el movimiento del héroe lo lleva a una bifurcación en el camino, deberá elegir una de las rutas disponibles de manera aleatoria y equitativa. Esto significa que si hay tres opciones en una bifurcación, cada ruta tiene una probabilidad de 1/3 de ser elegida.
3. El punto 3 es el punto de no retorno, lo que significa que el héroe no puede retroceder desde allí y no es una ruta posible para avanzar hacia la estrella.
4. Si al finalizar su turno, el héroe llega a una de las tres casillas donde posiblemente se encuentre la llave, debe verificar si la llave está allí. Si la encuentra, el héroe gana, rescata a la princesa y el juego termina. Si no encuentra la llave, permanece en esa casilla hasta el próximo lanzamiento del dado.

## Resultados
Los resultados obtenidos de las simulaciones incluyen:

1. Número de casos de éxito del héroe, comenzando desde las diferentes casillas iniciales.
2. Número de casos de éxito de la bruja, comenzando desde las diferentes casillas iniciales.
3. Cambios en los resultados si los números rojos del dado aumentan en 1 en cada cara y se mantienen los números azules sin cambios.
4. Cambios en los resultados si los números azules del dado aumentan en 1 en cada cara y se mantienen los números rojos sin cambios.
5. Número máximo y mínimo de lanzamientos o turnos requeridos para que el héroe encuentre la llave.
6. Número máximo y mínimo de lanzamientos o turnos requeridos para que la bruja llegue a la llave.


