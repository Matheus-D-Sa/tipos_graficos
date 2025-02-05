import matplotlib.pyplot as plt
import plotly.graph_objects as go
import seaborn as sns
import pandas as pd

df = pd.read_csv('ecommerce_estatistica.csv')
# print(df.head().to_string())

# Gráfico de Mapa de Calor
plt.figure(figsize=(10, 6))
corr = df[['Preço', 'Desconto']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação de Preço e Desconto')
# plt.savefig('grafico_3.png') # Salvar Imagem
# plt.show() # Mostrar em Formato Aplicativo

def grafico_3():
    # Mapa de Calor
    # Gerando dados de correlação
    corr = df[['Preço', 'Desconto']].corr()

    # Criando o mapa de calor
    fig3 = go.Figure(data=go.Heatmap(
        z=corr.values,  # Matriz de correlação
        x=corr.columns,  # Colunas (variáveis)
        y=corr.columns,  # Colunas (variáveis)
        colorscale='RdBu_r',  # Escala de cores
        zmin=-0,  # Valor mínimo para a escala de cores
        zmax=1,  # Valor máximo para a escala de cores
        colorbar=dict(title='Correlação')
    ))

    # Adicionando o título
    fig3.update_layout(
        title='Mapa de Calor - Correlação de Preço e Desconto',
        xaxis_title='Variáveis',
        yaxis_title='Variáveis',
        title_x=0.5,  # Centralizando o título
        width=800,
        height=500,
        margin=dict(t=50, b=50, l=50, r=50)
    )
    return  fig3