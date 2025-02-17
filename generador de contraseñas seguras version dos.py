import random  # Importa el módulo 'random' para generar números y selecciones aleatorias.
import string  # Importa el módulo 'string' para acceder a constantes de cadenas de caracteres (letras, dígitos, etc.).

def generar_contrasena_personalizada(longitud):
    """
    Permite al usuario crear su propia contraseña, validando la longitud.
    """
    while True:  # Bucle infinito que se rompe solo cuando se ingresa una contraseña válida.
        contrasena = input(f"Ingresa tu contraseña (debe tener {longitud} caracteres): ")  # Solicita la contraseña al usuario, mostrando la longitud requerida.
        if len(contrasena) == longitud:  # Verifica si la longitud de la contraseña ingresada es igual a la longitud especificada.
            return contrasena  # Si la longitud es correcta, devuelve la contraseña y sale de la función.
        else:
            print(f"Error: La contraseña debe tener {longitud} caracteres.")  # Si la longitud es incorrecta, imprime un mensaje de error.

def generar_contrasena_facil_decir(longitud):
    """
    Genera una contraseña fácil de decir (solo letras mayúsculas y minúsculas).
    """
    caracteres = string.ascii_letters  # Crea una cadena con todas las letras (mayúsculas y minúsculas).
    return ''.join(random.choice(caracteres) for _ in range(longitud))  # Genera la contraseña seleccionando 'longitud' caracteres aleatorios de 'caracteres' y los une en una cadena.

def generar_contrasena_facil_leer(longitud, incluir_numeros, incluir_simbolos):
    """
    Genera una contraseña fácil de leer (mayúsculas/minúsculas, con opción de números y símbolos).
    """
    caracteres = string.ascii_letters  # Inicializa la cadena de caracteres permitidos con letras mayúsculas y minúsculas.

    if incluir_numeros:  # Verifica si el usuario quiere incluir números.
        caracteres += string.digits  # Agrega los dígitos a la cadena de caracteres permitidos.
    if incluir_simbolos:  # Verifica si el usuario quiere incluir símbolos.
        caracteres += string.punctuation  # Agrega los símbolos de puntuación a la cadena de caracteres permitidos.

    return ''.join(random.choice(caracteres) for _ in range(longitud))  # Genera la contraseña, similar a generar_contrasena_facil_decir.

def generar_contrasena_todos_caracteres(longitud, usar_combinacion_por_defecto):
    """
    Genera una contraseña con todos los tipos de caracteres (con opción de personalizar).
    """
    if usar_combinacion_por_defecto:  # Verifica si se debe usar la combinación por defecto (letras, números y símbolos).
        caracteres = string.ascii_letters + string.digits + string.punctuation  # Crea una cadena con todos los caracteres.
        return ''.join(random.choice(caracteres) for _ in range(longitud)) #Genera la contrasena
    else:
        #  Opción personalizada (similar a la funcionalidad original "todas las características").
        return generar_contrasena_personalizada_caracteristicas(longitud) # Si no se usa la opción por defecto, llama a la función para personalizar la combinación.

def generar_contrasena_personalizada_caracteristicas(longitud):
    """
     Permite al usuario escoger los tipos de caracteres para su contraseña (mínimo 3).
    """
    opciones_disponibles = {  # Define un diccionario con las opciones de caracteres disponibles y sus correspondientes cadenas.
      "mayusculas": string.ascii_uppercase,
      "minusculas": string.ascii_lowercase,
      "numeros": string.digits,
      "simbolos": string.punctuation,
    }

    opciones_elegidas = []  # Inicializa una lista vacía para almacenar las opciones que elija el usuario.
    print("Elige al menos 3 de las siguientes opciones para tu contraseña:")
    for opcion, _ in opciones_disponibles.items():  # Itera a través de las opciones disponibles (claves del diccionario).
        while True:  # Bucle para asegurar una entrada válida (s/n).
          respuesta = input(f"¿Incluir {opcion}? (s/n): ").lower()  # Pregunta al usuario si quiere incluir la opción actual (convierte la entrada a minúsculas).
          if respuesta in ("s", "n"):  # Verifica si la respuesta es 's' o 'n'.
            if respuesta == "s":  # Si la respuesta es 's' (sí).
                opciones_elegidas.append(opcion)  # Agrega la opción a la lista de opciones elegidas.
            break  # Sale del bucle 'while' porque la respuesta es válida.
          else:
            print("Respuesta inválida. Ingresa 's' o 'n'.")  # Si la respuesta no es 's' ni 'n', muestra un mensaje de error.
    
    if len(opciones_elegidas) < 3:  # Verifica si el usuario ha elegido al menos 3 opciones.
        print("Debes elegir al menos 3 opciones. Intenta de nuevo.")
        return generar_contrasena_personalizada_caracteristicas(longitud) # Llamada recursiva para reintentar

    caracteres = "".join(opciones_disponibles[opcion] for opcion in opciones_elegidas)  # Crea la cadena de caracteres permitidos uniendo las cadenas correspondientes a las opciones elegidas.
    return "".join(random.choice(caracteres) for _ in range(longitud))  # Genera la contraseña seleccionando caracteres aleatorios de la cadena 'caracteres'.


def evaluar_fortaleza_contrasena(contrasena):
    """
    Evalúa la fortaleza de una contraseña (básica).
    """
    longitud = len(contrasena)  # Obtiene la longitud de la contraseña.
    tiene_mayusculas = any(c.isupper() for c in contrasena)  # Verifica si la contraseña contiene al menos una letra mayúscula.
    tiene_minusculas = any(c.islower() for c in contrasena)  # Verifica si la contraseña contiene al menos una letra minúscula.
    tiene_numeros = any(c.isdigit() for c in contrasena)  # Verifica si la contraseña contiene al menos un dígito.
    tiene_simbolos = any(c in string.punctuation for c in contrasena)  # Verifica si la contraseña contiene al menos un símbolo.

    #  Criterios básicos de fortaleza (puedes ajustarlos).
    if longitud < 8:  # Si la longitud es menor a 8.
        return "Débil"  # Demasiado corta.
    elif (  # Si la longitud es mayor o igual a 8 Y contiene mayúsculas Y minúsculas Y números Y símbolos.
        longitud >= 8
        and tiene_mayusculas
        and tiene_minusculas
        and tiene_numeros
        and tiene_simbolos
    ):
        return "Fuerte"  # Cumple con todos los criterios.
    elif ( #Si la longitud es mayor o igual a 8 Y tiene al menos tres tipos de caracter
        longitud >= 8 and (
            (tiene_mayusculas and tiene_minusculas and tiene_numeros) or
            (tiene_mayusculas and tiene_minusculas and tiene_simbolos) or
            (tiene_mayusculas and tiene_numeros and tiene_simbolos) or
            (tiene_minusculas and tiene_numeros and tiene_simbolos))
    ):
        return "Media" #Cumple con al menos tres criterios
    else:
        return "Débil"  # No cumple con los criterios suficientes.


def mostrar_reglas():
    """
    Muestra las reglas del generador de contraseñas.
    """
    print("\nReglas del Generador de Contraseñas:")  # Imprime un encabezado.
    print("- La longitud de la contraseña debe ser especificada por el usuario.")  # Imprime la primera regla.
    print("- Se pueden generar contraseñas con diferentes combinaciones de caracteres:")  # Imprime la segunda regla (general).
    print("  - Solo letras (mayúsculas y minúsculas).")  # Imprime una opción de combinación.
    print("  - Letras y números.")  # Imprime otra opción.
    print("  - Letras, números y símbolos.")  # Imprime otra opción.
    print("  - Combinación personalizada de caracteres (al menos 3 tipos).")  # Imprime la opción de combinación personalizada.
    print("- Se evaluará la fortaleza de la contraseña generada.\n")  # Imprime la última regla.


def main():
    """
    Función principal de la aplicación.
    """
    while True:  # Bucle principal del programa (se ejecuta hasta que el usuario decide salir).
        print("\nMenú Principal:")  # Imprime el encabezado del menú principal.
        print("1. Generar contraseña")  # Imprime la primera opción.
        print("2. Reglas del generador de contraseña")  # Imprime la segunda opción.
        print("3. Salir")  # Imprime la tercera opción.

        opcion_principal = input("Elige una opción: ")  # Solicita al usuario que elija una opción.

        if opcion_principal == "1":  # Si el usuario elige "Generar contraseña".
            while True: # Bucle para el submenú de generación de contraseñas
                print("\nOpciones de Generación de Contraseña:")  # Imprime el encabezado del submenú.
                print("1. Yo genero mi propia contraseña")  # Imprime las opciones del submenú.
                print("2. Contraseña automática fácil de decir")
                print("3. Contraseña automática fácil de leer")
                print("4. Todos los caracteres")
                print("5. Volver al menú principal") # Opción para regresar

                opcion_generacion = input("Elige una opción: ")  # Solicita al usuario que elija una opción de generación.

                if opcion_generacion == "1":  # Si el usuario elige "Yo genero mi propia contraseña".
                    longitud = int(input("Ingresa la longitud de la contraseña: "))  # Solicita la longitud de la contraseña (como entero).
                    contrasena = generar_contrasena_personalizada(longitud)  # Llama a la función para generar la contraseña personalizada.
                    fortaleza = evaluar_fortaleza_contrasena(contrasena)  # Evalúa la fortaleza de la contraseña.
                    print(f"Contraseña generada: {contrasena}")  # Imprime la contraseña generada.
                    print(f"Fortaleza de la contraseña: {fortaleza}")  # Imprime la fortaleza de la contraseña.

                elif opcion_generacion == "2":  # Si el usuario elige "Contraseña automática fácil de decir".
                    longitud = int(input("Ingresa la longitud de la contraseña: "))  # Solicita la longitud.
                    contrasena = generar_contrasena_facil_decir(longitud)  # Llama a la función correspondiente.
                    fortaleza = evaluar_fortaleza_contrasena(contrasena)  # Evalúa la fortaleza.
                    print(f"Contraseña generada: {contrasena}")  # Imprime la contraseña y su fortaleza.
                    print(f"Fortaleza de la contraseña: {fortaleza}")

                elif opcion_generacion == "3":  # Si el usuario elige "Contraseña automática fácil de leer".
                    longitud = int(input("Ingresa la longitud de la contraseña: "))  # Solicita la longitud.
                    incluir_numeros = input("¿Incluir números? (s/n): ").lower() == "s"  # Pregunta si se incluyen números (convierte a minúsculas y compara con "s").
                    incluir_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == "s"  # Pregunta si se incluyen símbolos.
                    contrasena = generar_contrasena_facil_leer(longitud, incluir_numeros, incluir_simbolos)  # Llama a la función.
                    fortaleza = evaluar_fortaleza_contrasena(contrasena)  # Evalúa la fortaleza.
                    print(f"Contraseña generada: {contrasena}")  # Imprime la contraseña y su fortaleza.
                    print(f"Fortaleza de la contraseña: {fortaleza}")

                elif opcion_generacion == "4":  # Si el usuario elige "Todos los caracteres".
                    longitud = int(input("Ingresa la longitud de la contraseña: "))  # Solicita la longitud.
                    print("Se generará una contraseña con mayúsculas, minúsculas, números y símbolos.")  # Informa al usuario sobre la combinación por defecto.
                    usar_combinacion_por_defecto = input("¿Usar esta combinación (s/n), o generar tu propia combinacion?: ").lower() == "s"  # Pregunta si se usa la combinación por defecto o una personalizada.
                    contrasena = generar_contrasena_todos_caracteres(longitud, usar_combinacion_por_defecto)  # Llama a la funcion para generar la contrasena
                    fortaleza = evaluar_fortaleza_contrasena(contrasena)  # Evalúa la fortaleza.
                    print(f"Contraseña generada: {contrasena}")  # Imprime la contraseña.
                    print(f"Fortaleza de la contraseña: {fortaleza}")  # Imprime la fortaleza.
                elif opcion_generacion == "5":
                  break  # Sale del bucle del submenú y regresa al menú principal

                else:
                    print("Opción inválida. Intenta de nuevo.")  # Si la opción no es válida, muestra un mensaje de error.

        elif opcion_principal == "2":  # Si el usuario elige "Reglas del generador de contraseña".
            mostrar_reglas()  # Llama a la función que muestra las reglas.

        elif opcion_principal == "3":  # Si el usuario elige "Salir".
            print("¡Hasta luego!")  # Imprime un mensaje de despedida.
            break  # Sale del bucle principal y termina el programa.

        else:
            print("Opción inválida. Intenta de nuevo.")  # Si la opción del menú principal no es válida, muestra un mensaje de error.


if __name__ == "__main__":  # Este bloque se ejecuta solo si el script se ejecuta directamente (no si se importa como módulo).
    main()  # Llama a la función principal para iniciar la aplicación.