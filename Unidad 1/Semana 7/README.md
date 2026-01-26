# Programa: Uso de Constructores y Destructores en Python

## Descripción del programa

Este proyecto demuestra el uso de **constructores (`__init__`)** y **destructores (`__del__`)** en Python mediante un ejemplo sencillo orientado a objetos. El programa simula la gestión de un archivo de texto, mostrando cómo un objeto inicializa recursos al crearse y cómo intenta liberarlos cuando deja de existir.

El proyecto está organizado siguiendo una **arquitectura por capas**, separando las responsabilidades en modelos, servicios y un archivo principal.

---

## Estructura del proyecto

```
proyecto_constructores/
│
├── modelos/
│   └── archivo.py
│
├── servicios/
│   └── gestor_archivos.py
│
└── main.py
```

---

## Cómo ejecutar el programa

1. Asegúrate de tener **Python 3** instalado.
2. Abre el proyecto en **PyCharm**, **Visual Studio Code** o cualquier IDE de tu preferencia.
3. Ejecuta el archivo principal con el siguiente comando:

```bash
python main.py
```

Al ejecutarse, el programa creará un archivo de texto, escribirá contenido en él y finalizará su ejecución.

---

## Uso de `__init__` y `__del__`

* El método **`__init__`** se utiliza en la clase `Archivo` (ubicada en `modelos/archivo.py`) para:

  * Inicializar el nombre del archivo
  * Abrir el archivo como recurso del sistema

* El método **`__del__`** se utiliza en la misma clase para:

  * Cerrar el archivo cuando el objeto es destruido
  * Registrar en consola que el recurso fue liberado

El uso del destructor se evidencia cuando el objeto `Archivo` deja de tener referencias dentro del servicio `GestorArchivos`.

---

## Observación importante

La ejecución del método `__del__` depende del **recolector de basura de Python**, por lo que su llamada no siempre ocurre en un momento exacto, pero el ejemplo permite evidenciar claramente su propósito y funcionamiento.
