import pandas as pd
import matplotlib.pyplot as plt

# Dataset
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'],
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(data)

# Separar las notas por materia
notas_matematicas = df[df['materia'] == 'Matemáticas']['nota']
notas_historia = df[df['materia'] == 'Historia']['nota']
notas_ciencias = df[df['materia'] == 'Ciencias']['nota']
notas_lenguaje = df[df['materia'] == 'Lenguaje']['nota']

# Graficar la distribución de notas con un boxplot y la distribución de aprobados con un pie chart
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

# Boxplot para la distribución de notas
boxplot_notas = ax1.boxplot([notas_matematicas, notas_historia, notas_ciencias, notas_lenguaje], vert=True, patch_artist=True, widths=0.6)
ax1.set_title('Distribución de Notas de Estudiantes', fontsize=16)
ax1.set_xticks(range(1, 5))
ax1.set_xticklabels(['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'])
ax1.set_ylabel('Notas')
ax1.set_xlabel('Materias')
ax1.grid(True)

# Colorear los boxplots según si aprobaron o no
colors_notas = ['Blue', 'Red']
for box, color in zip(boxplot_notas['boxes'], colors_notas):
    box.set_facecolor(color)

# Pie chart para la distribución de aprobados
aprobados_counts = df['aprobado'].value_counts()
colors_aprobados = ['Blue', 'Red']
ax2.pie(aprobados_counts, labels=aprobados_counts.index, autopct='%1.1f%%', colors=colors_aprobados, startangle=90)
ax2.set_title('Distribución de Aprobados y No Aprobados', fontsize=16)

# Mostrar el gráfico combinado
plt.tight_layout()
plt.show()
