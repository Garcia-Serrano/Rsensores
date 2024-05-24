Proyecto creado en conjunto por Marcos Serrano y Hugo Garcia

En este proyecto se detecta cuando una persona se ha puesto de puntillas a traves de un acelerometro y un giroscopio ya integrados en el micro que se ha usado.
El dicho micro es el arduino nano 33 ble.

La detección se realiza colocando el arduino con el codigo (proyecto_puntillas.ino) cargado y conectado a un ordenador, en la parte externa del tobillo derecho, 
con el puerto USB hacia el talón.

También se han tomado medidas a diferentes personas con distintas condiciones, como puede ser la edad, el sexo, etc. Estas medidas han sido tomadas implementando
el codigo c++ de la carpeta "Recogida_datos" y procesadas con el archivo matlab de la carpeta "DataBase" para ver el comportamiento que capta el sensor
y se ha creado un .csv y un excel donde se ubican todos los datos tomados de cada persona asi como las variables más interesantes graficadas (estos archivos 
estan ubicados en la misma carpeta) 

Y por último se ha comparado en un excel uicado en la carpeta "Componentes elegidos", los distintos sensores IMU disponibles en el mercado y distintos circuitos de alimentación de estos, donde se ha hecho un análisis decuál es la mejor opción.
