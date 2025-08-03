import string
import random


longitud=int(input("Ingrese la longitud de la contraseña mayor a 10 dígitos:"))

while longitud < 10:
    print("La longitud debe ser al menos 10 caracteres.")
    longitud=int(input("Ingrese la longitud de la contraseña mayor a 10 dígitos:"))

caracteres= string.ascii_letters + string.digits + string.punctuation

contrasena = "".join(random.choice(caracteres) for i in range(longitud))

print("La contraseña generada es:" + contrasena)