#se importan las librerias necesarias para el correcto funcionamiento.
import time
import board
import busio
#se importa la libreria de adafruit del sensor que se utiliza(ADXLl345).
import adafruit_adxl34x
#se utiliza la clase I2C del modulo busio, que esta constituia por el SCL y el SCA.
i2c = busio.I2C(board.SCL, board.SDA)
#se utiliza la clase del sensor utilizado, en este caso el ADXL345, en la dirección del i2c.
accelerometer = adafruit_adxl34x.ADXL345(i2c)
#se genera el bucle infinito.
while True:
    #se realiza la impresión de los valores extraidos del acelerometro.
    print(accelerometer.acceleration)
    #se genera un sleep de un segundo.
    time.sleep(1)
