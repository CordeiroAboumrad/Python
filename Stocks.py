import yfinance
import matplotlib.pyplot as plt

df = yfinance.download("TSLA",start="2018-11-01", end="2021-01-08", interval="1d")

df.head()
