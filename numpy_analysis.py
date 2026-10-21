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

        if result is not None:
            table1.add_row(f"Total P&L {result['sum']:.2f}")
            table1.add_row(f"Total P&L {result['mean']:.2f}")
            table1.add_row(f"Total P&L {result['max']:.2f}")
            table1.add_row(f"Total P&L {result['min']:.2f}")
        else:
            print("No trades available")

        tables.append(table1)



        result2 = self.more_in_depth_statistics_pnl(self.trades)

        table2 = Table(box=box.DOUBLE_EDGE, title="Statistics",
                       title_style="bold blue",
                       style="dark_blue"
                       )

        table2.add_column("Statistics", justify="center", style="dark_blue")
        table2.add_column("Values", justify="center", style="dark_blue")

        if result2 is not None:
            table2.add_row(f"PnL Median: {result2['median']}")
            table2.add_row(f"PnL Standard Deviation: {result2['std']:.2f}")
            table2.add_row(f"PnL 10% Percentile:  {result2['percentiles'][0]:.2f}")
            table2.add_row(f"PnL 25% Percentile:  {result2['percentiles'][1]:.2f}")
            table2.add_row(f"PnL 50% Percentile:  {result2['percentiles'][2]:.2f}")
            table2.add_row(f"PnL 75% Percentile:  {result2['percentiles'][3]:.2f}")
            table2.add_row(f"PnL 90% Percentile:  {result2['percentiles'][-1]:.2f}")
        else:
            print("No trades available")

        tables.append(table2)



        result3 = self.histogram_pnl()

        table3 = Table(box=box.DOUBLE_EDGE, title="Statistics",
                        title_style="bold blue",
                        style="dark_blue"
                        )
        table3.add_column("Statistics", justify="center", style="dark_blue")
        table3.add_column("Value", justify="center", style="dark_blue")

        counts = result3['counts']
        bin_edges = result3['bin_edges']

        if result3 is not None:
            table3.add_row(f"Bins from {bin_edges[0]} to"
                              f" {bin_edges[1]}\tAmount: {counts[0]}")
            
            table3.add_row(f"Bins from {bin_edges[1]} to"
                              f" {bin_edges[2]}\tAmount: {counts[1]}")
            
            table3.add_row(f"Bins from {bin_edges[2]} to"
                              f" {bin_edges[3]}\tAmount: {counts[2]}")
            
            table3.add_row(f"Bins from {bin_edges[3]} to"
                              f" {bin_edges[4]}\tAmount: {counts[3]}")
            
            table3.add_row(f"Bins from {bin_edges[4]} to"
                              f" {bin_edges[5]}\tAmount: {counts[4]}")

            tables.append(table3)
        else:
            print("No trades available")


            result4_p1 = self.running_maximum()
            result4_p2 = self.running_min()

            table4 = Table(box=box.DOUBLE_EDGE, title="Statistics",
                           title_style="bold blue",
                           style="dark_blue"
                           )
            table4.add_column("Statistics", justify="center", style="dark_blue")
            table4.add_column("Value", justify="center", style="dark_blue")

            if result4_p1 is not None and result4_p2 is not None:
                table4.add_row(f"Highest equity level to date: {result4_p1}")
                table4.add_row(f"Lowest equity level to date: {result4_p2}")

            tables.append(table4)

        return tables