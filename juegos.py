import random
import time
import datetime

def cachipun():
    """
    Esta función representa el juego de cachipun.
    Debes pedir al usuario que elija piedra, papel o tijera, y luego comparar su elección con la de la computadora.
    La computadora debe elegir una opción al azar.
    """
    eleccion= int(input("Escoge piedra (0), papel (1) o tijera (2): "))
    while eleccion not in [0,1,2]:
        eleccion= int(input("Selección inválida. Por favor vuelve a escoger.\nEscoge piedra (0), papel (1) o tijera (2): "))
    compu= random.randint(0,2)
    
    if compu==0:
        compustr="piedra."
    elif compu==1:
        compustr="papel."
    else:
        compustr="tijera."

    if eleccion == compu:
        print(f"¡Empate! El computador escogió {compustr}")
    elif (eleccion==0 and compu==2) or (eleccion==1 and compu==0) or (eleccion==2 and compu==1):
        print(f"¡Ganaste! El computador escogió {compustr}")
    else:
        print(f"Perdiste. El computador escogió {compustr} :(")

    pass
    

def adivinar_numero():
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """
    num_azar= random.randint(1,10)
    player= int(input("Estoy generando un número del 1-10. Adivina cuál es: "))

    if num_azar==player:
        print(f"Ganaste. El número era {num_azar}.")
    else:
        print(f"Perdiste. El número era {num_azar}. :(")
    pass

def reaccion_rapida():
    """
    Esta función representa el juego de reacción rápida.
    Debes pedir al usuario que presione Enter lo más rápido posible después de que vea "GO!".
    Debes medir el tiempo que tarda el usuario en reaccionar y mostrarlo al final del juego.
    """
    time.sleep(0.5)
    print("Este es un juego de reacción. En cualquiera de los siguientes segundos tendrás que presionar enter..")
    time.sleep(random.randint(1,12))
    inicio = time.time()
    t = input("GO!")
    press = time.time()
    dif = press-inicio
    print(f"Tu tiempo de reacción fue de {dif} segundos.")

    pass

def suma_rapida():
    """
    Esta función representa el juego de suma rápida.
    Debes generar dos números al azar y pedir al usuario que los sume lo más rápido posible.
    Debes medir el tiempo que tarda el usuario en responder y mostrarlo al final del juego.
    """
    time.sleep(0.5)
    print("¡Suma lo más rápido posible!")
    time.sleep(1)
    num1= random.randint(1,20)
    num2=random.randint(1,20)
    inicio = time.time()
    t = int(input(f"¿{num1} + {num2}? "))
    press = time.time()
    dif = press-inicio
    if num1+num2==t:
        print(f"¡Correcto, felicidades! Tu tiempo de reacción fue de {dif} segundos.")
    else:
        print(f"Incorrecto. Tu tiempo de reacción fue de {dif} segundos. :(")
    pass

def memoria():
    """
    Esta función representa el juego de memoria.
    Debes generar una secuencia de números al azar y mostrarla al usuario.
    Luego, debes pedir al usuario que repita la secuencia.
    Se debe mostrar un mensaje si el usuario acierta o no.
    """
    print("Te voy a mostrar 10 números. Memorízalos: ")
    listanums=[]
    for i in range(10):
        num=random.randint(0,9)
        listanums.append(num)
        print(num)
        time.sleep(1)
    for i in range(10):
        print("-"*20)
    num_adiv=input("¿Cuál era la secuencia? " )
    num_adiv=num_adiv.split()
    contador=0
    for i in range(10):
        if listanums[i]==int(num_adiv[i]):
            contador+=1
    if contador==10:
        print("¡Correcto! Esa era la secuencia. :)")
    else:
        print(f"Te equivocaste. Secuencia incorrecta, tuviste {contador} aciertos. :(")

    pass