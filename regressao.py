import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import pandas as pd

df = pd.read_csv('ecommerce_estatistica.csv')
# print(df.head().to_string())

# Gráfico de Regressão
sns.regplot(x='Desconto', y='Preço', data=df, color='#278f65', scatter_kws={'alpha': 0.5, 'color': '#34c289'})
plt.title('Regressão de Preço por Desconto')
plt.xlabel('Desconto')
plt.ylabel('Preço')
# plt.savefig('grafico_7.png') # Salvar Imagem
plt.tight_layout()
# plt.show() # Mostrar em Formato Aplicativo

def grafico_7():
    # Regressão
    fig7 = px.scatter(df, x='Desconto', y='Preço', trendline='ols',  # Adiciona a linha de regressão
        title='Regressão de Preço por Desconto')

    # Ajuste do layout e estilo do gráfico
    fig7.update_traces(
        marker=dict(
            color='#34c289',  # Cor dos pontos
            opacity=0.5  # Transparência dos pontos
        )
    )

    fig7.update_layout(
        xaxis_title='Desconto',
        yaxis_title='Preço',
        title_x=0.5,  # Centralizando o título
        height=600,  # Altura do gráfico
        margin=dict(t=50, b=50, l=50, r=50),
        plot_bgcolor='white'  # Fundo branco
    )
    return fig7