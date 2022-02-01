"""
[문제]
크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오. 
수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.

[입력]
첫째 줄에 행렬의 크기 N과 B가 주어진다. (2 ≤ N ≤  5, 1 ≤ B ≤ 100,000,000,000)
둘째 줄부터 N개의 줄에 행렬의 각 원소가 주어진다. 
행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0이다.

[출력]
첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다.

[입력 예시 1]
2 5
1 2
3 4

[출력 예시 1]
69 558
337 406

[입력 예시 2]
3 3
1 2 3
4 5 6
7 8 9

[출력 예시 2]
468 576 684
62 305 548
656 34 412

[입력 예시 3]
5 10
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1

[출력 예시 3]
512 0 0 0 512
512 0 0 0 512
512 0 0 0 512
512 0 0 0 512
512 0 0 0 512

"""

# numpy 사용

import numpy as np

n, power = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
arr_power = np.linalg.matrix_power(arr, power) % 1000
arr_1_dimension = arr_power.ravel()
count = 0
    
for i in arr_1_dimension:
    print(i, end=' ')
    count += 1
    if count % n == 0:
        print()


# PyPy3 제출    : 메모리(125284 KB) 시간(116 ms)
# Python3 제출  : 메모리(30864 KB)  시간(68 ms)

# 참고 : https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-10830-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%96%89%EB%A0%AC-%EC%A0%9C%EA%B3%B1-%EA%B3%A8%EB%93%9C4-%EB%B6%84%ED%95%A0-%EC%A0%95%EB%B3%B5

# 분할정복

import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]

def mul(U, V):
    n = len(U)
    Z = [[0]*n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += U[row][i] * V[i][col]
            Z[row][col] = e % 1000

    return Z

def square(A, B):
    if B == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= 1000
        return A
    
    tmp = square(A, B//2)
    if B % 2:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)

result = square(A, B)
for r in result:
    print(*r)