"""
[문제]
준서가 여행에 필요하다고 생각하는 N개의 물건이 있다. 각 물건은 무게 W와 가치 V를 가지는데, 
해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다. 
아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다. 
준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.

[입력]
첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다. 
두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와, 
해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.

입력으로 주어지는 모든 수는 정수이다.

[출력]
한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.

[입력 예시]
4 7
6 13
4 8
3 6
5 12

[출력 예시]
14

"""

# 출처 : https://myjamong.tistory.com/319


# 동적계획법

# PyPy3 제출    : 메모리(125936 KB) 시간(176 ms)
# Python3 제출  : 메모리(33688 KB)  시간(3880 ms)

N, K = map(int, input().split())
cache = [0] * (K+1)

for _ in range(N):
    w, v = map(int, input().split())
    for j in range(K, w-1, -1):
        cache[j] = max(cache[j], cache[j-w] + v)
print(cache[-1])


# 딕셔너리 이용

# PyPy3 제출    : 메모리(136596 KB) 시간(224 ms)
# Python3 제출  : 메모리(40684 KB)  시간(924 ms)

N, K = map(int, input().split())
cache = {0: 0}

for _ in range(N):
    curr_w, curr_v = map(int, input().split())
    temp = {}
    for w, v in cache.items():
        if curr_w + w <= K and curr_v + v > cache.get(curr_w + w, 0):
            temp[curr_w + w] = curr_v + v
    cache.update(temp)
print(max(cache.values()))

