# Guied Project: NeuralNine
# Code: https://www.youtube.com/watch?v=HqGlkACB3rg



import pandas_datareader as web
import mplfinance as mpf
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns

## The currency who we gonn' convert
currency = "USD"
metric = "Close"

## When start to now
start = dt.datetime(2018,1,1)
end = dt.datetime.now()

## The cryptos 
crypto = ['BTC', 'ETH', 'LTC', 'XRP', 'DASH', 'SC', '$SCCP']
colnames = []

## Program start
first = True

for ticker in crypto:
    data = web.DataReader(f"{ticker}-{currency}", "yahoo", start, end)
    if first:
        combined = data[[metric]].copy()
        colnames.append(ticker)
        combined.columns = colnames
        first = False
    else:
        combined = combined.join(data[metric])
        colnames.append(ticker)
        combined.columns = colnames

plt.yscale('log') # first show linear

for ticker in crypto:
    plt.plot(combined[ticker], label=ticker)

plt.legend(loc="upper right")

plt.show()

# # Correlation Heat Map

print(combined)

combined = combined.pct_change().corr(method='pearson')

sns.heatmap(combined, annot=True, cmap="coolwarm")
plt.show()
