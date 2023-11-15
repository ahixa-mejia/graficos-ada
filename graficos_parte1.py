import numpy as np
import matplotlib.pyplot as plt

# Generar datos sintéticos
rng = np.random.default_rng(42)

# Datos de calificaciones de los estudiantes
matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)
literatura = rng.integers(60, 100, 20)

# Crear el gráfico de dispersión
plt.scatter(matematicas, ciencias, color='blue', alpha=0.7)

# Personalizar el gráfico
plt.title('Relación entre Calificaciones de Matemáticas y Ciencias')
plt.xlabel('Calificaciones de Matemáticas')
plt.ylabel('Calificaciones de Ciencias')

# Mostrar el gráfico
plt.show()
