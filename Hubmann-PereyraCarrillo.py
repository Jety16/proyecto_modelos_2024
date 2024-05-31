from random import random
import numpy as np
import math

INF = 2**20


def sistema_rep_ej1(N, S):
    avaiable = N + S  # Cajas disponibles
    to_repair = 0  # Cajas a reparar
    break_moment = []  # Lista de los tiempos en los que las cajas tuvieron defectos
    repaird_moment = INF # Momento en el q
    sim_time = 0 # Denota el paso del tiempo dentro de la simulacion

    for _ in range(N):
        # Generamos las N exponenciales y las colocamos en la lista break_moment
        # Estas Exponenciales denotan los tiempos donde las cajas tuvieron defectos
        break_moment.append((-math.log(random())))
    break_moment.sort()

    while avaiable >= N:  # Verificamos guarda de fallo del sistema, si tenemos menos de N maquinas funcionales, paramos
        ## print("\n", avaiable, break_moment[0], repaird_moment, to_repair, sim_time)
        if break_moment[0] <= repaird_moment:
            to_repair += 1
            # Se Rompio una maquina antes de que se termine de reparar una
            avaiable -= 1 
            sim_time = break_moment[0]
            break_moment[0] = sim_time - math.log(random())
            break_moment.sort()
        else:
            # Se termino de reparar una maquina de que se rompa otra
            to_repair -= 1
            avaiable += 1
            sim_time = repaird_moment
            repaird_moment = INF
        if repaird_moment == INF and to_repair > 0:
            # Hay maquinas para reparar y el operario esta libre 
            repaird_moment = sim_time - (1/8 * math.log(random()))
        ## print(avaiable, break_moment[0], repaird_moment, to_repair, sim_time)



    return sim_time

e = 0
sum_cuadrados = 0
n_sim = 10_000
a = 0
for _ in range(n_sim):
    res_sim = sistema_rep_ej1(7, 3)
    e += res_sim
    sum_cuadrados += res_sim**2
esperanza = e/ n_sim

print(f"Esperanza: {esperanza}")
print(f"Varianza: {(sum_cuadrados/n_sim - esperanza**2)}")
print('------------------------')

