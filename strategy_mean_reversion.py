import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Télécharger les données du S&P500
data = yf.download("^GSPC", start="2020-01-01", end="2024-12-31", auto_adjust=True)
data = data[['Close']].copy()

# Calcul de la moyenne mobile sur 20 jours
data['MA20'] = data['Close'].rolling(window=20).mean()
data.dropna(inplace=True)

# Signal d'achat : 1 si prix < moyenne mobile, sinon 0
close = data['Close'].squeeze()
ma20 = data['MA20'].squeeze()
data['Position'] = (close < ma20).astype(int)

# Calcul des rendements
data['Return'] = data['Close'].pct_change()
data['Strategy_Return'] = data['Position'].shift(1) * data['Return']

# Ajout des frais de transaction
data['Signal'] = data['Position'].diff().abs()
transaction_cost = 0.001
data['Strategy_Return_Net'] = data['Strategy_Return'] - data['Signal'] * transaction_cost

# Capital cumulé
data['Buy_Hold'] = (1 + data['Return']).cumprod()
data['Strategy'] = (1 + data['Strategy_Return']).cumprod()
data['Strategy_Net'] = (1 + data['Strategy_Return_Net']).cumprod()

# Visualisation des résultats
plt.figure(figsize=(12, 6))
plt.plot(data['Buy_Hold'], label='Buy & Hold')
plt.plot(data['Strategy'], label='Mean Reversion Strategy (Gross)')
plt.plot(data['Strategy_Net'], label='Mean Reversion Strategy (Net)')
plt.title('Mean Reversion Strategy vs Buy & Hold (S&P500)')
plt.xlabel('Date')
plt.ylabel('Portfolio Value (Base 1)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
