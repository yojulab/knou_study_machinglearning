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
for iter in range(9):
    cluster_kind_idx = list()
    for i in range(row_all_count):
        distance_measure = np.full((kernel), fill_value=0)
        for j in range(kernel-1):
            distance = np.power(cluster_all[i, :] - means[j, :], 2)
            distance_measure[j] = np.linalg.norm(distance)
        cluster_kind_idx.append(np.argmin(distance_measure))

    cluster_kind_idx_np = np.asarray(cluster_kind_idx)
    # for j in range(kernel-1):
    cluster_kind_mask = (cluster_kind_idx_np == 0)
    plt.scatter(cluster_all[cluster_kind_mask, 0],
                cluster_all[cluster_kind_mask, 1])
    cluster_kind_mask = (cluster_kind_idx_np == 1)
    plt.scatter(cluster_all[cluster_kind_mask, 0],
                cluster_all[cluster_kind_mask, 1])
    cluster_kind_mask = (cluster_kind_idx_np == 2)
    plt.scatter(cluster_all[cluster_kind_mask, 0],
                cluster_all[cluster_kind_mask, 1])
    # plt.show()
