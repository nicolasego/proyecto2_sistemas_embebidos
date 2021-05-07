# proyecto2_sistemas_embebidos
Códigos implementados durante el desarrollo del segundo proyecto.

El presente repositorio presenta codigos en python que permiten la conmutación de pines del  GPIO de la raspberry.

conmutación pin 17 ----->
conmutación pin 27 ----->

Un script en bash que permite la conmutación de los dos pines mediante el comando &.

uso del comando & ------>

De igual forma se presenta un script que utiliza el sensor one wire  DS18B20, accediendo a la medida del mismo y enviandolas a un archivo CSV, que contiene la  fecha de extracción y el valor de temperatura.

sensor DS18B20 ----->

Por otro lado se tiene otro script que presenta el uso del protocolo I2C, mediante el sensor ADXL345, extrayendo las medidas del acelerometro.

sensor ADXL345 ---->

Tambien se presenta un script que extrae un promedio de N medidas extraidas del sensor ADXL345.

