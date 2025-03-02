import tkinter as tk  # Importa la biblioteca tkinter para la interfaz gráfica
import secrets  # Importa la biblioteca secrets para generación segura de números aleatorios
import string  # Importa la biblioteca string para trabajar con cadenas de caracteres


def generar_contraseña(longitud, caracteres):
    """Genera una contraseña aleatoria y segura."""
    alfabeto = caracteres  # Define el conjunto de caracteres posibles
    contraseña = ''.join(secrets.choice(alfabeto) for i in range(longitud))  # Crea la contraseña aleatoria
    return contraseña  # Devuelve la contraseña generada


def analizar_seguridad(contraseña):
    """Analiza la seguridad de una contraseña y devuelve su nivel."""
    longitud = len(contraseña)  # Obtiene la longitud de la contraseña
    tiene_mayuscula = any(c.isupper() for c in contraseña)  # Verifica si hay mayúsculas
    tiene_minuscula = any(c.islower() for c in contraseña)  # Verifica si hay minúsculas
    tiene_numero = any(c.isdigit() for c in contraseña)  # Verifica si hay números
    tiene_simbolo = any(c in string.punctuation for c in contraseña)  # Verifica si hay símbolos

    # Determina el nivel de seguridad
    if longitud >= 12 and tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_simbolo:
        return "Fuerte"
    elif longitud >= 8 and (tiene_mayuscula or tiene_minuscula) and tiene_numero:
        return "Moderada"
    else:
        return "Débil"


def generar_contraseña_personalizada():
    """Genera una contraseña personalizada según las opciones seleccionadas."""
    longitud = int(longitud_entry.get())  # Obtiene la longitud del campo de entrada
    caracteres = ""  # Inicializa los caracteres permitidos
    # Añade los caracteres según las selecciones de los checkboxes
    if mayusculas_var.get():
        caracteres += string.ascii_uppercase
    if minusculas_var.get():
        caracteres += string.ascii_lowercase
    if numeros_var.get():
        caracteres += string.digits
    if simbolos_var.get():
        caracteres += string.punctuation
    contraseña = generar_contraseña(longitud, caracteres)  # Genera la contraseña
    seguridad = analizar_seguridad(contraseña)  # Analiza la seguridad
    resultado_label.config(text=f"Contraseña: {contraseña}\nSeguridad: {seguridad}")  # Muestra el resultado


def generar_contraseña_facil_decir():
    """Genera una contraseña fácil de decir."""
    consonantes = "bcdfghjklmnpqrstvwxyz"  # Define las consonantes
    vocales = "aeiou"  # Define las vocales
    longitud = 8  # Define la longitud
    contraseña = ''.join(secrets.choice(consonantes if i % 2 == 0 else vocales) for i in range(longitud))  # Genera la contraseña
    seguridad = analizar_seguridad(contraseña)  # Analiza la seguridad
    resultado_label.config(text=f"Contraseña: {contraseña}\nSeguridad: {seguridad}")  # Muestra el resultado


def generar_contraseña_todos_caracteres():
    """Genera una contraseña con todos los caracteres posibles."""
    caracteres = string.ascii_letters + string.digits + string.punctuation  # Define todos los caracteres
    longitud = 12  # Define la longitud
    contraseña = generar_contraseña(longitud, caracteres)  # Genera la contraseña
    seguridad = analizar_seguridad(contraseña)  # Analiza la seguridad
    resultado_label.config(text=f"Contraseña: {contraseña}\nSeguridad: {seguridad}")  # Muestra el resultado


def generar_contraseña_facil_leer():
    """Genera una contraseña fácil de leer (sin caracteres ambiguos)."""
    caracteres = "abcdefghijkmnopqrstuvwxyz23456789"  # Define los caracteres sin ambiguos
    longitud = 10  # Define la longitud
    contraseña = generar_contraseña(longitud, caracteres)  # Genera la contraseña
    seguridad = analizar_seguridad(contraseña)  # Analiza la seguridad
    resultado_label.config(text=f"Contraseña: {contraseña}\nSeguridad: {seguridad}")  # Muestra el resultado


def activar_contraseña_propia():
    """Activa el campo de entrada para la contraseña propia y lo muestra."""
    if contraseña_propia_var.get():  # Si el checkbox está marcado
        contraseña_propia_entry.grid(row=0, column=1)  # Muestra el campo de entrada
        analizar_propia_button.grid(row=0, column=2)  # Muestra el botón de análisis
    else:  # Si el checkbox no está marcado
        contraseña_propia_entry.grid_forget()  # Oculta el campo de entrada
        analizar_propia_button.grid_forget()  # Oculta el botón de análisis


def analizar_contraseña_propia():
    """Analiza la seguridad de una contraseña ingresada por el usuario."""
    contraseña = contraseña_propia_entry.get()  # Obtiene la contraseña del campo de entrada
    seguridad = analizar_seguridad(contraseña)  # Analiza la seguridad de la contraseña
    resultado_label.config(text=f"Contraseña: {contraseña}\nSeguridad: {seguridad}")  # Muestra el resultado


# Creación de la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas Seguras")

# Creación de los widgets
menu_label = tk.Label(ventana, text="Seleccione una opción:")
menu_label.pack()

# Opción "Yo genero mi contraseña" con checkbox para activar el campo
contraseña_propia_var = tk.IntVar()
contraseña_propia_check = tk.Checkbutton(ventana, text="Yo genero mi contraseña", variable=contraseña_propia_var,
                                        command=activar_contraseña_propia)
contraseña_propia_check.pack()

contraseña_propia_frame = tk.Frame(ventana)
contraseña_propia_frame.pack()

contraseña_propia_label = tk.Label(contraseña_propia_frame, text="Contraseña:")
contraseña_propia_label.grid(row=0, column=0)
contraseña_propia_entry = tk.Entry(contraseña_propia_frame)
contraseña_propia_entry.grid_forget()  # Oculta inicialmente el campo de entrada

analizar_propia_button = tk.Button(contraseña_propia_frame, text="Analizar Contraseña",
                                    command=analizar_contraseña_propia)
analizar_propia_button.grid_forget()  # Oculta inicialmente el botón de análisis

personalizada_frame = tk.Frame(ventana)
personalizada_frame.pack()

longitud_label = tk.Label(personalizada_frame, text="Longitud:")
longitud_label.grid(row=0, column=0)
longitud_entry = tk.Entry(personalizada_frame)
longitud_entry.grid(row=0, column=1)

# Checkboxes para la selección de caracteres
mayusculas_var = tk.IntVar()
mayusculas_check = tk.Checkbutton(personalizada_frame, text="Mayúsculas", variable=mayusculas_var)
mayusculas_check.grid(row=1, column=0, columnspan=2, sticky="W")

minusculas_var = tk.IntVar()
minusculas_check = tk.Checkbutton(personalizada_frame, text="Minúsculas", variable=minusculas_var)
minusculas_check.grid(row=2, column=0, columnspan=2, sticky="W")

numeros_var = tk.IntVar()
numeros_check = tk.Checkbutton(personalizada_frame, text="Números", variable=numeros_var)
numeros_check.grid(row=3, column=0, columnspan=2, sticky="W")

simbolos_var = tk.IntVar()
simbolos_check = tk.Checkbutton(personalizada_frame, text="Símbolos", variable=simbolos_var)
simbolos_check.grid(row=4, column=0, columnspan=2, sticky="W")

personalizada_button = tk.Button(personalizada_frame, text="Generar Personalizada", command=generar_contraseña_personalizada)
personalizada_button.grid(row=5, columnspan=2)

# Botones para otras opciones de contraseña
facil_decir_button = tk.Button(ventana, text="Contraseña Fácil de Decir", command=generar_contraseña_facil_decir)
facil_decir_button.pack()

todos_caracteres_button = tk.Button(ventana, text="Todos los Caracteres", command=generar_contraseña_todos_caracteres)
todos_caracteres_button.pack()

facil_leer_button = tk.Button(ventana, text="Contraseña Fácil de Leer", command=generar_contraseña_facil_leer)
facil_leer_button.pack()

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

# Inicia el bucle de eventos
ventana.mainloop()