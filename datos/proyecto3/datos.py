import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("datosProyecto.csv")
x = df["AÑO"]
y = df["POBLACIÓN_5_16"]
#z = df["poblacionmatriculada"]
#t = df["personasmatriculadas"]

plt.plot(x,y)
#plt.plot(x,z)
#plt.plot(x,t)
#plt.bar(x, y)
plt.xlabel('Fecha')
plt.ylabel('Poblacion 5 16')
plt.title('Gráfico simple de Matplotlib')
plt.show()