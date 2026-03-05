# ============ RL Trader ============

# imports
import numpy as np
import pandas as pd
import matplotlib as plot
import torch
import tensorboard
import gymnasium as gym

class TradingEnv(gym.Env):
    def __init__(
            self,
            df: pd.DataFrame,
            window_size: int = 30,
            initial_balance: float = 1_000.0,
            transaction_cost: float = 0.01,
            render_mode: str | None = None,
    ):
        super().__init__()

        self.df = df.reset_index(drop=True)
        self.prices = self.df['Close'].values.astype(np.float32)
        self.window_size = int(window_size)
        self.initial_balance = float(initial_balance)
        self.transaction_cost = float(transaction_cost)
        self.render_mode = render_mode

        self.current_step: int | None = None
        self.balance: float | None = None
        self.position: float | None = None
        self.last_price: float | None = None





def main():
    df = pd.read_csv(
        'order_book/AAVEUSDT_d.csv',
        index_col='Date'
    )

    env = TradingEnv(
        df=df,
        window_size=30,
        initial_balance=10_000.0,
        transaction_cost=0.01,
        render_mode='human',
    )

    num_episodes =3

    for episode in range(num_episodes):




dates, open, close, high, low = df.index, df['Open'], df['Close'], df['High'], df['Low']

#print(f'dates: {dates}\n\n, open: {open}\n\n, close: {close}\n\n, high: {high}\n\n, low: {low}')

#x = int(input('enter day'))

#print(df.iloc[x::30].to_string())

df['log_ret_close'] = np.log(df['Close']).diff()
df['vol_7'] = df['log_ret_close'].rolling(7).std()
df['vol_35'] = df['log_ret_close'].rolling(35).std()
df['vol_365'] = df['log_ret_close'].rolling(365).std()

df.dropna()

print(df.to_string())


buy, sell, hold = 0, 1, 2
