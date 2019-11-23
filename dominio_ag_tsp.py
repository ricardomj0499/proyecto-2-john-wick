from dominio_ag import DominioAG
from dominio_tsp import DominioTSP

class DominioAGTSP(DominioAG, DominioTSP):
    """
    Representa el objeto de dominio que conoce los detalles de implementación y modelamiento
    del problema del vendedor viajero para ser resuelto con algoritmos genéticos.

    Las soluciones se modelan como listas de enteros, donde cada número representa
    una ciudad específica. Si el grafo contiene n ciudades, la lista siempre contiene
    (n-1) elementos. La lista nunca contiene elementos repetidos y nunca contiene la 
    ciudad de inicio y fin del circuito.

    Métodos:
    generar(n)
        Construye aleatoriamente una lista de listas que representa n 
        posibles soluciones al problema.

    cruzar(sol_a, sol_b)
        Produce una nueva posible solución cruzando las dos soluciones dadas por parámetro.

    mutar(sol)
        Produce una nueva solución aplicando un ligero cambio a la solución dada por
        parámetro.
    """
    def cargar_csv(self,ubicacion):
        with open(ubicacion,newline='') as csvfile:
            data=list(csv.reader(csvfile))
        return data
    
    def __init__(self, ciudades_rutacsv, ciudad_inicio):
        """Construye un objeto de modelo de dominio para una instancia
        específica del problema del vendedor viajero para ser resuelto
        con algoritmos genéticos.

        Entradas:
        ciudades_rutacsv (str)
            Ruta al archivo csv que contiene la matriz de pesos entre las ciudades
            para las que se quiere resolver el problema del vendedor viajero.

        ciudad_inicio (str)
            Nombre de la ciudad que será el inicio y fin del circuito a calcular.

        Salidas:
            Una instancia de DominioAGTSP correctamente inicializada.
        """
        self.ciudad_inicio=ciudad_inicio
        self.matriz=self.cargar_csv(ciudades_rutacsv)
        self.diccionario=self.crear_diccionario(self.cargar_csv(ciudades_rutacsv))
	

    def generar_n(self, n):
        """Construye aleatoriamente una lista de listas que representa n 
        posibles soluciones al problema.

        Entradas:
        n (int)
            Número de soluciones aleatorias a generar.

        Salidas:
        (list) Lista que contiene n listas, cada una representando
        una posible solución al problema modelado por el objeto de dominio.
        """
        resp=[]
        for i in range(n):
            resp+=[DominioTSP.generar(self)]
        return resp
    

    def cruzar(self, sol_a, sol_b):
        """Produce una nueva posible solución cruzando las dos soluciones dadas por parámetro.

        Entradas:
        sol_a (estructura de datos)
            Estructura de datos que modela la solución antecesora A que será cruzada con la B

        sol_b (estructura de datos)
            Estructura de datos que modela la solución antecesora B que será cruzada con la A

        Salidas:
        (estructura de datos) Una nueva solución producto del cruzamiento entre las soluciones A y B
        """
        #print(sol_a)
        resp=[]
        aleatorio=random.randint(0,len(sol_a))
        resp+=sol_a[:aleatorio]+sol_b[aleatorio:]
        return resp

    def mutar(self, sol):
        """Produce una nueva solución aplicando un ligero cambio a la solución dada por
        parámetro.

        Entradas:
        sol (estructura de datos)
            La solución a mutar.
        
        Salidas:
        (estructura de datos) Una nueva solución que refleja un ligero cambio con respecto 
        a la solución dada por parámetro
        """
        mutacion=DominioTSP.swap_random(self,sol)
        return mutacion
        
        
    def mergeSort_doble(self,lista,lista2):
        if(len(lista)!=len(lista2)):
            return "error malos tamanos"
        if(len(lista)>1):
            mitad=(len(lista))//2
            
            ListaSubA=lista[:mitad]
            ListaSubB=lista[mitad:]
            
            ListaSubA2=lista2[:mitad]
            ListaSubB2=lista2[mitad:]
            
            self.mergeSort_doble(ListaSubA,ListaSubA2)
            self.mergeSort_doble(ListaSubB,ListaSubB2)
            
            i=0
            j=0
            p=0
            
            while((i<len(ListaSubA)) and (j<len(ListaSubB))):
                if(ListaSubA[i]<ListaSubB[j]):
                    lista[p]=ListaSubA[i]
                    lista2[p]=ListaSubA2[i]
                    i+=1
                else:
                    lista[p]=ListaSubB[j]
                    lista2[p]=ListaSubB2[j]
                    j+=1
                p+=1
                #print(lista)
            while(i<len(ListaSubA)):
                lista[p]=ListaSubA[i]
                lista2[p]=ListaSubA2[i]
                i+=1
                p+=1
            while(j<len(ListaSubB)):
                lista[p]=ListaSubB[j]
                lista2[p]=ListaSubB2[j]
                j+=1
                p+=1
            return []+[lista2]+[lista]
