import random


numero_secreto = random.randint(1,101) 
cant_intentos = 0
cant_max_intentos = 5
adivinado = False #Es false porque aún no está adivinado.

print("Bienvenido, ¡Adivina el número secreto!")

while not adivinado:
    if not cant_intentos < cant_max_intentos:
        print("Game Over. No has podido adivinar dentro de los cinco intentos. :-(")
        break
    
    entrada = input("Introduce un número del 1 al 100: ")  # TODO: convertir a número
    numero = int(entrada)

    if numero == numero_secreto:
        print("¡Felicitaciones, has adivinado el número secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print("El número es mayor al ingresado.")
    else:
        print("El número es menor al ingresado.")

    cant_intentos += 1

