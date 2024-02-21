
d1 = input ("Ingresa primer numero:")
d2 = input ("Ingresa segundo numero:")

d1 = int (d1)
d2 = int (d2)

suma = d1 + d2
resta = d1 - d2 
multi = d1 * d2
div = d1 / d2 

mensaje = f"""
Para los numeros {d1} y {d2}.
El resultado de la suma es {suma}
El resultado de la resta es {resta}.
El resultado de la multiplicacion es {multi}.
El resultado de la division es {div}.
"""

print (mensaje)
