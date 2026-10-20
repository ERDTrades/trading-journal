import numpy as np
from journal import Journal


from rich.text import Text
from rich.table import Table
from rich.console import Console
from rich import box

console = Console()

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
        a =  np.maximum.accumulate(equity)
        return a.max()

    def running_min(self):
        """Lowest equity level to date"""
        equity = self.equity_curve()
        a = np.minimum.accumulate(equity)
        return a.min()

    def drawdown(self):
        equity = self.equity_curve()
        running_max = np.maximum.accumulate(equity)

        return equity - running_max

    def histogram_pnl(self):
        transaction_list = []

        for trade in self.trades:
            transaction_list.append(trade.pnl)

        counts, bin_edges = np.histogram(
            transaction_list, bins=5
        )

        return {
            "counts": counts,
            "bin_edges": bin_edges
        }

    def show_numpy_stats(self):
        tables = []

        result = self.calculate_pnl_statistics(self.trades)

        table1 = Table(box=box.DOUBLE_EDGE, title="Statistics",
                              title_style="bold blue",
                              style="dark_blue"
                              )
        table1.add_column("Statistics", justify="center", style="dark_blue")
        table1.add_column("Value", justify="center", style="dark_blue")

        table1.add_column("Statistics", justify="center")
        table1.add_column("Values", justify="right")


        if result is not None:
            table1.add_row(f"Total P&L {result['sum']:.2f}")
            table1.add_row(f"Total P&L {result['mean']:.2f}")
            table1.add_row(f"Total P&L {result['max']:.2f}")
            table1.add_row(f"Total P&L {result['min']:.2f}")
        else:
            print("No trades available")

        tables.append(table1)

        # Add 2nd table
        
        # Add 3rd .. and so on

        return tables