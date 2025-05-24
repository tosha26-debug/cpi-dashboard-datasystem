import pandas as pd
import dash
from dash import dcc, html
import plotly.graph_objs as go 

import sys
sys.path.append('data')

from df_ohlc_cleaned import fetch_all_symbols, SYMBOLS 
ohlc_df = fetch_all_symbols(SYMBOLS)

ohlc_df['timestamp'] = pd.to_datetime(ohlc_df['timestamp'])

#rename timestamp to date 
ohlc_df.rename(columns={'timestamp': 'date'}, inplace=True)


# Load data
# it is not a csv - ohlc_df = pd.read_csv('data/ohlc_data.csv', parse_dates=['Date'])
cpi_df = pd.read_csv('cpi_transformed.csv', parse_dates=['date'])

# Merge on nearest date 
merged_df = pd.merge_asof(
    ohlc_df.sort_values('date'),
    cpi_df.sort_values('date'),
    left_on= 'date',
    right_on= 'date', 
    direction= 'backward'
)

# App
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Stock Prices vs CPI Inflation"),
    dcc.Graph(
        id='linechart-cpi',
        figure={
            'data': [
                go.Scatter(
                    x=merged_df[merged_df['symbol_id'] == symbol]['date'],
                    y=merged_df[merged_df['symbol_id'] == symbol]['close'],
                    mode= 'lines',
                    name=symbol
                    
                )
                for symbol in SYMBOLS
            ] + [
                # go.Candlestick(
                #     x=merged_df['date'],
                #     open=merged_df['open'],
                #     high=merged_df['high'],
                #     low=merged_df['low'],
                #     close=merged_df['close'],
                #     name='Stock OHLC'
                # ), 
                go.Scatter(
                    x=merged_df["date"],
                    y=merged_df["cpi_value"],
                    mode='lines',
                    name='CPI',
                    yaxis='y2',
                    line=dict(dash='dot', color = 'black')
                )
                
            ],
            'layout': go.Layout(
                xaxis={'title': 'Date'},
                yaxis={'title': 'Stock Close Price'},
                yaxis2={
                    'title': 'CPI',
                    'overlaying': 'y',
                    'side': 'right',
                },
                title = 'Closing Price by Ticker with CPI Overlay', 
                legend=dict(x=0, y=1)
            )
        }
    )
])
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True) #changed port=8050 to port=80