"""
[문제]
상근이는 감옥에서 죄수 두 명을 탈옥시켜야 한다. 
이 감옥은 1층짜리 건물이고, 상근이는 방금 평면도를 얻었다.
평면도에는 모든 벽과 문이 나타나있고, 탈옥시켜야 하는 죄수의 위치도 나타나 있다. 
감옥은 무인 감옥으로 죄수 두 명이 감옥에 있는 유일한 사람이다.
문은 중앙 제어실에서만 열 수 있다. 
상근이는 특별한 기술을 이용해 제어실을 통하지 않고 문을 열려고 한다. 
하지만, 문을 열려면 시간이 매우 많이 걸린다. 
두 죄수를 탈옥시키기 위해서 열어야 하는 문의 개수를 구하는 프로그램을 작성하시오. 
문을 한 번 열면 계속 열린 상태로 있는다.

[입력]
첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스의 수는 100개를 넘지 않는다.
첫째 줄에는 평면도의 높이 h와 너비 w가 주어진다. (2 ≤ h, w ≤ 100) 
다음 h개 줄에는 감옥의 평면도 정보가 주어지며, 
빈 공간은 '.', 지나갈 수 없는 벽은 '*', 문은 '#', 죄수의 위치는 '$'이다.
상근이는 감옥 밖을 자유롭게 이동할 수 있고, 평면도에 표시된 죄수의 수는 항상 두 명이다. 
각 죄수와 감옥의 바깥을 연결하는 경로가 항상 존재하는 경우만 입력으로 주어진다.

[출력]
각 테스트 케이스마다 두 죄수를 탈옥시키기 위해서 열어야 하는 문의 최솟값을 출력한다.

[입력 예시]
3
5 9
****#****
*..#.#..*
****.****
*$#.#.#$*
*********
5 11
*#*********
*$*...*...*
*$*.*.*.*.*
*...*...*.*
*********.*
9 9
*#**#**#*
*#**#**#*
*#**#**#*
*#**.**#*
*#*#.#*#*
*$##*##$*
*#*****#*
*.#.#.#.*
*********

[출력 예시]
4
0
9

"""

# PyPy3 제출    : 메모리(136764 KB) 시간(300 ms)
# Python3 제출  : 메모리(32504 KB)  시간(780 ms)

# 참고 : https://paris-in-the-rain.tistory.com/123

# 0-1 BFS 
# deque 

import sys
from collections import deque

tc = int(input())

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(y, x):
    visited = [[-1]*(w+2) for _ in range(h+2)] # 맵의 외곽을 추가, 열어야 하는 문의 개수
    dq = deque()
    dq.append([y,x])
    visited[y][x] = 0
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0 <= ny <= h+1 and 0 <= nx <= w+1:
                if visited[ny][nx] == -1:
                    if board[ny][nx] == '.' or board[ny][nx] == '$': # 문을 안 열고 진행
                        visited[ny][nx] = visited[y][x]
                        dq.appendleft([ny, nx]) # 가장 앞에 삽입
                    elif board[ny][nx] == '#': # 문을 여는 경우
                        visited[ny][nx] = visited[y][x] + 1
                        dq.append([ny, nx])
    return visited

for _ in range(tc):
    h, w = map(int, input().split())
    board = [list('.' * (w+2))] # 맨 윗줄 추가
    for i in range(h):
        board.append(list('.' + input().strip() + '.'))
    board.append(list('.' * (w+2))) # 맨 아랫줄 추가
    
    prisoner = []
    for i in range(h+2):
        for j in range(w+2):
            if board[i][j] == '$':
                prisoner.append([i,j])
                
    one = bfs(prisoner[0][0], prisoner[0][1])
    two = bfs(prisoner[1][0], prisoner[1][1])
    sang = bfs(0,0)
    answer = sys.maxsize
    
    for i in range(h+2):
        for j in range(w+2):
            if one[i][j] != -1 and two[i][j] != -1 and sang[i][j] != -1 :
                result = one[i][j] + two[i][j] + sang[i][j] # 해당 위치에서 문을 여는 개수
                if board[i][j] == '*': # 벽은 제외
                    continue
                if board[i][j] == '#' : # 한 명만 열어도 되기 때문에 나머지 사람이 연 개수인 2을 빼줌
                    result -= 2
                answer = min(answer, result)
    print(answer)