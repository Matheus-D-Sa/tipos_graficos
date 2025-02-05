import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

df = pd.read_csv('ecommerce_estatistica.csv')
# print(df.head().to_string()) # Visualizar as primeiras 5 linhas

# Gráfico de Histograma
plt.figure(figsize=(10, 6))
plt.hist(df['Preço'], bins=100, color='#09b0ed', alpha=0.8)
plt.title('Histograma - Distribuição de Preço')
plt.xlabel('Preços')
plt.xticks(ticks=range(0, int(df['Preço'].max())+25, 25))
plt.ylabel('Frequência')
plt.grid(True)
# plt.savefig('grafico_1.png') # Salvar Imagem
# plt.show() # Mostrar em Formato Aplicativo

def grafico_h():
    # Histograma / WEB
    fig1 = px.histogram(df, x='Preço', nbins=100, title='Histograma - Distribuição de Preço', color_discrete_sequence=['#09b0ed'])
    fig1.update_layout(
        xaxis_title='Preços',
        yaxis_title='Frequência',
        title_x=0.5,  # Centralizando o título
        xaxis=dict(
            tickmode='linear',
            tick0=0,
            dtick=25,  # intervalo entre os ticks (25 como no seu original)
            range=[0, df['Preço'].max() + 25]  # range do eixo x
        )
    )
    return fig1