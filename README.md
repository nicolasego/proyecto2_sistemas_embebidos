# proyecto2_sistemas_embebidos
Códigos implementados durante el desarrollo del segundo proyecto.

El presente repositorio presenta codigos en python que permiten la conmutación de pines del  GPIO de la raspberry.

conmutación pin 17 -----> https://github.com/nicolasego/proyecto2_sistemas_embebidos/blob/main/pin17.c
conmutación pin 27 -----> https://github.com/nicolasego/proyecto2_sistemas_embebidos/blob/main/pin27.c

Un script en bash que permite la conmutación de los dos pines mediante el comando &.

uso del comando & ------> https://github.com/nicolasego/proyecto2_sistemas_embebidos/blob/main/conmutar.sh

De igual forma se presenta un script que utiliza el sensor one wire  DS18B20, accediendo a la medida del mismo y enviandolas a un archivo CSV, que contiene la  fecha de extracción y el valor de temperatura.

sensor DS18B20 -----> https://github.com/nicolasego/proyecto2_sistemas_embebidos/blob/main/extraccion_temperatura.sh

Por otro lado se tiene otro script que presenta el uso del protocolo I2C, mediante el sensor ADXL345, extrayendo las medidas del acelerometro.

sensor ADXL345 ----> https://github.com/nicolasego/proyecto2_sistemas_embebidos/blob/main/acelerometro.py

Tambien se presenta un script que extrae un promedio de N medidas extraidas del sensor ADXL345.

promedio sensor ADXL345 ----> https://github.com/nicolasego/proyecto2_sistemas_embebidos/blob/main/promedio_acelerometro.py

