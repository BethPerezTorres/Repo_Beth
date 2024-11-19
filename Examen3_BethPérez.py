# EJERCICIO 1.
# En un solo lanzamiento de dos dados de 6 caras (con el mismo peso), encuentre la probabilidad
# de que su suma sea como máximo 'n'. Cree una funcion llamada 'lanzamiento' que reciba un entero
# llamado 'n' y retorne un flotante que calcule la probabilidad de que el lanzamiento de 2 dados de
# 6 caras sea <= n.

n = 13 #Definimos valor de 'n'.
def lanzamiento(n: int) -> float: #Creamos la función
    total_combinaciones = 36
    combinaciones_validas = 0
    for dado1 in range(1, 7): #primer dado
        for dado2 in range(1, 7):  #segundo dado
            suma = dado1 + dado2
            if suma <= n: #condición para ver si la suma es <= n
                combinaciones_validas += 1
    #para calcular la probabilidad
    probabilidad = combinaciones_validas / total_combinaciones
    return probabilidad
print(f"La probabilidad de que la suma sea <= {n} es {lanzamiento(n)}")

#_______________________________________________________________________________________________________

# EJERCICIO 2.
# Analice el código en los archivos animation2_1 y animation2_2 y conteste lo siguiente:

# ¿Qué forma tiene el grafo?
    # El grafo es un dodecaedro, una figura de doce caras, cada una de ellas con forma de pentagono.

# ¿Cuántos nodos tiene el grafo?, ¿con qué comando descubres el número de nodos?
    # El grafo tiene 20 nodos, para llegar a este resultado se escribio el siguiente código:

            # print(G.number_of_nodes())

# ¿Cuántas aristas tiene el grafo?, ¿con qué comando descubres el número de aristas?
    # El grafo tiene 30 aristas, para llegar a este resultado se escribio el siguiente código:

            # print(G.number_of_edges())

# ¿Qué hace el código G.degree()?
    # Nos dice el grado de un nodo, y el grado se refiere al número de aristas incidentes a él. En este caso al
    # ser un grafo no direccionado solo nos arroja un valor, si fuera dirigido podriamos hacer la distinción
    # entre las aristas que entran y las que salen, para este ejercicio escribimos lo siguiente:

            # print(G.degree()): Que nos arrojó el número del nodo y su grado.
            # [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3),
            # (10, 3), (11, 3), (12, 3), (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3), (19, 3)]

            # print(G.degree([0, 1, 2])): Que nos arrojo el nodo y grado unicamente de los que especificamos.
            # [(0, 3), (1, 3), (2, 3)]

# ¿Cuál es el número máximo de aristas en el grafo?
    # Para calcular el número máximo de aristas en el grafo podemos usar el siguiente código, que al
    # final nos dira que "El número máximo de aristas en el grafo es = 190".

numero_de_nodos = 20
N = numero_de_nodos
def aristas_max(N, directed=False):
    if directed:
        return N * (N - 1)
    else:
        return (N * (N - 1)) // 2
print(f'El número máximo de aristas en el grafo es = {aristas_max(N, directed=False)}')

# ¿Cuál es la diferencia entre animation2_1 y animation2_2?
    # La diferencia está en las ultimas lineas del código. Estas se utilizaron para agregar una
    # animación de giro que no se observa en la animation 2_1:

            #def init():
                #return fig,
            #def animate(i):
                #ax.view_init(elev=20, azim=i*4)
                #return fig,
            #ani = animation.FuncAnimation(fig, animate, init_func=init, frames=90, interval=200, blit=False)

#_______________________________________________________________________________________________________

# EJERCICIO 3.
# Modifique el código de animation2_2 para usar la información de 'fve30.mat'. Para las coordenadas
# 'x', 'y', 'z' utiliza un arreglo de números enteros aleatorios en el intervalo [0, 50].

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import scipy.io
from matplotlib import animation

file = scipy.io.loadmat(r"/home/bubbleth/PycharmProjects/pythonProject/Repo_Beth/fve30.mat")
G = nx.from_numpy_array(file['CIJ'])

# Se definen las coordenadas de cada nodo
x = np.random.randint(0, 51, size= 32)
y = np.random.randint(0, 51, size= 32)
z = np.random.randint(0, 51, size= 32)

# Se crean los nodos y las aristas acorde al grafo
nodes = np.array([[i, j, k] for i, j, k in zip(x, y, z)])
edges = np.array([(nodes[u], nodes[v]) for u, v in G.edges()])

# Se grafica
fig = plt.figure(figsize = (15, 15))
ax = fig.add_subplot(111, projection="3d")

def init():
    # Se grafican los nodos
    ax.scatter(*nodes.T)  # Equivalente a ax.scatter(x, y, z)
    # Se grafican las aristas
    for edge in edges:
        ax.plot(*edge.T)
    return fig,

def animate(i):
    ax.view_init(elev=20, azim=i*4)
    return fig,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=90, interval=200, blit=False)
plt.show()

#_______________________________________________________________________________________________________

# Ejercicio 4.
# Para los datos de 'Coactivation_matrix.mat', filtre la matriz para obtener los valores > 0.2,
# con el nuevo arreglo muestre los nodos y vértices del grafo.

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from scipy.io import loadmat

file1 = loadmat(r"/home/bubbleth/PycharmProjects/pythonProject/Repo_Beth/Coactivation_matrix.mat")
adj_matrix = file1['Coactivation_matrix']

# Aqui filtramos la matriz para los valores > 0.2
adj_matrix[adj_matrix <= 0.2] = 0

# Creamos la matriz con los nuevos datos
G = nx.from_numpy_array(adj_matrix)

# Nodos del grafo
num_nodes = G.number_of_nodes()
x = np.random.randint(0, 50, size=num_nodes)
y = np.random.randint(0, 50, size=num_nodes)
z = np.random.randint(0, 50, size=num_nodes)
# Posición de los nodos
nodes = np.array([[i, j, k] for i, j, k in zip(x, y, z)])
# Vertices
edges = np.array([(nodes[u], nodes[v]) for u, v in G.edges()])

# Graficamos el grafo en 3D
fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(111, projection="3d")

def init():
    ax.scatter(*nodes.T)
    for edge in edges:
        ax.plot(*edge.T)
    return fig,
def animate(i):
    ax.view_init(elev=20, azim=i * 4)
    return fig,

from matplotlib import animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=90, interval=200, blit=False)
plt.show()

#_______________________________________________________________________________________________________

# Ejercicio 5.
# Para los datos de 'Coactivation_matrix.mat', filtre la matriz para que, para cada nodo, se
# mantenga aquel nodo con mayor comunicación, con el nuevo arreglo muestre los nodos y vértices
# del grafo.