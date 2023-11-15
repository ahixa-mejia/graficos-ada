import numpy as np
import matplotlib.pyplot as plt

# Generar datos sintéticos
rng = np.random.default_rng(42)

# Datos de calificaciones de los estudiantes
matematicas = rng.integers(50, 100, 20)

# Crear el histograma
plt.hist(matematicas, bins=10, color='skyblue', edgecolor='black')

# Personalizar el histograma
plt.title('Distribución de Calificaciones de Matemáticas')
plt.xlabel('Calificaciones')
plt.ylabel('Frecuencia')

# Mostrar el histograma
plt.show()
