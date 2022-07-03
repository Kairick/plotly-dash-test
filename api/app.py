import datetime

import plotly.express as px
import redis
from dash import Dash, dcc, html, Output, Input

from utils import generate_ticker_name

tickers = generate_ticker_name()
price_time = datetime.datetime.now()
start_price = 0

redis_client = redis.StrictRedis(host='redis', port=6379, db=0,
                                 charset="utf-8", decode_responses=True)

app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        dcc.Graph(id='ticker_chart'),
        dcc.Interval(
            id='interval-component',
            interval=1000,
            n_intervals=0
        ),
        html.Hr(),
    ]),
    html.Div([

        html.Div([
            dcc.Dropdown(
                tickers,
                tickers[0],
                searchable=True,
                id='tickers'
            ),
        ], style={'width': '100%', 'display': 'inline-block'})

    ]),

])


@app.callback(Output('ticker_chart', 'figure'),
              Input('interval-component', 'n_intervals'),
              Input('tickers', 'value'))
def update_graph_live(n_intervals, value):
    time_list = [price_time]
    price_list = [start_price]
    data = redis_client.xread({value: 1}, count=n_intervals + 1)
    if data:
        data = data[0][1]
    for price in data:
        new_time = time_list[-1] + datetime.timedelta(seconds=1)
        time_list.append(new_time)
        new_price = price_list[-1] + int(price[1]['price_inc'])
        price_list.append(new_price)
    fig = px.scatter(x=time_list, y=price_list)
    fig.update_yaxes(title=f'Цена {value}')

    fig.update_xaxes(title='Дата')

    return fig


server = app.server

if __name__ == '__main__':
    app.run_server()
