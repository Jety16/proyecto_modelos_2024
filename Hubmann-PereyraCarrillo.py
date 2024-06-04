from random import random
import numpy as np
import math

INF = 2**20

def sistema_rep_gen(N, S, OP):
    avaiable = N + S  # Cajas disponibles
    avaiable_op = OP  # Operarios disponibles
    to_repair = 0  # Cajas a reparar
    break_moment = []  # Lista de los tiempos en los que las cajas tuvieron defectos
    repaird_moment = [] # Momento en el que los operarios terminan de reparar las cajas
    sim_time = 0 # Denota el paso del tiempo dentro de la simulacion

    for _ in range(OP):
        # inicializacion de los tiempos de reparacion de las cajas
        repaird_moment.append(INF)

    for _ in range(N):
        # Generamos las N exponenciales y las colocamos en la lista break_moment
        # Estas Exponenciales denotan los tiempos donde las cajas tuvieron defectos
        break_moment.append((-math.log(random())))
    break_moment.sort()

    while avaiable >= N:  # Verificamos guarda de fallo del sistema, si tenemos menos de N maquinas funcionales, paramos
        min_repair_position = repaird_moment.index(min(repaird_moment))
        if break_moment[0] <= repaird_moment[min_repair_position]:
            # Se Rompio una maquina antes de que se termine de reparar una
            to_repair += 1
            avaiable -= 1
            sim_time = break_moment[0]
            break_moment[0] = sim_time - math.log(random())
            break_moment.sort()
        else:
            # Se termino de reparar una maquina de que se rompa otra
            to_repair -= 1
            avaiable += 1
            avaiable_op += 1
            sim_time = repaird_moment[min_repair_position]
            repaird_moment[min_repair_position] = INF

        if avaiable_op > 0 and to_repair > 0:
            # Hay maquinas para reparar y el operario esta libre
            max_position = repaird_moment.index(max(repaird_moment))
            repaird_moment[max_position] = sim_time - (1/8 * math.log(random()))
            avaiable_op -= 1

    return sim_time

def sistema_rep_ej1(N, S):
    return sistema_rep_gen(N,S,1)

# Calculo esperanza, variacion y desviacion estandar de los distintos casos de estudio

e = 0
sum_cuadrados = 0
n_sim = 10_000
for _ in range(n_sim):
    res_sim = sistema_rep_ej1(7, 3)
    e += res_sim
    sum_cuadrados += res_sim**2
esperanza = e/ n_sim
varianza = (sum_cuadrados/n_sim - esperanza**2)
print("Caso de estudio con 1 operarios, 7 maquinas en uso y 3 repuestos")
print(f"Esperanza: {esperanza}")
print(f"Varianza: {varianza}")
print(f"Desviacion estandar: {np.sqrt(varianza)}")
print('------------------------')



e = 0
sum_cuadrados = 0
for _ in range(n_sim):
    res_sim = sistema_rep_gen(7, 3, 2)
    e += res_sim
    sum_cuadrados += res_sim**2
esperanza = e/ n_sim
varianza = (sum_cuadrados/n_sim - esperanza**2)
print("Caso de estudio con 2 operarios, 7 maquinas en uso y 3 repuestos")
print(f"Esperanza: {esperanza}")
print(f"Varianza: {varianza}")
print(f"Desviacion estandar: {np.sqrt(varianza)}")
print('------------------------')

e = 0
sum_cuadrados = 0
for _ in range(n_sim):
    res_sim = sistema_rep_gen(7, 4, 1)
    e += res_sim
    sum_cuadrados += res_sim**2
esperanza = e/ n_sim
varianza = (sum_cuadrados/n_sim - esperanza**2)
print("Caso de estudio con 1 operarios, 7 maquinas en uso y 4 repuestos")
print(f"Esperanza: {esperanza}")
print(f"Varianza: {varianza}")
print(f"Desviacion estandar: {np.sqrt(varianza)}")
print('------------------------')



