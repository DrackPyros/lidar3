# Instrucciones de instalación y uso de Lidar
## Instalación
Voy a detallar los pasos para realizar la instalación de la unidad lidar en nuestro dispositivo Raspberry PI 4

*Són iguales para el sistema Ubuntu que he estado utilizando.*

1. Instalar Python 3.
    > sudo apt install python3

2. Instalar el paquete Lidar3 desde su repositorio de GitHub.
    > pip install PyLidar3

3. Instalar la librerias 
    - Matplot:
        > pip install matplotlib
    - Pandas:
        > pip install matplotlib
    - Libatlas:
        > sudo apt instal libatlas-base-dev

4. Añadir el usuario al grup tty y dialout.
    > sudo chmod tty dialout usuario

5. Salir de la sesión o reiniciar para que se apliquen los cambios del usuario en los grupos.

6. Crear un directorio para alojar nuestro proyecto.

7. Crear o importar un script de testing.

8. Hacerlo funcionar.
    > python3 script.py

*Un ejemplo de script lo podemos encontrar en el repositorio de PyLidar3*

Nota: En el script que nos proporciona el repositorio, hay que cambiar la linea que pide el puerto por la siguiente:
> port = "/dev/ttyUSB0"

Aunque el sistema no cuente con este puerto de manera natural, este se creará y se enlazará en cuanto se ejecute el script.

## Uso
Ejecutas el script y el lidar hará un intento de funcionar, pueden pasar 2 cosas:

- En caso de que todo vaya bien, parará e imprimirá por consola la información del mismo y comenzará a funcionar otra vez.

- Si va mal, imprimirá por consola "Error connecting to device" y la solución que hemos encontrado ha sido desconectar fisicamente el puerto USB  y volverlo a conectar. **Funciona 1 de cada 2 veces**

## Links
1. Repositorio de PyLidar3: https://github.com/lakshmanmallidi/PyLidar3

2. Manual de usuario Lidar X-4: 
    https://www.ydlidar.com/Public/upload/files/2020-04-13/YDLIDAR-X4-USER%20Manual.pdf