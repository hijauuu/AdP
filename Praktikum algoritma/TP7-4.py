"PROGRAM MEMPLOT DATA OSILASI.CSV"
import matplotlib.pyplot as plt
import csv
osilasi = []
with open ('osilasi.csv') as csv_data:
    csv_reader = csv.reader(csv_data)
    for row in csv_reader:
        osilasi.append(row)
t = []
Y = []
for i in range(1,len(osilasi)):
    t.append(osilasi[i][1])
    Y.append(osilasi[i][2])
plt.plot(t,Y,'b-')
plt.title('Grafik Hubungan Waktu Terhadap Simpangan',pad=5,fontsize=10,color='black')
plt.xlabel('t(s)',labelpad=2)
plt.ylabel('Simpangan',labelpad=2)
plt.show()
