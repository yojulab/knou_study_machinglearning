from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(50)

row_count = 50
cluster_1 = np.random.randn(row_count, 2)
mean_2 = np.array([3, 0])
cluster_2 = np.random.randn(row_count, 2) + mean_2
mean_3 = np.array([0, 3])
cluster_3 = np.random.randn(row_count, 2) + mean_3
cluster_all = np.vstack([cluster_1, cluster_2, cluster_3])

kernel = 3
indices = np.random.randint(cluster_all.shape[0], size=3)
print(indices)
means = cluster_all[indices, :]

# plt.scatter(cluster_1[:, 0], cluster_1[:, 1], label='cluster 1')
# plt.scatter(cluster_2[:, 0], cluster_2[:, 1], label='cluster 2')
# plt.scatter(cluster_3[:, 0], cluster_3[:, 1], label='cluster 3')
# plt.scatter(means[:, 0], means[:, 1], marker='v', s=90, label='means')
# plt.legend()

# means
row_all_count = cluster_all.shape[0]
cmode = ["green", "yellow", "blue"]
from scipy.spatial import distance as dstn

for iteration in range(10):
    plt.figure(iteration+1)
    cluster_label = np.zeros((row_all_count))
    for i in range(row_all_count):
        distance_measure = np.full((kernel), fill_value=0)
        for j in range(kernel):
            distance = dstn.euclidean(cluster_all[i, :], means[j, :])
            distance_measure[j] = distance
        cluster_label[i] = np.argmin(distance_measure)

    past_means = means.copy()
    for j in range(kernel):
        cluster_label_mask = (cluster_label == j)
        cluster_label_cnt = cluster_all[cluster_label_mask].shape[0]
        plt.scatter(cluster_all[cluster_label_mask, 0],
                    cluster_all[cluster_label_mask, 1], label='{}, {}'.format(j,cluster_label_cnt), color=cmode[j])
        means[j,:] = np.mean(cluster_all[cluster_label_mask, :], axis=0)    # 새로운 벡터 계산
    plt.scatter(past_means[:, 0], past_means[:, 1], marker='v', color='red', label='mean')
    pass
    plt.legend()
    plt.show()

    if (np.array_equal(means, past_means)):
        break
