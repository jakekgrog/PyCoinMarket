# PyCoinMarket

A Human-Friendly Python API Service for Crypto Currency Information.

Currently supported markets:
    1. Coin Market Cap


## Example usage

```python
from pycoin.CoinMarketCap import CoinMarketCap

cmc = CoinMarketCap('ethereum') # Defaults to bitcoin


cmc.name() # Returns the name of the currency

cmc.id() # Returns the currency ID

cmc.symbol() # Returns the coin symbol

cmc.rank() # Returns the coins rank

cmc.price() # Returns the coins price in USD

cmc.price_btc() # Returns the coins price in BTC

cmc.volume() # Returns the volume of the coin traded in the past 24 hours (USD)

cmc.market_cap() # Returns the coins market cap

cmc.available() # Returns the coins available supply

cmc.total() # Returns the coins total supply

cmc.max() # Returns the coins maximum supply

cmc.percent_change_hour() # Returns the percentage change for the past hour

cmc.percent_change_day() # Returns the percentage change for the past day

cmc.percent_change_week() # Returns the percentage change for the past week

cmc.last_update() # Returns the last update (POSIX time)
```
