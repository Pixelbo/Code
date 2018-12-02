from iexfinance.stocks import Stock
import matplotlib.pyplot as plt
from iexfinance.stocks import get_historical_data
from datetime import datetime
from iexfinance.stocks import get_historical_intraday

tsla = Stock('TSLA')
tesla = tsla.get_price()
print(tesla)

batch = Stock(["TSLA", "AAPL"])
price = batch.get_price()

print(price)

start = datetime(2017, 1, 1)
end = datetime(2018, 1, 1)
df = get_historical_data("TSLA", start, end, output_format='pandas')
df.plot()
plt.show()

tslas = Stock("TSLA", output_format='pandas')
info = tslas.get_quote()
print(info)

date = datetime(2018, 11, 28)

now = get_historical_intraday("AAPL", date)
print(now)

now2 = get_historical_intraday("AAPL", date, output_format='pandas')
now2.plot()
plt.show()
