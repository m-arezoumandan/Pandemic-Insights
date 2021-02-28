import sys
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer
from sklearn.cluster import AgglomerativeClustering, DBSCAN, OPTICS
from tslearn.clustering import TimeSeriesKMeans
from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.cluster.encoder import type_encoding, cluster_encoder


def clustering_methods(alg_num, dm, arr):
    if alg_num == "1":
        k = input("enter k:\n")
        clustering = TimeSeriesKMeans(n_clusters=int(k), metric="dtw",max_iter=5).fit(arr)
        return clustering.labels_
    elif alg_num == "2":
        k = input("enter # of clusters:\n")
        clustering = AgglomerativeClustering(n_clusters=int(k), linkage="complete", affinity="precomputed").fit(dm)
        return clustering.labels_
    elif alg_num == "3":
        eps = input("enter eps:\n")
        clustering = DBSCAN(eps=float(eps), min_samples=4, metric="precomputed").fit(dm)
        return clustering.labels_
    elif alg_num == "4":
        clustering = OPTICS(min_samples=2, cluster_method='dbscan', metric="precomputed").fit(dm)
        return clustering.labels_
    elif alg_num == "5":
        k = input("enter k:\n")
        initial_medoids = kmeans_plusplus_initializer(dm, int(k)).initialize(return_index=True)
        kmedoids_instance = kmedoids(dm, initial_medoids, data_type='distance_matrix')
        kmedoids_instance.process()
        clusters = kmedoids_instance.get_clusters()
        kmedoids_repr = kmedoids_instance.get_cluster_encoding()
        kmedoids_encoder = cluster_encoder(kmedoids_repr, clusters, dm)
        kmedoids_encoder.set_encoding(type_encoding.CLUSTER_INDEX_LABELING)
        return kmedoids_encoder.get_clusters()
    else:
        sys.exit()
