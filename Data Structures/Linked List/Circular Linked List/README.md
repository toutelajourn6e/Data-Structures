# Circular Linked List
![CircularSinglyLinkedList](https://github.com/toutelajourn6e/Data_Structures-Algorithms/assets/118504009/a8d957ae-6c32-405b-80b3-f6338ac3989a)

* 원형 연결 리스트는 요소들이 메모리 상에 인접한 위치에 저장되지 않고 각 요소가 포인터를 사용하여 다음 요소에 연결되는 자료 구조이다.
* 원형 연결 리스트는 모든 노드가 연결되어 원을 형성한다.
* 첫 번째 노드의 참조인 헤드가 있고 마지막 노드의 참조가 헤드로 다시 연결된다. 즉 리스트 내에 NULL값이 없다.
* 마지막 노드를 첫 번째 노드에 연결하는 것을 제외하면 단순 연결 리스트와 유사하다.

## ADT
* is_empty : 연결 리스트의 요소 존재 여부 확인
* get_size : 연결 리스트의 노드 갯수 반환
* first : 첫 번째 노드 확인
* insert : 연결 리스트 첫 항목에 노드 삽입
* delete : 연결 리스트 첫 항목의 노드 삭제
* traverse : 연결 리스트 순회


## Time Complexity

|   연산    |    시간 복잡도    |
|:-------:|:------------:|
|   삽입    |O(1)|
|   삭제    |O(1)|
| 첫 노드 접근 |O(1)|
|   순회    |O(n)|
