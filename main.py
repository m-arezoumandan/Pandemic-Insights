from clustering_methods import clustering_methods
from compute_matrix import compute_matrix
from plot_distance import plot_distance
from data_cleaning import cleaning, cleaning2
from data_smoothing import smoothing
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from sklearn.metrics import silhouette_score


daily_cases = pd.DataFrame(cleaning())
daily_cases_norm = MinMaxScaler().fit_transform(daily_cases.values ** 0.5)
daily_cases_smoothed = pd.DataFrame(smoothing(daily_cases_norm))
daily_cases_smoothed.columns = daily_cases.columns

dist_num = input("enter '1' for euclidean distances, '2' for DTW, or anything else for termination!\n")

distance_matrix = compute_matrix(dist_num, daily_cases_smoothed)

alg_num = input("enter '1' for K-Means, '2' for AGNES, '3' for DBSCAN, "
                "'4' for OPTICS, '5' for K-medoids, or anything else for termination!\n")

labels = clustering_methods(alg_num, distance_matrix, daily_cases_smoothed.values.T)

xx = zip(list(labels), daily_cases.columns)
for x in xx:
    print(x)

plot_distance(distance_matrix, labels, daily_cases.columns)

print("Silhouette score: ",  silhouette_score(distance_matrix, labels, metric="precomputed"))