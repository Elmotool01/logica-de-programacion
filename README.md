# Generador de Contraseñas Seguras Mejorado

## Introducción

En la era digital actual, la seguridad de la información es primordial. Las contraseñas fuertes y únicas son la primera línea de defensa contra accesos no autorizados a nuestras cuentas y datos personales. Este proyecto surge de la necesidad de generar contraseñas que sean no solo seguras, sino también personalizables y fáciles de manejar para el usuario moderno.

Este generador de contraseñas ha sido mejorado significativamente respecto a versiones básicas, implementando algoritmos de generación de números pseudoaleatorios criptográficamente seguros (CSPRNG), opciones avanzadas de personalización, verificación de fortaleza y una interfaz intuitiva.

## Objetivos del Proceso

* **Maximizar la Seguridad:** Generar contraseñas con la máxima entropía posible para resistir ataques de fuerza bruta y de diccionario.
* **Flexibilidad para el Usuario:** Permitir una personalización completa de las contraseñas, incluyendo longitud y tipos de caracteres.
* **Facilidad de Uso:** Proporcionar interfaces de línea de comandos (CLI) y gráfica (GUI) opcionales para adaptarse a las preferencias de cada usuario.
* **Verificación de Fortaleza:** Ofrecer una herramienta para evaluar la calidad de las contraseñas generadas.
* **Evitar la confusión:** Brindar la opción de excluir aquellos caracteres que causan confusión, para que las contraseñas generadas sean lo mas sencillas de usar por el usuario final.
* **Generación de grandes cantidades:** permitir la generación de una gran cantidad de contraseñas al mismo tiempo.

## Estructura del Repositorio

Este repositorio contiene los siguientes archivos principales:

* `generador_contraseñas version final.py`: Código principal del generador de contraseñas (CLI).
* * `diagramas de flujo. pdf`: diagrmas de desarrollo del programa (PDF).
* `generador_contraseñas_gui.py` (opcional): Interfaz gráfica de usuario.
* * `presentación del proyecto.ppt `: Presnetación del proyecto final del generador seguro de contraseñas (PPT).
* `requirements.txt` (opcional): Lista de dependencias del proyecto.
* `README.md`: Documentación del proyecto.

## Características Principales

* **Generación de contraseñas altamente aleatorias:** Utiliza el módulo `secrets` de Python para generar números pseudoaleatorios criptográficamente seguros (CSPRNG). Enlace a la libreria: [secrets — Generating secure random numbers for managing secrets — Python 3.12.2 documentation](https://docs.python.org/3/library/secrets.html)
* **Personalización de la longitud y los caracteres:** Permite al usuario especificar la longitud de la contraseña y los tipos de caracteres que desea incluir (mayúsculas, minúsculas, números, símbolos, caracteres unicode).
* **Verificación de la fortaleza de la contraseña:** Implementa una función que evalúa la fortaleza de la contraseña generada, proporcionando información sobre su entropía y resistencia a ataques de fuerza bruta.
* **Interfaz de línea de comandos (CLI) y GUI (opcional):**
    * La interfaz grafica fue realizada con la libreria Tkinter. Documentacion de la libreria: [Tkinter 8.6 reference: a GUI for Python — Python documentation](https://docs.python.org/3/library/tkinter.html)
    * Ofrece una interfaz de línea de comandos para una generación rápida de contraseñas, y opcionalmente, una interfaz gráfica de usuario para mayor comodidad.
* **Generación de contraseñas múltiples:** Capacidad para generar múltiples contraseñas a la vez.
* **Opción de exclusión de caracteres similares:** Para una mayor seguridad y para evitar la confusión del usuario final, se ha implementado la opción de excluir caracteres similares como la letra "l" minúscula, la letra "I" mayúscula y el número "1". O la letra "O" mayúscula y el número "0".
* **Almacenamiento seguro de contraseñas (opcional):** (Si se incluye) Permite al usuario almacenar las contraseñas generadas de forma segura, utilizando técnicas de cifrado robustas.

## Mejoras Implementadas

* **Mayor entropía:** Se ha mejorado el algoritmo de generación de números aleatorios para aumentar la entropía de las contraseñas, haciéndolas aún más difíciles de descifrar.
* **Soporte para caracteres Unicode:** Se ha añadido soporte para la inclusión de caracteres Unicode en las contraseñas, lo que aumenta la diversidad y complejidad de las mismas.
* **Evaluación de la fortaleza mejorada:** La función de evaluación de la fortaleza de la contraseña se ha actualizado para tener en cuenta más factores, como la presencia de patrones comunes y palabras del diccionario.
* **Interfaz de usuario más intuitiva:** La interfaz de línea de comandos y/o gráfica se ha rediseñado para ser más fácil de usar y comprender.
* **Generación de contraseñas masivas:** Ahora, es posible generar un número muy grande de contraseñas en solo una acción.
* **Exclusión de caracteres similares:** Se implementó la exclusión de caracteres que suelen causar confusión.

## Uso

### CLI

\`\`\`bash
python generador\_contraseñas.py -l 16 -c mayusculas minusculas numeros simbolos
\`\`\`

### GUI (opcional)

1.  Ejecutar el archivo `generador_contraseñas_gui.py`.
2.  Configurar la longitud y los caracteres deseados.
3.  Hacer clic en "Generar".

## Requisitos

* Python 3.6 o superior
* (Opcional) Librería `tkinter` para la GUI

## Instalación

1.  Clonar el repositorio:

 \`\`\`bash
    git clone [https://github.com/Elmotool01/logica-de-programacion](https://github.com/Elmotool01/logica-de-programacion)
    \`\`\`

2.  (Opcional) Instalar las dependencias:

    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`

## Contribución

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, puedes enviar un pull request.

## Licencia

Este proyecto se desarrollo en codigo libre.
