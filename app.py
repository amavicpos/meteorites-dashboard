from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

df = pd.read_json('meteorites.json')

app = Dash(__name__)

app.layout = html.Div([
    html.H1("NASA meteorite strike dashboard"),
    
    dcc.Graph(
        id='meteorite-map',
        figure=px.scatter_geo(
            df,
            lon='reclong',
            lat='reclat',
            projection="natural earth"
        ).update_traces(
            customdata=df['name'],
            hovertemplate='<b>%{customdata}</b><br>Coordinates: (%{lon}, %{lat})'
        ),
    ),
    
    dcc.Graph(
        id='year-histogram',
        figure=px.histogram(
            df,
            x='year',
            title='Meteorites by year of landing',
            labels={'year': 'Year'},
        ),
    ),
    
    dcc.Graph(
        id='composition-histogram',
        figure=px.histogram(
            df,
            x='recclass',
            title='Meteorites by composition',
            labels={'recclass': 'Composition'},
        ),
    ),
])

if __name__ == '__main__':
    app.run(debug=False, dev_tools_hot_reload=True)
