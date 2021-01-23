import data_cleaning as dc
import data_normalization as dn
import pandas as pd

data = dc.cleaning()
daily_cases = pd.DataFrame(data)
daily_cases_norm = dn.normalizing(daily_cases.values)
daily_cases_norm.columns = daily_cases.columns
print(daily_cases_norm)
