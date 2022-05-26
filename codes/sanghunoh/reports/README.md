### 과제 수행
| 주제 | 주요 항목 | 작성 | dataset | 참조 |
| :---: | --- | :---: | :---: | :---: |
| 분포 | 가우시안 분포 데이터 생성 | [link](./과제_1_1_가우시안분포따른4개클래스.ipynb) | random |  |
| 분포 | 가우시안 분포 공분산 계산 | [link](./과제_1_2_표본평균과공분산계산.ipynb) | random |  |
| 분류기 | 베이지안 분포 분류 | [link](./과제_2_1_가우시안분포산점도.ipynb) | random |  |
| 분류기 | iris 분포 KNN 분류 | [link](./과제_2_2_iris_KNN분류.ipynb) | [zip](../../../datas/iris.zip) |  |
|  선형분류 | Perceptron | [link](./과제_3_1_선형판별함수_perceptron.ipynb) | [mat](../../../datas/HW3Data_1.mat) |  |
| Clustering | K-means | [link](./과제_3_2_군집화_K_means.ipynb) | random |  |
| 특징 추출 | PCA & LDA | [ipynb](./과제_4_1_PCA_LDA.ipynb) | random |  |
| 차원 축소 | COIL20_PCA_LDA| [ipynb](./과제_4_2_COIL20_PCA_LDA.ipynb) | [mat](../../../datats/HW4_COIL20.mat) |  |
| 가우시안혼합 모델 |가우시안혼합 | [ipynb](./과제_5_1_1_가우시안혼합모델.ipynb) | [mat](../../../datats/HW5Data_1.mat) |  |
| Kmeans Model |Kmeans| [ipynb](./과제_5_1_3_Kmeans.ipynb) | [mat](../../../datats/HW5Data_1.mat) |  |
| MLP |MLP| [ipynb](./과제_5_2_MLP.ipynb) | [mat](../../../datats/HW5Data_2.mat) |  |
| Term2 | dataset preprocess| [ipynb](./Term_2_preprocess.ipynb)| [zip](../../../datats/mpie_30_shuffle.zip) |  |
| Term2 | CNN(Face Detection)| [ipynb](./Term_2_CNN_MPIE.ipynb), [ipynb](./Term_2_CNN_MPIE_results.ipynb) | [zip](../../../datats/mpie_30_shuffle.zip) |  |

## Term 1 Project refer
|국내외|발행년도| 명칭 | 설명 | URI |
| :---:| :---: | :---: | --- | :---: |
|국내|1997|표본 데이터 선정 방법에 따른 MLP분류기의 성능 고찰|MLP 분류기의 많은 반복 학습 시간을 최소화시키기 위한 제안|[link](http://www.riss.kr/link?id=T6949443)|
|국내|2020|내장형 시스템을 위한 효율적인 CNN 구조 연구|고성능의 PC환경이 아닌 위와 같은 제한적인 환경에서의 동작을 위한 효율적인 CNN 구조를 제안|[link](http://www.riss.kr/link?id=T15499947)|

## Term 2 Project dataset
-> MPIE 얼굴 이미지 데이터.
     http://www.cs.cmu.edu/afs/cs/project/PIE/MultiPie/Multi-Pie/Home.html  
 
-> MPIE 데이터는 기본적으로 유료 데이터이며, 본 프로젝트에서 제공되는 데이터는 원본 데이터의 일부를 가져와 추가적인 클래스(gender, age, race)를 임의로 라벨링(labeling) 한 것입니다. 따라서 원본 이미지를 제공해 드리지 못한 점 양해 바랍니다.  
 
-> Traindata.csv, Testdata.csv : 학습/테스트 데이터의 픽셀 값 (1024 차원)  
 
-> Trainlabel.csv, Testlabel.csv : 학습/테스트 데이터의 클래스 값. 총 6가지의 클래스  
      1열 : identity label (몇 번째 사람인가에 대한 클래스, 총 30개의 라벨 (0~29))  
      2열 : expression label(표정 클래스, 총 6개의 라벨 (0~5))  
      3열 : pose label (촬영 각도에 대한 클래스, 총 5개의 라벨(0~4))  
      4열 : gender label (성별 클래스, 총 2개의 라벨(0,1))  
      5열 : age label (나이 클래스, 총 5개의 라벨(0~4))  
      6열 : race label (인종에 대한 클래스, 총 4개의 라벨(0~3))  
 
-> 학습 데이터는 18777개, 테스트 데이터는 5086개로 구성되어 있음.
