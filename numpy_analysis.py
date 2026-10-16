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
        pass

        # I need transaction list and extract trade.pnl from it with loop
        # Calculate cumulative PnL across trades in chronological order
        # using np.cumsum(). Return the cumulative PnL values for later
        # visualization with Matplotlib or Plotly.
        #with visualization

    def running_maximum(self):
        """the highest equity level to date"""
        pass
        #Running max — Max equity value to this moment
        #Use np.maximum.accumulate()

    def running_min(self):
        """Lowest equity level to date"""
        pass

        #minimum equity value to this moment
        #Use np.minimum.accumulate()

    def drawdown(self):
        pass
    #drawdown = equity - running_max
    #max_drawdown = drawdown.min()

    def histogram_pnl(self):
        pass

    #np.histogram(pnl_array, bins=10)

    