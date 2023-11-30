## VAQUERITO
<em> VAQUERITO </em>

### Juego estilo Arcade
Este es un juego de estilo arcade salto de obstaculos
Teclas:

**Space** = Saltar

libreria: 

1. **python**                    **3.10.11**
2. **pygame**                    **2.5.1**

A continuacion le dejo una guia de como copilarlo:
Vamos a crear un entorno virtual con Pipenv en la raíz del proyecto.

Para ello necesitamos instalar Pipenv si no lo tenemos:

***pip install pipenv**

Ahora configuramos el **requirements.txt**con los paquetes mínimos necarios:

Y creamos en Game\ el entorno virtual a partir del requirements:

**pipenv install -r requirements.txt**

Esto creará en la raíz un Pipfile y un Pipfile.lock.

A continuación instalamos en ese entorno virtual auto-py-to-exe para generar el ejecutable:

**pipenv install auto-py-to-exe**

*Y ejecutamos el programa en este entorno con los paquetes mínimos:

**pipenv run auto-py-to-exe**

En la pantalla web del programa seleccionaremos:

Script Location será el main.py del videojuego.
One Directory (OneFile podría no funcionar o requerir directorios).
Console Window Based.
Additional Files añadiremos el directorio res de recursos externos.
Icon si tenemos una imagen ico para el ejecutable.








