"""
[문제]
채영이는 거울을 들여다보는 것을 참 좋아한다. 
그래서 집 곳곳에 거울을 설치해두고 집 안을 돌아다닐 때마다 거울을 보곤 한다.

채영이는 새 해를 맞이하여 이사를 하게 되었는데, 
거울을 좋아하는 그녀의 성격 때문에 새 집에도 거울을 매달만한 위치가 여러 곳 있다. 
또한 채영이네 새 집에는 문이 두 개 있는데, 채영이는 거울을 잘 설치하여 장난을 치고 싶어졌다. 
즉, 한 쪽 문에서 다른 쪽 문을 볼 수 있도록 거울을 설치하고 싶어졌다.

채영이네 집에 대한 정보가 주어졌을 때, 한 쪽 문에서 다른 쪽 문을 볼 수 있도록 하기 위해 설치해야 하는 거울의 최소 개수를 구하는 프로그램을 작성하시오.

거울을 설치할 때에는 45도 기울어진 대각선 방향으로 설치해야 한다. 
또한 모든 거울은 양면 거울이기 때문에 양 쪽 모두에서 반사가 일어날 수 있다. 
채영이는 거울을 매우 많이 가지고 있어서 거울이 부족한 경우는 없다고 하자.

거울을 어떻게 설치해도 한 쪽 문에서 다른 쪽 문을 볼 수 없는 경우는 주어지지 않는다.


[입력]
첫째 줄에 집의 크기 N (2 ≤ N ≤ 50)이 주어진다. 
다음 N개의 줄에는 N개의 문자로 집에 대한 정보가 주어진다. 

‘#’는 문이 설치된 곳으로 항상 두 곳이며, 
‘.’은 아무 것도 없는 것으로 빛은 이 곳을 통과한다. 
‘!’은 거울을 설치할 수 있는 위치를 나타내고, 
‘*’은 빛이 통과할 수 없는 벽을 나타낸다.


[출력]
첫째 줄에 설치해야 할 거울의 최소 개수를 출력한다.


[입력 예시]
5
***#*
*.!.*
*!.!*
*.!.*
*#***


[출력 예시]
2


"""

# PyPy3 제출    : 메모리(127608 KB) 시간(156 ms)
# Python3 제출  : 메모리(32552 KB)  시간(108 ms)

# 참고 : https://chelseashin.tistory.com/81


# BFS

# 도착 좌표를 만났다고 바로 리턴해버리는 것이 아니라 이후에 또 갱신될 수 있기 때문에 큐에 값이 있는 동안 끝까지 다 해봐야한다.
# Input 받으면서 시작좌표(sr, sc), 도착좌표(gr, gc)를 저장한다.
# 맵 내이고, 벽이 아니라면 모두 탐색해야 하므로 큐에 좌표와 방향을 모두 담아준다.
# BFS 함수 내에서 check를 맵의 크기대로 그리되, 각 위치별로 4방향(상하좌우) 정보를 담을 수 있도록 * 4 해줬다.
# 거울 사용 횟수를 표현할 것이므로 check배열의 초기화는 -1로 해줬다.
# 최초의 큐에 담긴 위치와 방향 값을 돌리며 check 배열에 0으로 표시한다. 거울을 아직 사용하지 않은 경우이므로 0이다.
# 큐에서 값을 하나씩 꺼내며 너비우선탐색으로 갈 수 있는 곳을 퍼트린다.
# 이동할 곳이 격자 밖이거나 벽이면 continue
# 그리고 크게 두 가지 경우로 빈 공간("*") 이거나 거울을 설치할 수 있는 곳("!") 일 때로 나누어 조건문을 구성했다.
  # 그리고 두 경우에 대해 첫 방문인 경우, 그리고 이미 방문한 적이 있는 경우일 때로 또 두 경우를 나누었다.
    # 첫 방문인 경우는 그대로 이동할 곳을 거울 사용 횟수로 표시하고, 큐에 값을 담았다.
    # 이미 방문한 적이 있는 경우에는 최솟값으로 갱신할 수 있는 경우에만 거울 사용 횟수를 표시하고, 큐에 값을 담았다.
    # 추가로 고려한 것은 거울을 설치할 수 있는 곳에 거울을 설치하는 경우와 거울을 설치하지 않는 경우로 두 경우를 나누었다.
       # 거울 설치하지 않는 경우는 빈 공간에 가는 경우와 같이 첫 방문일 때, 이미 방문 표시가 되어 있는 경우를 각각 처리해준다.
       # 거울을 설치하는 경우, 미리 만들어둔 changeDir에서 현재 방향에서 갈 수 있는 두 가지 방향에 대해 새로운 방향을 검사하는데, 이 때도 마찬가지로 첫 방문일 때와, 이미 방문 표시가 되어 있을 때를 구분해 각각 처리해준다.
    # 이렇게 모든 경우에 대해 조건문을 구성해야 한다.

# 큐에 있는 모든 값의 검사가 끝나면, check 배열의 목적지(gr, gc)에 담긴 상하좌우에 해당하는 4개 값 중 -1을 제외하고 가장 적은 거울 사용횟수를 리턴한다.
# 성급하게 큐에서 뽑은 gr, gc일 때 값을 리턴해버리면 절대 안 된다. 
# 목적지에 첫 도착 이후에도 언제든 최솟값으로 갱신될 수 있기 때문이다.


from sys import stdin
input = stdin.readline
from collections import deque

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
changeDir = ((2, 3), (2, 3), (0, 1), (0, 1))

def bfs():
    check = [[[-1] * 4 for _ in range(N)] for _ in range(N)]
    for sr, sc, sd in Q:
        check[sr][sc][sd] = 0
    while Q:
        r, c, d = Q.popleft()
        nr = r + dr[d]
        nc = c + dc[d]
        # 격자 밖이거나 벽이면
        if not (0 <= nr < N and 0 <= nc < N) or A[nr][nc] == "*":
            continue
            
        # 빈 공간인 경우
        if A[nr][nc] == ".":
            if check[nr][nc][d] == -1:      # 첫 방문
                check[nr][nc][d] = check[r][c][d]
                Q.append((nr, nc, d))
            else:     # 이미 방문했다면 갱신할 수 있는 경우에만
                if check[nr][nc][d] > check[r][c][d]:
                    check[nr][nc][d] = check[r][c][d]   # 최솟값 갱신
                    Q.append((nr, nc, d))
                    
        # 거울 설치할 수 있는 경우
        elif A[nr][nc] == "!":
            # 거울 설치 X
            if check[nr][nc][d] == -1:      # 첫 방문
                check[nr][nc][d] = check[r][c][d]
                Q.append((nr, nc, d))
            else:     # 이미 방문했다면 갱신할 수 있는 경우에만
                if check[nr][nc][d] > check[r][c][d]:
                    check[nr][nc][d] = check[r][c][d]   # 최솟값 갱신
                    Q.append((nr, nc, d))
            # 거울 설치 O
            for nd in changeDir[d]:
                if check[nr][nc][nd] == -1:     # 첫 방문
                    check[nr][nc][nd] = check[r][c][d] + 1
                    Q.append((nr, nc, nd))
                else:     # 이미 방문했다면 갱신할 수 있는 경우에만
                    if check[nr][nc][nd] > check[r][c][d] + 1:      # 최솟값 갱신
                        check[nr][nc][nd] = check[r][c][d] + 1
                        Q.append((nr, nc, nd))

    temp = []   # 가능한 경우의 수
    for chk in check[gr][gc]:
        if chk == -1:
            continue
        temp.append(chk)
    return min(temp)

# main
N = int(input())
A = []
doors = []
for i in range(N):
    A.append(list(input().strip()))
    for j in range(N):
        if A[i][j] == "#":
            doors.append([i, j])
            A[i][j] = "."

sr, sc = doors[0]   # 시작 좌표
gr, gc = doors[1]   # 도착 좌표

Q = deque()
for d in range(4):
    nr = sr + dr[d]
    nc = sc + dc[d]
    if not (0 <= nr < N and 0 <= nc < N) or A[nr][nc] == "*":
        continue
    Q.append((sr, sc, d))   # 시작 가능한 방향 모두 큐에 담기

print(bfs())