import numpy as np
from journal import Journal


journal = Journal()

class numpy_statistics():
    def __init__(self, trades):
        self.trades = trades

    def pnl_in_depth(self):
        pnl = []
        for trade in self.trades:
            pnl.append(trade.pnl)
        return pnl

    def calculate_pnl_statistics(self):
        pnl_array = np.array(self.pnl_in_depth())

        if pnl_array.size == 0:
            return None

        return {
            "sum": pnl_array.sum(),
            "mean": pnl_array.mean(),
            "std": pnl_array.std(),
            "max": pnl_array.max(),
            "min": pnl_array.min(),
    }