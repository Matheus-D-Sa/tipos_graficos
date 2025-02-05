from histograma import grafico_h
from dispersao import grafico_di
from mapa_de_calor import grafico_m
from barra import grafico_b
from pizza import grafico_p
from densidade import grafico_de
from regressao import grafico_r
import pandas as pd
from dash import Dash, html, dcc


def cria_graficos(df):
    return grafico_h() , grafico_di(), grafico_m(), grafico_b(), grafico_p(), grafico_de(), grafico_r()

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