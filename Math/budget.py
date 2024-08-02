import calendar
import pandas as pd
from datetime import datetime


#Pull todays date

today = datetime.today().strftime('%Y-%m-%d')
print(today)

income = pd.Series[660, 0, 0, 0]
bills = pd.Series[-850,-250,-1000,450]
due_dates = pd.Series[2, 15, 20, 25]


mybudget = pd.concat([income, bills, due_dates], axis = 1)

print(mybudget)