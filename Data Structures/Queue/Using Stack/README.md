# Queue(Using Stack)
![fifo-property-in-Queue](https://github.com/toutelajourn6e/Data_Structures-Algorithms/assets/118504009/fb5aed1a-75b0-4d82-9a09-76b648f27a92)

* 큐는 먼저 들어간 데이터가 가장 먼저 나오는 선형 자료구조이다. (First In First Out, FIFO)
* 큐는 처리을 위해 기다리는 대기 줄을 생각하면 된다.
* 큐의 앞부분을 front 라고 하며, 뒷부분을 rear 라고 한다.
* 연결 리스트로 구현한 큐와 달리, 자료구조의 한계로 인해 (요소를 삽입, 삭제하면 나머지 요소를 앞으로 또는 뒤로 옮겨야 하기 때문)<br> enqueue 혹은 dequeue의 시간복잡도가 O(n)이 된다.


## ADT
* is_empty : 큐가 비어있는지 확인
* get_size : 큐에 들어있는 요소의 갯수 반환
* enqueue : rear에 데이터 삽입
* dequeue : front의 데이터 삭제
* peek : front의 데이터 확인
* print_queue : 큐의 요소를 front부터 차례대로 확인

## Time Complexity

|      연산       | 시간 복잡도 |
|:-------------:|:------:|
|      enqueue       |  O(n)  |
|      dequeue       |  O(1)  |
| peek |  O(1)  |
| print_queue |  O(n)  |
