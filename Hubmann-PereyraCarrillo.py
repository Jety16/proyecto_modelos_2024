from random import random
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

def sistema_rep_gen(N, S, OP):
    avaiable = N + S  # Cajas disponibles
    avaiable_op = OP  # Operarios disponibles
    to_repair = 0  # Cajas a reparar
    break_moment = []  # Lista de los tiempos en los que las cajas tuvieron defectos
    repaird_moment = [] # Momento en el que los operarios terminan de reparar las cajas
    sim_time = 0 # Denota el paso del tiempo dentro de la simulacion

    for _ in range(OP):
        # inicializacion de los tiempos de reparacion de las cajas
        repaird_moment.append(np.inf)

    for _ in range(N):
        # Generamos las N exponenciales y las colocamos en la lista break_moment
        # Estas Exponenciales denotan los tiempos donde las cajas tuvieron defectos
        break_moment.append((-math.log(random())))

    while avaiable >= N:  # Verificamos guarda de fallo del sistema, si tenemos menos de N maquinas funcionales, paramos
        min_repair_position = repaird_moment.index(min(repaird_moment))
        min_break_position = break_moment.index(min(break_moment))
        if break_moment[min_break_position] <= repaird_moment[min_repair_position]:
            # Se Rompio una maquina antes de que se termine de reparar una
            to_repair += 1
            avaiable -= 1
            sim_time = break_moment[min_break_position]
            break_moment[min_break_position] = sim_time - math.log(random())
        else:
            # Se termino de reparar una maquina antes de que se rompa otra
            to_repair -= 1
            avaiable += 1
            avaiable_op += 1
            sim_time = repaird_moment[min_repair_position]
            repaird_moment[min_repair_position] = np.inf

        if avaiable_op > 0 and (to_repair > OP - avaiable_op):
            # Hay maquinas para reparar y el operario esta libre
            max_position = repaird_moment.index(max(repaird_moment))
            repaird_moment[max_position] = sim_time - (1/8 * math.log(random()))
            avaiable_op -= 1

    return sim_time

def sistema_rep_ej1(N, S):
    return sistema_rep_gen(N,S,1)

# Calculo esperanza, variacion y desviacion estandar de los distintos casos de estudio

def statics(N,S,OP):
    sum = 0
    sum_cuadrados = 0
    n_sim = 10_000
    results = []
    for _ in range(n_sim):
        res_sim = sistema_rep_gen(N, S, OP)
        results.append(res_sim)
        sum += res_sim
        sum_cuadrados += res_sim**2
    esperanza = sum/ n_sim
    varianza = (sum_cuadrados/n_sim - esperanza**2)
    print(F"\nCaso de estudio con {OP} operarios, {N} maquinas en uso y {S} repuestos")
    print(f"Esperanza: {esperanza} meses")
    print(f"Varianza: {varianza} meses")
    print(f"Desviacion estandar: {np.sqrt(varianza)} meses")
    print('------------------------')
    return esperanza, np.sqrt(varianza), results


casos_de_estudio = [[7,3,1], [7,3,2], [7,4,1]]
results = []    # used for making the graph of the esperanza and desviación estandar
another_results = []    # used for making the histogram of the results
i = 0
for value in casos_de_estudio:
    esperanza, desviacion_estandar, sim_result = statics(*value)
    # This will graph the results of each simualtion
    plt.figure(figsize=(10, 6))
    plt.hist(sim_result, bins=175, alpha=0.75, color='skyblue', edgecolor='black')
    plt.title(f'Histograma de Resultados con - N: {value[0]}, OP: {value[2]}, S: {value[1]}')
    plt.xlabel('Tiempo de Falla del Sistema en Meses')
    plt.ylabel('Frecuencia')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xticks(range(0, 32, 1))
    plt.show()
    i +=1

    # This will graph the esperanza and desviación estandar
    results.append({'N': value[0], 'S': value[1], 'OP': value[2], 'Media': esperanza, 'Desviación Estándar': desviacion_estandar})
    another_results.append(sim_result)

# Generate some sample data
data = another_results

# Create a box plot
plt.figure(figsize=(10, 6))
plt.boxplot(data, patch_artist=True, vert=False,
            boxprops=dict(facecolor='lightblue', color='black'),  # color of box and outline
            whiskerprops=dict(color='black', linewidth=2),  # color and thickness of whiskers
            capprops=dict(color='black', linewidth=2),  # color and thickness of caps
            medianprops=dict(color='black', linewidth=2),  # color and thickness of median line
            flierprops=dict(marker='o', markersize=6, markerfacecolor='red'))  # style of outliers)

# Customizing the plot
plt.title('Comparación de los tiempos de falla del sistema en cada simulación')
plt.xlabel('Tiempo de Falla del Sistema en Meses')
plt.xticks(range(0, 36, 1))
plt.ylabel('Casos de estudio: Operarios (OP) y Repuestos (S)')
plt.yticks([1, 2, 3], ['OP: 1, S: 3', 'OP: 2, S: 3', 'OP: 1, S: 4'])

# Add mean points and standard deviation lines
for i in range(len(results)):
    # Mean point
    media_muestral = results[i]['Media']
    desviacion_estandar = results[i]['Desviación Estándar']

    # Standard deviation lines
    plt.plot([media_muestral- desviacion_estandar , media_muestral + desviacion_estandar], [i + 1, i + 1], 'g-', linewidth=3)  # green line
    plt.plot(media_muestral, i + 1,'b*', color = "purple", markersize=10)  # red star

# Display the plot
plt.show()
