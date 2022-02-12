"""
[문제]
n(2 ≤ n ≤ 100)개의 도시가 있다. 
그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1 ≤ m ≤ 100,000)개의 버스가 있다. 
각 버스는 한 번 사용할 때 필요한 비용이 있다.

모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.


[입력]
첫째 줄에 도시의 개수 n이 주어지고 둘째 줄에는 버스의 개수 m이 주어진다. 
그리고 셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다. 
먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 
버스의 정보는 버스의 시작 도시 a, 도착 도시 b, 한 번 타는데 필요한 비용 c로 이루어져 있다. 
시작 도시와 도착 도시가 같은 경우는 없다. 비용은 100,000보다 작거나 같은 자연수이다.

시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.


[출력]
n개의 줄을 출력해야 한다. i번째 줄에 출력하는 j번째 숫자는 도시 i에서 j로 가는데 필요한 최소 비용이다. 
만약, i에서 j로 갈 수 없는 경우에는 그 자리에 0을 출력한다.


[입력 예시]
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4


[출력 예시]
0 2 3 1 4
12 0 15 2 5
8 5 0 1 1
10 7 13 0 3
7 4 10 6 0

"""


# PyPy3 제출    : 메모리(127016 KB) 시간(236 ms)
# Python3 제출  : 메모리(30864 KB)  시간(728 ms)

# 참고 : https://my-coding-notes.tistory.com/231


# 플로이드-와샬  (DP의 연장선)
# 하나의 정점에서 모든 정점으로의 최단 거리 구할 때 사용

import sys
input = sys.stdin.readline

n,m = int(input()), int(input())
graph = [[float('inf')]*n for i in range(n)]

# 인접 행렬 생성
for _ in range(m):
    s,e,w = map(int,input().split())
    s-=1;e-=1
    graph[s][e] = min(graph[s][e], w)

# 플로이드-와샬 수행
for k in range(n):
    graph[k][k] = 0
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 출력
for i in graph:
    for j in i:
        print(j if j!=float('inf') else 0, end = " ")
    print()