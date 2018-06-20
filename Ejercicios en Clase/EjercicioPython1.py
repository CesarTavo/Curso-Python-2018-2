###PRACTICA 1 ###
###Curso intersemestral Python Unica 19/06/18
###Hacer un programa para la entrada del antro
###Si tiene 18 años deja pasar pero pide INE
###Si es mayor de 18 años lo deja pasar
###Si es menor a 18 años no lo deja pasar

edad = int(input("\n\nIntroduce tu edad: ")) #pedimos al usuario ingresar edad

if (edad <= 0):
	print("\n\tNo se permite ese tipo de edad, ¿Qué clase de humano eres?\n")
elif (edad < 18): #comparamos si la edad ingresada es menor a 18 años
	print("\n\tNo puedes pasar morro xD xD xD ...\n") #imprimimos cuando el usuario es menor a 18 años
elif (edad == 18): #comparamos si la edad es igual a 18 años
	print("\n\tPuedes pasar si me muestras tu INE\n") #imprimimos cuando el usuario tiene exactamente 18 años
elif (edad >= 85): #comparamos si la edad es igual o mayor a 85 años
	print("\n\t¿Aún vienes a estos lugares? La old school esta vigente.\n") #imprimimos cuando el usuario tiene mayor o igual a 95
else:
	print("\n\tPasa papu, ¿Te ofrezco unas escorts? :V\n") #imprimimos el caso cuando el usuario es mayor a 18 años
