# Mean Reversion Strategy on S&P500

This project simulates a simple **mean-reversion trading strategy** using Python, with historical data from the S&P500 index.

## 🧠 Idea
Buy when the price is **below its 20-day moving average**, expecting a reversion to the mean.

## ⚙️ Tools Used
- Python (Pandas, NumPy, Matplotlib)
- yfinance (to get historical market data)

## 📊 Strategy Logic
1. Download historical price data (`^GSPC` - S&P500).
2. Calculate 20-day moving average.
3. Generate signal: 1 (long) if price < MA20, 0 otherwise.
4. Backtest the strategy vs buy & hold.
5. Include simple transaction costs.
6. Visualise cumulative returns.
