# Stack
![stack drawio2](https://github.com/toutelajourn6e/Data_Structures-Algorithms/assets/118504009/c5b85179-699d-440f-bb66-84aee4589856)

* 스택은 가장 나중에 들어간 데이터가 가장 먼저 나오는 선형 자료구조이다. (Last In First Out, LIFO)
* 스택은 '차곡차곡 쌓인 더미'라는 의미를 가졌으며 접시나 책이 쌓인 모습을 생각하면 된다.


## ADT
* is_empty : 스택이 비어있는지 확인
* get_size : 스택에 들어있는 요소의 갯수 반환
* push : 스택 최상단에 데이터 삽입
* pop : 스택 최상단의 데이터 삭제
* peek : 스택 최상단의 데이터 확인
* print_stack : 스택 요소를 최상단부터 차례대로 확인

## Time Complexity

|      연산       | 시간 복잡도 |
|:-------------:|:------:|
|      push       |  O(1)  |
|      pop       |  O(1)  |
| peek |  O(1)  |
| print |  O(n)  |
