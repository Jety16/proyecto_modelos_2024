 # Trabajo Practico Especial - Simulación de sistema
 
 ## Introducción:
 En el presente trabajo se aborda la problemática de maximizar el tiempo de vida del sistema de cajas registradoras de un supermercado. Para ello se simularan los siguientes casos de estudio:
 
 - 1 operarios, 7 maquinas en uso y 3 repuestos
 - 2 operarios, 7 maquinas en uso y 3 repuestos
 - 1 operarios, 7 maquinas en uso y 4 repuestos
 
 Se tomaran metricas de los resultados de estos casos (Esperanza, Desviacion Estandar) para su posterior analisis y asi determinar cual es el sistema que mejor se adapta a las necesidades del supermercado.
 
 ## Algoritmo y descripción de las Variables:
 
 ### Constantes y variables utilizadas dentro del algoritmo
- **N**: *Numero de cajas registradoras en servicio*
- **S:** *Numero de cajas en reservas al inicio de la simulacion*
- **OP:** *Numero de operarios al inicio de la simulaciòn*
- **avaiable**: *Numero de cajas disponibles en un momento dado de la simulacion*
- **avaiable_op**: *Operarios disponibles en un momento dado de la simulacion*
- **to_repair**: *Cajas a reparar en un momento dado de la simulacion*
- **break_moment**: *Lista de los tiempos en los que las cajas en servicio tendran defectos*
- **repaird_moment**: *Momento en el que los operarios terminan de reparar las cajas defectuosas*
- **sim_time**: *Denota el paso del tiempo dentro de la simulacion*
- **min_repair_position**: *posicion del tiempo de reparacion mas proximo*
- **min_break_position**: * posicion del tiempo de ruptura mas proximo*
 
 
 ## Explicación Algoritmo
 Las ideas principales utilizadas para realizar la simulación se basaron en lo provisto por el Capítulo 6 del libro Simulación (Segunda Edición ed.) de S.Ross (1999).
 
- Simulación mediante eventos discretos
- Sistema de linea de espera con un servidor
- Sistema de linea de espera con dos servidores en paralelo

El algoritmo **sistema_rep_gen** simula el tiempo de vida de un sistema de cajas registradoras en un supermercado, considerando el número de operarios y la disponibilidad de repuestos.
Consiste en ir avanzando en eventos discretos de 2 tipos (ocurrió un desperfecto o se termino de reparar una caja registradora). En función de cual es la categoria del proximo evento se actualizan los valores de las variables de la simulación hasta que se cumplen las condiciones de falla del sistema y devolvemos el valor *sim_time* el cual representa el tiempo total que duró la simulación

#### Parámetros de Entrada


    N (int): Número de máquinas en uso.
    S (int): Número de repuestos disponibles.
    OP (int): Número de operarios disponibles.

#### Variables Iniciales

    avaiable = N + S  # Cajas disponibles
    avaiable_op = OP  # Operarios 

#### Cajas a Reparar:

    to_repair = 0  # Cajas a reparar

#### Tiempos de Falla y Reparación:

    break_moment = []  # Lista de los tiempos en los que las cajas tuvieron defectos
    repaird_moment = [] # Momento en el que los operarios terminan de reparar las cajas

#### Tiempo de Simulación:
    sim_time = 0 # Denota el paso del tiempo dentro de la simulacion
#### Inicialización de Tiempos de Reparación

Para cada operario, se establece un tiempo de reparación infinito inicialmente:

    for _ in range(OP):
        repaird_moment.append(np.inf)

#### Generación de Tiempos de Falla

Se generan N tiempos exponenciales de falla para las máquinas en uso:

    for _ in range(N):
        break_moment.append(-math.log(random()))

#### Bucle Principal de Simulación

El bucle se ejecuta mientras el número de cajas disponibles sea mayor o igual a N:

    while avaiable >= N:

#### Determinación de la Próxima Acción:
Encuentra las posiciones de la máquina con el menor tiempo de reparación y la máquina con el menor tiempo de falla:

    min_repair_position = repaird_moment.index(min(repaird_moment))
    min_break_position = break_moment.index(min(break_moment))

#### Comparación de Tiempos:
Si el próximo evento es una falla:

    if break_moment[min_break_position] <= repaird_moment[min_repair_position]:

Aumenta el conteo de máquinas a reparar.
Reduce el número de cajas disponibles.
Actualiza el tiempo de simulación y genera un nuevo tiempo de falla para la máquina.

    to_repair += 1
    avaiable -= 1
    sim_time = break_moment[min_break_position]
    break_moment[min_break_position] = sim_time - math.log(random())

#### Si el próximo evento es una reparación:
Disminuye el conteo de máquinas a reparar.
Aumenta el número de cajas y operarios disponibles.
Actualiza el tiempo de simulación y establece el tiempo de reparación de la máquina a infinito.

    to_repair -= 1
    avaiable += 1
    avaiable_op += 1
    sim_time = repaird_moment[min_repair_position]
    repaird_moment[min_repair_position] = np.inf

#### Asignación de Reparaciones:

Si hay máquinas para reparar y operarios disponibles, asigna una reparación:

    if avaiable_op > 0 and to_repair > 0:

Encuentra la posición del tiempo de reparación máximo y asigna un nuevo tiempo de reparación.
Reduce el número de operarios disponibles.

        max_position = repaird_moment.index(max(repaird_moment))
        repaird_moment[max_position] = sim_time - (1/8 * math.log(random()))
        avaiable_op -= 1

#### Retorno del Resultado

El algoritmo finaliza y retorna el tiempo de simulación:
    
    return sim_time


### Resultados: 
#### Histogramas de Resultados

A continuación, se presentan los histogramas de los resultados de 10,000 simulaciones para cada caso de estudio:

* Caso de Estudio 1: 1 Operario, 7 Máquinas en Uso y 3 Repuestos

* Caso de Estudio 2: 2 Operarios, 7 Máquinas en Uso y 3 Repuestos

* Caso de Estudio 3: 1 Operario, 7 Máquinas en Uso y 4 Repuestos

#### Comparación de Métricas

Se presentan las métricas obtenidas (esperanza, varianza, desviación estándar) para cada caso de estudio:
##### Caso de Estudio 1: 1 Operario, 7 Máquinas en Uso y 3 Repuestos
![[study_case_1.png]]
    Esperanza: 1.65
    Varianza: 2.04
    Desviación Estándar:  1.43

##### Caso de Estudio 2: 2 Operarios, 7 Máquinas en Uso y 3 Repuestos
![[study_case_2.png]]
    Esperanza:  4.51
    Varianza: 19.60
    Desviación Estándar: 4.43

##### Caso de Estudio 3: 1 Operario, 7 Máquinas en Uso y 4 Repuestos
![[study_case_3.png]]
    Esperanza: 2.61
    Varianza: 5.13
    Desviación Estándar: 2.26

A continuación se presenta un gráfico comparativo de las medias y desviaciones estándar de los tiempos de vida y desviación estándar del sistema para los tres casos de estudio:

#### Gráfico de Medias y Desviaciones Estándar
![[media_desviation_graph.png]]
#### Análisis de los Resultados

Al comparar los tres casos de estudio, se observan las siguientes características sobresalientes:

    Caso de Estudio 1:
        Tiempo de vida promedio del sistema (esperanza) es el más bajo.
        Varianza y desviación estándar son relativamente bajas, lo que indica menor variabilidad en los tiempos de vida.

    Caso de Estudio 2:
        Tiempo de vida promedio del sistema (esperanza) es el más alto.
        Varianza y desviación estándar son significativamente altas, lo que indica una mayor variabilidad en los tiempos de vida.

    Caso de Estudio 3:
        Tiempo de vida promedio del sistema (esperanza) es intermedio.
        Varianza y desviación estándar también son intermedias, indicando una variabilidad moderada en los tiempos de vida.

### Conclusión

El análisis de los resultados muestra que, aunque el sistema con dos operarios y tres repuestos tiene el mayor tiempo de vida promedio, también presenta la mayor variabilidad. Esto podría traducirse en una mayor incertidumbre respecto al tiempo de vida del sistema. Por otro lado, el sistema con un operario y cuatro repuestos ofrece una mejora significativa en el tiempo de vida promedio en comparación con un solo operario y tres repuestos, con una variabilidad moderada.

La elección del sistema óptimo dependerá de las prioridades del supermercado entre maximizar el tiempo de vida del sistema y minimizar la variabilidad e incertidumbre.