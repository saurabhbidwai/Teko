import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

dat = pd.read_csv('E:/Jobs/Teko/2014-new-york-city-taxi-trips/nyc_taxi_data_2014.csv/nyc_taxi_data_20141.csv')

#dat.describe()

app = dash.Dash()
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='NYC Taxi',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Total Amount by Payment Type', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(
        id='Graph1',
        figure={
            'data': [
                 {'x': dat.payment_type, 'y': dat.total_amount, 'type': 'bar', 'name': 'SF'}
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)