#!/usr/bin/env python
# -*- coding: utf-8 -*-
#=== IMPORTS ===
import snap7
import time
import time
import dht_config
import RPi.GPIO as GPIO
from pantalla import *

#=== CONSTANTES ===
tiempo_bucle = 1 #En segundos

#Datos de conexion
IP = "192.168.0.1"
RACK = 0
SLOT = 1

#=== VARIABLES ===
#Definimos PLC como cliente de Snap7
global PLC
PLC = snap7.client.Client()
#Interruptor encendido
encendido = 0
GPIO.setmode(GPIO.BCM)
global gpio_pin_switch
gpio_pin_switch = 24
#Buzzer
global gpio_pin_buzzer
gpio_pin_buzzer = 23
#LEDs
global gpio_pin_led_r
gpio_pin_led_r = 25
global gpio_pin_led_a
gpio_pin_led_a = 26
#Sensor temperatura y humedad
gpio_pin_sensorTH = 18
GPIO.setup(gpio_pin_switch, GPIO.IN)
sensor = dht_config.DHT(gpio_pin_sensorTH)

#Parametros de funcionamiento
temp_min = 0 #en *C
temp_max = 30 #en *C
humedad_min = 20 #en %
humedad_max = 70 #en %

#=== FUNCIONES ===
def conectar(IP,RACK,SLOT):
    PLC.connect(IP,RACK,SLOT)

def desconectar():
    PLC.disconnect()

def leer_DB(n_DB, offset, cant_bytes):
    db = ""
    try:
        conectar(IP,RACK,SLOT)
        db = PLC.db_read(n_DB, offset, cant_bytes)
    except snap7.snap7exceptions.Snap7Exception:
        desconectar()
        print("Lectura imposible, revisar PLC")
        return("Lectura imposible, revisar PLC")
    desconectar()
    return db

def leer_temperatura_humedad():
    humi, temp = sensor.read()
    #print('Temperatura {0:.1f}'.format(temp))
    return humi, temp


def procesar(numcanal):
    global encendido
    encendido = GPIO.input(24)

#=== CODIGO ===
#PARAMETRIZACION INICIAL TODO Que si no metes nada no pete
temp_min = int(input('Temperatura minima(°C): ')) #en *C
temp_max = int(input('Temperatura maxima(°C): ')) #en *C
humedad_min = int(input('Humedad minima(%): ')) #en %
humedad_max = int(input('Humedad maxima(%): ')) #en %
#Iniciamos el pin del sensor de temperatura
GPIO.setup(gpio_pin_switch, GPIO.IN)
GPIO.add_event_detect(gpio_pin_switch, GPIO.BOTH, callback=procesar)
#Iniciamos el pin del buzzer
GPIO.setup(gpio_pin_buzzer, GPIO.OUT)
#Iniciamos el pin del LED rojo
GPIO.setup(gpio_pin_led_r, GPIO.OUT)
#Iniciamos el pin del LED azul
GPIO.setup(gpio_pin_led_a, GPIO.OUT)


#ELEMENTOS DE LA PANTALLA
pantalla = Aplicacion()


#BUCLE DE ACTUALIZACION DE LOS DATOS
while True:
    if encendido:
        #Reseteamos el valor del zumbador para este ciclo
        zumbador = False

        #db = leer_DB(300,0,1)
        db = bytearray(b'\x00\x00\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xe4\x0c\x16\x03\t.\x16\x01\xd4\xbc\x18\x07\xe4\x0c\x16\x03\n\x024 =\xd8`\x00\x0f\x1c\x94\xfe\x02A4                                                                                                                                                                                                                                                            \xfe\x08Paquillo                                                                                                                                                                                                                                                      \xfe\x04Paroha\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00c\x00F\x00\x1d\x00c?5\x02\x96\xfe\nAleta DCHA                                                                                                                                                                                                                                                    \x00\x00+\x03\xfe\x02A4                                                                                                                                                                                                                                                            \xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00') 
        
        #Leemos cada booleano como una aviso separado
        aviso0 = snap7.util.get_bool(db, 1324, 0)
        aviso1 = snap7.util.get_bool(db, 1324, 1)
        aviso2 = snap7.util.get_bool(db, 1324, 2)
        aviso3 = snap7.util.get_bool(db, 1324, 3)
        aviso4 = snap7.util.get_bool(db, 1324, 4)
        aviso5 = snap7.util.get_bool(db, 1324, 5)
        aviso6 = snap7.util.get_bool(db, 1324, 6)
        aviso7 = snap7.util.get_bool(db, 1324, 7)
        aviso8 = snap7.util.get_bool(db, 1325, 0)
        aviso9 = snap7.util.get_bool(db, 1325, 1)
        aviso10 = snap7.util.get_bool(db, 1325, 2)

        if aviso0:
            print("Maquina sin pintura.")
            zumbador = True
        if aviso1:
            print("Nivel de pintura bajo.")
        if aviso2:
            print("Paro de emergencia activo.")
            zumbador = True
        if aviso3:
            print("Tiempo de ciclo excedido.")
            zumbador = True
        if aviso4:
            print("Puerta de estación abierta.")
            zumbador = True
        if aviso5:
            print("Robot en fallo.")
            zumbador = True
        if aviso6:
            print("Robot desconectado.")
            zumbador = True
        if aviso7:
            print("Boquilla obstruida.")
            zumbador = True
        if aviso8:
            print("Pieza no ha alcanzado posición.")
            zumbador = True
        if aviso9:
            print("Pieza terminada en espera.")
            zumbador = True
        if aviso10:
            print("Máquina parada, falta de piezas de entrada.")

        #Forzado provisional
        """
        aviso2 = True
        aviso4 = True
        aviso6 = True
        aviso7 = True
        aviso10 = True
        """

        #Info pantalla
        Info_pantalla = {
            "0": aviso0,
            "1": aviso1,
            "2": aviso2,
            "3": aviso3,
            "4": aviso4,
            "5": aviso5,
            "6": aviso6,
            "7": aviso7,
            "8": aviso8,
            "9": aviso9,
            "10": aviso10,
        }        

        #Leemos temperatura y humedad actual
        humedad_actual, temp_actual = leer_temperatura_humedad()
        #Y los pasamos a la info de la pantalla
        Info_pantalla["humedad"] = humedad_actual
        Info_pantalla["temp"] = temp_actual

        #Comparamos con los valores de la parametrizacion
        #Temperatura
        if temp_min > temp_actual:
            #Error temperatura demasiado baja, activar LED
            print("Hace frio ({0:.1f}°C)".format(temp_actual))
            zumbador = True
            GPIO.output(gpio_pin_led_a,1)
        else:
            GPIO.output(gpio_pin_led_a,0)

        if temp_max < temp_actual:
            #Error temperatura demasiado alta, activar LED
            print("Hace calor ({0:.1f}°C)".format(temp_actual))
            zumbador = True
            GPIO.output(gpio_pin_led_r,1)
        else:
            GPIO.output(gpio_pin_led_r,0)

        #Humedad
        if humedad_min > humedad_actual:
            #Error humedad demasiado baja
            print("Ambiente demasiado seco ({0:.1f}%)".format(humedad_actual))
            zumbador = True
        if humedad_max < humedad_actual:
            #Error humedad demasiado alta
            print("Ambiente demasiado húmedo ({0:.1f}%)".format(humedad_actual))
            zumbador = True
        
        if zumbador:
            print("bzzzzz")
            #GPIO.output(gpio_pin_buzzer,1)
            time.sleep(0.2)
            GPIO.output(gpio_pin_buzzer,0)
            time.sleep(0.8)
        else:
            GPIO.output(gpio_pin_buzzer,0)
            time.sleep(tiempo_bucle)

        #Actualizacion pantalla
        pantalla.verinfo(Info_pantalla)
        
        print("===========================") #Separador de prints

        #Actualizamos la pantalla
        pantalla.raiz.update_idletasks()
        pantalla.raiz.update()