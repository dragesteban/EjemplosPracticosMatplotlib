#Ejemplos de tipos de graficos

#Ejemplo usando el comando plot
import matplotlib.pyplot as plt
import numpy as np

#Estilo del grafico
plt.style.use('_mpl-gallery')

#Datos de x y y
x = np.linspace(0, 10, 100)
y = 4 + 2 * np.sin(2 * x)

#Se indica que se va a usar el comando plot
fig, ax = plt.subplots()
ax.plot(x, y, linewidth=2.0)

#Limites de x y y
ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

#Se muestra la grafica
plt.show()

#Ejemplo usando el comando contourf
import matplotlib.pyplot as plt2
import numpy as np2

#Estilo del grafico
plt2.style.use('_mpl-gallery-nogrid')

# Se escriben los datos que se van a usar
X, Y = np2.meshgrid(np2.linspace(-3, 3, 256), np2.linspace(-3, 3, 256))
Z = (1 - X/2 + X**5 + Y**3) * np2.exp(-X**2 - Y**2)
levels = np2.linspace(Z.min(), Z.max(), 7)

# Se indica que se va a usar el comando contourf
fig, ax = plt2.subplots()
ax.contourf(X, Y, Z, levels=levels)

#Se muestra la grafica
plt2.show()

#Nota: Para ver el segundo grafico se debe cerrar el primero