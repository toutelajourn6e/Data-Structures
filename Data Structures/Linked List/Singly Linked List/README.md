# Singly Linked List

![SLL](https://github.com/toutelajourn6e/Data_Structures-Algorithms/assets/118504009/f5fd66b5-2e23-4d69-be93-441e032ab6fe)

* 단일 연결 리스트는 요소들이 메모리 상에 인접한 위치에 저장되지 않고 각 요소가 포인터를 사용하여 다음 요소에 연결되는 선형 자료구조이다.
* 각 노드는 단일 값과 연결 리스트의 다음 노드에 대한 참조를 보유하고 있다.
* 첫 번째 노드에 대한 참조인 헤드와 연결 리스트의 마지막 노드에 대한 참조인 테일이 있다.
* 단일 연결 리스트의 요소에 접근하려면 메모리의 특정 노드에 직접 액세스할 수 없으므로 헤드에서 원하는 노드로 연결 리스트를 순회해야 한다.

## ADT

* is_empty : 연결 리스트의 요소 존재 여부 확인
* get_size : 연결 리스트의 노드 갯수 반환
* search_idx : 특정 인덱스의 노드 접근
* search_value : 특정 값을 가지고 있는 노드 탐색
* add_first : 연결 리스트의 헤더에 노드 추가
* add_last : 연결 리스트의 테일에 노드 추가
* insert : 특정한 위치에 노드 추가
* delete_first : 헤더의 노드를 삭제
* delete_last : 테일의 노드를 삭제
* remove : 특정한 위치의 노드 삭제
* reverse : 연결 리스트 뒤집기
* traverse : 연결 리스트를 순회

## Time Complexity

|      연산       | 시간 복잡도 |
|:-------------:|:------:|
|      접근       |  O(n)  |
|      탐색       |  O(n)  |
| 특정한 위치에 노드 삽입 |  O(n)  |
| 특정한 위치의 노드 제거 |  O(n)  |
|  가장 앞에 노드 삽입  |  O(1)  |
|  가장 뒤에 노드 삽입  |  O(1)  |
|  가장 앞의 노드 제거  |  O(1)  |
|  가장 뒤의 노드 제거  |  O(n)  |
|  연결 리스트 뒤집기   |  O(n)  |
