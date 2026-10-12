PROJECT V2 - TODO / ROADMAP

PHASE 1 - FINISH CURRENT VERSION

1. Finish current pytest tests + manual tests

Test every meaningful public function [x]

Test normal cases [x]

Test edge cases [x]

Test W / L / BE [X]

Test invalid input [x]

Test rounding [x]

Test statistics with known expected values [x]

Remove meaningless "invalid" tests [x]

Fix every bug found during testing [x]

2. Add pytest fixtures [x]

3. Manually test the whole application

Test adding trades [x]

Test editing trades [x]

Test deleting trades [x]

Test searching by ID [x]

Test JSON saving/loading [x]

Test every user-input possibility [x]

Test valid and invalid inputs [x]

Check edge cases and unexpected inputs [x]

Fix every bug found during testing [x]

PHASE 2 - Add P&L

4. add pnl parameter + refactor whole program for it [x]

5.
Add pnl Visualization in plotly [x]

Add pnl Visualization in matplotlib [x]

Add hovers to plotly for a trade descriptions etc [x]

6. Add basic pnl statistics

Total pnl [x]

Best winning trade [ ]

Worst losing trade [ ]

PHASE 3 - DATAFRAME / PANDAS

7. Add Trade → DataFrame conversion ONLY FOR ANALYSIS

JSON
  ↓
list[Trade]
  ↓
Journal
  ↓
DataFrame
  ↓
pandas / NumPy

Keep:

Journal.trades -> list[Trade]

Do NOT make DataFrame the main storage/model.

8. Create a clean DataFrame representation

Convert Trade objects using to_dict() [ ]

Handle empty journal [ ]

Make sure columns have correct data types [ ]

9. Learn/use pandas for

Filtering [ ]

Grouping [ ]

Aggregation [ ]

Sorting [ ]

value_counts [ ]

groupby [ ]

Pivot tables [ ]

10. Add filtering by

Session [ ]

Direction [ ]

Pair [ ]

Market condition [ ]

Result [ ]

was_valid [ ]

PHASE 4 - REFACTOR STATISTICS

11. Separate data preparation from calculations

Data preparation

Filtering [ ]

Creating columns [ ]

Converting results to R [ ]

Handling invalid/abnormal trades [ ]

Calculations

Win rate [ ]

Expectancy [ ]

Profit factor [ ]

Average R [ ]

Drawdown [ ]

etc. [ ]

12. Refactor Statistics using pandas where useful

Replace repetitive loops where appropriate [ ]

Use groupby for grouped statistics [ ]

Use filtering instead of manually creating many lists [ ]

Do NOT use pandas just for the sake of using pandas [ ]

PHASE 5 - R ANALYTICS

13. Add R-result column

14. Add cumulative R

Example:

Trades:
+2R
-1R
+1.5R
-1R

Cumulative:
2
1
2.5
1.5

15. Add peak R / peak equity

16. Add drawdown

Current R - previous peak R [ ]

Add maximum drawdown [ ]

17. Handle BE correctly

BE = 0R [ ]

Do not count BE as W or L in win-rate calculations [ ]

18. Handle empty DataFrame / empty journal

19. Separate trade populations

Valid trades

Invalid / abnormal trades

All trades

Each group should be analyzable separately.

PHASE 6 - EXPECTANCY + PROFIT FACTOR

20. Add Expectancy

Determine exact implementation first.

Basic concept:

Expectancy = average R-result per trade

Example:

+0.24R per trade

21. Add Profit Factor

Profit Factor = Gross Profit / Gross Loss

Example:

Gross profit = 85R
Gross loss   = 52R

PF = 85 / 52

22. Verify both metrics with pytest

Use known trade data [ ]

Calculate expected result manually [ ]

Assert exact/appropriate value [ ]

PHASE 7 - MORE TRADING STATISTICS

23. Add

Average winning R [ ]

Average losing R [ ]

Win/Loss ratio [ ]

Median RR [ ]

RR standard deviation [ ]

Best winning trade [ ]

Worst losing trade [ ]

Winning streak [ ]

Losing streak [ ]

24. Add statistics by

Session [ ]

Direction [ ]

Pair [ ]

Market condition [ ]

25. Add combined statistics

Groupby combinations [ ]

Pivot tables [ ]

e.g. Session × Direction [ ]

e.g. Market condition × Session [ ]

PHASE 8 - NUMPY

26. Add NumPy where vectorized numerical calculations actually make sense

27. Use NumPy for more advanced numerical/statistical work

28. Do NOT replace simple Python/pandas operations with NumPy just to use NumPy

PHASE 9 - VALIDATION REFACTOR

29. Create validation.py

30. Move repeated validation rules there

31. Add constants for

Sessions [ ]

Directions [ ]

Results [ ]

Market conditions [ ]

32. Add reusable validation functions

33. Consider Enum later !!!

Do NOT rush this part.

PHASE 10 - RISK CALCULATOR

34. Add Risk Calculator

User inputs:

Account size [ ]

Risk % [ ]

RR [ ]

Calculate:

Risk amount [ ]

Potential profit [ ]

Potential loss [ ]

Example:

Account = $10,000
Risk = 1%

Risk amount = $100

RR = 2.5

Potential profit = $250

35. Keep Risk Calculator separate from Trade model

PHASE 11 - VISUALIZATION

36. Add cumulative R chart

37. Add drawdown chart

38. Add W/L/BE visualization

39. Add win rate by session

40. Add win rate by market condition

41. Add RR distribution / histogram

42. Keep visualizations useful

Less is more.

43. Optional

Custom chart colors [ ]

Dark/white theme [ ]

PHASE 12 - STORAGE REFACTOR

44. Refactor storage.py

Goal:

Journal
   ↓
Storage
   ↓
JSON

Keep loading/saving JSON separate from business logic.

45. Consider CSV export

46. Consider Excel export

47. Consider Notion export/integration later

PHASE 13 - USER EXPERIENCE

48. Improve CLI/menu

49. Improve error messages

50. Make input validation consistent

51. Make statistics output cleaner

52. Add filtering options

53. Add ability to inspect specific trades

PHASE 14 - EXPORT

54. Add CSV export

55. Add Excel export

56. Export statistics

57. Export filtered trades

FUTURE - NOT NOW

Advanced filtering [ ]

More advanced statistics [ ]

Dashboard [ ]

Database [ ]

PostgreSQL [ ]

SQLAlchemy [ ]

FastAPI [ ]

GUI [ ]

Real market data [ ]

Backtesting [ ]

Risk analytics [ ]

AI-assisted trade analysis [ ]

These are far-future features.

Do NOT work on them before completing the core analytics.







/// Previous one

 =========================
 PROJECT V2 - TODO
 =========================

 REFACTOR
 Separate data preparation from calculations
 Keep OOP structure, but use pandas/NumPy where they actually help

 PANDAS
 Add Trade -> DataFrame conversion (only for analysis) 
 so do not change trade as a list of...
 Use pandas for filtering, grouping and aggregation
 Add groupby statistics
 Add pivot tables
 Add filtering by:
 - session
 - direction
 - pair
 - market_condition
 - result
 - was_valid

 NUMPY
 Add NumPy where vectorized numerical calculations make sense
 Use NumPy for more advanced statistical calculations
 Avoid using NumPy/pandas just for the sake of using them

 TRADING STATISTICS
 Add expectancy -> and figure out what will exactly do
 Add - Profit Factor = Gross Profit / Gross Loss
 so basically i have to make a refactor
 for a % as a profit  as a separate input to journal
 or just assume do r profit so
 1.55 rr one trade 1 second and second one is a loser
 which means that im +0.55 rr 
 and i can makce rr calculator
 where u will basically input stoploss % amount or $ amount
 and it will just count your profit
 Best winning trade and worst losing one

 Add RR standard deviation
 Add winning streaks
 Add losing streaks

 Add combined statistics / pivot tables

 DATA PREPARATION
 Add R-result column
 Add cumulative R
 Add peak equity / peak R
 Add drawdown (max drawdown input + than analysis ofc)
 Handle empty DataFrame / empty journal
 Make sure invalid / abnormal trades do not contaminate 
 normal trade statistics
 so i can basically make a separation
 1. valid trades  + analysis 2. invalid + analysis 3. both + analysis


 VALIDATION
 Create validation.py
 Move repeated validation rules there
 Add constants for:
 - sessions
 - directions
 - results
 - market conditions
 Add reusable validation functions
 Consider Enum later !!!

 VISUALIZATION
 Add cumulative R chart
 Add drawdown chart
 Add W/L visualization
 Add win rate by session
 Add win rate by market condition
 Keep visualizations useful
 Less is more
 Custom chart colors??? 
 Dark/white theme?

 TESTING
 Test every meaningful public function
 Test normal cases
 Test edge cases
 Test empty data
 Test W / L / BE
 Test invalid input
 Test rounding
 Test statistics with known expected values
 Use pytest fixtures for repeated trade data
 Add actual tests instead of only manual testing
 Fix every bug found during testing

 STORAGE
 storage.py
 Keep loading/saving JSON separate from business logic
 Consider CSV export
 Consider Excel export later + Notion

 USER EXPERIENCE
 Improve CLI/menu
 Improve error messages
 Make input validation consistent
 Make statistics output cleaner
 Add filtering options
 Add ability to inspect specific trades

 EXPORT
 Add CSV export
 Add Excel export
 Export statistics
 Export filtered trades

 FUTURE # some of them are really far future.
 Advanced filtering
 More advanced statistics
 Dashboard
 Database
 PostgreSQL
 SQLAlchemy
 FastAPI
 GUI
 Real market data
 Backtesting
 Risk analytics
 AI-assisted trade analysis # Far far future still not sure