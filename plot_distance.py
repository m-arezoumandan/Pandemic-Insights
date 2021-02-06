from sklearn.manifold import MDS
import matplotlib.pyplot as plt


def plot_distance(distance_matrix, labels):
    mds = MDS(n_components=2, dissimilarity="precomputed")
    results = mds.fit(distance_matrix)
    countries = labels
    coords = results.embedding_
    fig = plt.figure(figsize=(12, 10))
    plt.subplots_adjust(bottom=0.1)
    plt.scatter(coords[:, 0], coords[:, 1])
    for label, x, y in zip(countries, coords[:, 0], coords[:, 1]):
        plt.annotate(label, xy=(x, y), xytext=(-10, 10), textcoords='offset points')
    plt.show()
