#se importan las librerias necesarias para el correcto funcionamiento.
import time
import board
import busio
import numpy as np
#la libreria statics es utilizada durante el proceso del promedio.
import statistics as stats
#se importa la libreria de adafruit del sensor que se utiliza(ADXLl345).
import adafruit_adxl34x
#se utiliza la clase I2C del modulo busio, que esta constituia por el SCL y el SCA.
i2c = busio.I2C(board.SCL, board.SDA)
#se utiliza la clase del sensor utilizado, en este caso el ADXL345, en la dirección del i2c.
accelerometer = adafruit_adxl34x.ADXL345(i2c)
#se realiza una impresión con el fin de que posterior a esta se ingrese el valor de N.
print("ingrese el valor de N")
#se pide el ingreso del valor de N.
N=int(input())
#se crean los vectores vacios que seran utilizados para guardar los valores.
medidas=[]
x=[]
y=[]
z=[]
#se genera el ciclo for para limitar la toma de datos para la extracción del promedio.
for i in range(N):
    #se extrae la medida del sensor.
    medidas=np.array(accelerometer.acceleration)
    #se anexan los correspondientes valores de medidas extraidas al eje respectivo.
    x.append(medidas[0])
    y.append(medidas[1])
    z.append(medidas[2])
    #se genera un sleep de un segundo.
    time.sleep(1)
#una vez se cumple el ciclo for, se procede a realizar el promedio de cada uno de los ejes.
promedio=[stats.mean(x),stats.mean(y),stats.mean(z)]
#se realiza la impresion del promedio.
print(promedio)
        
    
