###Practica 3
###Curso Intersemestral Python
###Facultad de Ingeniería Única
###Elaborar un programa donde capture el nombre, apellido y edad
###Esos datos se tienen que guardar en una lista
###Además puede ingresar los usuarios que quiera

import os

print("\n")
cadena = "\n|¡Hola!|\n"
print(cadena.center(26,"-"))

lista_Personas = []
nombre = input("\nIngresa el nombre: ")
lista_Personas.append(nombre)
apellido = input("Ingresa el apellido: ")
lista_Personas.append(apellido)
edad = input("Ingresa la edad: ")
lista_Personas.append(edad)

respuesta = input("\t\n¿Deseas agregar más personas?: S/N \n S = Sí \n N = No \n")

while (respuesta == "S") or (respuesta == "s"):
	nombre = input("\nIngresa el nombre: ")
	lista_Personas.append(nombre)
	apellido = input("Ingresa el apellido: ")
	lista_Personas.append(apellido)
	edad = input("Ingresa la edad: ")
	lista_Personas.append(edad)
	continuar = input("¿Deseas agregar personas: S/N \n S = Sí \n N = No \n")
	if (continuar == "S") or (respuesta == "s"):
		print(lista_Personas,"\n")
		os.system("pause")
		break

if(respuesta == "N") or (respuesta == "n"):
	print(lista_Personas)
	os.system("pause")
	




'''contador = 0 
while (contador < 10):
	print("El contador tiene valor de: ",contador)
	contador += 1

print("\n")'''