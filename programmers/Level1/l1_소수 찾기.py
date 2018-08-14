"""
문제 설명


1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
 (1은 소수가 아닙니다.)

제한 조건
•n은 2이상 1000000이하의 자연수입니다.

입출력 예


n  result
10 4
5 3

입출력 예 설명

입출력 예 #1
 1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환

입출력 예 #2
 1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환

"""
import math

n = 1000000
"""
def solution(n):
    max_list = [i for i in range(2, n + 1)]

    for m in max_list:
        for j in max_list:
            if j != m and j % m == 0:
                max_list.remove(j)
        if float(m) > math.sqrt(n):
            break


    return len(max_list)



print(solution(n))
"""
def sieve(n):
    """Return list of prime numbers less than equal to n"""

    results = [1 for _ in range(n+1)]
    results[0], results[1] = 0, 0

    div = 2
    while div <= n // 2 + 1:
        for i in range(div * div, n+1, div):
            if results[i] == 0:
                continue
            else:
                results[i] = 0
        div += 1

    return sum(results)

print(sieve(n))