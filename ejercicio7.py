#pylab inline
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import random
from time import time
from  ejercicio5 import Insert_Sort
from ejercicio6 import quick_sort

datos = [ii*100 for ii in range(1,21)]
time_is = []
time_qs = []

for ii in datos:
    lista_is = random.sample(range(0,10000000),ii)
    lista_qs = lista_is.copy()
    t0 = time()
    Insert_Sort(lista_is)
    time_is.append(round(time()-t0,6))

    t0 = time()
    quick_sort(lista_qs)
    time_qs.append(round(time()-t0,6))


print("Tiempos parciales de ejecucin en insert sort {} [s]".format(time_is))
print("Tiempos parciales de ejecucin en quick sort {} [s]".format(time_qs))
figura, ax = plt.subplots()
ax.plot(datos,time_is,label="insert sort",marker="*",color="r")
ax.plot(datos,time_qs,label="quick sort",marker="o",color="b")
ax.set_xlabel("Datos")
ax.set_ylabel("Tiempo")
ax.grid(True)
ax.legend(loc=2)
plt.title("Tiempo de ejecucion en [s] insert sort vs quick sort")
plt.show()

