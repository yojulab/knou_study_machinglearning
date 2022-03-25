# read dataset file
import scipy.io
mat = scipy.io.loadmat('./datas/dataCh4_7.mat')
# type(mat), mat.keys(),

import numpy as np

class_kernel_count = 3
class_A = mat['X1']
class_B = mat['X2']
class_C = mat['X3']
class_All = np.vstack([class_A, class_B, class_C])
class_A.shape, type(class_A), class_B.shape, class_C.shape, class_All.shape

import matplotlib.pyplot as plt

# plt.plot(class_A[:,0], class_A[:,1], marker='o', linestyle='None', label='class_A')
# plt.plot(class_B[:,0], class_B[:,1], marker='v', linestyle='None', label='class_B')
# plt.plot(class_C[:,0], class_C[:,1], marker='^', linestyle='None', label='class_C')
# plt.legend()
# plt.show()

"""# class 평균, 공분산 구하기 """

import numpy as np

class_A_mean = np.mean(class_A, axis=0)
class_A_mean.shape, class_A_mean

class_B_mean = np.mean(class_B, axis=0)
class_C_mean = np.mean(class_C, axis=0)
class_All_mean = np.mean(class_C, axis=0)

class_A_cov = np.cov(class_A.T)
class_A_cov.shape, class_A_cov

class_B_cov = np.cov(class_B.T)
class_C_cov = np.cov(class_C.T)
class_All_cov = np.cov(class_All.T)

"""## 판별함수 따른 각 class 확률 계산"""

class_list = [class_A, class_B, class_C]

for idx in range(len(class_list)):
  class_temp = class_list[idx]
  class_temp_mean = np.mean(class_temp, axis=0)
  class_temp_cov = np.cov(class_temp.T)
  metrix_result = np.empty((0,2))
  for row in class_temp:
    metrix_temp = ((row-class_All_mean) * (row-class_All_mean)).reshape(1,-1)
    metrix_result = np.append(metrix_result, metrix_temp, axis=0)
  # print('metrix_temp : ',np.min(metrix_temp))
  # print('metrix_result.shape : ',metrix_result.shape)
  print('metrix_result min : ', np.min(metrix_result,axis=0))

