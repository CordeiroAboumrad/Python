import yfinance
import matplotlib.pyplot as plt
from datetime import date

df = yfinance.download("TSLA",start="2018-11-01", end=date.today(), interval="1d")

print(df.head(5))
plt.plot(df.Close)
#print(df.Close)

plt.xlabel('Date')
plt.ylabel('Price($)')
plt.title('Tesla stocks - movement')

plt.show()
#(figsize=(14,7))