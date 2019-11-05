import random
import csv
import math


def mat(texto):
	with open(texto,newline='') as csvfile:
		data=list(csv.reader(csvfile))
	return data

class nodo:
	def __init__(self,nombrep,vecinosp,pesosp):
		self.nombre=nombrep
		self.vecinos=vecinosp
		self.pesos=pesosp
		self.siguiente=None
		
	
		
	
class grafo:
	def __init__(self):
		self.capital=None
	
	def O_raiz(self):
		return self.capital
		
	def agregar(self, nodo_nuevo):
		if(self.capital==None):
			self.capital=nodo_nuevo
		else:
			aux=self.capital
			anterior=None
			while(aux!=None):
				anterior=aux
				aux=aux.siguiente
			aux=nodo_nuevo
			anterior.siguiente=aux
	
	def imprimir(self):
		aux=self.capital
		while(aux!=None):
			print(aux.nombre)
			aux=aux.siguiente
			
	def aleatorio(self):
		lista=self.capital.vecinos
		i=0
		lista_nueva=[]
		j=len(lista)
		while(i<j):
			numero=random.randint(0,len(lista)-1)
			lista_nueva.append(lista[numero])
			lista=lista[:numero]+lista[numero+1:]
			i=i+1
		return lista_nueva
		
		
	def distancia(self,nombre1,nombre2):
		aux=self.capital
		while(aux!=None):
			if(aux.nombre==nombre1):
				break;
			else:
				aux=aux.siguiente
		if(aux==None):
			return None
		i=0
		while(i<len(aux.vecinos)):
			if(aux.vecinos[i]==nombre2):
				return aux.pesos[i]
			else:
				i=i+1
		return None
		
		
	def costo_recorrer(self,lista):
		lista_pesos=0
		i=0
		j=1
		while(j<len(lista)):
			lista_pesos+=float(self.distancia(lista[i],lista[j]))
			i=i+1
			j=j+1
		return lista_pesos
		
	
def revolver(lista):
	numero1=random.randint(0,len(lista)-1)
	numero2=random.randint(0,len(lista)-1)
	dato=lista[numero1]
	lista[numero1]=lista[numero2]
	lista[numero2]=dato
	return lista
			
			


	



def crear_grafo(matriz):
	
	grafillo=grafo()
	i=1
	while(i<len(matriz)):
		no=nodo(matriz[i][0],matriz[0][1:],matriz[i][1:])
		grafillo.agregar(no)
		i=i+1

	return grafillo
	
	
def SimulatedAnnealing(grafo, temp = float("inf") , tasaenfr = 0.95):
	sol = grafo.aleatorio()
	costo=grafo.costo_recorrer(sol)
	while(temp > 0.01) :
		sol1=revolver(sol)
		costo1=grafo.costo_recorrer(sol1)
		p=math.exp((-abs(costo1-costo))/temp)
		pazar=random.uniform(0,1)
		if(costo1 < costo or pazar <= p):
			sol = sol1
			costo = costo1
			temp = temp * tasaenfr
			print(temp)
			print(costo)
	return sol
	

	
grafo_ciudades=crear_grafo(mat('ciudades_cr1.csv'))
print(SimulatedAnnealing(grafo_ciudades, temp = 2 , tasaenfr = 0.95))


