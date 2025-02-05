import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

df = pd.read_csv('ecommerce_estatistica.csv')
# print(df.head().to_string())

# Gráfico de Barra
x = df['Gênero'].value_counts().index
y = df['Gênero'].value_counts().values

plt.figure(figsize=(17, 6))
plt.bar(x, y, color='#03800f')
plt.title('Divisão de Gêneros')
plt.xlabel('Tipos de Gêneros Disponíveis')
plt.ylabel('Quantidade')
# plt.savefig('grafico_4.png') # Salvar Imagem
plt.tight_layout()
# plt.show() # Mostrar em Formato Aplicativo

def grafico_b():
    # Barra
    # Dados
    gender_counts = df['Gênero'].value_counts().reset_index()
    gender_counts.columns = ['Gênero', 'Quantidade']

    # Criando o gráfico de barras
    fig4 = px.bar(gender_counts, x='Gênero', y='Quantidade',
                 title='Barra - Divisão de Gêneros',
                 labels={'Gênero': 'Tipos de Gêneros Disponíveis', 'Quantidade': 'Quantidade'},
                 color='Quantidade', color_discrete_sequence=['red'])

    # Ajustando o tamanho do gráfico
    fig4.update_layout(
        # width=1200,  # Largura do gráfico
        height=1000,  # Altura do gráfico
        title_x=0.5,  # Centralizando o título
    )
    return fig4