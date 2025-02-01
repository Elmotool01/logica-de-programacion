import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(password_length))
    password_label.config(text=password)

def copy_password():
    password = password_label.cget("text")
    window.clipboard_clear()
    window.clipboard_append(password)

window = tk.Tk()
window.title("Generador de Contraseñas")

length_label = tk.Label(window, text="Longitud de la contraseña:")
length_label.pack()

length_entry = tk.Entry(window)
length_entry.pack()

generate_button = tk.Button(window, text="Generar contraseña", command=generate_password)
generate_button.pack()

password_label = tk.Label(window, text="")
password_label.pack()

copy_button = tk.Button(window, text="Copiar contraseña", command=copy_password)
copy_button.pack()

window.mainloop()