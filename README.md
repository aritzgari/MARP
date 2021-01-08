# MARP
Este el proyecto final de la asignatura de sistemas embebidos. Creado el grupo formado por Rubén Domínguez, Gorka Gómez y Aritz Garitano.

#Librerias
Antes de iniciar el programa es necesario instalar varias librerias. En este punto podrían ayudar los diferentes pantallazos de la carpeta de imagenes.
Pasos:
-Comprobar que exista pip3 o instalar en caso de que no exista.
-pip3 install python-snap7 para instalar snap7.
-Además necesitaremos instalar una segunda libreria, en este caso la carpeta que habria que descargar va incluida en la carpeta de librerias adjunta en el proyecto.
-Para instalar esta libreria vamos a la carpeta de librerias y entramos en /.../MARP/Librerias/snap7-full-1.4.2/build/unix en la que encontraremos el archivo 
arm_v7_linux.mk.
-Le hacemos make -f arm_v7_linux.mk all. (el archivo cambia según el sistema operativo en este caso es el de Raspberry 3)
-Luego buscamos el archivo libsnap7.so que se habrá creado al hacer el make en en caso de no encontrarlo esta dentro de /.../MARP/Librerias/snap7-full-1.4.2/build/bin/arm_v7-linux.
-Hay que cambiar el archivo common.py y que apunte directamente a ese archivo (/.../.local/lib/python3.7/site-packages/snap7 common.py).
-Por ultimo hay que descargarse la libreria de tkinter, para ello hay que introducir sudo apt-get install python3-tk.
#Ejecución
Para iniciar el programa hay que ejecutar el archivo main.py mediante python3 main.py

