"""
[문제]
히스토그램은 직사각형 여러 개가 아래쪽으로 정렬되어 있는 도형이다. 
각 직사각형은 같은 너비를 가지고 있지만, 높이는 서로 다를 수도 있다. 
예를 들어, 왼쪽 그림은 높이가 2, 1, 4, 5, 1, 3, 3이고 너비가 1인 직사각형으로 이루어진 히스토그램이다.
< 6549.histogram.png 참고 > 
히스토그램에서 가장 넓이가 큰 직사각형을 구하는 프로그램을 작성하시오.

[입력]
입력은 테스트 케이스 여러 개로 이루어져 있다. 
각 테스트 케이스는 한 줄로 이루어져 있고, 직사각형의 수 n이 가장 처음으로 주어진다. (1 ≤ n ≤ 100,000) 
그 다음 n개의 정수 h1, ..., hn (0 ≤ hi ≤ 1,000,000,000)가 주어진다. 
이 숫자들은 히스토그램에 있는 직사각형의 높이이며, 왼쪽부터 오른쪽까지 순서대로 주어진다. 
모든 직사각형의 너비는 1이고, 입력의 마지막 줄에는 0이 하나 주어진다.

[출력]
각 테스트 케이스에 대해서, 히스토그램에서 가장 넓이가 큰 직사각형의 넓이를 출력한다.

[입력 예시]
7 2 1 4 5 1 3 3
4 1000 1000 1000 1000
0

[출력 예시]
8
4000

"""

# PyPy3 제출    : 메모리(147792 KB) 시간(252 ms)
# Python3 제출  : 메모리(46764 KB)  시간(512 ms)

# 참고 : https://hooongs.tistory.com/330


# 방법
# 1. 스택 이용
# 2. 세그먼트 트리와 분할정복

# 1. 스택 이용

from collections import deque
import sys

while True :
    rec = list(map(int, sys.stdin.readline().split()))
    n = rec.pop(0)
    
    if n == 0:
        break
    
    stack = deque()
    answer = 0
    
    # 왼쪽부터 차례대로 탐색
    for i in range(n):
        while len(stack) != 0 and rec[stack[-1]] > rec[i]:
            tmp = stack.pop()
            
            if len(stack) == 0:
                width = i
            else :
                width = i - stack[-1] -1
            answer = max(answer, width * rec[tmp])
        stack.append(i)
            
    # 스택에 남아있는 것을 처리
    while len(stack) != 0 :
        tmp = stack.pop()
        
        if len(stack) == 0:
            width = n
        else :
            width = n - stack[-1] -1
        answer = max(answer, width * rec[tmp])

    print(answer)