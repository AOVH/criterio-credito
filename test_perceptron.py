#!/usr/bin/env python
from perceptron import Perceptron

## Datos de Cliente
input_data = [[1,1,1,1,0],
              [1,1,0,0,1],
              [0,1,0,0,1],
              [1,0,0,0,1],
              [0,0,0,0,0]]


## Creamos el perceptron
pr = Perceptron(5,0.1) # Perceptron con 4 entradas
weights = [] # Lista con los pesos
errors = []  # Lista con los errores

## Fase de entrenamiento
for _ in range(100):
    # Vamos a entrenarlo varias veces sobre los mismos datos
    # para que los 'pesos' converjan
    for person in input_data:
        output = person[-1]
        inp = [1] + person[0:-1] # Agregamos un uno por default
        weights.append(pr._w)
        err = pr.train(inp,output)
        errors.append(err)

l = float(raw_input("El salario mensual de cliente es mayor de $10,000.00. ?  1 para SI 0 para NO - "))
o = float(raw_input("El cliete cuenta con trabajo ?  1 para SI 0 para NO - "))
v = float(raw_input("El cliete tiene antecedentes penales? 1 para SI 0 para NO.- "))
e = float(raw_input("El clientie tiene problemas en buro? 1 para SI 0 para NO .- "))

if pr.predict([1,l,o,v,e]) == 1: print "Candidato aptro para credito"
else: print "Candidato NO aptro para credito"

#print """
#Nota: El resultado puede estar incorrecto.
#Esto puede ser debido a sesgo en la muestra, o porque es imposible separar
#a hombres y mujeres perfectamente basados unicamente en talla y peso."""

## Fase de graficacion
import imp
import sys

can_plot = True
try:
    imp.find_module('matplotlib')
except:
    can_plot = False

if not can_plot:
    print "No es posible graficar los resultados porque no tienes matplotlib"
    sys.exit(0)
    pass

import matplotlib.pyplot as plt

plt.plot(errors)
plt.show()