"""
[문제]
n×n짜리의 배열이 하나 있다. 이 배열의 (1, 1)에서 (n, n)까지 이동하려고 한다. 
이동할 때는 상, 하, 좌, 우의 네 인접한 칸으로만 이동할 수 있다.

이와 같이 이동하다 보면, 배열에서 몇 개의 수를 거쳐서 이동하게 된다. 
이동하기 위해 거쳐 간 수들 중 
최댓값과 최솟값의 차이가 가장 작아지는 경우를 구하는 프로그램을 작성하시오.


[입력]
첫째 줄에 n(2 ≤ n ≤ 100)이 주어진다. 다음 n개의 줄에는 배열이 주어진다. 
배열의 각 수는 0보다 크거나 같고, 200보다 작거나 같은 정수이다.


[출력]
첫째 줄에 (최대 - 최소)가 가장 작아질 때의 그 값을 출력한다.


[입력 예시]
5
1 1 3 6 8
1 2 2 5 5
4 4 0 3 3
8 0 2 3 4
4 3 0 2 1


[출력 예시]
2


"""


# PyPy3 제출    : 메모리(131880 KB) 시간(284 ms)
# Python3 제출  : 메모리(32428 KB) 시간(1808 ms)

# 참고 : https://hillier.tistory.com/95


# BFS + Queue

from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q = deque()
    c = [[0]*n for _ in range(n)]
    q.append([0, 0])
    c[0][0] = 1
    while q:
        x, y = q.popleft()
        if x == n-1 and y == n-1:
            return 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if left <= a[nx][ny] <= right and not c[nx][ny]:
                    c[nx][ny] = 1
                    q.append([nx, ny])
    return 0

n = int(input())

a, r_max, l_min = [], 0, sys.maxsize
for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)
    l_min = min(l_min, min(row))
    r_max = max(r_max, max(row))

l_max = min(a[0][0], a[n-1][n-1])
r_min = max(a[0][0], a[n-1][n-1])

left, right = l_min, r_min
ans = sys.maxsize
while l_min <= left <= l_max and r_min <= right <= r_max:
    l_flag, r_flag = 0, 0
    if bfs():
        ans = min(ans, right - left)
        left += 1
        l_flag = 1
    else:
        if l_flag and r_flag:
            left += 1
            right += 1
        else:
            right += 1
            r_flag = 1
print(ans)