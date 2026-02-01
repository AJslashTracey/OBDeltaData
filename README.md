# Trading Bot based on Orderbook Delta 
(Just data provided in this repo no bot included)

## Repository Structure
```
OBDeltaData/
├── data/               # Data files and analysis results
│   ├── deltaEmaPrice/ # EMA price analysis data
│   ├── 1%delta/       # 1% depth delta analysis
│   ├── ohcl/          # OHLC data
│   └── 2019.csv       # Historical data
├── docs/              # Documentation and visualizations
    └── imgs/          # Analysis images and charts

```
 
## Dataset Overview

- **Timeframe:** ~2 days of 1-minute interval logs
- **Exchange:** Coinbase
- **Depth:** 5% orderbook depth
- **Included Data:**
  - **Timestamp** (Unix format)
  - **BTC Price** (In US Dollar)
  - **Orderbook Delta** (5% depth calculation)

## 

I'm currently working on expanding the dataset to include a longer timeframe 

[real time data mining progress](https://customchart-production.up.railway.app/)

##



![Dat preview](https://github.com/AJslashTracey/OBDeltaData/blob/main/docs/imgs/Screenshot%202025-02-27%20at%2020.14.00.png)



##
Delta quality check 
![Data](https://github.com/AJslashTracey/OBDeltaData/blob/main/docs/imgs/Screenshot%202025-03-15%20at%2019.29.28.png)
