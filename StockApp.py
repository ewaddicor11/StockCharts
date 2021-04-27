import sys

# Raw Package
import numpy as np
import pandas as pd

# Data Source
import yfinance as yf

# Data visualization
import plotly.graph_objs as go

#Get ticker symbol from command line
tickerSymbol = sys.argv[1]

#Query yahoo finance for stock data
data = yf.download(tickers=tickerSymbol, period='7d', interval='1m')

#declare figure
fig = go.Figure()

print(data)

#Candlestick Stock Graph
fig.add_trace(
	go.Candlestick(
		x=data.index,
		open=data['Open'],
		high=data['High'],
		low=data['Low'],
		close=data['Close'],
		name = 'market data'
	)
)

#Add Titles
fig.update_layout(
	title=tickerSymbol + ' live share prices evolution',
	yaxis_title='Stock Price (USD per Share)'
)

#X-axes
fig.update_xaxes(
	rangeslider_visible=True,
	rangeselector=dict(
		buttons=list([
			dict(count=15, label='15m', step='minute', stepmode='backward'),
			dict(count=45, label='45m', step='minute', stepmode='backward'),
			dict(count=1, label='1h', step='hour', stepmode='backward'),
			dict(count=3, label='3h', step='hour', stepmode='backward'),
			dict(step="all", label='1w')
		])
	)
)

#Make Slider Invisible
fig.update_layout(xaxis_rangeslider_visible = False)

#Update HTML File
fig.write_html("graph.html")