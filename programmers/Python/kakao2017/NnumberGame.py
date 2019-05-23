"""
진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p 가 주어진다.

2 ≦ n ≦ 16
0 ＜ t ≦ 1000
2 ≦ m ≦ 100
1 ≦ p ≦ m

2	4	2	1	0111
16	16	2	1	02468ACE11111111
16	16	2	2	13579BDF01234567

"""
n = 16
t = 16
m = 2
p = 2

def solution(n, t, m, p):

    candidate_list = []
    p_count = 1
    m_count = m
    for i in range(m * t):
        if p_count == p:
            candidate_list.append(convert(i, n))

        p_count += 1
        if p_count == (m_count + 1):
            p_count = 1
    return candidate_list


def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]


print(solution(n,t,m,p))
