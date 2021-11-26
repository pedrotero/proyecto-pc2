import dash
import time
import pandas as pd
from dash import dcc
from dash import html
import plotly.express as px
from dash.dependencies import Input, Output

time.sleep(30)

app = dash.Dash(__name__)

movcat = pd.read_csv('/app/movcat.csv')
prodpcust = pd.read_csv('/app/prodpcust.csv')
ageincome = pd.read_csv('/app/ageincome.csv')

figm = px.bar(movcat, x="category",y='movies_per_category')
figp = px.histogram(prodpcust, x="products_per_customer")
figc = px.density_heatmap(ageincome, x="age", y="income")

app.layout = html.Div(children=[
    html.H1(children='DellStore Data'),

    html.Div(children='''
        data taken from: https://ftp.postgresql.org/pub/projects/pgFoundry/dbsamples/dellstore2/dellstore2-normal-1.0/dellstore2-normal-1.0.tar.gz
    '''),

    dcc.Graph(
        id='movcat',
        figure=figm
    ),
    dcc.Graph(
        id='prodpcust',
        figure=figp
    ),
    dcc.Graph(
        id='figc',
        figure=figc
    )
])


if __name__ == '__main__':
    app.run_server(host='0.0.0.0',port=8888)
