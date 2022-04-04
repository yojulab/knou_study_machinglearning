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

"""## 판별함수 따른 각 class 확률 계산"""
import numpy as np

kernel_count = 5
error_count = np.full((3),0,dtype=np.int64) # class A,B,C
# row 수 만큼 측정 
for idx, item in enumerate(class_All):
  # 행 단위 모든 거리 계산
  distance_norm = np.linalg.norm(class_All - item, axis=1)
  # 거리순 정렬
  distance_idx = np.argsort(distance_norm)
  distance = np.sort(distance_norm)

  # 거리별 속하는 Class 종류 갯수 세기
  kernel_items = np.stack((distance_idx, distance), axis=1)
  class_type = np.full((3), 0)

  import math
  class_idx = math.floor((idx-1) / 100)
  for kernel_item in kernel_items[1:kernel_count+1]:
    if kernel_item[0] <= 100: 
      class_type[0] = class_type[0] + 1
    elif kernel_item[0] > 200: 
      class_type[2] = class_type[2] + 1
    else : 
      class_type[1] = class_type[1] + 1
  # 오류 데이터 측정
  max_idx = np.argmax(class_type)
  if class_idx != max_idx:
    error_count[class_idx] = error_count[class_idx] + 1
  pass
# print(idx, item, distance_norm.shape, distance.shape, distance_idx.shape)
print('error rate : {}'.format(error_count/class_A.shape[0]))