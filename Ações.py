from yahooquery import Ticker
import matplotlib.pyplot as plt


vvar = Ticker('VVAR3.SA')
vvar_prices = vvar.history(start="2020-10-08", end="2021-01-08", interval="1d")
print(vvar_prices.close)
print(vvar.major_holders)

plt.plot(vvar_prices.close)
plt.xlabel('Date')
plt.ylabel('Price($)')
plt.title('Via Varejo stocks - movement')

plt.show()