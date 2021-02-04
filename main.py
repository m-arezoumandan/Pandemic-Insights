import data_cleaning as dc
from sklearn.preprocessing import MinMaxScaler
import data_smoothing as ds
import pandas as pd
from tslearn.metrics import dtw
import numpy as np
import matplotlib.pyplot as plt

data = dc.cleaning()
daily_cases = pd.DataFrame(data)
# daily_cases_trans = daily_cases ** 0.5
daily_cases_norm = MinMaxScaler().fit_transform(daily_cases.values)
daily_cases_smoothed = pd.DataFrame(ds.smoothing(daily_cases_norm))
daily_cases_smoothed.columns = daily_cases.columns

# plotting different countries patterns and their dtw score
# dtw_score = dtw(daily_cases_smoothed["Italy"], daily_cases_smoothed["China"])
# x = np.linspace(1, 300, 300)
# plt.plot(x, daily_cases_smoothed["China"], label="China")
# plt.plot(x, daily_cases_smoothed["Italy"], color='red', label="Italy")
# plt.legend()
# dtw_str = "DTW Score = " + str(dtw_score)
# plt.title(dtw_str)
# plt.show()

# calculate the distance matrix
num_countries = len(daily_cases_smoothed.columns)
distance_matrix = np.zeros((num_countries, num_countries))
for index_i, i in enumerate(daily_cases_smoothed.values.T):
    for index_j, j in enumerate(daily_cases_smoothed.values.T):
        distance_matrix[index_i, index_j] = dtw(i, j)
print("Distance Matrix:")
print(distance_matrix)

'''
compute the matrix of distances : DONE

Hopkins statistics

Use different clustering methods 

Evaluate all clustering methods used

Visualization

Final analysis
'''