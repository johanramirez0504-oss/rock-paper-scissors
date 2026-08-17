import random
def main_menu():
    back=True
    while back:
        print("*"*20)
        print("*PIEDRA, PAPEL O TIJERAS*".center(20,"*"))
        print("*"*20)        
        print("""\nElija una de las siguientes opciones:
    1.Play
    2.Salir del programa""")
        try:
            op=int(input("Elección: "))
            if op==1:
                juego_VS_pc(lista_op)
                while back:
                    respuesta=input("\n¿Desea volver a intentar? S/N:  ").upper().strip()
                    if respuesta=="S":
                        break
                    elif respuesta=="N":
                        print("Gracias por jugar :)")
                        back=False
                    else:
                        print("Solo S o N.")
            elif op==2:
                print("Adiós :(")
                break
            else:
                print("Esta opción no está disponible.")
                continue
        except ValueError:
                print("Opción no disponible")
lista_op=["🪨", "🧻️", "✂"]
def jugada_pc(lista_op):
    op_pc=random.choice(lista_op)
    return op_pc

def juego_VS_pc(lista_op):
    puntos_jugador=0
    puntos_pc=0
    while True:
        try:
            meta_victoria=int(input("¿Cuál será la meta en victorias?: "))
            if meta_victoria<1:
                print("La meta tiene que ser de 1 o más.")
            else:
                break
        except ValueError:
            print("Solo números.")
    print(f"La meta será de {meta_victoria} victorias.")
    print(f"Marcador: {puntos_jugador}-{puntos_pc}")
    while puntos_jugador<meta_victoria and puntos_pc<meta_victoria:
        try:
            op_jugador= int(input("""\nElije el número: 1.🪨 2.️🧻️ 3.✂:
\n️"""))
            if op_jugador==1:
                op_jugador=lista_op[0]
            elif op_jugador==2:
                op_jugador=lista_op[1]
            elif op_jugador==3:
                op_jugador=lista_op[2]
            else:
                print("Esta opción no está disponible.")
                continue
            print(f"\nJugador elije {op_jugador}.")
            op_pc=jugada_pc(lista_op)
            print(f"La pc elige {op_pc}.\n")
            resultado=ganador_partida(op_jugador,op_pc)
            if resultado == "empate":
                print("¡Es un empate!")
            elif resultado == "jugador":
                print(f"Ganó el jugador.")
                puntos_jugador+=1
            else:
                print("Ganó la PC.")
                puntos_pc+=1
            print(f"Marcador: {puntos_jugador}-{puntos_pc}")

        except ValueError:
                print("Opción no disponible.")
    if puntos_jugador==meta_victoria:
        print("\n🎉️¡EL CAMPEÓN ERES TÚ!🎉️ Toma tu premio ️🏆. Eres todo un exitoso.️")
    else:
        print("️\n¡PERDISTE!🫵️😂 Toma tu premio 💩️. Tremendo perdedor, eres toda una basura🤮️.")
combinaciones=[
    ["🪨", "✂"],
    ["🧻️", "🪨"],
    ["✂", "🧻️"]
             ]
def ganador_partida(op_jugador,op_pc):
    if op_jugador==op_pc:
        return "empate"
    for i in combinaciones:
        if op_jugador==i[0] and op_pc==i[1]:
            return "jugador"
    return "pc"
main_menu()
