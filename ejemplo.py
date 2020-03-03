print("Ejemplo de codigo caida libre")

t=input("Ingrese el instante de tiempo en el que desea calcular la posicion: ")
t=float(t)
y=input("Ingrese la altura inicial: ")
y=float(y)
g= 9.81
z=y+0.5*g*t**2
print(z)

