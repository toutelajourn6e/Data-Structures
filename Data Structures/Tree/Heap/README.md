# Heap
![MinHeapAndMaxHeap1](https://github.com/toutelajourn6e/Data_Structures/assets/118504009/70436783-fc00-4d01-88e5-031cdf58e0c6)

* Heap은 우선 순위 큐를 구현한 자료구조이다.
* Heap Tree는 완전 이진 트리를 기본으로 하며, 일반적으로 배열을 이용해 구현한다.
* Heap은 Min Heap 과 Max Heap이 있으며, 각각 트리 내의 최솟값, 최댓값을 찾는데 특화되어 있다.
- - -

Min Heap : 부모 노드의 값이 자식 노드들의 값보다 항상 **작거나** 같다.<br>
Max Heap : 부모 노드의 값이 자식 노드들의 값보다 항상 **크거나** 같다.

###### 완전 이진 트리란?
* 노드가 위에서 아래로, 왼쪽에서 오른쪽으로 차례대로 채워진다.
* 리프 노드들의 높이 차가 최대 1이다.
* 트리 높이가 항상 logN 이다.

## ADT
* heapify : 부모와 자식간의 관계를 정리하며, 트리의 최소/최대 값을 루트 노드로 올린다.
* heappush : 새로운 노드를 남은 리프노드 자리의 제일 왼쪽에 삽입하고 heapify를 수행한다.
* heappop : 루트 노드의 값을 반환하고, 리프 노드의 제일 오른쪽 노드 값을 다시 루트 로드로 올린 뒤 heapify를 수행한다.

## Time Complexity
|      연산       | 시간 복잡도 |
|:-------------:|:------:|
|      heappush  |  O(logN)  |
|      heappop    |  O(logN)  |

heappush 와 heappop 연산을 하고 항상 heapify 작업을 하는데, 이때 최대 트리의 높이(logN)까지만 연산이 되므로 시간 복잡도는 O(logN)이다.
