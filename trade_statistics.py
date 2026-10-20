import pandas as pd

from rich.text import Text
from rich.table import Table
from rich.console import Console
from rich import box

console = Console()




class Statistics(): #later do this class using NumPy
    def __init__(self, trades):
        self.trades = trades
        
    def trade_count(self):
        """"Count trades"""
        return len(self.trades)
    def win_rate(self, trades):
        """win rate mean"""
        losses = []
        for trade in trades:
            if trade.result == "L":
                losses.append(trade)
        if not trades:
            return None

        wins = len(trades) - len(losses)
        win_rate = wins / len(trades) * 100

        return win_rate

    def cumulative_winrate(self, trades):
        """Function built for matplotlib"""
        y = []

        current_w = 0
        processed_trades = 0

        for trade in trades:
            if trade.result == "BE":
                continue
            
            processed_trades += 1
            if trade.result == "W":
                current_w += 1
            y.append(round(current_w / processed_trades * 100, 2))

        return y
    
    def average_rr(self): 
        if not self.trades:
            return None
        rr_mean = [trade.rr for trade in self.trades]
        count_sum = sum(rr_mean)
        final = count_sum / len(rr_mean)
        return f"{final:.2f}"

    def average_win_rr(self):
        awr = []
        for trade in self.trades:
            if trade.result == "W":
                awr.append(trade.rr)


        if awr:
            awr_count_sum = sum(awr)
            awr_final = awr_count_sum / len(awr)
            return awr_final
        else:
            print("Empty")

    def average_loss_rr(self):
        awl = []
        for trade in self.trades:
            if trade.result == "L":
                awl.append(trade.rr)

        if awl:
            awl_count_sum = sum(awl)
            awl_final = awl_count_sum / len(awl)
            return awl_final
        else:
            print("Empty")

    def most_common_session(self):
        if not self.trades:
            return None
        london = []
        nyc = []
        asia = []
        for trade in self.trades:
            if trade.session == "LONDON":
                london.append(trade.session)

            elif trade.session == "NYC":
                nyc.append(trade.session)

            elif trade.session == "ASIA":
                asia.append(trade.session)

        if len(london) > len(nyc) and len(london) > len(asia):
            return "London"

        elif len(nyc) > len(london) and len(nyc) > len(asia):
            return "NYC"

        elif len(asia) > len(london) and len(asia) > len(nyc):
            return "Asia"

        elif len(london) == len(nyc) > len(asia):
            return "London and Nyc"

        elif len(london) == len(asia) > len(nyc):
            return "London and Asia"

        elif len(nyc) == len(asia) > len(london):
            return "NYC and Asia"

        elif len(london) == len(nyc) == len(asia):
            return "All sessions have the same amount of trades."
        


    def market_condition_wrs(self):
        """Basically defines on which market condition
        U have the biggest winratio"""
        if not self.trades:
            return None
        trending = []
        trending_lower_tf = []
        ranging = []
        high_volume = []
        low_volume = []
        counter_trending_ltf = []
        counter_trending = []
        

        for trade in self.trades:
            if trade.market_condition == "trending":
                trending.append(trade)

            elif trade.market_condition == "trending(lower-tf)":
                trending_lower_tf.append(trade)

            elif trade.market_condition == "ranging":
                ranging.append(trade)

            elif trade.market_condition == "high-volume":
                high_volume.append(trade)

            elif trade.market_condition == "low-volume":
                low_volume.append(trade)

            elif trade.market_condition == "counter-trending(lower-tf)":
                counter_trending_ltf.append(trade)

            elif trade.market_condition == "counter-trending":
                counter_trending.append(trade)

        trending_w = self.win_rate(trending)
        if trending_w is None:
            print("Win rate on trending: No trades")
        else:
            print(f"Win rate on trending: {trending_w:.2f}%")

        trending_ltf_w = self.win_rate(trending_lower_tf)
        if trending_ltf_w is None:
            print("Win rate on trending Lower timeframe: No trades")
        else:
            print(f"Win rate on trending lower timeframe: {trending_ltf_w:.2f}%")

        ranging_w = self.win_rate(ranging)
        if ranging_w is None:
            print("Win rate on ranging: No trades")
        else:
            print(f"Win rate on ranging: {ranging_w:.2f}%")

        high_vol_w = self.win_rate(high_volume)
        if high_vol_w is None:
            print("Win rate on high volume: No trades")
        else:
            print(f"Win rate on high volume: {high_vol_w:.2f}%")

        low_vol_w = self.win_rate(low_volume)
        if low_vol_w is None:
            print("Win rate on low volume: No trades")
        else:
            print(f"Win rate on low volume: {low_vol_w:.2f}%")


        counter_t_ltf = self.win_rate(counter_trending_ltf)
        if counter_t_ltf is None:
            print("Win rate on counter trending lower timeframe: No trades")
        else:
            print(f"Win rate on counter trending lower timeframe is:"
              f" {counter_t_ltf:.2f}%")


        counter_t_w = self.win_rate(counter_trending)
        if counter_t_w is None:
            print("Win rate on counter trending: No trades")
        else:
            print(f"Win rate on counter trending: {counter_t_w:.2f}%")

# For future refactor -> change list to dict 
# so replace print with return dict 
#market_conditions = {
#    "trending": [],
#    "trending(lower-tf)": [],
#    "ranging": [],
#    "high-volume": [],
#    "low-volume": [],
#    "counter-trending(lower-tf)": [],
#    "counter-trending": []
#}

    def long_vs_short_wr(self):
        if not self.trades:
            return None
        
        long = []
        short = []
        for trade in self.trades:
            if trade.direction == "LONG":
                long.append(trade)

            elif trade.direction == "SHORT":
                short.append(trade)

        long_wr = self.win_rate(long)
        if long_wr is None:
            print("Win rate on long positions: No trades")
        else:
            print(f"Win rate on long positions: {long_wr:.2f}%")

        short_wr = self.win_rate(short)
        if short_wr is None:
            print("Win rate on short positions: No trades")
        else:
            print(f"Win rate on short positions: {short_wr:.2f}%")

    def win_rate_by_session(self):
        if not self.trades:
            return None

        london = []
        nyc = []
        asia = []
        for trade in self.trades:
            if trade.session == "LONDON":
                london.append(trade)

            elif trade.session == "NYC":
                nyc.append(trade)

            elif trade.session == "ASIA":
                asia.append(trade)

        london_wr = self.win_rate(london)
        if london_wr is None:
            print("Win rate on london session: No trades")
        else:
            print(f"Win rate on London session is: {london_wr:.2f}%")

        nyc_wr = self.win_rate(nyc)
        if nyc_wr is None:
            print("Win rate on Nyc session: No trades")
        else:
            print(f"Win rate on NYC session is: {nyc_wr:.2f}%")

        asia_wr = self.win_rate(asia)
        if asia_wr is None:
            print("Win rate on Asia session: No trades")
        else:
            print(f"Win rate on Asia session is: {asia_wr:.2f}%")


    def most_traded_pair(self):
        if not self.trades:
            return None        

        pairs = {}
        for trade in self.trades:
            if trade.pair in pairs:
                pairs[trade.pair] += 1

            if trade.pair not in pairs:
                pairs[trade.pair] = 1

        highest_count = 0
        most_traded = ""
        for pair, value in pairs.items():
               if value > highest_count:
                   highest_count = value
                   most_traded = pair
        
        return most_traded

    def max_losing_streak(self):
        if not self.trades:
            return None

        l_streak = 0
        max_l_streak = 0 
        for trade in self.trades:

            if trade.result == "W":
                l_streak = 0

            elif trade.result == "L":
                l_streak += 1

                if l_streak > max_l_streak:
                    max_l_streak = l_streak

        return max_l_streak
    def max_winning_streak(self):
        if not self.trades:
            return None

        w_streak = 0
        max_w_streak = 0
        for trade in self.trades:

            if trade.result == "L":
                w_streak = 0

            elif trade.result == "W":
                w_streak += 1

                if w_streak > max_w_streak:
                    max_w_streak = w_streak

        return max_w_streak

    def pnl_count(self):
        if not self.trades:
            return None

        p_and_l = [trade.pnl for trade in self.trades]

        return sum(p_and_l)

    def cumulative_pnl(self):
        y = []

        current_pnl = 0

        for trade in self.trades:
            current_pnl += trade.pnl
            y.append(current_pnl)

        return y

    def session_cumulative_pnl(self, session):
        """Not used yet"""
        # add to show_statistics maybe
        y = []
        current_pnl = 0

        for trade in self.trades:
            if trade.session == session:
                current_pnl += trade.pnl
                y.append(current_pnl)


        return y

    def best_winning_trade(self):
        winners = [trade.pnl for trade in self.trades if trade.pnl > 0]
        return max(winners, default=None)

    def worst_losing_trade(self):
        winners = [trade.pnl for trade in self.trades if trade.pnl < 0]
        return min(winners, default=None)
    
    def show_statistics(self):
        console.print(f"\n\n\nAmount of trades: {len(self.trades)}\n",
                      style="dark_blue"
                      )

        table = Table(box=box.DOUBLE_EDGE, title="Statistics",
                      title_style="bold blue",
                      style="dark_blue"
                      )

        table.add_column("Statistics", justify="center", style="dark_blue")
        table.add_column("Value", justify="center", style="dark_blue")
        
        table.add_row(
            "Win rate",
            f"{self.win_rate(self.trades):.2f}"
        )

        table.add_row(
            "Total P&L",
            f"{self.pnl_count():.2f}"
        )

        table.add_row(
            "Average RR",
            f"{self.average_rr()}"
        )

        table.add_row(
            "Average Winners  RR",
            f"{self.average_win_rr():.2f}"
        )

        table.add_row(
            "Average Losses RR",
            f"{self.average_loss_rr():.2f}"
        )

        table.add_row(
            "Most Common Session",
            f"{self.most_common_session()}"
        )

        table.add_row(
            "Market Condition",
            f"{self.market_condition_wrs()}"
        )

        table.add_row(
            "Long vs Short Win Ratio",
            f"{self.long_vs_short_wr()}"
        )

        table.add_row(
            "Most Traded pair",
            f"{self.most_traded_pair()}"
        )

        table.add_row(
            "Biggest wining streak",
            f"{self.max_winning_streak()}"
        )

        table.add_row(
            "Biggest losing streak",
            f"{self.max_losing_streak()}"
        )

        table.add_row(
            "Best winning day",
            f"{self.best_winning_trade()}"
        )

        table.add_row(
            "Worst losing trade",
            f"{self.worst_losing_trade()}"
        )
        return console.print(table)
