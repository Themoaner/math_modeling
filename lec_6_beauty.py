import matplotlib.pyplot as plt 
import numpy as np 

x = [3,4,5]
y = [40,10,30]

plt.plot(x,y, color='g', label='luchte', marker='>', ms=5)

#украшательства
plt.xlabel('Coord: x') # подпись оси Х
plt.ylabel('Coord:  y')
plt.legend()
plt.title('Base')#общее название
plt.grid()#подключение сетки
plt.show()
