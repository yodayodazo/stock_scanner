import pandas as pd
import pandas_datareader as web
from pandas_datareader import data
import math
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta
from condition import *
from stock_screener import *
from stock_screener_backtest import *

test_Date = datetime(2021,3,18)
end = datetime(2021,4,1)
while test_Date <= end:
    if (0 <= test_Date.weekday() <= 4):
        scan_temp = stock_screen('midcap', test_Date)
    test_Date = test_Date + timedelta(days=1)

