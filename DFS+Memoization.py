"""
[문제]
알파벳 대문자가 한 칸에 한 개씩 적혀있는 N×M 크기의 문자판이 있다. 
편의상 모든 문자는 대문자라 생각하자. 예를 들어 아래와 같은 문자판을 보자.

K	A	K	T
X	E	A	S
Y	R	W	U
Z	B	Q	P

이 문자판의 한 칸(아무 칸이나 상관없음)에서 시작하여 움직이면서, 
그 칸에 적혀 있는 문자들을 차례대로 모으면 하나의 단어를 만들 수 있다. 
움직일 때는 상하좌우로 K개의 칸까지만 이동할 수 있다. 
예를 들어 K=2일 때 아래의 그림의 가운데에서는 'X' 표시된 곳으로 이동할 수 있다.

 	 	X	 	 
 	 	X	 	 
X	X	 	X	X
 	 	X	 	 
 	 	X	 	 
        
반드시 한 칸 이상 이동을 해야 하고, 같은 자리에 머물러 있을 수 없다. 
또, 같은 칸을 여러 번 방문할 수 있다.

이와 같은 문자판과 K, 그리고 하나의 영단어가 주어졌을 때, 
이와 같은 영단어를 만들 수 있는 경로가 총 몇 개 존재하는지 알아내는 프로그램을 작성하시오.

위의 예에서 영단어가 BREAK인 경우에는 다음과 같이 3개의 경로가 존재한다. 
앞의 수는 행 번호, 뒤의 수는 열 번호를 나타낸다.

(4, 2) (3, 2) (2, 2) (1, 2) (1, 1)
(4, 2) (3, 2) (2, 2) (1, 2) (1, 3)
(4, 2) (3, 2) (2, 2) (2, 3) (1, 3)


[입력]
첫째 줄에 N(1 ≤ N ≤ 100), M(1 ≤ M ≤ 100), K(1 ≤ K ≤ 5)가 주어진다. 
다음 N개의 줄에는 M개의 알파벳 대문자가 주어지는데, 이는 N×M 크기의 문자판을 나타낸다. 
다음 줄에는 1자 이상 80자 이하의 영단어가 주어진다. 
모든 문자들은 알파벳 대문자이며, 공백 없이 주어진다.


[출력]
첫째 줄에 경로의 개수를 출력한다. 이 값은 2^31-1보다 작거나 같다.


[입력 예시]
4 4 1
KAKT
XEAS
YRWU
ZBQP
BREAK


[출력 예시]
3


"""


# PyPy3 제출    : 메모리(139500 KB) 시간(872 ms)
# Python3 제출  : 메모리(36268 KB)  시간(6128 ms)

# 참고 : https://dirmathfl.tistory.com/

# DFS + 메모이제이션

from sys import stdin


def dfs(loc, idx):
    global answer
    x, y = loc
    
    # 가지치기 1: 이미 체크한 경우
    if check[x][y][idx] != -1:
        return check[x][y][idx]
    
    # 가지치기 2: target 문자와 일치하지 않을 경우
    if board[x][y] != target[idx]:
        check[x][y][idx] = 0
        return 0
    
    # 찾는 문자와 일치하는 경우
    if idx == len(target) - 1:
        return 1

    cur_answer = 0
    for k in range(-K, K + 1):
        if not k:
            continue

        next_x, next_y = x + k, y + k

        if 0 <= next_x < N:
            cur_answer += dfs((next_x, y), idx + 1)
        if 0 <= next_y < M:
            cur_answer += dfs((x, next_y), idx + 1)

    check[x][y][idx] = cur_answer

    return check[x][y][idx]


if __name__ == '__main__':
    answer = 0
    N, M, K = map(int, stdin.readline().split())
    board = [stdin.readline().strip() for _ in range(N)]
    target = stdin.readline().strip()

    dirs = ((0, 1), (0, -1), (-1, 0), (1, 0))
    check = [[[-1] * len(target) for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j] == target[0]:
                answer += dfs((i, j), 0)

    print(answer)