# EJERCICIOS DE GRAFOS
# Del .mat file de coativation_matrix, realizar los siguientes ejercicios:

# 1) Crear un dataframe con la información del ndarray de coativation_matrix,
# las columnas deben ser números desde el 1, los índices deben ser iguales a
# las columnas.

# 2) Mostrar el heatmap de coativation_matrix.

# 3) Crear un dataframe subconjunto del dataframe anterior que contenga de
# la fila 10 a la 30 y de la columna 10 a la 30.

# 4) Mostrar el heatmap del nuevo dataframe.

# 5) Crear el grafo dirigido del nuevo dataframe.

# 6) ¿Qué nodo tiene más conexiones del nuevo dataset?

# 7) Del dataframe con el array de coactivation_matrix, calcular los quantiles
# 0.25, 0.5, 0.75 de los valores de los datos (quantiles de las conexiones).

# 8) Mostrar el histograma de distriibución de valores de la matriz de coactivación.

# 9) Filtra el nuevo dataframe usando como threshold  el valor de cero, es decir,
# binarizar la matriz de activación con valores mayores a cero.

# EJERCICIO DEL ARCHIVO FVE32.MAT

# 1) Muestra el heatmap de la matriz de activación.

# 2) Utilizando los nombres del archivo .mat, muestra el grafo en 4 formas distintas
# (shell debe ser una de ellas).

# 3) Determina el nodo con mayores conexiones.

# 4) Muestra el grado solo destacando las conexiones del nodo encontrado en el
# ejercicio anterior.

# EJERCICIO

# 1) Generar un número aleatorio entero en el rango [-3, 3] con seed=5002.
import random
random.seed(5002)
numero_entero = random.randint(-3, 3)
print("Número entero aleatorio:", numero_entero)

# 2) Generar un número aleatorio flotante en el rango [-10, 10] con seed=5002.
import random
random.seed(5002)
numero_flotante = random.uniform(-10, 10)
print("Número flotante aleatorio:", numero_flotante)

# 3) Genera un array de 1000 números con distribución normal, con mu= ej1, y
# sigma= ej2.
import numpy as np
mu= numero_entero #Parametros de la distribución
sigma= numero_flotante #Parametros de la distribución
numeros = np.random.normal(mu, sigma, 1000)
print("Total de números generados", len(numeros))
print("Mu:", mu, "Sigma:", sigma)


# 4) Plotear la distribución de los 1000 números y # 5) Calcular el valor de 1sigma, 2sigma, 3sigma.
import numpy as np
import matplotlib.pyplot as plt
media = np.mean(numeros)
desviacion_estandar = np.std(numeros)
#Calculamos los rangos de 1sigma, 2sigma, 3sigma.
sigma_1 = (media - desviacion_estandar, media + desviacion_estandar)
sigma_2 = (media - 2 * desviacion_estandar, media + 2 * desviacion_estandar)
sigma_3 = (media - 3 * desviacion_estandar, media + 3 * desviacion_estandar)
print("1σ:", sigma_1)
print("2σ:", sigma_2)
print("3σ:", sigma_3)
#Hacemos el histograma de la distribución
plt.hist(numeros, bins=30, density=True, alpha=0.6, color='blue')
plt.axvline(sigma_1[0], color='orange', linestyle='--', label='-1σ')
plt.axvline(sigma_1[1], color='orange', linestyle='--', label='+1σ')
plt.axvline(sigma_2[0], color='green', linestyle='--', label='-2σ')
plt.axvline(sigma_2[1], color='green', linestyle='--', label='+2σ')
plt.axvline(sigma_3[0], color='red', linestyle='--', label='-3σ')
plt.axvline(sigma_3[1], color='red', linestyle='--', label='+3σ')
#Añadimos leyendas del histograma
plt.title("Distribución de los 1000 Números Generados")
plt.xlabel("Valor")
plt.ylabel("Densidad de Probabilidad")
plt.legend()
plt.show()



# 6) Calcular el porcentaje de números que están en el rango [-1sigma, 1sigma].

# 7) Calcular el porcentaje de números que están en el rango [-2sigma, 2sigma].

# 8) Calcular el porcentaje de números que están en el rango [-3sigma, 3sigma].

# 9) Crear una función que reciba un entero (mu), un flotante (sigma) y un entero
# (total de números) y: genere array de números con distribución normal, con mu,
# y sigma. Plotee la distribución, calcule los sigmas, calcule el porcentaje de
# números que están en los rangos de +-1sigmam +-2sigma, +-3sigma.

# 10) Usar la función anterior con los valores (0, 1., 1000), (3, 5, 5000),
# (-3, 3, 10000)