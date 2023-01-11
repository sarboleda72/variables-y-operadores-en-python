c=float(input("Ingrese el capital= "))
r=float(input("Ingrese la tasa de interes= "))
t=float(input("Ingrese el tiempo= "))
m=((1+(r/100))**t)*c
i=m-c
print("="*25)
print("El interes es de ",i,"el monto es de ",m)