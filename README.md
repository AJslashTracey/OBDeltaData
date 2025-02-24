# Trading Bot Orderbook Delta Data

This dataset was generated from one of my trading bots. Since I couldn't find any publicly available orderbook delta data, I decided to publish this dataset. 

## Dataset Overview

- **Timeframe:** ~2 days of 1-minute interval logs
- **Exchange:** Coinbase
- **Depth:** 5% orderbook depth
- **Included Data:**
  - **Timestamp** (Unix format)
  - **BTC Price** (Coinbase)
  - **Orderbook Delta** (5% depth calculation)

## Future Plans

I'm currently working on expanding the dataset to include a longer timeframe up to a month or so


(In side of the OBfetch.py you can find the functions from my trading bot which fetch fetch the whole Orderbook with all resting orders and calculate the delta) 
