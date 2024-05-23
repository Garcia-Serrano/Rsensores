import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

y = 0
dato = 0
datos = 0
promedio = 0
desv = 0

ser = serial.Serial('COM4', 9600)

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [], 'ro')


def init():
    ax.set_xlim(0, 100)
    ax.set_ylim(-1, 1)
    return ln,


def update(frame):
    global datos, y
    dato = (ser.readline().decode("utf-8").strip())
    xdata.append(frame)
    ydata.append(dato)
    ln.set_data(xdata, ydata)
    datos = datos + dato
    y[frame] = dato
    return ln,


ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True)
plt.show()

ser.close()

promedio = datos/100
print("El promedio de las aceleraciones es ")
print(promedio)
while i < 100:
    desv += y[i] - promedio
    i = i+1

desv_estandar = math.sqrt(desv*desv/100)
print("La desviacion estandar es de ")
print(desv_estandar)
