import data_cleaning as dc
import data_normalization as dn
import data_smoothing as ds
import pandas as pd


data = dc.cleaning()
daily_cases = pd.DataFrame(data)
#daily_cases_trans = daily_cases ** 0.5
daily_cases_norm = dn.normalizing(daily_cases.values)
daily_cases_norm.columns = daily_cases.columns
daily_cases_smoothed = pd.DataFrame(ds.smoothing(daily_cases_norm.values))
daily_cases_smoothed.columns = daily_cases.columns
print(daily_cases_smoothed)