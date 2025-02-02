import secrets
import string

def generar_contraseña(longitud=12, incluir_mayusculas=True, incluir_numeros=True, incluir_simbolos=True):
  """Genera una contraseña segura.

  Args:
    longitud: La longitud de la contraseña a generar.
    incluir_mayusculas: Si se deben incluir letras mayúsculas.
    incluir_numeros: Si se deben incluir números.
    incluir_simbolos: Si se deben incluir símbolos.

  Returns:
    Una contraseña segura.
  """

  caracteres = string.ascii_lowercase
  if incluir_mayusculas:
    caracteres += string.ascii_uppercase
  if incluir_numeros:
    caracteres += string.digits
  if incluir_simbolos:
    caracteres += string.punctuation

  contraseña = ''.join(secrets.choice(caracteres) for i in range(longitud))
  return contraseña

# Generar una contraseña con la configuración por defecto
contraseña = generar_contraseña()
print(contraseña)

# Generar una contraseña de 16 caracteres, sin mayúsculas
contraseña = generar_contraseña(longitud=16, incluir_mayusculas=False)
print(contraseña)