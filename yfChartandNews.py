
# Output: chart the users stock of choice and display recent headlines with links
# best used to get a quick snapshot of a specific stock
# currently on 1yr period with intervals of 1d, 
# if you want to change the times for chart must be done manually in the code


import yfinance as yf
import finplot as fplt


# ask user for stock ticker they wanna get news on / see 1yr chart
stock = yf.Ticker(input("Ticker?  "))

news_headlines = stock.news

for headline in news_headlines:
    print(headline['title'])
    print(headline['link'])
    print()

# RETRIEVE 1 YEAR WORTH OF DAILY DATA OF TICKER
df = stock.history(interval='1d',period='1y')

# PLOT THE OHLC CANDLE CHART
fplt.candlestick_ochl(df[['Open','Close','High','Low']])
fplt.show()