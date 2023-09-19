"PROGRAM MEMPLOT GRAFIK FUNGSI DARI Y=50 SIN(2X)"
import numpy as np
import matplotlib.pyplot as plt
from math import pi
#Membuaat masukkan 
x = np.linspace(0,4.*np.pi,200)
y = 50.*np.sin(2*x)
#Menampilkan data plot 
plt.plot(x,y,'b-')
plt.title('Grafik Fungsi y = 50sin(2x)',pad=10,fontsize=10,color='black')
plt.xlabel('x',labelpad=5)
plt.ylabel('y = 50sin(2x)',labelpad=5)
plt.grid(color='darkgrey',linestyle='--')
plt.show()
