import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import seaborn as sns
import pandas as pd

df = pd.read_csv('ecommerce_estatistica.csv')
# print(df.head().to_string())

# Gráfico de Densidade
plt.figure(figsize=(12, 8))
sns.kdeplot(df['Preço'], fill=True, color='#863e9c')
plt.title('Densidade dos Preços')
plt.xlabel('Preço')
plt.ylabel('Densidade')
# plt.savefig('grafico_6.png') # Salvar Imagem
plt.tight_layout()
# plt.show() # Mostrar em Formato Aplicativo

def grafico_de():
    # Densidade
    # Gerando os dados de densidade com preenchimento
    fig6 = ff.create_distplot(
        [df['Preço']],  # Dados
        group_labels=['Preços'],  # Legenda
        colors=['#863e9c'],  # Cor da linha e do preenchimento
        curve_type='kde',  # Tipo de curva (kde para densidade)
        show_hist=False  # Ocultar o histograma
    )

    # Ajuste do layout
    fig6.update_layout(
        title='Densidade dos Preços',
        xaxis_title='Preço',
        yaxis_title='Densidade',
        title_x=0.5,  # Centralizando o título
        height=600,  # Altura do gráfico
        margin=dict(t=50, b=50, l=50, r=50),
        showlegend=False,  # Ocultar a legenda
        xaxis=dict(
            tickmode='linear',
            tick0=0,
            dtick=25,  # intervalo entre os ticks (25 como no seu original)
            range=[0, df['Preço'].max() + 25]  # range do eixo x
        )
    )

    # Ajustando transparência do preenchimento
    fig6.update_traces(opacity=0.5)  # Deixa o preenchimento semitransparente
    return fig6