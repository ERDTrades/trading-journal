from journal import Journal
from trade_input import create_trade
from trade_input import guide
from trade_statistics import Statistics

from plot_matplotlib import cumulative_wr, wlbe_bar_chart, rr_graph
from plot_plotly import cumulative_winrate_plotly, wlbe_graph_plotly
from plot_plotly import pnl_amount_of_trades, session_pnl, describe_chart

journal = Journal()

from numpy_analysis import numpy_statistics



journal.load_from_json()

stats = Statistics(journal.trades)

numpy_stats = numpy_statistics(journal.trades)

def show_menu():
    print(
        "========================"
        "\nTrading Journal"
        "\n========================"
        "\n0. Exit"
        "\n1. Parameter Guidelines (Adding/Editing trades)"
        "\n2. Add Trade"
        "\n3. View Journal"
        "\n4. Search trade by ID"
        "\n5. Delete Trade by ID"
        "\n6. Edit Trade"
        "\n7. Show General Statistics"
        "\n8. Show more in-depth Statistics" #Pandas & Numpy
        "\n9. Show visualization menu"
    )
          
def menu_loop():
    """Main menu loop"""
    while True:
        if input("Show menu (Y/N): ").strip().upper() == "Y":
            show_menu()
        option = input("Choose an option (0-9): ").strip()


        if option == "1":
             guide()

        elif option == "2":
            if input("\nDo you want to see Users Guide"
                " before entering new trade? (Y/N): "
                ).strip().upper() == "Y":
                guide()
            while True:
                    trade = create_trade()
                    journal.add_trade(trade)
                    journal.save_to_json()
                    if input("Do you want to add another trade?"
                    " Y / N: ").strip().upper() != "Y":
                            break
                        
        elif option == "3":
            journal.display_trades()

        elif option == "4":       
          trade_id = int(input("Enter trade ID: "))
          trade = journal.id_find(trade_id)

          if trade:
               print(trade)
          else:
               print("Trade not found.")

        elif option == "5":
             if (input("Do you want to delete trade? (Y/N): ")
             .strip().upper() == "Y"
             ):
                  
                  trade_id = int(input("Enter trade ID that you want to delete: "))
                  trade = journal.del_trade(trade_id)

                  if trade:
                       journal.save_to_json()
                       print("Trade deleted")
                  else:
                       print("Trade not found")

        elif option == "6":
             if (input("Do you want to see a parameter guidelines? (Y/N): ")
                    .strip().upper() == "Y"
                    ):
                  print("\nAvailable parameters:"
                        "\twas_valid \tdate \tsession"
                        "\npair \tdirection \tmarket_condition"
                        "\nrr \tresult \t"
                        "\nentry \texit \tnotes")
               
             try:
               edt_trade = int(input("Enter Trade ID that you want to edit: ")
                             .strip())
             except ValueError:
                  print("Please enter a valid Trade ID")
                  continue

             
             trade = journal.edit_trade(edt_trade)

             if trade:
               journal.save_to_json()
               print("Change saved")
             

                  

        elif option == "7":
             stats.show_statistics()

        elif option == "8":
               from numpy_analysis import numpy_statistics

               numpyy_stats = numpy_statistics(journal.trades)

               from rich.console import Console

               console = Console()

               tables = numpyy_stats.show_numpy_stats()

               for table in tables:
                    console.print(table)

        elif option ==  "9":
            print("----------Visualization menu----------"
                    "\nCumulative winrate graph - input A "
                    "\nW/L/BE bar chart - input B "
                    "\nRR Graph - input C "
                    "\ncumulative pnl sessions + trade amount - Input D"
                    "\nShow All - input E")

            choice = input("Choice: ")

               # For now I have both plotly and matplotlib 
               # for visualization
               # Later -> Add dark/white theme as a choice
            if choice.upper().strip() == "A":
                 cumulative_wr(journal)
                 cumulative_winrate_plotly(journal)

            elif choice.upper().strip() == "B":
                 wlbe_bar_chart(journal)
                 wlbe_graph_plotly(journal)

            elif choice.upper().strip() == "C":
                 rr_graph(journal)

            elif choice.upper().strip() == "D":
                 session_pnl(journal)
                 pnl_amount_of_trades(journal)

            elif choice.upper().strip() == "E":
                cumulative_wr(journal)
                cumulative_winrate_plotly(journal)
                wlbe_bar_chart(journal)
                wlbe_graph_plotly(journal)
                rr_graph(journal)
                pnl_amount_of_trades(journal)
                session_pnl(journal)
                describe_chart(journal)
                
            else:
                 print("Please enter correct input")

        elif option == "0":
                break

        else: 
             print("Invalid option")
