import math
import random
def optimizar(dominio, tam_pobl, porc_elite, prob_mut, reps):
    """Algoritmo genético para optimización estocástica.

    Entradas:
    dominio (DominioAG)
        Un objeto que modela el dominio del problema que se quiere aproximar.
    
    tam_pobl (int)
        Tamaño de la población.
    
    porc_elite (float)
        Porcentaje de la población que se tomará como elite.
    
    prob_mut (float)
        Probabilidad de mutación, debe estar en el rango [0, 1]
    
    reps (int)
        Número de iteraciones a ejecutar.

    Salidas:
        (estructura de datos) Estructura de datos según el dominio, que representa una
        aproximación a la mejor solución al problema.
    """
    pobl=dominio.generar_n(tam_pobl)
    aptitud_de_poblacion=[]
    while(reps>0):
        for i in(pobl):
            #print(pobl)
            aptitud_de_poblacion.append(dominio.fcosto(i))
        #print(len(aptitud_de_poblacion))
        #print(len(pobl))
        ordenar=dominio.mergeSort_doble(aptitud_de_poblacion,pobl)
        #print(ordenar)
        #print(ordenar)
        pobl=ordenar[0]
        aptitud_de_poblacion=ordenar[1]
        tamano_poblacion=len(pobl)
        num_padres=math.floor((tamano_poblacion*porc_elite))
        num_hijos=(tamano_poblacion-num_padres)
        sig_gen=pobl[0:num_padres]
        decendencia=[]
        while(num_hijos>0):
            #print(sig_gen)
            padre_a=random.choice(sig_gen)
            padre_b=random.choice(sig_gen)
            hijo=dominio.cruzar(padre_a,padre_b)
            p=random.uniform(0,1)
            if(p<=prob_mut):
                hijo=dominio.mutar(hijo)
            decendencia+=[hijo]
            #print(hijo)
            num_hijos-=1
        pobl=sig_gen+decendencia
        aptitud_de_poblacion=[]
        #print(reps)
        reps-=1
		
	
	#dominio.ordenar(pobl,llave=aptitud)
			
    # Pendiente: implementar este método
    #pass
