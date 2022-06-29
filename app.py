import plotly.express as px
from dash import Dash, dcc, html, Output, Input

app = Dash(__name__)

tickers = ['ticker_000', 'ticker_001', 'ticker_002']
prices = {
    'ticker_000':
        {
            'prices': [1, 2, 3, 5, 3, 5, 4, 4],
            'date': ['2022-01-01', '2022-02-01', '2022-03-01',
                     '2022-04-01', '2022-05-01', '2022-06-01',
                     '2022-07-01', '2022-08-01']
        },
    'ticker_001':
        {
            'prices': [1, 2, 3, 4, 1, 2, 3, 4],
            'date': ['2022-01-01', '2022-02-01', '2022-03-01',
                     '2022-04-01', '2022-05-01', '2022-06-01',
                     '2022-07-01', '2022-08-01']
        },

    'ticker_002':
        {
            'prices': [1, 2, 2, 3, 1, 2, 3, 2],
            'date': ['2022-01-01', '2022-02-01', '2022-03-01',
                     '2022-04-01', '2022-05-01', '2022-06-01',
                     '2022-07-01', '2022-08-01']
        }
}

app.layout = html.Div([
    html.Div([
        dcc.Graph(id='ticker_chart'),
        html.Hr(),
    ]),
    html.Div([

        html.Div([
            dcc.Dropdown(
                tickers,
                searchable=True,
                id='tickers'
            ),
        ], style={'width': '100%', 'display': 'inline-block'})

    ]),

])


@app.callback(Output('ticker_chart', 'figure'),
              Input('tickers', 'ticker_name'))
def update_graph(ticker_name):
    fig = px.scatter(x=prices.get(ticker_name).get('prices'),
                     y=prices.get(ticker_name)('date'))

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
