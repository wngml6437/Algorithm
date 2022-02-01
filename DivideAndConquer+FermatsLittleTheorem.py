"""
[문제]
자연수 N과 정수 K가 주어졌을 때 이항 계수 (N, K)를 
1,000,000,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 N과 K가 주어진다. 
(1 ≤ N ≤ 4,000,000) 
(0 ≤ K ≤ N)

[출력]
(N, K)를 1,000,000,007로 나눈 나머지를 출력한다.

[입력 예시]
5 2

[출력 예시]
10

"""

# PyPy3 제출    : 메모리(124504 KB) 시간(160 ms)
# Python3 제출  : 메모리(30864 KB)  시간(1780 ms)

# 참고 : https://hwiyong.tistory.com/372

# 페르마의 소정리
# 분할 정복

# 거듭제곱을 빠르게 구하는 방법은 
# 백준 1629번을 참고하세요.
def solve(A, B):
    if(B % 2 > 0):
        return solve(A, B - 1) * A
    elif(B == 0):
        return 1
    elif(B == 1):
        return A
    else:
        result = solve(A, B//2)
        return result ** 2 % p

N, K = map(int, input().split())    

n_part = 1
nk_part = 1

p =  1000000007

# N! 부분
for num in range(1, N+1):
    n_part *= num; n_part %= p

# K! 부분
for num in range(1, K+1):
    nk_part *= num; nk_part %= p

# (N-K)! 부분
for num in range(1, N-K+1):
    nk_part *= num; nk_part %= p
    
# (p-2) 제곱 부분은 거듭제곱을 빠르게 구하는 방법을
# 그대로 가져와서 사용합니다.
nk_part = solve(nk_part, p-2) % p

result = (n_part * nk_part) % p
print(result)