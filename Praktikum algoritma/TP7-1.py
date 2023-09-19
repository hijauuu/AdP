# LOLA PUNYA

"PROGRAM MEMPLOT DATA X TERHADAP F1(X) DAN F2(X)"
import numpy as np
import matplotlib.pyplot as plt
#Masukkan program
x = np.array([1,3,5,7,9,11,13,15,17,19,21,23])
f1 = np.array([1609.5,373.2,146.3,60,18.4,-4.1,-17.1,-25.1,-30.1,-33.4,-35.5,-36.9])
f2 = np.array([-32,-71.7,-109.5,-142.4,-165.8,-173.4,-157.8,-109.5,-17.9,129.3,345.9,647.6])
plt.plot(x,f1,'go-',label='x-f1(x)')
plt.plot(x,f2,'bo-',label='x-f2(x)')
plt.title('Grafik Hubugan nilai x terhadap f(x)',pad=10,fontsize=10,color='black')
plt.xlabel('x',labelpad=5)
plt.ylabel('f(x)',labelpad=5)
plt.grid(color='darkgrey',linestyle='--')
plt.legend(loc='upper right',title='Keterangan')
plt.show()
