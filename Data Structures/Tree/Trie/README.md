# Trie
![Triedatastructure1](https://github.com/toutelajourn6e/Data-Structures/assets/118504009/decea95d-2e66-4c96-8962-b5c763249d54)

* Trie는 문자열을 효율적으로 저장하고 탐색하기 위한 트리 형태의 자료구조이다.
* 검색 엔진의 자동완성 기능이나 사전 검색 등 문자열을 탐색하는데 특화되어 있다.
* 만약 "Hello" 라는 문자열을 탐색한다면, 'H'가 먼저 있는지 확인 -> 'e'가 있는지 확인 -> 'l'이 있는지 확인 -> ...... -> 마지막 문자 노드에 문자열의 끝이 표시되어 있는지 확인한다. 


### Trie의 장단점
* M = 문자열의 길이
* 문자열을 (균형이 잘 잡힌)이진 탐색 트리에서 탐색하게 된다면 시간복잡도가 Mlog(N)에 달하지만, Trie는 O(M)으로 해결할 수 있다.
* 각 노드에서 자식들에 대한 포인터들을 배열로 저장하고 있기 때문에 메모리 측면에서는 비효율적 일 수도 있다.



### ADT
* insert : Trie에 문자열을 삽입
* search : Trie 안에 특정 문자열이 있는지 없는지 확인
* remove : 특정 문자열을 Trie에서 제거

## Time Complexity
|      연산       | 시간 복잡도 |
|:-------------:|:------:|
|      insert  |  O(M)  |
|      search  |  O(M)  |
|      remove  |  O(M)  |