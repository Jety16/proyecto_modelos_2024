# Trabajo Practico Especial - Simulacion de sitema

### Introduccion:
En el presente trabajo se aborda la problematica de maximizar el tiempo de vida del sistema de cajas registradoras de un supermercado. Para ello se simularan los siguientes casos de estudio:

- 1 operarios, 7 maquinas en uso y 3 repuestos
- 2 operarios, 7 maquinas en uso y 3 repuestos
- 1 operarios, 7 maquinas en uso y 4 repuestos

Se tomaran metricas de los resultados de estos casos (Esperanza, Desviacion Estandar) para su posterior analisis y asi determinar cual es el sistema que mejor se adapta a las necesidades del supermercado.

### Algoritmo y descripción de las Variables:

#### Constantes y variables utilizadas dentro del algoritmo
    N: Numero de cajas registradoras en servicio (arg)
    S: Numero de cajas en reservas al inicio de la simulacion (arg)
    OP: Numero de operarios al inicio de la simulaciòn (arg)
    avaiable: Numero de cajas disponibles en un momento dado de la simulacion
    avaiable_op: Operarios disponibles en un momento dado de la simulacion
    to_repair: Cajas a reparar en un momento dado de la simulacion
    break_moment: Lista de los tiempos en los que las cajas en servicio tendran defectos
    repaird_moment: Momento en el que los operarios terminan de reparar las cajas defectuosas
    sim_time: Denota el paso del tiempo dentro de la simulacion (return)
    min_repair_position: posicion del tiempo de reparacion mas proximo (indice)
    min_break_position:  posicion del tiempo de ruptura mas proximo (indice)


#### Explicaciòn Algoritmo
La ideas principales utilizadas para realizar la simulaciòn se basaron en lo provisto por el Capítulo 6 del libro Simulación (Segunda Edición ed.) de S.Ross (1999). Estas son:
*