

class pandas_statistics():
    def __init__(self, trades):
        self.trades = trades

    def session_comparison_np(self):
        pass
    #list at the beggining - table for rich:
    #session, directions and pnl from self.trades
    #for every session create mask that choses long/short transactions
    # calculate wr, pnl, transaction amount for each
    # calculate LONG-SHORT difference for winrate and pnl
    # return results using dict so later i can use rich or visualization

