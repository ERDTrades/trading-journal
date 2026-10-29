import pandas as pd

from journal import Journal


from rich.text import Text
from rich.table import Table
from rich.console import Console
from rich import box

console = Console()

journal = Journal()

class pandas_statistics():
    def __init__(self, trades):
        self.trades = trades

    def session_comparison_pd(self):
        df = pd.DataFrame(self.trades)


        result = (df.groupby(['session', 'direction'])
                  .agg(['pnl', 'count'],
                       ['pnl', 'sum'],
                       ['pnl', 'median'],
                       ['pnl', lambda x: sum(x > 0) / len(x) * 100],
                       ['rr', 'sum','mean']
                       ).reset_index()
                       )

        return result
    def rolling_expectancy(self, window=30):
        pass
        # Convert trades into a DataFrame

        # Sort trades chronologically using date or trade ID

        # Select realized trade results (R-multiples or PnL)

        # Validate window size against the number of trades

        # Calculate rolling expectancy using pandas .rolling() and .mean()

        # Store rolling expectancy alongside trade dates or IDs in a DataFrame

        # Return the DataFrame

        # Visualize the rolling expectancy using Plotly separately

        # Window = 30 -> basically 30 observations

    def bootstrap_expectancy_comparison(self, n_iterations=10000):
        pass
        # Convert trades into a DataFrame

        # Separate LONG and SHORT trades using pandas filtering

        # Calculate observed expectancy for each direction using .mean()

        # Calculate the observed LONG - SHORT expectancy difference

        # Generate bootstrap samples with replacement
        # Use pandas .sample() for resampling

        # Calculate expectancy for LONG and SHORT in each iteration

        # Store bootstrap differences in a DataFrame

        # Calculate confidence interval using pandas .quantile()

        # Return observed difference and confidence interval

        # Visualize bootstrap differences using Seaborn separately
        
    def pandas_rich_table(self):
        pass
        #make necessary rich tables from those functions above


# In Addition!!!

# U already have advanced statistics option in menu
# maybe instead of adding another thing to choose
# expand this option by adding pandas
# and make user decide what he wants to see
# also a option withing that 8th one to visualize everything
