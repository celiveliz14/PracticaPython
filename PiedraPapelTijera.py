nombre1 = input("Nombre Jugador 1: ")
nombre2 = input("Nombre Jugador 2: ")

jugardor1 = input("¿Que eliges Piedra - Papel - Tijera? : ")
jugardor2 = input("¿Que eliges Piedra - Papel - Tijera? : ")

condicion1 = jugardor1 == "PIEDRA" and jugardor2 == "TIJERA"
condicion2 = jugardor1 == "TIJERA" and jugardor2 == "PAPEL"
condicion3 = jugardor1 == "PAPEL" and jugardor2 == "PIEDRA"


if jugardor1 == jugardor2:
    print("Empatados")
elif (condicion1) or (condicion2) or (condicion3):
    print("Ha ganado: ", nombre1)
else:
    print("Ha ganado: ", nombre2)