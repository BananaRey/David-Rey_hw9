import numpy as np
import matplotlib.pyplot as plt

#se importan los datos
arch_py=np.loadtxt('times_python.csv')
arch_c++=np.loadtxt('times_cpp.csv')
#se crea la lista para el eje x de ambos datos
dominio_py=np.arange(len(arch_py))
dominio_c++=np.arange(len(arch_c++))
#se grafica
plt.plot(dominio_py,arch_py)
plt.plot(dominio_c++,arch_c++)
plt.show()
