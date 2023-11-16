import pandas as pd
import plotly.express as px

# Cargar el dataset
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'],
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
}

df = pd.DataFrame(data)

# Definir colores para cada materia
colors = px.colors.qualitative.Set3

# Graficar la distribución de notas con un boxplot usando Plotly
fig = px.box(df, x='materia', y='nota', points='all', title='Distribución de Notas de Estudiantes',
            labels={'nota': 'Notas', 'materia': 'Materias'}, color='materia', color_discrete_map=dict(zip(df['materia'].unique(), colors)))

# Ajustar el ancho de las barras
fig.update_traces(marker=dict(size=1))

# Ajustar el diseño del gráfico
fig.update_layout(
    xaxis_title='Materias',
    yaxis_title='Notas',
    boxmode='group',  # Mostrar boxplots agrupados por materia
)

# Crear una columna 'aprobado' basada en algún criterio (por ejemplo, nota mayor o igual a 70)
df['aprobado'] = df['nota'] >= 70

# Contar la cantidad de aprobados y no aprobados
aprobados_count = df['aprobado'].sum()
no_aprobados_count = len(df) - aprobados_count

# Crear un pie chart para la distribución de aprobados
fig_pie = px.pie(names=['Aprobados', 'No Aprobados'], values=[aprobados_count, no_aprobados_count],
                title='Distribución de Aprobados', color_discrete_sequence=['blue', 'red'])

# Mostrar el gráfico en el notebook
fig_pie.show()
fig.show()
