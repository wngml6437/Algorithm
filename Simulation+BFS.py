"""
[문제]
창영과 상근은 한 동굴을 놓고 소유권을 주장하고 있다. 
두 사람은 막대기를 서로에게 던지는 방법을 이용해 누구의 소유인지를 결정하기로 했다. 
싸움은 동굴에서 벌어진다. 
동굴에는 미네랄이 저장되어 있으며, 던진 막대기가 미네랄을 파괴할 수도 있다.

동굴은 R행 C열로 나타낼 수 있으며, R×C칸으로 이루어져 있다. 
각 칸은 비어있거나 미네랄을 포함하고 있으며, 
네 방향 중 하나로 인접한 미네랄이 포함된 두 칸은 같은 클러스터이다.

창영은 동굴의 왼쪽에 서있고, 상근은 오른쪽에 서있다. 두 사람은 턴을 번갈아가며 막대기를 던진다. 
막대를 던지기 전에 던질 높이를 정해야 한다. 막대는 땅과 수평을 이루며 날아간다.
막대가 날아가다가 미네랄을 만나면, 그 칸에 있는 미네랄은 모두 파괴되고 막대는 그 자리에서 이동을 멈춘다.
미네랄이 파괴된 이후에 남은 클러스터가 분리될 수도 있다. 
새롭게 생성된 클러스터가 떠 있는 경우에는 중력에 의해서 바닥으로 떨어지게 된다. 
떨어지는 동안 클러스터의 모양은 변하지 않는다. 
클러스터는 다른 클러스터나 땅을 만나기 전까지 게속해서 떨어진다. 
클러스터는 다른 클러스터 위에 떨어질 수 있고, 그 이후에는 합쳐지게 된다.
동굴에 있는 미네랄의 모양과 두 사람이 던진 막대의 높이가 주어진다. 

모든 막대를 던지고 난 이후에 미네랄 모양을 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 동굴의 크기 R과 C가 주어진다. (1 ≤ R,C ≤ 100)

다음 R개 줄에는 C개의 문자가 주어지며, '.'는 빈 칸, 'x'는 미네랄을 나타낸다.

다음 줄에는 막대를 던진 횟수 N이 주어진다. (1 ≤ N ≤ 100)

마지막 줄에는 막대를 던진 높이가 주어지며, 공백으로 구분되어져 있다. 
모든 높이는 1과 R사이이며, 높이 1은 행렬의 가장 바닥, R은 가장 위를 의미한다. 
첫 번째 막대는 왼쪽에서 오른쪽으로 던졌으며, 
두 번째는 오른쪽에서 왼쪽으로, 이와 같은 식으로 번갈아가며 던진다.

공중에 떠 있는 미네랄 클러스터는 없으며, 
두 개 또는 그 이상의 클러스터가 동시에 떨어지는 경우도 없다. 
클러스터가 떨어질 때, 
그 클러스터 각 열의 맨 아래 부분 중 하나가 바닥 또는 미네랄 위로 떨어지는 입력만 주어진다.

[출력]
입력 형식과 같은 형식으로 미네랄 모양을 출력한다.

[입력 예시 1]
5 6
......
..xx..
..x...
..xx..
.xxxx.
1
3

[출력 예시 1]
......
......
..xx..
..xx..
.xxxx.

[입력 예시 2]
8 8
........
........
...x.xx.
...xxx..
..xxx...
..x.xxx.
..x...x.
.xxx..x.
5
6 6 4 3 1

[출력 예시 2]
........
........
........
........
.....x..
..xxxx..
..xxx.x.
..xxxxx.

[입력 예시 3]
7 6
......
......
xx....
.xx...
..xx..
...xx.
....x.
2
6 4

[출력 예시 3]
......
......
......
......
..xx..
xx.xx.
.x..x.

"""

# PyPy3 제출    : 메모리(129888 KB) 시간(252 ms)
# Python3 제출  : 메모리(32592 KB)  시간(972 ms)

# 참고 : https://chelseashin.tistory.com/88

# Simulation + BFS

from sys import stdin
input = stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 미네랄 떨어질 수 있는지 칸 세기
def checkDownCnt(fallLst, check):
    downCnt, flag = 1, 0      # downCnt 크기 1씩 늘려가며
    while True:
        for r, c in fallLst:
            if r+downCnt == R-1:        # 땅을 만나거나
                flag = 1
                break
            if cave[r+downCnt+1][c] == 'x' and check[r+downCnt+1][c]:   # 다른 미네랄 만나면
                flag = 1
                break
        if flag:    # 그 때가 떨어질 수 있는 최대 downCnt 값
            break
        downCnt += 1
    return downCnt

def checkLand():
    check = [[0] * C for _ in range(R)]
    # 땅에 붙어 있는 미네랄 check 배열에 표시
    for lc in range(C):
        if cave[R-1][lc] == "x" and not check[R-1][lc]:     # 미네랄이면서 첫 방문이면
            check[R-1][lc] = 1
            Q = deque([(R-1, lc)])
            while Q:
                r, c = Q.popleft()
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if not (0 <= nr < R and 0 <= nc < C):       # 격자 밖이면
                        continue
                    if cave[nr][nc] == "x" and not check[nr][nc]:   # 미네랄이거나 방문한 적 없으면
                        check[nr][nc] = 1
                        Q.append((nr, nc))
    return check


def breakMinerals(br, bc):
	# 2단계 - 땅에 붙어 있는 미네랄 1로 표시되어 있는 맵 리턴
    check = checkLand()

	# 3단계 - 공중에 떠있는 미네랄 2로 표시, 동굴에서 지우기
    minerals = []    # 공중에 떠있는 미네랄 리스트
    fallLst = []     # 떨어질 수 있는 클러스터의 아랫부분만 저장
    for nd in range(4):     # 깨진 곳 기준으로 4방향 확인
        r = br + dr[nd]
        c = bc + dc[nd]
        if not (0 <= r < R and 0 <= c < C):
            continue

        # 미네랄인데 땅에 붙어 있지 않다면(check 배열에서 0으로 표시되어 있다면) 2로 표시
        if cave[r][c] == "x" and not check[r][c]:
            Q = deque([(r, c)])
            check[r][c] = 2
            minerals.append((r, c))
            cave[r][c] = "."
            while Q:
                r, c = Q.popleft()
                if cave[r+1][c] == ".":     # 바로 밑이 빈 공간인 미네랄
                    fallLst.append((r, c))
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if not (0 <= nr < R and 0 <= nc < C):
                        continue
                    if cave[nr][nc] == "x" and not check[nr][nc]:
                        check[nr][nc] = 2           # 공중에 떠있는 미네랄 클러스터 표시
                        Q.append((nr, nc))
                        minerals.append((nr, nc))   # 미네랄 위치 리스트에 담기
                        cave[nr][nc] = "."          # 동굴에서 공중에 떠 있는 미네랄 제거

    if fallLst:    # 공중에 떠있는 미네랄이 있다면
    	# 4단계 - 떨어질 최대 칸의 수 리턴
        downCnt = checkDownCnt(fallLst, check)

        # 5단계 - 미네랄 떨어질 위치 동굴에 그리기
        for mr, mc in minerals:
            cave[mr+downCnt][mc] = "x"

# main
R, C = map(int, input().split())
cave = [list(input().rstrip()) for _ in range(R)]
N = int(input())
heights = list(map(int, input().split()))

# 1단계 - 좌우에서 막대기 던져 미네랄 깨기
for i in range(N):
    br = R - heights[i]
    if not i % 2:       # 왼쪽에서 깸
        for bc in range(C):
            if cave[br][bc] == "x":
                cave[br][bc] = "."
                breakMinerals(br, bc)   # 깨진 위치 인자로 넘겨 미네랄 깨기
                break
    else:               # 오른쪽에서 깸
        for bc in range(C-1, -1, -1):
            if cave[br][bc] == "x":
                cave[br][bc] = "."
                breakMinerals(br, bc)
                break
    
# 형식에 맞게 출력
for row in cave:
    print(''.join(row))