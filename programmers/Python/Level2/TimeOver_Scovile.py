"""
scoville	            K	return
[1, 2, 3, 9, 10, 12]	7	2
"""

import timeit
import sys
sys.setrecursionlimit(10**7)


scoville = [1, 2, 3, 9, 10, 12,5234,1236,3123,3122,315123,6123,1236,12367,876,3434,566543]

for i in range(10000):
    scoville.append(0)

K = 7


def solution(scoville, K):
    f_scoville = scoville[:]
    r_final = []
    r_final = scoville_calculation(scoville, K)

    if len(r_final) == 1 and r_final[0] < K:
        return -1
    else:
        return len(f_scoville) - len(r_final)


def scoville_calculation(scoville, K):

    # 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    final_scoville = scoville

    if inspect_scoville(scoville,K):
        return final_scoville
    else:
        if len(final_scoville) > 1:
            final_scoville.sort()
            final_scoville.append(final_scoville[0] + (final_scoville[1] * 2))
            del(final_scoville[0])
            del(final_scoville[0])
            scoville_calculation(final_scoville, K)
        else :
            return -1

    return final_scoville


def inspect_scoville(array,K):
    if min(array) >= K: return True
    else: return False


start = timeit.default_timer()

# 여기에 측정할 코드를 넣으세요
print(solution(scoville, K))
#

stop = timeit.default_timer()
print("%f" % (stop - start))


