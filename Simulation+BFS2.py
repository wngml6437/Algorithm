"""
[문제]
러시아 가스를 크로아티아로 운반하기 위해 자그레브와 모스코바는 파이프라인을 디자인하고 있다. 
두 사람은 실제 디자인을 하기 전에 파이프 매니아 게임을 이용해서 설계를 해보려고 한다.

이 게임에서 유럽은 R행 C열로 나누어져 있다. 
각 칸은 비어있거나, 아래 그림과 같은 일곱가지 기본 블록으로 이루어져 있다.

< block.png >

가스는 모스크바에서 자그레브로 흐른다. 가스는 블록을 통해 양방향으로 흐를 수 있다. 
'+'는 특별한 블록으로, 아래 예시처럼 두 방향 (수직, 수평)으로 흘러야 한다.

< gas-flow.jfif >

파이프 라인의 설계를 마친 후 두 사람은 잠시 저녁을 먹으러 갔다. 
그 사이 해커가 침임해 블록 하나를 지웠다. 지운 블록은 빈 칸이 되어있다.

해커가 어떤 칸을 지웠고, 그 칸에는 원래 어떤 블록이 있었는지 구하는 프로그램을 작성하시오.


[입력]
첫째 줄에 유럽의 크기 R과 C가 주어진다. (1 ≤ R, C ≤ 25)

다음 R개 줄에는 C개 글자가 주어지며, 다음과 같은 글자로 이루어져 있다.

빈칸을 나타내는 '.'
블록을 나타내는 '|'(아스키 124), '-','+','1','2','3','4'
모스크바의 위치를 나타내는 'M'과 자그레브를 나타내는 'Z'. 두 글자는 한 번만 주어진다.
항상 답이 존재하고, 가스의 흐름이 유일한 경우만 입력으로 주어진다.
또, 모스크바와 자그레브가 하나의 블록과 인접해 있는 입력만 주어진다. 
또, 불필요한 블록이 존재하지 않는다. 
즉, 없어진 블록을 추가하면, 모든 블록에 가스가 흐르게 된다.


[출력]
지워진 블록의 행과 열 위치를 출력하고, 어떤 블록이었는지를 출력한다.


[입력 예시 1]
3 7
.......
.M-.-Z.
.......


[출력 예시 1]
2 4 -


[입력 예시 2]
3 5
..1-M
1-+..
Z.23.


[출력 예시 2]
2 4 4


[입력 예시 3]
6 10
Z.1----4..
|.|....|..
|..14..M..
2-+++4....
..2323....
..........


[출력 예시 3]
3 3 |


"""


# PyPy3 제출    : 메모리(126168 KB) 시간(136 ms)
# Python3 제출  : 메모리(32744 KB) 시간(96 ms)

# 참고 : https://yanoo.tistory.com/73

# simulation + BFS

from collections import deque

r, c = map(int,input().split())

def pip_list(pipe):
    if pipe == "|":
        return [0,2]
    if pipe == "-":
        return [1,3]
    if pipe == '+':
        return [0,1,2,3]
    if pipe == "1":
        return [1,2]
    if pipe == "2":
        return [0,1]
    if pipe == "3":
        return [0,3]
    if pipe == "4":
        return [2,3]

visited = [[False] * c for _ in range(r)]
arr = []
start = []

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(r):
    arr.append(list(input()))
    for j in range(c):
        if arr[i][j] == "M" or arr[i][j] == "Z":
            visited[i][j] == True
            start.append((i,j))
q = deque()

ax = 0
ay = 0

def bfs(q, visited):
    global ax, ay
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for i in pip_list(arr[x][y]):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c or visited[nx][ny]:
                continue
            if arr[nx][ny] == "M" or arr[nx][ny] == "Z":
                continue
            if visited[nx][ny] == True:
                continue
            if arr[nx][ny] == '.':
                ax = nx
                ay = ny
            else:
                q.append((nx,ny))

flag=False

for s in start:
    x, y = s
    visited[x][y] = True
    # 북 동 남 서
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= r or ny >= c or visited[nx][ny]:
            continue
        if arr[nx][ny] != '.':
            flag = True
            if i == 0 and (arr[nx][ny] == '|' or arr[nx][ny] == '+' or arr[nx][ny] == '1' or arr[nx][ny] == '4'):
                q.append((nx,ny))
            if i == 1 and (arr[nx][ny] == '-' or arr[nx][ny] == '+' or arr[nx][ny] == '3' or arr[nx][ny] == '4'):
                q.append((nx,ny))
            if i == 2 and (arr[nx][ny] == '|' or arr[nx][ny] == '+' or arr[nx][ny] == '2' or arr[nx][ny] == '3'):
                q.append((nx,ny))
            if i == 3 and (arr[nx][ny] == '-' or arr[nx][ny] == '+' or arr[nx][ny] == '1' or arr[nx][ny] == '2'):
                q.append((nx,ny))
            
    if flag :
        bfs(q,visited)
        break
pipe=""
direction = [False]*4
[False, False, False, False]
if flag :
    # 북0 동1 남2 서3
    for i in range(4):
        nx = ax + dx[i]
        ny = ay + dy[i]
        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue
        if i == 0 and (arr[nx][ny] == '|' or arr[nx][ny] == '+' or arr[nx][ny] == '1' or arr[nx][ny] == '4' ):
            direction[i] = True
        if i == 1 and (arr[nx][ny] == '-' or arr[nx][ny] == '+' or arr[nx][ny] == '3' or arr[nx][ny] == '4' ):
            direction[i] = True
        if i == 2 and (arr[nx][ny] == '|' or arr[nx][ny] == '+' or arr[nx][ny] == '2' or arr[nx][ny] == '3' ):
            direction[i] = True
        if i == 3 and (arr[nx][ny] == '-' or arr[nx][ny] == '+' or arr[nx][ny] == '1' or arr[nx][ny] == '2' ):
            direction[i] = True
    
    if direction[0] and direction[2] and not direction[1] and not direction[3]:
        pipe = "|"
    if direction[1] and direction[3] and not direction[0] and not direction[2]:
        pipe = "-"
    if direction[0] and direction[1] and direction[2] and direction[3]:
        pipe = "+"
    if direction[1] and direction[2] and not direction[0] and not direction[3]:
        pipe = "1"
    if direction[0] and direction[1] and not direction[2] and not direction[3]:
        pipe = "2"
    if direction[0] and direction[3] and not direction[1] and not direction[2]:
        pipe = "3"
    if direction[2] and direction[3] and not direction[0] and not direction[1]:
        pipe = "4"
else:
    if start[0][0] == start[1][0]:
        pipe = "-"
        ax = start[0][0]
        ay = (start[0][1] + start[1][1])//2
    else:
        pipe = "|"
        ax = (start[0][0] + start[1][0])//2
        ay = start[0][1]
print(ax+1,ay+1,pipe)