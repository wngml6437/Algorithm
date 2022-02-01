"""
[문제]
두 마리의 백조가 호수에서 살고 있었다. 
그렇지만 두 마리는 호수를 덮고 있는 빙판으로 만나지 못한다.
호수는 행이 R개, 열이 C개인 직사각형 모양이다. 어떤 칸은 얼음으로 덮여있다.
호수는 차례로 녹는데, 매일 물 공간과 접촉한 모든 빙판 공간은 녹는다. 
두 개의 공간이 접촉하려면 가로나 세로로 닿아 있는 것만 (대각선은 고려하지 않는다) 생각한다.
아래에는 세 가지 예가 있다.

=======================================================

...XXXXXX..XX.XXX ....XXXX.......XX .....XX.......... 
....XXXXXXXXX.XXX .....XXXX..X..... ......X.......... 
...XXXXXXXXXXXX.. ....XXX..XXXX.... .....X.....X..... 
..XXXXX..XXXXXX.. ...XXX....XXXX... ....X......XX.... 
.XXXXXX..XXXXXX.. ..XXXX....XXXX... ...XX......XX.... 
XXXXXXX...XXXX... ..XXXX.....XX.... ....X............ 
..XXXXX...XXX.... ....XX.....X..... ................. 
....XXXXX.XXX.... .....XX....X..... ................. 
      처음               첫째 날             둘째 날
      
======================================================

백조는 오직 물 공간에서 세로나 가로로만(대각선은 제외한다) 움직일 수 있다.
며칠이 지나야 백조들이 만날 수 있는 지 계산하는 프로그램을 작성하시오.


[입력]
입력의 첫째 줄에는 R과 C가 주어진다. 단, 1 ≤ R, C ≤ 1500.
다음 R개의 줄에는 각각 길이 C의 문자열이 하나씩 주어진다. 
'.'은 물 공간, 'X'는 빙판 공간, 'L'은 백조가 있는 공간으로 나타낸다.


[출력]
첫째 줄에 문제에서 주어진 걸리는 날을 출력한다.

[입력 예시 1]
10 2
.L
..
XX
XX
XX
XX
XX
XX
..
.L

[출력 예시 1]
3

[입력 예시 2]
4 11
..XXX...X..
.X.XXX...L.
....XXX..X.
X.L..XXX...

[출력 예시 2]
2

[입력 예시 3]
8 17
...XXXXXX..XX.XXX
....XXXXXXXXX.XXX
...XXXXXXXXXXXX..
..XXXXX.LXXXXXX..
.XXXXXX..XXXXXX..
XXXXXXX...XXXX...
..XXXXX...XXX....
....XXXXX.XXXL...

[출력 예시 3]
2

"""

# PyPy3 제출    : 메모리(368964 KB) 시간(1556 ms)
# Python3 제출  : 불가능 (시간 초과)

# 참고 : https://chldkato.tistory.com/58

# BFS + Queue

from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    while q:
        x, y = q.popleft()
        if x == x2 and y == y2:
            return 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not c[nx][ny]:
                    if a[nx][ny] == '.':
                        q.append([nx, ny])
                    else:
                        q_temp.append([nx, ny])
                    c[nx][ny] = 1
    return 0

def melt():
    while wq:
        x, y = wq.popleft()
        if a[x][y] == 'X':
            a[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not wc[nx][ny]:
                    if a[nx][ny] == 'X':
                        wq_temp.append([nx, ny])
                    else:
                        wq.append([nx, ny])
                    wc[nx][ny] = 1

m, n = map(int, input().split())
c = [[0]*n for _ in range(m)]
wc = [[0]*n for _ in range(m)]

a, swan = [], []
q, q_temp, wq, wq_temp = deque(), deque(), deque(), deque()

for i in range(m):
    row = list(input().strip())
    a.append(row)
    for j, k in enumerate(row):
        if a[i][j] == 'L':
            swan.extend([i, j])
            wq.append([i, j])
        elif a[i][j] == '.':
            wc[i][j] = 1
            wq.append([i, j])

x1, y1, x2, y2 = swan
q.append([x1, y1])
a[x1][y1], a[x2][y2], c[x1][y1] = '.', '.', 1
cnt = 0

while True:
    melt()
    if bfs():
        print(cnt)
        break
    q, wq = q_temp, wq_temp
    q_temp, wq_temp = deque(), deque()
    cnt += 1