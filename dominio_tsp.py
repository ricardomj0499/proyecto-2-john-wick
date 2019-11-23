from dominio import Dominio
import csv   #agregada por desarrollador
import random#agregada por desarrollador

class DominioTSP(Dominio):
    """
    Esta clase modela el dominio del problema del Vendedor Viajero para su resolución
    con algoritmos probabilísticos.

    Las soluciones se modelan como listas de enteros, donde cada número representa
    una ciudad específica. Si el grafo contiene n ciudades, la lista siempre contiene
    (n-1) elementos. La lista nunca contiene elementos repetidos y nunca contiene la 
    ciudad de inicio y fin del circuito.

    Métodos:
    generar()
        Construye aleatoriamente una lista que representa una posible solución al problema.

    fcosto(sol)
        Calcula el costo asociado con una solución dada.

    vecino(sol)
        Calcula una solución vecina a partir de una solución dada.

    validar(sol)
        Valida que la solución dada cumple con los requisitos del problema.

    texto(sol)
        Construye una representación en hilera legible por humanos de la solución
        con el fin de reportar resultados al usuario final.
    """
    def cargar_csv(self,ubicacion):
        with open(ubicacion,newline='') as csvfile:
            data=list(csv.reader(csvfile))
        return data
	
    def crear_diccionario(self,matriz):
        lista=matriz[0][1:]
        dic={}
        for x in range(len(lista)):
            dic1={lista[x]:x}
            dic.update(dic1)
        return dic

    def __init__(self, ciudades_rutacsv, ciudad_inicio):
        """Construye un objeto de modelo de dominio para una instancia
        específica del problema del vendedor viajero.

        Entradas:
        ciudades_rutacsv (str)
            Ruta al archivo csv que contiene la matriz de pesos entre las ciudades
            para las que se quiere resolver el problema del vendedor viajero.

        ciudad_inicio (str)
            Nombre de la ciudad que será el inicio y fin del circuito a calcular.

        Salidas:
            Una instancia de DominioTSP correctamente inicializada.
        """
        self.ciudad_inicio=ciudad_inicio
        self.matriz=self.cargar_csv(ciudades_rutacsv)
        self.diccionario=self.crear_diccionario(self.cargar_csv(ciudades_rutacsv))
        

	
	
    def existe_ciudad(self,ciudad,lista):
        l=len(lista)
        for i in range(1,l):
            if(ciudad==lista[i]):
                return True
        return False
        
    def existen_repetidos(self,lista):
	#True si hay repetidos, false si no lo hay
        a=set(lista)
        if(list(a)!=lista):
            return True
        else:
        	return False
	
    def validar(self, sol):
        """Valida que la solución dada cumple con los requisitos del problema.

        Si n es el número de ciudades en el grafo, la solución debe:
        - Tener tamaño (n-1)
        - Contener sólo números enteros menores que n (las ciudades se numeran de 0 a (n-1))
        - No contener elementos repetidos
        - No contener la ciudad de inicio/fin del circuito

        Entradas:
        sol (list)
            La solución a validar.

        Salidas:
        (bool) True si la solución es válida, False en cualquier otro caso
        """
	cp=self.ciudad_inicio
        matriz=self.matriz
        ciudades=matriz[1:]
        if(len(sol)>=len(ciudades)):
            return False
        for i in(sol):
            if(type(int(i))!=int):
                return False
        if(self.existen_repetidos(sol)==True):
            return False
        numero_ci=self.diccionario.get(self.ciudad_inicio)
        print(numero_ci)
        for i in(sol):
            if(i==numero_ci):
                return False
        return True

       
    def pasar_texto_numero(self,lista):
        dic=self.diccionario
        lista2=[]
        for x in lista:
            for key in dic:
                if(key==x):
                    lista2.append(dic[key])
        #print(dic)
        return lista2    

    def texto(self, sol):
        """Construye una representación en hilera legible por humanos de la solución
        con el fin de reportar resultados al usuario final.

        La hilera cumple con el siguiente formato:
        Nombre ciudad inicio -> Nombre ciudad 1 -> ... -> Nombre ciudad n -> Nombre ciudad inicio

        Entradas:
        sol (list)
            Solución a representar como texto legible

        Salidas:
        (str) Hilera en el formato mencionado anteriormente.
        """

        texto=self.pasar_de_numero_texto(sol)
        cd=self.ciudad_inicio
        return cd+texto+cd

    def generar(self):
        """Construye aleatoriamente una lista que representa una posible solución al problema.

        Entradas:
        ninguna

        Salidas:
        (list) Una lista que representa una solución válida para esta instancia del vendedor viajero
        """
	ciudades=self.matriz[0]
        cd=self.ciudad_inicio
        solucion=[]
        for i in ciudades:
            if(i!=cd):
                solucion+=[i]
        solucion=solucion[1:]
        solucion=self.pasar_texto_numero(solucion)
        random.shuffle(solucion)
        return solucion

    def distancia_entre_2_ciudades(self,matriz,c1,c2):
        """Este metodo calcula la distancia entre dos ciudades"""
        ciudades=self.matriz[0]
        p1=0
        p2=0
        for i in ciudades:
            if(i==c1):
                break
            p1+=1
        for j in ciudades:
            if(j==c2):
                break	
            p2+=1
        return float(matriz[p1][p2])

    def fcosto(self, sol):
        """Calcula el costo asociado con una solución dada.

        Entradas:
        sol (list)
            Solución cuyo costo se debe calcular

        Salidas:
        (float) valor del costo asociado con la solución
        """
	ci=self.ciudad_inicio
        numero_ci=self.diccionario.get(ci)
        sol=[numero_ci]+sol+[numero_ci]
        matriz=self.matriz
        resp=0
        l=len(sol)
        i=0
        j=1
        while(j<l):
            resp+=float(matriz[int(sol[i])+1][int(sol[j])+1])
            i+=1
            j+=1
        return resp


    def swap(self,lista,p1,p2):
        temp=lista[p1]
        lista[p1]=lista[p2]
        lista[p2]=temp
        return lista
	
    def swap_random(self,lista):
        a=random.randint(0,len(lista)-1)
        b=random.randint(0,len(lista)-1)
        self.swap(lista,a,b)
        return lista

    def vecino(self, sol):
        """Calcula una solución vecina a partir de una solución dada.

        Una solución vecina comparte la mayor parte de su estructura con 
        la solución que la origina, aunque no son exactamente iguales. El 
        método transforma aleatoriamente algún aspecto de la solución
        original.

        Entradas:
        sol (list)
            Solución a partir de la cual se originará una nueva solución vecina

        Salidas:
        (list) Solución vecina
        """
        a=self.diccionario.get(self.ciudad_inicio)
        l=len(sol)-1
        c=sol[1:l]
        v=self.swap_random(c)
        return [a]+v+[a]
