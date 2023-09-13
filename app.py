from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

df = pd.read_json('meteorites.json')

app = Dash(__name__)

app.layout = html.Div([
    html.H1("NASA meteorite strike dashboard", style={'text-align': 'center'}),
    dcc.Graph(
        id='meteorite-map',
        figure=px.scatter_geo(
            df,
            lon='reclong',
            lat='reclat',
            hover_name='name',
            projection="natural earth"
        ),
    ),
])

if __name__ == '__main__':
    app.run(debug=True)
