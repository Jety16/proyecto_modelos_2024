# Trabajo Práctico Especial - Sistema con operarios

## Introducción:
En el presente trabajo se aborda la problemática de maximizar el tiempo de vida del sistema de cajas registradoras de un supermercado. Para ello se simularán los siguientes casos de estudio:

- 1 operario, 7 máquinas en uso y 3 repuestos
- 2 operarios, 7 máquinas en uso y 3 repuestos
- 1 operario, 7 máquinas en uso y 4 repuestos

Se tomarán métricas de los resultados de estos casos (Esperanza, Desviación Estándar) para su posterior análisis y así poder determinar cuál es el sistema que mejor se adapta a las necesidades del supermercado.

## Algoritmo y descripción de las Variables:

### Constantes y variables utilizadas dentro del algoritmo
- **N**: *Número de cajas registradoras en servicio*
- **S**: *Número de cajas en reserva al inicio de la simulación*
- **OP**: *Número de operarios al inicio de la simulación*
- **available**: *Número de cajas disponibles en un momento dado de la simulación*
- **available_op**: *Operarios disponibles en un momento dado de la simulación*
- **to_repair**: *Cajas a reparar en un momento dado de la simulación*
- **break_moment**: *Lista de los tiempos en los que las cajas en servicio tendrán defectos*
- **repaired_moment**: *Momento en el que los operarios terminan de reparar las cajas defectuosas*
- **sim_time**: *Denota el paso del tiempo dentro de la simulación*
- **min_repair_position**: *Posición del tiempo de reparación más próximo*
- **min_break_position**: *Posición del tiempo de ruptura más próximo*


<div style="page-break-after: always;"></div>


### Explicación del Algoritmo
Las ideas principales utilizadas para realizar la simulación se basaron en lo provisto por el Capítulo 6 del libro "Simulación" (Segunda Edición) de S. Ross (1999).

- Simulación mediante eventos discretos
- Sistema de línea de espera con un servidor
- Sistema de línea de espera con dos servidores en paralelo

El algoritmo **sistema_rep_gen** simula el tiempo de vida de un sistema de cajas registradoras en un supermercado, considerando el numero de cajas registradoras en servicio (**N**),
cuantos operarios se tienen contratados (**OP**) y la cantidad de repuestos (**S**).

La idea general del algoritmo consiste en simular los tiempos en que ocurren 2 tipos de eventos discretos (una caja registradora sufrió un desperfecto o se terminó de reparar). En función de cuál es la categoría del próximo evento, se actualizan los valores de las variables de la simulación hasta que se cumplen las condiciones de falla del sistema (que se tengan menos de N cajas disponibles en un momento dado) y devolvemos el valor de *sim_time*, el cual representa el momento en el cual el supermercado dejo de ser operativo.

### Inicialización de variables
	avaiable = N + S
	avaiable_op = OP
	to_repair = 0
    break_moment = []
    repaird_moment = []
    sim_time = 0

### Inicialización de Tiempos de Reparación y de Falla

Para cada operario, se establece un tiempo de reparación infinito inicialmente debido a que no hay maquinas en reparacion al inicio de la simulación:

    for _ in range(OP):
        repaired_moment.append(np.inf)

<div style="page-break-after: always;"></div>


De manera similar se generan N tiempos exponenciales (con parametro igual a 1) de falla para las máquinas en uso:

    for _ in range(N):
        break_moment.append(-math.log(random()))

#### Bucle Principal de Simulación

El bucle se ejecuta mientras el número de cajas disponibles sea mayor o igual a N:

    while available >= N:

#### Determinación de la Próxima Acción:
Obtenemos los tiempos más próximos de cada tipo de evento, se terminó de reparar una máquina o una máquina sufrió un desperfecto. Luego se comparan esos tiempos para decidir cuál de los dos es el próximo evento a ocurrir en la simulación.

    min_repair_position = repaired_moment.index(min(repaired_moment))
    min_break_position = break_moment.index(min(break_moment))

    if break_moment[min_break_position] <= repaired_moment[min_repair_position]:

##### Si el próximo evento es una falla:

	to_repair += 1
    available -= 1
    sim_time = break_moment[min_break_position]
    break_moment[min_break_position] = sim_time - math.log(random())

1. Aumenta el conteo de máquinas a reparar.
2. Reduce el número de cajas disponibles.
3. Actualiza el tiempo de simulación y genera un nuevo tiempo de falla para la máquina que se está utilizando como reemplazo de la que se averió.

###### Si el próximo evento es una reparación:

    to_repair -= 1
    available += 1
    available_op += 1
    sim_time = repaired_moment[min_repair_position]
    repaired_moment[min_repair_position] = np.inf

1. Disminuye el conteo de máquinas a reparar.
2. Aumenta el número de cajas y operarios disponibles.
3. Actualiza el tiempo de simulación y establece el tiempo de reparación de la próxima máquina por parte de ese operario como infinito.

#### Asignación de Reparaciones:

Revisamos si hay operarios disponibles y si el número de máquinas a reparar es mayor que el número de operarios ocupados.

    if available_op > 0 and (to_repair > OP - available_op):

Si se cumple esta condición tomamos un operario que esté libre (el que tenga el mayor tiempo de reparación ya que este será infinito si no está reparando ninguna máquina) y le asignamos un nuevo tiempo de reparación, reduciendo el número de operarios disponibles.

        max_position = repaired_moment.index(max(repaired_moment))
        repaired_moment[max_position] = sim_time - (1/8 * math.log(random()))
        available_op -= 1

#### Retorno del Resultado

El algoritmo finaliza cuando el número de cajas registradoras disponibles es menor que N y retorna el tiempo de simulación denotando el tiempo en el que el supermercado dejó de ser operativo:

    return sim_time




<div style="page-break-after: always;"></div>



### Resultados:

A continuación, se presentan los resultados del tiempo hasta que el supermercado deja de ser operativo en meses de 10,000 simulaciones para cada caso de estudio.
Las métricas obtenidas son la esperanza, varianza y desviación estándar para cada caso de estudio.

##### Caso de Estudio 1: 1 Operario, 7 Máquinas en Uso y 3 Repuestos
![](study_case_1.png)
   - Esperanza: 1.65 meses
   - Varianza: 2.04 meses
   - Desviación Estándar: 1.43 meses

<div style="page-break-after: always;"></div>


##### Caso de Estudio 2: 2 Operarios, 7 Máquinas en Uso y 3 Repuestos
![](study_case_2.png)
   - Esperanza: 3.35 meses
   - Varianza: 10.11 meses
   - Desviación Estándar: 3.18 meses
<div style="page-break-after: always;"></div>


##### Caso de Estudio 3: 1 Operario, 7 Máquinas en Uso y 4 Repuestos
![](study_case_3.png)
   - Esperanza: 2.60 meses
   - Varianza: 5.06 meses
   - Desviación Estándar: 2.25 meses

<div style="page-break-after: always;"></div>



#### Gráfico de Medias y Desviaciones Estándar
![](media_desviation_graph.png)

#### Análisis de los Resultados

Al comparar los tres casos de estudio, se observan las siguientes características sobresalientes:

- Características Generales:
  - Presentan valores extremos muy alejados de la esperanza.
  - Tienen una alta frecuencia en los valores más bajos del gráfico.

- Caso de Estudio 1:
    - El tiempo de vida promedio del sistema (esperanza) es el más bajo.
    - Su varianza y desviación estándar son relativamente bajas, lo que indica menor variabilidad en los tiempos de vida.


<div style="page-break-after: always;"></div>



- Caso de Estudio 2:
    - El tiempo de vida promedio del sistema (esperanza) es el más alto.
    - La varianza y desviación estándar son significativamente altas, lo que indica una mayor variabilidad en los tiempos de vida.

- Caso de Estudio 3:
    - El tiempo de vida promedio del sistema (esperanza) es intermedio.
    - La varianza y desviación estándar también son intermedias, indicando una variabilidad moderada en los tiempos de vida.

### Conclusión

El análisis de los resultados muestra que, aunque el sistema con dos operarios y tres repuestos tiene el mayor tiempo de vida promedio, también presenta la mayor variabilidad. Esto se traduce en una mayor incertidumbre respecto al tiempo de vida del sistema, ya que hay casos donde que se rompan 4 maquinas en tiempos proximos al principio de la simulacion puede causar que el tiempo de vida del sistema sea menor a 1 mes. A su vez hay casos en los que las rupturas estan lo suficientemente distanciadas para que los operarios mantengan el sistema libre fallas logrando un tiempo de vida de hasta 30 meses. Por otro lado, el sistema con un operario y cuatro repuestos al tener una desviacion estandar menor nos da la capacidad de dar un intervalo mas acotado para el tiempo de vida que puede alcanzar el supermercado y por lo tanto, la estimacion tendra mayor certeza.

Si nos guiaramos solo por el tiempo de vida promedio del sistema la mejor eleccion seria el sistema con 2 operarios. Pero al tener en cuenta la varianza que presentan los dos sistemas hace que la elección de añadir un operario o aumentar en uno los repuestos dependerá de las prioridades del supermercado entre maximizar el tiempo de vida del sistema que se puede llegar a alcanzar y minimizar la variabilidad e incertidumbre de la duracion.
