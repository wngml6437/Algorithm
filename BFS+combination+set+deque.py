"""
[문제]
0으로 시작하지 않는 정수 N이 주어진다. 
이때, M을 정수 N의 자릿수라고 했을 때, 다음과 같은 연산을 K번 수행한다.

1 ≤ i < j ≤ M인 i와 j를 고른다. 
그 다음, i번 위치의 숫자와 j번 위치의 숫자를 바꾼다. 
이때, 바꾼 수가 0으로 시작하면 안 된다.

위의 연산을 K번 했을 때, 나올 수 있는 수의 최댓값을 구하는 프로그램을 작성하시오.


[입력]
첫째 줄에 정수 N과 K가 주어진다. 
N은 1,000,000보다 작거나 같은 자연수이고, K는 10보다 작거나 같은 자연수이다.


[출력]
첫째 줄에 문제에 주어진 연산을 K번 했을 때, 만들 수 있는 가장 큰 수를 출력한다. 
만약 연산을 K번 할 수 없으면 -1을 출력한다.


[입력 예시 1]
16375 1


[출력 예시 1]
76315


[입력 예시 2]
132 3


[출력 예시 2]
312


[입력 예시 3]
432 1


[출력 예시 3]
423


[입력 예시 4]
90 4


[출력 예시 4]
-1


[입력 예시 5]
5 2


[출력 예시 5]
-1


[입력 예시 6]
436659 2


[출력 예시 6]
966354


"""

# PyPy3 제출    : 메모리(130672 KB) 시간(220 ms)
# Python3 제출  : 메모리(32420 KB) 시간(264 ms)

# 참고 : https://dailymapins.tistory.com/65

# BFS + combination 응용 + set으로 방문 체크 + swap 하는 방법 파이썬 내부 기능 이용 + deque

# 1. 먼저 자리를 교체할 후보를 선정하기. 자리수가 n일 때, 2개를 뽑는 경우 -> nC2
# 2. K번 동안, 해당 후보들을 가지고, 시뮬레이션을 돌리고, 그 중에서 제일 큰 값을 뽑아오는 형식
# 3. visited는 방문하는 애들만 등록하는 형식. set으로 만들기
# 4. 만약, ans가 그대로 0이면, 바꿔도 작아지기만 하는거니까 -1 출력하기

from collections import deque
from itertools import combinations
import sys
import copy

input = sys.stdin.readline

def bfs():
    visited = set()
    ans = 0
    for _ in range(len(dq)):
        x = dq.popleft()
        num = list(str(x))
        for i, j in idx:
            s = copy.deepcopy(num)
            s[i], s[j] = s[j], s[i]
            if s[0] == '0':
                continue
            nx = int(''.join(s))
            if nx not in visited:
                ans = max(ans, nx)
                visited.add(nx)
                dq.append(nx)
    return ans

N, K = map(int, input().split())
item = [ch for ch in range(len(str(N)))]
idx = list(combinations(item,2))
dq = deque()
dq.append(N)
ans=0

while K:
    ans = bfs()
    K -= 1

if not ans:
    print(-1)
else:
    print(ans)