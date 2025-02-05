from histograma import grafico_1
from dispersao import grafico_2
from mapa_de_calor import grafico_3
from barra import grafico_4
from pizza import grafico_5
from densidade import grafico_6
from regressao import grafico_7
import pandas as pd
from dash import Dash, html, dcc


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