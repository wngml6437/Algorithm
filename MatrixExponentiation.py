"""
[문제]
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 
그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.
n=17일때 까지 피보나치 수를 써보면 다음과 같다.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 n이 주어진다. n은 1,000,000,000,000,000,000보다 작거나 같은 자연수이다.

[출력]
첫째 줄에 n번째 피보나치 수를 1,000,000으로 나눈 나머지를 출력한다.

[입력 예시]
1000

[출력 예시]
228875

"""

# PyPy3 제출    : 메모리(123316 KB) 시간(124 ms)
# Python3 제출  : 메모리(30864 KB)  시간(72 ms)

# 참고 : https://myjamong.tistory.com/305
# 참고 : https://hwiyong.tistory.com/378

# 방법

# 1. 재귀함수 이용 : 시간복잡도 n^2
# 2. 동적계획법 이용 : 시간복잡도 n
# 3. 행렬 멱법 이용 : 시간복잡도 log n

def make_matrix(A, matrix):
    dummy_matrix = [[0 for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                dummy_matrix[i][j] += (matrix[i][k] * A[k][j])
            dummy_matrix[i][j] %= 1000000
    return dummy_matrix

def matmul(A, B):
    if(B == 1):
        for i in range(2):
            for j in range(2):
                A[i][j] %= 1000000
        return A
    
    elif((B%2) == 1):
        matrix = matmul(A, B-1)
        new_matrix = make_matrix(A, matrix)
        return new_matrix
    
    else:
        matrix = matmul(A, B//2)
        new_matrix = make_matrix(matrix, matrix)
        return new_matrix

N = int(input())

A = [[1, 1], [1, 0]]
result = matmul(A, N)

print(result[0][1] % 1000000)


# 3. 행렬 멱법

# 기본 개념
def matrix_mult(A, B):
    temp = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j] += (A[i][k] * B[k][j])
    return temp

def matrix_pow(n, M):
    if n == 1:
        return M
    if n % 2 == 0:
        temp = matrix_pow(n//2, M)
        return matrix_mult(temp, temp)
    else:
        temp = matrix_pow(n-1, M)
        return matrix_mult(temp, M)

A = [[1, 1], [1, 0]]
print(matrix_pow(int(input())-1, A)[0][0])