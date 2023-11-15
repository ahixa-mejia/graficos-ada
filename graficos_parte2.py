import numpy as np
import matplotlib.pyplot as plt

# Generar datos sintéticos
rng = np.random.default_rng(42)

# Datos de calificaciones de los estudiantes
matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)
literatura = rng.integers(60, 100, 20)

# Datos de errores para el gráfico de barras de error
errores_matematicas = rng.uniform(2, 5, 2)
errores_matematicas = [min(errores_matematicas), max(errores_matematicas)]

errores_ciencias = rng.uniform(1, 4, 2)
errores_ciencias = [min(errores_ciencias), max(errores_ciencias)]

errores_literatura = rng.uniform(3, 6, 2)
errores_literatura = [min(errores_literatura), max(errores_literatura)]

# Calcular calificaciones promedio y errores
promedio_matematicas = np.mean(matematicas)
promedio_ciencias = np.mean(ciencias)
promedio_literatura = np.mean(literatura)

# Crear el gráfico de barras de error
materias = ['Matemáticas', 'Ciencias', 'Literatura']
calificaciones_promedio = [promedio_matematicas, promedio_ciencias, promedio_literatura]
errores = np.array([errores_matematicas, errores_ciencias, errores_literatura])

# Crear el gráfico de barras de error
plt.errorbar(materias, calificaciones_promedio, yerr=errores.T, fmt='o', capsize=5)

# Añadir etiquetas y título
plt.title('Calificaciones Promedio con Barras de Error')
plt.xlabel('Materias')
plt.ylabel('Calificaciones Promedio')

# Mostrar el gráfico
plt.show()
