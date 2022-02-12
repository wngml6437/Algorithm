"""
[문제]
각고의 노력 끝에 찬민이는 2014 Google Code Jam World Finals에 진출하게 되었다.
구글에서 온 초대장을 받고 기뻐했던 것도 잠시, 찬찬히 읽어보던 찬민이는 중요한 사실을 알아차렸다.
최근의 대세에 힘입어 구글 역시 대기업답게 비용 감축에 열을 내고 있었던 것이다.

초대장 내용에 의하면 구글은 찬민에게 최대 M원까지의 비용만을 여행비로써 부담해주겠다고 한다. 
인천에서 LA행 직항 한 번 끊어주는게 그렇게 힘드냐고 따지고도 싶었지만, 
다가올 결승 대회를 생각하면 대회 외적인 곳에 마음을 쓰고 싶지 않은 것 또한 사실이었다. 
그래서 찬민은 인천에서 LA까지 M원 이하로 사용하면서 도착할 수 있는 가장 빠른 길을 차선책으로 택하기로 하였다.

각 공항들간 티켓가격과 이동시간이 주어질 때, 찬민이 인천에서 LA로 갈 수 있는 가장 빠른 길을 찾아 찬민의 대회 참가를 도와주자.


[입력]
입력 파일의 첫 번째 줄에 테스트 케이스의 수를 의미하는 자연수 T가 주어진다. 그 다음에는 T개의 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 줄에는 공항의 수 N (2 ≤ N ≤ 100), 총 지원비용 M (0 ≤ M ≤ 10,000), 
티켓정보의 수 K (0 ≤ K ≤ 10,000)가 공백으로 구분되어 주어진다. 

이어서 K개의 줄에 걸쳐 각 티켓의 출발공항 u, 도착공항 v (1 ≤ u, v ≤ N, u ≠ v), 
비용 c (1 ≤ c ≤ M, 정수), 그리고 소요시간 d (1 ≤ d ≤ 1,000) 가 공백으로 구분되어 주어진다.

인천은 언제나 1번 도시이고, LA는 언제나 N번 도시이다


[출력]
각 테스트 케이스당 한 줄에 찬민이 LA에 도착하는 데 걸리는 가장 짧은 소요시간을 출력한다.

만약, LA에 도착할 수 없는 경우 "Poor KCM"을 출력한다.


[입력 예시]
2
3 100 3
1 2 1 1
2 3 1 1
1 3 3 30
4 10 4
1 2 5 3
2 3 5 4
3 4 1 5
1 3 10 6


[출력 예시]
2
Poor KCM


"""

# PyPy3 제출    : 메모리(164544 KB) 시간(6144 ms)
# Python3 제출  : 불가능. 시간 초과

# 참고 : https://codekodo.tistory.com/57

# 다익스트라 + DP

# 1. 소요시간은 짧지만 비용이 비싼 경우
# 2. 소요시간은 길지만 비용이 싼 경우

# "주어진 정점 x 총 지원 비용" 크기의 배열을 생성하고 INF로 초기화
# 즉, 모든 정점에 대해 총 지원 비용 이내에 해당하는 모든 금액으로 탐색을 진행한다는 의미
# 최종적으로 도착 공항(=N)의 최소값을 리턴

import heapq
import sys
INF = float('inf')

def dijkstra(airport, clock, n, m): # 공항의 개수, 지원 금액
    queue = list()
    heapq.heappush(queue, (1, 0, 0)) # 현재 지점, 비용, 소요 시간

    clock[1][0] = 0

    for cost in range(m+1):
        for here in range(1, n+1):
            if clock[here][cost] == INF:
                continue

            distance = clock[here][cost]
            for nextHere, nextCost, nextTime in airport[here]:
                if cost + nextCost > m:
                    continue

                clock[nextHere][cost + nextCost] = min(clock[nextHere][cost + nextCost], distance + nextTime)

    return clock

def main():
    t = int(input())
    
    for _ in range(t):
        n, m, k = map(int, input().split())

        airport = [[] for _ in range(n+1)]
        clock = [[INF for _ in range(m+1)] for _ in range(n+1)]
        for _ in range(k):
            src, dst, cost, time = map(int, sys.stdin.readline().split())
            airport[src].append((dst, cost, time))
        
        clock = dijkstra(airport, clock, n, m)
        if min(clock[n]) == INF:
            print("Poor KCM")
        else:
            print(min(clock[n]))

if __name__ == "__main__":
    main()