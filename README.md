# PyCoinMarket

A Human-Friendly Python API Service for Crypto Currency Information.

Currently supported markets:
    1. Coin Market Cap


## Example usage

```python
pcm = PyCoinMarket('ethereum') # Defaults to bitcoin


pcm.name() # Returns the name of the currency

pcm.id() # Returns the currency ID

pcm.symbol() # Returns the coin symbol

pcm.rank() # Returns the coins rank

pcm.price() # Returns the coins price in USD

pcm.price_btc() # Returns the coins price in BTC

pcm.volume() # Returns the volume of the coin traded in the past 24 hours (USD)

pcm.market_cap() # Returns the coins market cap

pcm.available() # Returns the coins available supply

pcm.total() # Returns the coins total supply

pcm.max() # Returns the coins maximum supply

pcm.percent_change_hour() # Returns the percentage change for the past hour

pcm.percent_change_day() # Returns the percentage change for the past day

pcm.percent_change_week() # Returns the percentage change for the past week

pcm.last_update() # Returns the last update (POSIX time)

```
