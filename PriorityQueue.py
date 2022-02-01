"""
[문제]
백준이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다. 
백준이가 정수를 하나씩 외칠때마다 동생은 지금까지 백준이가 말한 수 중에서 중간값을 말해야 한다. 
만약, 그동안 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.

예를 들어 백준이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면, 
동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다. 
백준이가 외치는 수가 주어졌을 때, 동생이 말해야 하는 수를 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에는 백준이가 외치는 정수의 개수 N이 주어진다. 
N은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수이다. 
그 다음 N줄에 걸쳐서 백준이가 외치는 정수가 차례대로 주어진다. 
정수는 -10,000보다 크거나 같고, 10,000보다 작거나 같다.

[출력]
한 줄에 하나씩 N줄에 걸쳐 백준이의 동생이 말해야 하는 수를 순서대로 출력한다.

[입력 예시]
7
1
5
2
10
-99
7
5

[출력 예시]
1
1
2
2
2
2
5

"""

# PyPy3 제출    : 메모리(153272 KB) 시간(488 ms)
# Python3 제출  : 메모리(36874 KB)  시간(244 ms)

# 참고 : https://slowsure.tistory.com/129

# 우선순위 큐

import sys
import heapq

input = sys.stdin.readline

N = int(input())

right, left = [], []    
now = int(input())
print(now)

for i in range(1, N):
    temp = int(input())
    if len(right) == len(left):
        if now > temp:
            heapq.heappush(right, now)
            heapq.heappush(left, -temp)
        else:
            heapq.heappush(right, temp)
            heapq.heappush(left, -now)
        now = -heapq.heappop(left)
    else:
        if now > temp:
            heapq.heappush(left, -temp)
        else:
            heapq.heappush(left, -now)
            heapq.heappush(right, temp)
            now = heapq.heappop(right)
    print(now)


# 정렬 이용
# 시간 초과

n = int(input())
num_arr = []
answer = []

for i in range(n):
    num_arr.append(int(input()))
    num_arr.sort()
    length = len(num_arr)
    if length % 2 == 0 :
        answer.append(num_arr[(length // 2) -1])
    else :
        answer.append(num_arr[length // 2])
        
for i in answer :
    print(i)