"PROGRAM MEMBUAT HUBUNGAN KETINGGIAN, KECEPATAN, PERCEPATAN TERHADAP WAKTU"
import numpy as np
import matplotlib.pyplot as plt
#Masukkan program
vo = int(input("Masukkan nilai kelajuan awal peluru=",))
yo = int(input("Masukkan nilai ketinggian awal peluru=",))
g = int(input("Masukkan nilai kecepatan gravitasi=",))
dt = float(input("Masukkan range waktu=",))
t_kem = (2*vo)/g #Waktu untuk yang dibutuhkan untuk kembali ke tanah
#Perhitungan
t = np.arange(0,t_kem+dt,dt)
yt = np.array(yo+vo*t-0.5*g*t**2)
vt = np.array(vo-g*t)
at = np.array(g*t-g*(t-1))

#Plot nilai t dengan yt
plt.subplot(2,2,1)
plt.plot(t,yt,'ro-')
plt.title('Grafik Hubungan Waktu dengan Ketinggian',pad=5,fontsize=10,color='black')
plt.xlabel('t(s)',labelpad=2)
plt.ylabel('yt(m)',labelpad=2)
plt.grid(color='darkgrey',linestyle='--')

#Plot nilai t dengan vt
plt.subplot(2,1,2)
plt.plot(t,vt,'bo-')
plt.title('Grafik Hubungan Waktu dengan Kecepatan',pad=5,fontsize=10,color='black')
plt.xlabel('t(s)',labelpad=2)
plt.ylabel('vt(m/s)',labelpad=2)
plt.grid(color='darkgrey',linestyle='--')

#Plot nilai t dengan at
plt.subplot(2,2,2)
plt.plot(t,at,'ro-')
plt.title('Grafik Hubungan Waktu dengan Percepatan',pad=5,fontsize=10,color='black')
plt.xlabel('t(s)',labelpad=2)
plt.ylabel('at(m/s^2)',labelpad=2)
plt.grid(color='darkgrey',linestyle='--')
plt.show()
