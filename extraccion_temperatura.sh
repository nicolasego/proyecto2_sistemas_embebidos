#!/bin/bash
#se genera en fecha el nombre del archivo que en este caso es la fecha,hora y el .csv
fecha=`date +"%Y%m%d-%H:%M:%S".csv`
#se va a la dirección en la que se encuentra nuestra medida de temperatura del sensor
cd /sys/bus/w1/devices/28-3c01d075651a
#se genera el bucle para la extracción de la medida de temperatura y el envio al csv
while [ 1 ]
do		
	#se le asiga a la variable temp el valor extraido del sensor
	temp=$(cat temperature)
	#se realiza el adecuamiento de este valor mediante la division por 1000 y se establece el numero de decimales
	temp=$(echo "scale=2; $temp/1000" | bc -l)"°C"
	#se agraga al archivo las dos columas requeridas separadas por coma. las columas son la fecha y la temperatura
	date +"%Y%m%d %H%M%S"","$temp>>/home/pi/$fecha 
	#se genera el sleep que permite la toma cada 10 segundos
	sleep 10
done

