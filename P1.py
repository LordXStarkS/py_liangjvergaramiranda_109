def sumarDosNumeros(num1,num2):
    resultado = num1 + num2
    print("el resultado es : ",resultado)
    return resultado
    
    
print("esto es mi primero funcion")
x = 18
y = 19
sumarDosNumeros(x,y)

def sumarTresNumeros(num1,num2,num3):
    sumadedosNumeros = sumarDosNumeros(num1,num2)
    resultado = sumadedosNumeros + num3
    print("el resultado es : ",resultado)
    
sumarTresNumeros(x,y,x)

def saludarAlumnos():
    print("hola bienvenidos al curos de python")
    
    
    
def configurar_juego():
    """Configura el número secreto y la cantidad de intentos"""
    numero_secreto = int(input("Ingresa el número secreto (entre el 1 y el 10): "))
    max_intentos = int(input("Ingresa el número máximo de intentos: "))
    print("Valores configurados, ahora puedes jugar")
    return numero_secreto, max_intentos


def jugar(numero_secreto, max_intentos):
    """Función para jugar al adivinar el número"""
    intentos = 0

    while intentos < max_intentos:
        numeroPorAdivinar = int(input("Adivina el número secreto (entre el 1 y el 10, -1 para salir): "))

        # Opción para salir durante el juego
        if numeroPorAdivinar == -1:
            print("Has salido del juego.")
            return

        intentos += 1

        if numeroPorAdivinar == numero_secreto:
            print("¡Has adivinado el número secreto!")
            return
        elif numeroPorAdivinar > numero_secreto:
            print("El número ingresado es mayor al número secreto.")
        else:
            print("El número ingresado es menor al número secreto.")

        print(f"Te quedan {max_intentos - intentos} intento(s).")

    print("😢 Has agotado tus intentos. El número secreto era:", numero_secreto)


def menu():
    """Menú principal del juego"""
    numero_secreto = None
    max_intentos = None

    while True:
        print("\n===== MENÚ DEL JUEGO =====")
        print("1) Ingresar los valores para configurar el juego")
        print("2) Jugar")
        print("3) Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero_secreto, max_intentos = configurar_juego()
        elif opcion == "2":
            if numero_secreto is None or max_intentos is None:
                print("Primero debes configurar el juego (opción 1).")
            else:
                jugar(numero_secreto, max_intentos)
        elif opcion == "3":
            print("Has salido del juego.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")