"""
[문제]
V개의 마을와 E개의 도로로 구성되어 있는 도시가 있다. 
도로는 마을과 마을 사이에 놓여 있으며, 일방 통행 도로이다. 
마을에는 편의상 1번부터 V번까지 번호가 매겨져 있다고 하자.

당신은 도로를 따라 운동을 하기 위한 경로를 찾으려고 한다. 
운동을 한 후에는 다시 시작점으로 돌아오는 것이 좋기 때문에, 우리는 사이클을 찾기를 원한다. 
단, 당신은 운동을 매우 귀찮아하므로, 사이클을 이루는 도로의 길이의 합이 최소가 되도록 찾으려고 한다.

도로의 정보가 주어졌을 때, 도로의 길이의 합이 가장 작은 사이클을 찾는 프로그램을 작성하시오. 
두 마을을 왕복하는 경우도 사이클에 포함됨에 주의한다.


[입력]
첫째 줄에 V와 E가 빈칸을 사이에 두고 주어진다. (2 ≤ V ≤ 400, 0 ≤ E ≤ V(V-1)) 
다음 E개의 줄에는 각각 세 개의 정수 a, b, c가 주어진다. 
a번 마을에서 b번 마을로 가는 거리가 c인 도로가 있다는 의미이다.
(a → b임에 주의) 거리는 10,000 이하의 자연수이다. 
(a, b) 쌍이 같은 도로가 여러 번 주어지지 않는다.


[출력]
첫째 줄에 최소 사이클의 도로 길이의 합을 출력한다. 
운동 경로를 찾는 것이 불가능한 경우에는 -1을 출력한다.


[입력 예시]
3 4
1 2 1
3 2 1
1 3 5
2 3 2


[출력 예시]
3


"""

# PyPy3 제출    : 메모리(126648 KB) 시간(2740 ms)
# Python3 제출  : 불가능. 시간 초과

# 참고 : https://yuuj.tistory.com/61


# 플로이드 와샬

import sys

# V: 마을 갯수, E: 도로 갯수
V, E = map(int, sys.stdin.readline().split())

INF = sys.maxsize
arr = [[INF for _ in range(V)] for _ in range(V)]

for _ in range(E):
    i, j, c = map(int, sys.stdin.readline().split())
    arr[i-1][j-1] = c

for k in range(V):  # 거쳐가는애
    for i in range(V):  # from
        for j in range(V):  # to
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

result = INF
#  계속 갱신한 뒤 사이클은 본인부터 본인까지에 저장됨
for i in range(V):
    result = min(result, arr[i][i])

if result == INF:
    print(-1)
else:
    print(result)
