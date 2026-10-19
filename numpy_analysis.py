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
            "max": pnl_array.max(),
            "min": pnl_array.min(),
    }

        #with rich table
    def more_in_depth_statistics_pnl(self):
        pnl_array = np.array(self.pnl_in_depth())

        if pnl_array.size == 0:
            return None

        a = np.median(pnl_array)
        b = np.std(pnl_array)
        c = np.percentile(pnl_array, [10, 25, 50, 75, 90])
        return {
            "median": a,
            "std": b,
            "percentiles": c
        }

        #with rich table later
    def equity_curve(self):
        transaction_list = []
        for trade in self.trades:
            transaction_list.append(trade.pnl)

        equity_crv = np.cumsum(transaction_list)

        return equity_crv

    def running_maximum(self):
        """the highest equity level to date"""
        equity = self.equity_curve()
        return np.maximum.accumulate(equity)

    def running_min(self):
        """Lowest equity level to date"""
        equity = self.equity_curve()
        return np.minimum.accumulate(equity)

    def drawdown(self):
        equity = self.equity_curve()
        running_max = np.maximum.accumulate(equity)

        return equity - running_max

    def histogram_pnl(self):
        transaction_list = []

        for trade in self.trades:
            transaction_list.append(trade.pnl)

        counts, bin_edges = np.histogram(
            transaction_list, bins=10
        )

        return {
            "counts": counts,
            "bin_edges": bin_edges
        }


    def session_comparison_np(self):
        pass
    #table for:
    #session, directions and pnl from self.trades
    #for every session create mask that choses long/short transactions
    # calculate wr, pnl, transaction amount for each
    # calculate LONG-SHORT difference for winrate and pnl
    # return results using dict so later i can use rich or visualization