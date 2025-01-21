from plotly.subplots import make_subplots
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import statsmodels
from dash import Dash, html, dcc

def grafico_1():
    # Histograma
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

def grafico_2():
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
        title='Correlação de Preço e Desconto',
        xaxis_title='Variáveis',
        yaxis_title='Variáveis',
        title_x=0.5,  # Centralizando o título
        width=800,
        height=500,
        margin=dict(t=50, b=50, l=50, r=50)
    )
    return  fig3

def grafico_4():
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

def grafico_5():
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

def grafico_6():
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

def cria_graficos(df):
    return grafico_1() , grafico_2(), grafico_3(), grafico_4(), grafico_5(), grafico_6(), grafico_7()

def cria_app(df):
    # Criar App
    app = Dash(__name__)

    fig1, fig2, fig3, fig4, fig5, fig6, fig7 = cria_graficos(df)

    app.layout = html.Div([
        html.H1("Tipos de Gráficos - Web", style={
                'textAlign': 'center',  # Centraliza horizontalmente o texto
                'margin': '0',         # Remove margens padrão
                'padding': '20px'      # Espaçamento interno (opcional)
            }
),
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3),
        dcc.Graph(figure=fig4),
        dcc.Graph(figure=fig5),
        dcc.Graph(figure=fig6),
        dcc.Graph(figure=fig7),
    ])
    return app

df = pd.read_csv('ecommerce_estatistica.csv')

# Executar App
if __name__ == '__main__':
    app = cria_app(df)
    app.run_server(debug=True, port=8050) # Default 8050