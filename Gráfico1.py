import pandas as pd
import dash
from dash import dcc # Dash Core Components
from dash import html # Hyper Text Markup Language
from dash.dependencies import Input, Output


df= pd.read_csv("/Users/diegolunasantizo/Downloads/Ors_entidad.csv")

df_emision=pd.read_csv("/Users/diegolunasantizo/Downloads/Emision.csv")

app = dash.Dash()


app.layout = html.Div([
    html.H1("Actividad 1", style={'textAlign':'center','color':'#794AD9','font-family': 'Helvetica'}), # CSS
    html.Hr(),
    html.H3("Dashboard Dash"),
    html.P("Mostraremos dos gráficos diferentes en base al proyecto que hemos estado trabajando"),
    dcc.Graph(
        id='graph_1',
        figure={
        'data': [
            {'x': df['ENTIDAD'], 'y': df['NUMERO DE POLIZAS VIGENTES'], 'type': 'bar', 'name': 'Barras', 'marker': {'color': '#E62021'}}
        ],
        'layout': {
            'title': 'Gráfico de polizas vigentes por Entidad'
        }
    }),
    dcc.Graph(
        id='graph_2',
        figure={
        'data': [
            {'x': df_emision['SEXO'], 'y': df_emision['PRIMA EMITIDA'], 'mode': 'markers', 'name': 'Puntos', 'marker': {'color': '#2ABC2B'}}
        ],
        'layout': {
            'title': 'Gráfico de sexo y prima emitida'
        }
    }
    )
    ])

if __name__ == '__main__':
    app.run_server(debug=True)