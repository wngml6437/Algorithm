"""
[문제]
크기가 1×1인 정사각형으로 나누어진 W×H 크기의 지도가 있다. 
지도의 각 칸은 빈 칸이거나 벽이며, 두 칸은 'C'로 표시되어 있는 칸이다.
'C'로 표시되어 있는 두 칸을 레이저로 통신하기 위해서 설치해야 하는 거울 개수의 최솟값을 구하는 프로그램을 작성하시오. 
레이저로 통신한다는 것은 두 칸을 레이저로 연결할 수 있음을 의미한다.
레이저는 C에서만 발사할 수 있고, 빈 칸에 거울('/', '\')을 설치해서 방향을 90도 회전시킬 수 있다. 
아래 그림은 H = 8, W = 7인 경우이고, 빈 칸은 '.', 벽은 '*'로 나타냈다. 
왼쪽은 초기 상태, 오른쪽은 최소 개수의 거울을 사용해서 두 'C'를 연결한 것이다.

7 . . . . . . .         7 . . . . . . .
6 . . . . . . C         6 . . . . . /-C
5 . . . . . . *         5 . . . . . | *
4 * * * * * . *         4 * * * * * | *
3 . . . . * . .         3 . . . . * | .
2 . . . . * . .         2 . . . . * | .
1 . C . . * . .         1 . C . . * | .
0 . . . . . . .         0 . \-------/ .
  0 1 2 3 4 5 6           0 1 2 3 4 5 6
  

[입력]
첫째 줄에 W와 H가 주어진다. (1 ≤ W, H ≤ 100)
둘째 줄부터 H개의 줄에 지도가 주어진다. 지도의 각 문자가 의미하는 것은 다음과 같다.

. : 빈 칸
* : 벽
C : 레이저로 연결해야 하는 칸
'C'는 항상 두 개이고, 레이저로 연결할 수 있는 입력만 주어진다.

[출력]
첫째 줄에 C를 연결하기 위해 설치해야 하는 거울 개수의 최솟값을 출력한다.

[입력 예시]
7 8
.......
......C
......*
*****.*
....*..
....*..
.C..*..
.......

[출력 예시]
3

"""

# PyPy3 제출    : 메모리(128124 KB) 시간(156 ms)
# Python3 제출  : 메모리(32412 KB)  시간(116 ms)

# 참고 : https://juhee-maeng.tistory.com/66

# BFS

from collections import deque


def bfs(x,y):
    queue = deque([(x,y)])
    visited[x][y] = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            ## 동 남 서 북 순서
            nx, ny = x+dx[i], y+dy[i]
            while True:
                ## 범위를 벗어난다
                if not(0<=nx<n and 0<=ny<m): break
                ## 벽을 만난다
                if board[nx][ny]=='*': break
                ## 지난 적 있는 곳인데, 지금 경로로는 너무 많은 거울이 필요해서 break
                if visited[nx][ny] < visited[x][y]+1: break
                ## board업데이트, queue 추가
                queue.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
                nx = nx+dx[i]
                ny = ny+dy[i]

if __name__=='__main__':
    ## 입력값
    m,n = map(int, input().split())
    board = [input() for _ in range(n)]

    ## 동 남 서 북
    dx = (0,1,0,-1)
    dy = (1,0,-1,0)

    ## C위치
    C = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'C':
                C.append((i,j))
    ## sx,sy : 시작지점
    ## ex,ey : 도착지점
    (sx,sy), (ex,ey) = C

    visited = [[float('inf')]*m for _ in range(n)]
    bfs(sx,sy)
    
    print(visited[ex][ey]-1)
