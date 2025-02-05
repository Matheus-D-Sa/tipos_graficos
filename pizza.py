import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

df = pd.read_csv('ecommerce_estatistica.csv')
# print(df.head().to_string())

# Gráfico de Pizza
x = df['Qtd_Vendidos'].value_counts().index
y = df['Qtd_Vendidos'].value_counts().values

plt.figure(figsize=(6, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
plt.title('Distribuição de Quantidade de Produtos Vendidos')
# plt.savefig('grafico_5.png') # Salvar Imagem
plt.tight_layout()
# plt.show() # Mostrar em Formato Aplicativo

def grafico_p():
    # Pizza
    # Preparação dos dados
    df_pie = df['Qtd_Vendidos'].value_counts().reset_index()
    df_pie.columns = ['Qtd_Vendidos', 'Quantidade']

    # Gráfico de pizza
    fig5 = px.pie(
        df_pie,
        names='Qtd_Vendidos',
        values='Quantidade',
        title='Pizza - Distribuição de Quantidade de Produtos Vendidos',
        hole=0.4,  # Para gráfico sólido (sem buraco no centro)
    )

    # Ajuste do layout (ângulo inicial e rótulos)
    fig5.update_traces(
        textinfo='percent+label',  # Mostra percentual e rótulos
        rotation=90  # Ângulo inicial (equivale ao `startangle` no Matplotlib)
    )

    fig5.update_layout(
        height=600,  # Altura do gráfico
        title_x=0.5,  # Centralizando o título
        margin=dict(t=50, b=50, l=50, r=50)
    )
    return fig5