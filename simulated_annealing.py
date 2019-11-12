#def optimizar(dominio, temperatura = 10e32, tasa_enfriamiento = 0.95):
    """Algoritmo de optimización estocástica simulated annealing.

    Entradas:
    dominio (Dominio)
        Un objeto que modela el dominio del problema que se quiere aproximar.

    temperatura (float/int)
        Temperatura inicial del algoritmo, se recomienda un número alto

    tasa_enfriamiento (float)
        Porcentaje de enfriamiento de la temperatura durante cada iteración, el valor
        por defecto es 0.95, lo que indica una tasa de enfriamiento del 5%.

    Salidas:
        (estructura de datos) Estructura de datos según el dominio, que representa una
        aproximación a la mejor solución al problema.
    """
import math  
import random
import time

    def optimizar(dominio, temperatura=10e26,tasa_enfriamiento=0.999999):
        sol=dominio.generar()
	    costo=dominio.fcosto(sol)
        while(temperatura>=0.001):
            sol_prima=dominio.vecino(sol)
            costo_prima=dominio.fcosto(sol_prima)
            p=math.exp(-abs(costo_prima-costo)/temperatura)
            p_azar= random.randint(0,1)
            #print("uno: "+str(costo)+".....dos: "+str(costo_prima))
            if(costo_prima<=costo or p_azar<p):
                sol=sol_prima
                costo=costo_prima	
            temperatura=temperatura*tasa_enfriamiento
            #print(temperatura)
        return "Solucion: "+str(sol)+"\nCosto: "+str(costo)
    
    
