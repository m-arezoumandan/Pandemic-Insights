import scipy.signal
import numpy as np
import matplotlib.pyplot as plt


def smoothing(daily_cases_norm):
    smoothed = []
    for col in daily_cases_norm.T:
        # window size 35, polynomial order 3
        yhat = scipy.signal.savgol_filter(col, 35, 3)
        smoothed.append(yhat)

    # x = np.linspace(1, 300, 300)
    # yhat = scipy.signal.savgol_filter(daily_cases_norm.T[90], 35, 3)  # window size 51, polynomial order 3
    # plt.plot(x, daily_cases_norm.T[90])
    # plt.plot(x, yhat, color='red')
    # plt.show()
    smoothed_transpose = np.array(smoothed).transpose()
    return smoothed_transpose
