#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 14:28:06 2017

@author: chomi
"""
import math
#relleno la matriz Fila_elementos
z=0
Fila_elementos={}
Archivo1=open('aspa_elementos.txt','r')

for linea in Archivo1:
    A=linea.split()
    Fila_elementos[z]=A
    z=z+1

Archivo1.close()
numero_triangulos=z

#relleno la matriz Fila_nodos
Archivo2=open('aspa_nodos.txt','r')
Fila_nodos={}
c=0

for linea in Archivo2:
    B=linea.split()
    Fila_nodos[c]=B
    #print(Fila_nodos[c])
    c=c+1 
Archivo2.close()
#matriz densidades como diccionario 
densidad=[[1.46*math.exp(-6),10],[1.46*math.exp(-6),10],[1.84*math.exp(-6),20],[1.84*math.exp(-6),20],[1.79*math.exp(-6),30],[1.69*math.exp(-6),10],[1.46*math.exp(-6),15],[1.69*math.exp(-6),12],[1.84*math.exp(-6),10],[1.69*math.exp(-6),20]]
#print(densidad[5][1])

#crear matriz_final, donde se almacenan en el indice 0 el valor correspondiente a la densidad, en los siguientes 9 indices se alamcenan los valores de las cordenadas de los 3 nodos
matriz_final=[]
for i in range(4417):
    matriz_final.append([0]*10)
a=0
j=0
for i in matriz_final:
    matriz_final[j][0]=int(Fila_elementos[j][0])
    z=1
    b=4
    d=7
    #print(matriz_final[j][0])
    #print (i)
    #if j>1000 :
        #print (matriz_final[j][0])
        #break
    for valor in Fila_nodos[int(Fila_elementos[j][1])]:
        matriz_final[j][z]=valor
        #print(matriz_final[j][z])
        #print(z)
        z=z+1
    for valor1 in Fila_nodos[int(Fila_elementos[j][2])]:
        matriz_final[j][b]=valor1
        #print(matriz_final[j][b])
        #print(b)
        b=b+1
    for valor2 in Fila_nodos[int(Fila_elementos[j][3])]:
        matriz_final[j][d]=valor2
        #print(matriz_final[j][d])
        #print(d)
        d=d+1
    j=j+1
#for linea in matriz_final:
    #print (linea)    
    #if a>10:
        #break

#crear las funciones necesarias para los calculos

def lado_triangulo(nodo1,nodo2):
    x1=float(nodo1[0])
    x2=float(nodo2[0])
    y1=float(nodo1[1])
    y2=float(nodo2[1])
    z1=float(nodo1[2])
    z2=float(nodo2[2])
    lado=math.sqrt((x1-x2)**2+(y1-y2)**2 +(z1-z2)**2)
    return lado
def distancia(x1,y1,z1,x2,y2,z2):    
    lado=math.sqrt((x1-x2)**2+(y1-y2)**2 +(z1-z2)**2)
    return lado
    
def area_triangulo(lado1,lado2,lado3):
    semiper=(lado1+lado2+lado3)/2
    Area=math.sqrt(semiper*(semiper-lado1)*(semiper-lado2)*(semiper-lado3))
    return Area
    
    
def peso_triangulo(densidad,area,espesor):
    Peso=densidad*(area*espesor)
    return Peso

def centro_triangulo(x1,y1,z1,x2,y2,z2,x3,y3,z3):
    centro_masa=[]
    X0=(x1+x2+x3)/3
    Y0=(y1+y2+y3)/3
    Z0=(z1+z2+z3)/3
    centro_masa.append(X0)
    centro_masa.append(Y0)
    centro_masa.append(Z0)
    return centro_masa
    
#hago pruebas,creo una matriz con los puntos de los nodos de cada triangulo
#Nodo1=Fila_nodos[int(Fila_elementos[1][1])]
#Nodo2=Fila_nodos[int(Fila_elementos[1][2])]
#Nodo3=Fila_nodos[int(Fila_elementos[1][3])]
#lado=lado_triangulo(Nodo1,Nodo2)
#crear el vector lados, donde se alamcenan en forma ordenada los lados de cada triangulo//pude hacerlo con una matriz
lados={}
contador_lado=0
for linea in matriz_final:
    x1=float(linea[1])
    y1=float(linea[2])
    z1=float(linea[3])
    x2=float(linea[4])
    y2=float(linea[5])
    z2=float(linea[6])
    x3=float(linea[7])
    y3=float(linea[8])
    z3=float(linea[9])
    lados[contador_lado]=distancia(x1,y1,z1,x2,y2,z2)
    lados[contador_lado+1]=distancia(x1,y1,z1,x3,y3,z3)
    lados[contador_lado+2]=distancia(x2,y2,z2,x3,y3,z3)
    contador_lado=contador_lado+3 
#crear la matriz areas, en donde se almacena la densidad en el indice 0 y el area en el indice 1 y el espesor en el indice 2
areas=[]
for j in range(numero_triangulos):
    areas.append([0]*3)
contador=0
for g in range(numero_triangulos):
    indice=int(matriz_final[g][0])-1
    areas[g][0]=densidad[indice][0]
    areas[g][2]=densidad[indice][1]
    lado1=lados[contador]
    lado2=lados[contador+1]
    lado3=lados[contador+2]
    areas[g][1]=area_triangulo(lado1,lado2,lado3)
    contador=contador+3
#crear el vector peso, que contiene los pesos de cada uno de los triangulos
pesos={}   
for g in range(numero_triangulos):
    d=areas[g][0]
    a=areas[g][1]
    e=areas[g][2]
    pesos[g]=peso_triangulo(d,a,e)
#sumamos los pesos de los triangulos
peso_total=0
for i in pesos:
    peso_total=peso_total + pesos[i]
    if i>=4416 :
        print("el valor de W0 (peso total) es :\n",peso_total,"kilogramos")
#crear matriz con los centros de masas de cada uno de los triangulos
centros_triangulos={}
for j in range(numero_triangulos):
    x1=float(matriz_final[j][1])
    y1=float(matriz_final[j][2])
    z1=float(matriz_final[j][3])
    x2=float(matriz_final[j][4])
    y2=float(matriz_final[j][5])
    z2=float(matriz_final[j][6])
    x3=float(matriz_final[j][7])
    y3=float(matriz_final[j][8])
    z3=float(matriz_final[j][9])
    centros_triangulos[j]=centro_triangulo(x1,y1,z1,x2,y2,z2,x3,y3,z3)
#for numero in centros_triangulos:
    #print(centros_triangulos[numero])
#calculo del centro de masa de la estructura completa
X0_TOTAL=0
sum_x0=0
sum_y0=0
sum_z0=0
for centro in centros_triangulos:
    x0=centros_triangulos[centro][0]
    sum_x0=sum_x0+x0*pesos[centro]
    y0=centros_triangulos[centro][1]
    sum_y0=sum_y0+y0*pesos[centro]
    z0=centros_triangulos[centro][2]
    sum_z0=sum_z0+z0*pesos[centro]
#imprimir las coordenadas de el centro de masa de la estructura completa
X0_TOTAL=(sum_x0)/peso_total
Y0_TOTAL=(sum_y0)/peso_total
Z0_TOTAL=(sum_z0)/peso_total
print("Las coordenadas (x0,y0,z0) del centro de masa total es :\n",X0_TOTAL,Y0_TOTAL,Z0_TOTAL)
#se calcula la reaccion en el eje Y y luego en el eje x
Ry=peso_total*X0_TOTAL
Rx=peso_total*Y0_TOTAL
print("El valor en de la reaccion en el eje X es :\n",Rx,"Nmm")
print("El valor en de la reaccion en el eje Y es :\n",Ry,"Nmm")