#with open('hola.txt','rb') as archivo:
#print(archivo.read())
#archivo.close()

#for linea in archivo:
#    print(linea.strip())
#print(archivo.readlines())
# print(archivo.read())

#archivo.close()
"""
r = lectura
w = escritura
a = agregar al final
x = crear archivo
b = modo binario
t = modo texto
"""
import pandas as pd
df=pd.read_csv('persona.csv')
ordenar_By_nombre=df.sort_values(by='NOMBRE',ascending=True)
df['APROBADO'] = df['NOMBRE']!=''

df.to_csv('resultado.csv',index=False)

import matplotlib.pyplot as plt
plt.bar(df['NOMBRE'],df['TELEFONO'])
plt.title('Puntaje de ventas')
plt.xlabel('Nombre')
plt.ylabel('Puntuaje')
plt.show()