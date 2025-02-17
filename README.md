# Generador de Contraseñas Seguras con Aprendizaje Autónomo

[![Código Abierto](https://img.shields.io/badge/C%C3%B3digo-Abierto-brightgreen.svg)](LICENSE)

Este repositorio contiene el código fuente, diagramas de flujo y documentación de un proyecto de generador de contraseñas seguras, con la capacidad de adaptarse y mejorar con el tiempo mediante un sistema de aprendizaje autónomo (actualmente en desarrollo, representado en los diagramas).

## Objetivos del Proyecto

*   **Desarrollar un generador de contraseñas robusto:** Crear una aplicación que genere contraseñas que cumplan con altos estándares de seguridad.
*   **Implementar aprendizaje autónomo (en desarrollo):** Dotar al generador de la capacidad de aprender de patrones y adaptarse a nuevas amenazas (representado en los diagramas, aún no implementado en el código).
*   **Explorar algoritmos:** Experimentar con diferentes enfoques para la generación de contraseñas.
*   **Documentar el proceso:** Proporcionar documentación clara y completa, incluyendo diagramas, código comentado y explicaciones.

## Estructura del Repositorio

El repositorio contiene los siguientes *archivos*:

*   **`diagramas.pdf`:** Diagrama de flujo del algoritmo *inicial* del generador. Muestra la generación básica de contraseñas. ([https://github.com/Elmotool01/logica-de-programacion/blob/main/diagramas.pdf](https://github.com/Elmotool01/logica-de-programacion/blob/main/diagramas.pdf))
*   **`diagramas generador seguro de contraseñas aprendizaje autonomo 2 Francisco Martínez.pdf`:** Diagramas de flujo que representan la *lógica del futuro sistema de aprendizaje autónomo*.  (Este sistema aún *no* está implementado en el código, pero los diagramas muestran el diseño). ([https://github.com/Elmotool01/logica-de-programacion/blob/main/diagramas%20generador%20seguro%20de%20contrase%C3%B1as%20aprendizaje%20autonomo%202%20Francisco%20mart%C3%ADnez.pdf](https://github.com/Elmotool01/logica-de-programacion/blob/main/diagramas%20generador%20seguro%20de%20contrase%C3%B1as%20aprendizaje%20autonomo%202%20Francisco%20mart%C3%ADnez.pdf))
*   **`generador_contrasenas.py` (¡Nombre real del archivo!):** Código fuente del generador de contraseñas. Implementa la lógica descrita en `diagramas.pdf`, con opciones para configurar la longitud y los tipos de caracteres. *Este archivo contiene el código que proporcionaste y mejoraste previamente.*  (Añade aquí el enlace al archivo en GitHub)
*   **`entorno de programación primer avance primera prueba.jpg`:** Captura de pantalla del entorno de programación, mostrando la configuración (versiones de Python, etc.). ([https://github.com/Elmotool01/logica-de-programacion/blob/main/entorno%20de%20programaci%C3%B3n%20primer%20avance%20primera%20prueba.jpg](https://github.com/Elmotool01/logica-de-programacion/blob/main/entorno%20de%20programaci%C3%B3n%20primer%20avance%20primera%20prueba.jpg))
*   **`entorno de programación primer avance.jpg`:** Captura de pantalla de la interfaz de usuario del generador de contraseñas en acción. ([https://github.com/Elmotool01/logica-de-programacion/blob/main/entorno%20de%20programaci%C3%B3n%20primer%20avance.jpg](https://github.com/Elmotool01/logica-de-programacion/blob/main/entorno%20de%20programaci%C3%B3n%20primer%20avance.jpg))

## Requisitos y Configuración del Entorno

*   **Python:** Versión 3.12 (o superior).  Puedes descargar la última versión desde la página oficial de Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
    *   **Instalación en Windows:**  Durante la instalación, *asegúrate de marcar la casilla "Add Python X.Y to PATH"* (donde X.Y es la versión). Esto es crucial para que puedas ejecutar Python desde la línea de comandos.
    *   **Instalación en Linux/macOS:** Python 3 a menudo viene preinstalado. Abre una terminal y escribe `python3 --version` para comprobarlo. Si no está instalado o necesitas una versión más reciente, usa el gestor de paquetes de tu distribución (ejemplos: `apt install python3` en Debian/Ubuntu, `brew install python3` en macOS).

*   **Librerías:**
    *   **`random`:**  Parte de la biblioteca estándar de Python (no necesita instalación).  `random` proporciona funciones para generar números pseudoaleatorios.  En este proyecto, se utiliza para seleccionar caracteres aleatoriamente al crear las contraseñas.  Sin aleatoriedad, las contraseñas serían predecibles y, por lo tanto, inseguras.
    *   **`string`:** Parte de la biblioteca estándar de Python (no necesita instalación).  `string` contiene constantes útiles que representan conjuntos de caracteres comunes.  En este código, se usan:
        *   `string.ascii_letters`: Todas las letras ASCII, mayúsculas y minúsculas (a-z, A-Z).
        *   `string.digits`:  Los dígitos del 0 al 9.
        *   `string.punctuation`:  Símbolos de puntuación (como !"#$%&'()*+, etc.).
        Estas constantes permiten definir fácilmente qué tipos de caracteres se pueden incluir en una contraseña, y facilitan la creación de contraseñas con diferentes niveles de complejidad.

## Cómo Ejecutar la Aplicación

1.  **Clona el repositorio:**

    ```bash
    git clone [https://github.com/Elmotool01/logica-de-programacion.git](https://github.com/Elmotool01/logica-de-programacion.git)
    cd logica-de-programacion
    ```

2.  **Ejecuta el generador de contraseñas:**

    ```bash
    python generador_contrasenas.py  # ¡Usa el nombre de archivo correcto!
    ```

    El programa te presentará un menú con opciones para generar diferentes tipos de contraseñas. Sigue las instrucciones en la consola.

## Imágenes del Entorno de Programación
Configuracion del entorno de programacion:
(https://github.com/Elmotool01/logica-de-programacion/blob/main/entorno%20de%20programaci%C3%B3n%20primer%20avance%20primera%20prueba.jpg)
Ejemplo de interfaz del generador:
(https://github.com/Elmotool01/logica-de-programacion/blob/main/entorno%20de%20programaci%C3%B3n%20primer%20avance.jpg)

## Contribuciones

Las contribuciones son bienvenidas. Si quieres mejorar este proyecto:

1.  Haz un *fork* del repositorio.
2.  Crea una nueva rama: `git checkout -b mi-feature`
3.  Realiza tus cambios y haz *commit*: `git commit -m "Agregada nueva funcionalidad"`
4.  Sube la rama: `git push origin mi-feature`
5.  Abre un *Pull Request* en GitHub.

## Licencia

Este proyecto es de código libre.

## Contacto

Si tienes preguntas, sugerencias o encuentras errores, por favor, abre un *issue* en este repositorio de GitHub.  [Opcional: añade tu correo electrónico si quieres que te contacten directamente].
