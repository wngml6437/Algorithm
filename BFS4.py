"""
[문제]
N×M의 행렬로 표현되는 맵이 있다. 
맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 
한 칸에서 다른 칸으로 이동하려면, 두 칸이 인접해야 한다. 
두 칸이 변을 공유할 때, 인접하다고 한다.

각각의 벽에 대해서 다음을 구해보려고 한다.

    벽을 부수고 이동할 수 있는 곳으로 변경한다.
    그 위치에서 이동할 수 있는 칸의 개수를 세어본다.
    
한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.


[입력]
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 
다음 N개의 줄에 M개의 숫자로 맵이 주어진다.


[출력]
맵의 형태로 정답을 출력한다. 
원래 빈 칸인 곳은 0을 출력하고, 벽인 곳은 이동할 수 있는 칸의 개수를 10으로 나눈 나머지를 출력한다.


[입력 예시 1]
3 3
101
010
101


[출력 예시 1]
303
050
303


[입력 예시 2]
4 5
11001
00111
01010
10101


[출력 예시 2]
46003
00732
06040
50403

"""

# PyPy3 제출    : 메모리(208208 KB) 시간(656 ms)
# Python3 제출  : 메모리(55072 KB)  시간(2504 ms)

# 참고 : https://rebas.kr/800


# BFS

from collections import deque
from sys import stdin, stdout
input = stdin.readline
print = stdout.write

n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
b = [[0]*m for _ in range(n)]
v = [0]
check = [[False]*m for _ in range(n)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

def bfs(x, y, z):
    q = deque()
    q.append((x, y))
    check[x][y] = True
    cnt = 1
    while q:
        x, y = q.popleft()
        b[x][y] = z
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not check[nx][ny] and not a[nx][ny]:
                q.append((nx, ny))
                check[nx][ny] = True
                cnt += 1
    return cnt

def flood():
    z = 1
    for i in range(n):
        for j in range(m):
            if not a[i][j] and not check[i][j]:
                v.append(bfs(i, j, z))
                z += 1

def solve():
    for i in range(n):
        for j in range(m):
            if a[i][j]:
                s = set()
                for k in range(4):
                    ni, nj = i+dx[k], j+dy[k]
                    if 0 <= ni < n and 0 <= nj < m:
                        s.add(b[ni][nj])
                for k in s:
                    a[i][j] += v[k]
                    a[i][j] %= 10

for i in range(n):
    for j in range(m):
        if a[i][j] == '0':
            a[i][j] = 0
        else:
            a[i][j] = 1
flood()
solve()
for i in range(n):
    print(''.join(map(str, a[i])))
