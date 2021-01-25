import scipy.signal
import numpy as np


def smoothing(daily_cases_norm):
    smoothed = []
    for col in daily_cases_norm.T:
        # window size 11, polynomial order 3
        yhat = scipy.signal.savgol_filter(col, 11, 3)
        smoothed.append(yhat)

    smoothed_transpose = np.array(smoothed).transpose()
    return smoothed_transpose