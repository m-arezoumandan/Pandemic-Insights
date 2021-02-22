import sys
from sklearn.metrics import euclidean_distances
from tslearn.metrics import dtw
import numpy as np


def compute_matrix(choice, data):
    if choice == "1":
        return euclidean_distances(data.T.values)
    elif choice == "2":
        # calculate the distance matrix with dtw score
        num_countries = len(data.columns)
        distance_matrix = np.zeros((num_countries, num_countries))
        for index_i, i in enumerate(data.values.T):
            for index_j, j in enumerate(data.values.T):
                distance_matrix[index_i, index_j] = dtw(i, j)
        return distance_matrix
    else:
        sys.exit()
