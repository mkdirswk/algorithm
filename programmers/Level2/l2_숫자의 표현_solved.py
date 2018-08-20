"""
문제 설명

Finn은 요즘 수학공부에 빠져 있습니다.
수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다.
예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

1 + 2 + 3 + 4 + 5 = 15
4 + 5 + 6 = 15
7 + 8 = 15
15 = 15
자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

제한사항

n은 10,000 이하의 자연수 입니다.
입출력 예

n	result
15	4
입출력 예 설명

입출력 예#1
문제의 예시와 같습니다.
"""
n = 10000
def solution(n):

    mod = n // 2
    start_count = 1
    temp_list = []
    while start_count <= mod:
        end_count = start_count + 1
        result = start_count
        while end_count < mod + 2:
            result += end_count
            if result == n:
                temp_list.append(result)
            else : end_count += 1


        start_count += 1


    return len(temp_list) + 1 # +1은 자기 자신을 표현할때 사용


def solution_1(n):

    mod = n // 2
    start_count = 1
    total_count = 0
    while start_count <= mod:
        end_count = start_count + 1
        result = start_count
        while end_count < mod + 2:
            result += end_count
            if result > n: break
            if result == n:
                total_count += 1
            else : end_count += 1


        start_count += 1


    return total_count + 1 # +1은 자기 자신을 표현할때 사용

print(solution(n))
print(solution_1(n))


