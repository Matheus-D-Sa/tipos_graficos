import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('ecommerce_estatistica.csv')
# print(df.head().to_string())

# Múltiplos gráficos
plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1) # 2 Linha, 2 Colunas, 1° Gráfico

# Gráfico de Dispersão 1
plt.scatter(df['Preço'], df['Preço'], color='#fc0328')
plt.title('Dispersão - Preço e Preço')
plt.xlabel('Preço')
plt.ylabel('Preço')

# Gráfico de Dispersão 2
plt.subplot(1, 2, 2) # 1 Linha, 2 Colunas, 2° Gráfico
plt.scatter(df['Preço'], df['Desconto'], color='#fc0328', alpha=0.6, s=30)
plt.title('Dispersão - Preço e Desconto')
plt.xlabel('Preço')
plt.ylabel('Desconto')

# plt.savefig('grafico_2.png') # Salvar Imagem
plt.tight_layout() # Ajustar espaçamentos
# plt.show() # Mostrar em Formato Aplicativo

def grafico_di():
    # Dispersão
    # Criar figura com subplots
    fig2 = make_subplots(rows=1, cols=2, subplot_titles=('Dispersão - Preço e Preço', 'Dispersão - Preço e Desconto'))

    # Adicionar primeiro gráfico de dispersão
    fig2.add_trace(
        go.Scatter(
            x=df['Preço'],
            y=df['Preço'],
            mode='markers',
            marker=dict(color='#fc0328'),
            showlegend=False
        ),
        row=1, col=1
    )

    # Adicionar segundo gráfico de dispersão
    fig2.add_trace(
        go.Scatter(
            x=df['Preço'],
            y=df['Desconto'],
            mode='markers',
            marker=dict(color='#fc0328', opacity=0.6, size=10),
            showlegend=False
        ),
        row=1, col=2
    )

    # Atualizar layout
    fig2.update_layout(
        margin=dict(t=50, b=50, l=50, r=50),
        showlegend=False
    )

    # Atualizar títulos dos eixos
    fig2.update_xaxes(title_text="Preço", row=1, col=1)
    fig2.update_yaxes(title_text="Preço", row=1, col=1)
    fig2.update_xaxes(title_text="Preço", row=1, col=2)
    fig2.update_yaxes(title_text="Desconto", row=1, col=2)
    return fig2