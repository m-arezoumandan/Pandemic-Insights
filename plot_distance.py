from sklearn.manifold import MDS
import matplotlib.pyplot as plt
import numpy as np


def plot_distance(distance_matrix, labels, countries):
    mds = MDS(n_components=2, dissimilarity="precomputed")
    results = mds.fit(distance_matrix)
    my_colors = ['red', 'green', 'blue']
    coords = results.embedding_
    fig = plt.figure(figsize=(12, 10))
    plt.subplots_adjust(bottom=0.1)
    plt.scatter(coords[:, 0], coords[:, 1], c=labels)
    for country, x, y in zip(countries, coords[:, 0], coords[:, 1]):
        plt.annotate(country, xy=(x, y), xytext=(-10, 10), textcoords='offset points')

    plt.show()
