import random

numero_secreto = random.randint(1,101)
cant_intentos = 0
cant_max = 7
adivinado = False

print("Bienvenido al juego")

while not adivinado:
    if not cant_intentos < cant_max:
        print("No has podido completar el juego, superaste los 7 intentos")
        break
    numero = int(input("Introduce un numero desde el 1 al 100: "))
    if numero == numero_secreto:
        print("Adivinaste")
        adivinado = True
    elif numero < numero_secreto:
        print("El numero el mayor")
    else:
        print("El numero el menor")

    cant_intentos += 1

if not cant_intentos < cant_max:
    print("No has podido completar el juego, superaste los 7 intentos")


