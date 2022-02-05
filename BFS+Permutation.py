"""
[문제]
오늘은 직사각형 모양의 방을 로봇 청소기를 이용해 청소하려고 한다. 
이 로봇 청소기는 유저가 직접 경로를 설정할 수 있다.

방은 크기가 1×1인 정사각형 칸으로 나누어져 있으며, 로봇 청소기의 크기도 1×1이다. 
칸은 깨끗한 칸과 더러운 칸으로 나누어져 있으며, 
로봇 청소기는 더러운 칸을 방문해서 깨끗한 칸으로 바꿀 수 있다.

일부 칸에는 가구가 놓여져 있고, 가구의 크기도 1×1이다. 
로봇 청소기는 가구가 놓여진 칸으로 이동할 수 없다. 

로봇은 한 번 움직일 때, 인접한 칸으로 이동할 수 있다. 
또, 로봇은 같은 칸을 여러 번 방문할 수 있다.

방의 정보가 주어졌을 때, 더러운 칸을 모두 깨끗한 칸으로 만드는데 필요한 이동 횟수의 최솟값을 구하는 프로그램을 작성하시오.


[입력]
입력은 여러 개의 테스트케이스로 이루어져 있다.

각 테스트 케이스의 첫째 줄에는 방의 가로 크기 w와 세로 크기 h가 주어진다. (1 ≤ w, h ≤ 20) 
둘째 줄부터 h개의 줄에는 방의 정보가 주어진다. 
방의 정보는 4가지 문자로만 이루어져 있으며, 각 문자의 의미는 다음과 같다.

. : 깨끗한 칸
* : 더러운 칸
x : 가구
o : 로봇 청소기의 시작 위치

더러운 칸의 개수는 10개를 넘지 않으며, 로봇 청소기의 개수는 항상 하나이다.
입력의 마지막 줄에는 0이 두 개 주어진다.


[출력]
각각의 테스트 케이스마다 더러운 칸을 모두 깨끗한 칸으로 바꾸는 이동 횟수의 최솟값을 한 줄에 하나씩 출력한다. 
만약, 방문할 수 없는 더러운 칸이 존재하는 경우에는 -1을 출력한다.


[입력 예시]
7 5
.......
.o...*.
.......
.*...*.
.......
15 13
.......x.......
...o...x....*..
.......x.......
.......x.......
.......x.......
...............
xxxxx.....xxxxx
...............
.......x.......
.......x.......
.......x.......
..*....x....*..
.......x.......
10 10
..........
..o.......
..........
..........
..........
.....xxxxx
.....x....
.....x.*..
.....x....
.....x....
0 0


[출력 예시]
8
49
-1

"""

# PyPy3 제출    : 메모리(129100 KB) 시간(736 ms)
# Python3 제출  : 불가능. 시간초과

# 참고 : https://velog.io/@djagmlrhks3/Algorithm-BaekJoon-4991.-%EB%A1%9C%EB%B4%87-%EC%B2%AD%EC%86%8C%EA%B8%B0-by-Python

# BFS + 순열

import sys
from collections import deque
from itertools import permutations

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(i, j):
    visited = [[0] * w for _ in range(h)]
    visited[i][j] = 1
    queue = deque([(i, j)])
    while queue:
        r, c = queue.popleft()
        for idx in range(4):
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc]:
                if maps[nr][nc] != 'x':
                    queue.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1
    return visited


while True:
    w, h = map(int, input().split())
    if w + h:
        maps = [list(''.join(map(str, sys.stdin.readline().rstrip()))) for _ in range(h)]
        dusts = [] # 더러운 칸의 좌표를 담을 배열
        cr, cc = 0, 0 # 로봇 청소기의 위치(행, 열)
        for r in range(h):
            for c in range(w):
                if maps[r][c] == 'o':
                    cr, cc = r, c
                elif maps[r][c] == '*':
                    dusts.append((r, c))

        cleaner = [0] * len(dusts) # 로봇 청소기 ~ 첫 번째로 청소할 더러운 칸까지의 거리를 담을 배열
        visited = bfs(cr, cc)
        is_possible = True # 로봇 청소기가 모든 더러운 칸을 방문할 수 있는지 확인
        for idx, rc in enumerate(dusts):
            temp = visited[rc[0]][rc[1]]
            if not temp: # 로봇 청소기가 방문할 수 없는 칸이 나오면 False
                print(-1)
                is_possible = False
                break
            cleaner[idx] += temp - 1 

        if is_possible:
            dists = [[0] * (len(dusts)) for _ in range(len(dusts))] # 더러운 칸마다의 거리를 계산한다.
            for i in range(len(dusts) - 1):
                visited = bfs(dusts[i][0], dusts[i][1])
                for j in range(i + 1, len(dusts)):
                    dists[i][j] = visited[dusts[j][0]][dusts[j][1]] - 1
                    dists[j][i] = dists[i][j]
            answer = int(1e9)
            for li in permutations(range(len(dists))): # 순열을 이용하여 최적의 순서를 찾는다.
                temp = cleaner[li[0]]
                start = li[0]
                for idx in range(1, len(li)): # 순열을 기준으로 시작점(start), 도착점(end)을 바꿔가며 거리를 더한다. 
                    end = li[idx]
                    temp += dists[start][end]
                    start = end
                answer = min(answer, temp) # answer에 이동횟수의 최소값을 담는다.
            print(answer)
    else:
        break 