# Ejercicio 2
# Complete el siguiente codigo para recorrer la lista `x` e imprima
# los numeros impares y que pare de imprimir al encontrar un numero mayor a 800
import numpy as np

#n=0
i=1
a=800
l=[]
x = np.int_(np.random.random(100)*1000)

for i in range(800):
    if (x[i]<(a) and x[i]%2!=0):
        l.append(x[i])
        
    elif(x[i]>800):
        
        break
        
print (l);

#while(n<800):
#    if n%2!=0:
#        print (i)
        
#print(x)



