#Este código calcula el área de un cuadrado o un triángulo
#Autor: Luis Elías Huatay Salcedo
#Fecha: 04/08/2024
#Todos los derechos reservados XD

base = int(input("Ingrese la base: \n"))
altura = int(input("Ingrese la altura: \n"))
shape = input("¿La figura es un triángulo? (y/n): \n")
if shape == "y":
    area = base * altura / 2
else: 
    area = base * altura
print("El área es: ", area)
